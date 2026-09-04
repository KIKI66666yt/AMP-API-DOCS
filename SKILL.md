---
name: amp-panel-api
description: Automate CubeCoders AMP game server panels via its undocumented JSON HTTP API — auth, instance lifecycle, console, file manager, app catalog.
---

# AMP (Application Management Panel) API — agent skill

CubeCoders AMP (used to manage Minecraft/Palworld/Rust/etc. game servers) has
no *published/external* API docs — but every AMP install serves its own
built-in interactive docs browser at `https://<panel-host>/API` (the "AMP API
Browser"), and the panel itself is a thin client over a real JSON-RPC-style
HTTP API at `/API/<Module>/<Command>`. Check `/API` on your own instance
first — it always matches your exact installed version. This skill exists
because that in-panel browser alone doesn't tell you the practical stuff:
auth quirks, permission-model surprises, and worked end-to-end examples.

**For the full up-to-date method list**, don't rely on a static snapshot —
pull it live (see "Discovering the full API surface" below). A community
project, [p0t4t0sandwich/ampapi](https://github.com/p0t4t0sandwich/ampapi),
also documents which plugin modules each instance type (GenericModule,
Minecraft, Rust, srcds, FiveM, ADS) inherits — useful for that mapping, but
**check its last-commit date before trusting its `APISpec.json`/
`FriendlySpec.txt` as current**: as of this writing it's pinned to an AMP
version several releases behind current, and its auto-refresh CI workflow
has its trigger disabled despite the README implying it's still active.
Every AMP panel also serves its own interactive docs browser at
`https://<panel-host>/API` — check that first, it always matches the exact
version installed.

## When to use this skill

Trigger on requests like: "start/stop/restart my \[game\] server", "check
status of my AMP instances", "create a new \[game\] server via AMP", "list
console output", "manage files on my game server", or generally anything
involving a CubeCoders AMP panel.

## Prerequisites

You need:
- The panel's base URL, e.g. `https://your-amp-panel.example.com`
- A username + password for an AMP account with the permissions needed for
  the requested action (or use AMP's role system to create a scoped
  service account — see "Least-privilege service account" below)

**Never hardcode credentials in code or commit them to version control.**
Source them from environment variables or a secrets file the user controls.

## Step 1: Authenticate

```bash
curl -sk -X POST "$AMP_URL/API/Core/Login" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -d "{\"username\":\"$AMP_USERNAME\",\"password\":\"$AMP_PASSWORD\",\"token\":\"\",\"rememberMe\":false}"
```

Returns `{"success":true,"sessionID":"<uuid>", "permissions":[...], "userInfo":{...}}`.

**Two things that will silently break every call if you miss them:**

1. **Every request must include `Accept: application/json`** (or
   `text/javascript` / `application/vnd.cubecoders-ampapi`). Without it you
   get a 400 `"Invalid accept header value"` — `Content-Type` alone is not
   sufficient.
2. **Pass the session via the `Authorization: Bearer <sessionID>` header**,
   not just in the request body. The older pattern of also including
   `"SESSIONID":"<uuid>"` in the JSON body still works but is deprecated —
   AMP logs a warning on every call that uses it (visible in
   `Core/GetUpdates`'s `ConsoleEntries`). Prefer the header for new code;
   include SESSIONID in the body too for maximum compatibility with older
   AMP versions if unsure.

Sessions appear long-lived (no observed expiry after 30+ minutes idle in
testing) — treat as session-cookie-like, and just re-login if a call ever
401s.

## Step 2: Call any endpoint

```bash
curl -sk -X POST "$AMP_URL/API/<Module>/<Command>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $SESSION_ID" \
  -d "{\"SESSIONID\":\"$SESSION_ID\", \"<param1>\": \"...\"}"
```

## Discovering the full API surface

`Core/GetAPISpec` is AMP's own self-describing spec endpoint — but its
response size depends entirely on auth state:

- Called **anonymously** (no valid session): returns only ~10 stub methods
  (login, 2FA, module info). Easy to mistake for the whole API — it isn't.
- Called **with a valid authenticated session**: returns the full method
  list scoped to that session's role — for an admin account, the complete
  surface (200+ methods across Core, ADSModule, FileManagerPlugin,
  StorePlugin, and a few smaller plugin modules).

```bash
curl -sk -X POST "$AMP_URL/API/Core/GetAPISpec" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer $SESSION_ID" \
  -d "{\"SESSIONID\":\"$SESSION_ID\"}"
```

Always re-fetch with a real session when exploring what's available to a
given account.

## Most useful calls

| Call | Notes |
|---|---|
| `POST /API/ADSModule/GetInstances` | Full fleet status in one shot: every instance's name, running state, ports, live CPU/RAM/user metrics (`Metrics` field, delivered via polling — no special console session needed) |
| `POST /API/ADSModule/GetInstance` | Same, single instance by GUID; also returns full `DeploymentArgs` (port manifest, app config Id) |
| `POST /API/ADSModule/StartInstance` / `StopInstance` / `RestartInstance` | Body: `{"SESSIONID":..., "InstanceName":"<name>"}` — use the instance **name**, not its GUID. Restart stops then auto-starts within ~15s. |
| `POST /API/Core/SendConsoleMessage` | Body: `{"SESSIONID":..., "message":"..."}` — sends a console command to whatever instance the *calling session's* context is scoped to (see gotcha below) |
| `POST /API/ADSModule/GetSupportedApplications` | Every app template AMP can deploy (240+ entries, several MB) — filter client-side by `FriendlyName`, don't dump raw |
| `POST /API/ADSModule/CreateInstance` | Scriptable equivalent of the "Create Instance" wizard — see the worked example below |
| `POST /API/Core/GetStatus` | Status of the **controller/ADS instance itself only** — not a specific game server. Don't confuse with per-instance status (use `GetInstances`/`GetInstance` instead). |

## Gotchas (confirmed by testing, not just reading the spec)

### Per-instance permissions are two-layer

Standard role/permission nodes (`ADS.InstanceManagement.*`,
`Core.AppManagement.*`, etc.) are only half the picture. AMP **also**
enforces per-instance permission nodes shaped
`Instances.<TargetID>.<InstanceID>.<Start|Stop|Restart|Update|Manage>`
(visible in `Core/GetPermissionsSpec`'s `Instances` tree). Granting a scoped
role only the top-level nodes is **not enough** — the account's
`GetInstances()` call will only show the controller itself until you also
grant the 5 per-instance sub-permissions for every existing instance. New
instances created afterward need the same grants added manually — there's
no discovered wildcard/inherited grant. Even with those grants,
`GetInstances()` (the bulk list call) can still under-report for a scoped
account while `GetInstance(InstanceId)` (direct lookup) and named action
calls work fine — plan automation around known instance names/GUIDs rather
than relying on the list call for a non-admin account.

### Per-instance console/context switching does not work the way it looks

`ADSModule.ManageInstance(InstanceId)` looks like it should switch your
session's context to the target instance. It does not, server-side —
`Core/GetUpdates`/`SendConsoleMessage` called afterward on the same session
still only affect the controller. AMP internally proxies to the instance's
own local webserver using a short-lived exchanged token entirely
server-side; there's no confirmed way to redeem that token from a plain API
client. If you need true two-way console I/O per instance, expect to invest
real reverse-engineering effort (WebSocket frame inspection via a real
browser session) — this remains an open problem in the community at large.
**Workaround that covers most needs:** `GetInstances()`/`GetInstance()`
already deliver live per-instance CPU/RAM/user-count metrics without
needing console access — sufficient for monitoring/dashboard use cases.

### Misc

- `ADSModule.GetDeploymentTemplates()` returns your **saved custom
  templates**, not the built-in app catalog — expect `[]` on a fresh
  install.
- `Core.Restart()` / `Core.RestartAMP()` restart the **AMP controller app
  itself**, not any game instance — don't confuse with
  `ADSModule.RestartInstance(InstanceName)`.
- `ADSModule.CreateInstance(...)` — before calling, fetch
  `ADSModule.GetProvisionArguments(ModuleName)` for the target app to get
  the exact provisioning field names it expects, and cross-check the
  `Module`/app `Id` string via `GetSupportedApplications()`.

## Least-privilege service account (recommended for ongoing automation)

Don't reuse an admin/personal login for routine automation. Create a
dedicated AMP user + role instead:

1. `Core.CreateUser(Username)` then `Core.ResetUserPassword(Username, NewPassword)`.
2. `Core.CreateRole(Name)` to make a scoped role.
3. `Core.SetAMPRolePermission(RoleId, PermissionNode, Enabled)` — loop over
   the specific top-level nodes needed (e.g.
   `ADS.InstanceManagement.StartInstances`,
   `Core.AppManagement.SendConsoleInput`) — there's no batch-grant endpoint.
4. **Also grant the per-instance nodes** for every existing instance (see
   gotcha above) — `Core/GetPermissionsSpec` lists the exact node paths
   including each instance's real GUID.
5. `Core.SetAMPUserRoleMembership(UserId, RoleId, IsMember=true)` to attach
   the role to the new user.
6. Verify least-privilege with a negative test: confirm a call requiring an
   excluded permission (e.g. `Core.CreateUser`) correctly 401s for the new
   account.

## Worked example: full lifecycle on a game instance

Concrete curl-by-curl walkthrough — find an app in the catalog, inspect a
deployed instance, start/stop/restart it, send console commands, and script
a brand-new instance from scratch (using Palworld as the example, but the
pattern generalizes to any `GenericModule`-based game):
https://github.com/KIKI66666yt/AMP-API-DOCS/blob/main/PALWORLD-EXAMPLE.md

## Discovery method for finding more endpoints/behavior

While logged into the panel in a real (or automated) browser tab:

```js
performance.getEntriesByType('resource').filter(r => r.name.includes('API/')).map(r => r.name)
```

Lists every `/API/...` URL the UI actually called as you click around —
gives you the Module/Command name immediately. Combine with
`Core/GetAPISpec` (authenticated) for the exact parameter names/types each
call expects, so you rarely need to guess.

## References

- Community module-inheritance map (⚠️ check last-commit date — has gone
  stale before, don't trust the bundled spec as current without verifying):
  https://github.com/p0t4t0sandwich/ampapi
- Gotchas + worked example (source for this skill):
  https://github.com/KIKI66666yt/AMP-API-DOCS
