# Gotchas & undocumented behavior

Things about the AMP API that aren't obvious from the spec dump alone — found by testing against a live instance, not just reading `GetAPISpec`.

## Auth

- **`Accept: application/json` is mandatory** on every call. `Content-Type: application/json` alone is not enough — you'll get a 400 `"Invalid accept header value"`. Also acceptable: `text/javascript` or `application/vnd.cubecoders-ampapi`.
- **Two ways to pass the session, one is deprecated.** The header form — `Authorization: Bearer <sessionID>` — is what the real panel actually sends. The older form, passing `"SESSIONID":"<uuid>"` inside the JSON body, still works today but AMP logs a deprecation warning on every call that uses it (visible in `Core/GetUpdates`'s `ConsoleEntries`: *"SessionID passed in request body - this is deprecated, please pass session ID in the Authorization header instead"*). Use the header for new code.
- Sessions appear long-lived — no observed expiry after 30+ minutes idle in testing. Treat as session-cookie-like; re-login if a call ever 401s.
- `Core/GetAPISpec` returns a **radically different response depending on auth state**: ~10 methods (login/2FA/module-info stubs) when called anonymously, vs. the full role-scoped list (up to 205 methods for an admin) when called with a valid session. If you're exploring the API and only see a handful of methods, you're almost certainly calling it unauthenticated.

## Permissions

- Standard role/permission nodes (`ADS.InstanceManagement.*`, `Core.AppManagement.*`, etc.) are only half the picture. AMP **also** enforces **per-instance** permission nodes shaped like `Instances.<TargetID>.<InstanceID>.<Start|Stop|Restart|Update|Manage>` — visible in `Core/GetPermissionsSpec`'s `Instances` tree, which lists every existing instance's actual GUID.
- Consequence: granting a scoped/service-account role only the top-level `ADS.InstanceManagement.*` permissions is **not enough** for that account to see existing instances via `ADSModule.GetInstances()` — the list call will only return the controller itself. You must also grant the 5 per-instance sub-permissions (Start/Stop/Restart/Update/Manage) for *each* instance individually. There is no discovered wildcard or "all current + future instances" grant.
- New instances created after you've set up a scoped role will need those same per-instance grants added manually — check `Core/GetPermissionsSpec` again after creating an instance to find its new node paths.
- Even with all per-instance grants applied, `ADSModule.GetInstances()` (the bulk **list** call) can still only return the controller for a scoped account — while `ADSModule.GetInstance(InstanceId)` (direct lookup by GUID) and action calls (`StartInstance`/`StopInstance`/`RestartInstance` by name) work fine. Not fully explained (likely a still-missing list-level permission), but not blocking if your automation already knows the instance name/GUID it's targeting.

## Per-instance console access — unsolved

The AMP web UI clearly reaches a live per-instance console (you can see real-time CPU/Memory/User gauges and console I/O when you open an instance's page). This does **not** work the way it first appears via the API:

- `ADSModule.ManageInstance(InstanceId)` looks like it should "switch" your session's context to the target instance. It does not, server-side. Confirmed by testing: calling `ManageInstance` for an instance, then calling `Core/GetUpdates` on the *same* session afterward still returns the **controller's** own ports/status, never the target instance's.
- The controller's own audit log shows AMP internally proxying to the instance's own local webserver (`http://127.0.0.1:8082/` style, port varies) using a short-lived exchanged auth token — this exchange happens entirely server-side. There's no confirmed way to redeem that token from outside.
- The browser's real console page opens actual WebSocket connections when you enter an instance view, but replicating this via plain `curl`/HTTP calls was not achieved. **CubeCoders' own community has a thread specifically about this "proxying instance auth" mechanism** — worth reading before spending time reverse-engineering it yourself: [AMP Discord #development](https://discord.com/channels/266012086423912458/266015417842139136/1151622027388657744) (requires a Discord account and membership in CubeCoders' server to view). We haven't independently verified its contents from outside Discord, so treat it as a lead, not a confirmed answer — if you work through it, consider PRing the resolution back into this file.
- **Workaround that covers most needs:** `ADSModule.GetInstances()` / `GetInstance()` already return live per-instance CPU/RAM/user-count metrics (field: `Messages[].Parameters.Metrics`, keyed by instance ID, delivered via polling `Core/GetUpdates` on your plain top-level session). If you just need monitoring/dashboards, you don't need true console access — polling this is enough. Only true two-way console I/O per instance remains unsolved here.

## Misc

- `ADSModule.GetSupportedApplications()` returns **every app template AMP knows about** (240+ entries, ~7MB raw response) as one large JSON array — don't dump it raw, filter client-side by `FriendlyName`. Each entry's `Id` field is the stable per-app template identifier, matching the `<Module>.Meta.AppConfigId` field you'll see in `DeploymentArgs` on an already-deployed instance of that app. See [`APP-CATALOG.md`](./APP-CATALOG.md) (auto-regenerated daily) for the full name/module/Id table, and PALWORLD-EXAMPLE.md for how this `Id` is used when scripting a deploy.
- `ADSModule.GetDeploymentTemplates()` returns your **saved custom templates**, not the built-in app catalog — expect `[]` on a fresh install with no custom templates saved.
- `ADSModule.CreateInstance(...)` is the scriptable equivalent of the "Create Instance" wizard in the UI. Before calling it, fetch `ADSModule.GetProvisionArguments(ModuleName)` for your target app to get the exact provisioning field names/values it expects, and `GetSupportedApplications()` / `GetDeploymentTemplates()` to confirm the right `Module` string.
- `Core.Restart()` / `Core.RestartAMP()` restart the **AMP controller app itself**, not any game instance — don't confuse with `ADSModule.RestartInstance(InstanceName)`, which restarts one game server.

## Discovery method for finding more undocumented behavior

While logged into the panel in a browser:

```js
performance.getEntriesByType('resource').filter(r => r.name.includes('API/')).map(r => r.name)
```

Lists every `/API/...` URL actually called by the UI as you click around — gives you the Module/Command name immediately. Cross-reference against your own panel's `/API` docs browser (always current) for the exact parameter names/types that call expects; [p0t4t0sandwich/ampapi](https://github.com/p0t4t0sandwich/ampapi)'s `FriendlySpec.txt` can help too but check its last-commit date first — it's known to lag behind current AMP releases.
