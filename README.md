# AMP-API-DOCS

Unofficial, reverse-engineered API documentation for [CubeCoders AMP](https://cubecoders.com/AMP) (Application Management Panel) — the web panel used to manage Minecraft/Palworld/etc. game servers.

CubeCoders does **not** publish public API docs. The web panel itself is a thin client over a real JSON-RPC-style HTTP API at `/API/<Module>/<Command>`. This repo documents that API as reverse-engineered by capturing the panel's own network traffic and querying its self-describing spec endpoint.

**Verified against AMP 2.8.0.4** (September 2026). AMP is actively developed — CubeCoders can change this API at any time without notice. Treat everything here as a snapshot, not a stable contract.

## Contents

- [`API-REFERENCE.md`](./API-REFERENCE.md) — the full 205-method API surface: every module, method, parameter (name/type/required-optional), return type, and required permission node. Auto-generated from AMP's own `Core/GetAPISpec` endpoint and lightly reformatted for readability.
- [`GOTCHAS.md`](./GOTCHAS.md) — things that will bite you that aren't obvious from the spec alone: auth quirks, permission model surprises, and one genuinely unsolved problem (per-instance console access).
- [`PALWORLD-EXAMPLE.md`](./PALWORLD-EXAMPLE.md) — a worked, end-to-end example against a real game server: find the app, inspect a deployed instance, start/stop/restart, send console commands, and script a brand-new instance from scratch. Generalizes to any `GenericModule`-based game, not just Palworld.
- [`APP-CATALOG.md`](./APP-CATALOG.md) — every app template AMP currently knows how to deploy (243 entries as of this writing): friendly name, module, and template Id, needed for scripting `CreateInstance` calls for any app.

## Quick start

### 1. Authenticate

```bash
curl -sk -X POST "https://your-amp-panel.example.com/API/Core/Login" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -d '{"username":"YOUR_USER","password":"YOUR_PASSWORD","token":"","rememberMe":false}'
```

Returns `{"success":true,"sessionID":"<uuid>", "permissions":[...], "userInfo":{...}}`.

### 2. Call any endpoint

```bash
curl -sk -X POST "https://your-amp-panel.example.com/API/<Module>/<Command>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>", "<param1>": "..."}'
```

**Two must-haves or every call fails:**
- `Accept: application/json` header — omit it and you get a 400 `"Invalid accept header value"`. `Content-Type` alone is not enough.
- A valid session — pass it as `Authorization: Bearer <sessionID>` (current/preferred) — the older pattern of also including `"SESSIONID":"<uuid>"` in the JSON body still works but is deprecated by AMP itself (it logs a warning telling you to move to the header).

### 3. Most useful calls to start with

| Call | What it does |
|---|---|
| `POST /API/Core/GetAPISpec` | Full self-describing spec of every method your session's role can see (send with a valid session to get the real list, not the ~10-method anonymous stub) |
| `POST /API/ADSModule/GetInstances` | Full fleet status in one shot — every instance's name, running state, ports, live CPU/RAM/user metrics |
| `POST /API/ADSModule/GetInstance` | Same, for one instance by GUID — includes full deployment/port config |
| `POST /API/ADSModule/StartInstance` / `StopInstance` / `RestartInstance` | Body: `{"SESSIONID":..., "InstanceName":"<name>"}` — use the instance *name*, not its GUID |

See `API-REFERENCE.md` for the complete list.

## How this was built

1. Logged into the AMP panel in a real browser and captured its own XHR calls via:
   ```js
   performance.getEntriesByType('resource').filter(r => r.name.includes('API/')).map(r => r.name)
   ```
   This reveals every `/API/<Module>/<Command>` the UI actually calls as you click around.
2. Called `Core/GetAPISpec` **with an authenticated admin session** — this is the key trick. Called anonymously, AMP only returns ~10 stub methods (login, 2FA, module info). Called with a real session, it returns the full list scoped to that session's role — for an admin, that's the complete 205-method surface across 7 modules.
3. Reformatted the raw JSON spec into readable markdown (module, method, params with types, return type, required permission node).
4. Tested the most commonly-needed calls against a live instance to confirm real-world behavior, catching the gotchas documented in `GOTCHAS.md`.

If you're reverse-engineering a different undocumented panel, step 1 + step 2's pattern (find a self-describing spec/schema endpoint, then re-query it *authenticated*) generalizes well beyond AMP.

## Disclaimer

This is unofficial, community-produced documentation, not affiliated with or endorsed by CubeCoders. Use at your own risk — always test against a non-production instance first, and keep credentials/tokens out of scripts and version control.
