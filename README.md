# AMP-API-DOCS

Field notes and worked examples for [CubeCoders AMP](https://cubecoders.com/AMP)'s HTTP API — the real-world quirks, permission gotchas, and end-to-end workflows you hit once you go past "here's the method list."

## This is a companion, not a duplicate

The definitive, auto-updated reference for AMP's raw API surface already exists and is actively maintained:

**→ [p0t4t0sandwich/ampapi](https://github.com/p0t4t0sandwich/ampapi)** — CI-refreshed `APISpec.json` / `FriendlySpec.txt`, a `ModuleInheritance.json` mapping which plugin modules each instance type (GenericModule, Minecraft, Rust, srcds, FiveM, ADS) actually inherits, and client libraries in C#, Node, Python, Java, Go, and Rust.

**Also worth knowing:** your own AMP panel serves built-in interactive API docs at `https://<your-panel>/API` (the "AMP API Browser") — no separate tooling needed to browse the live method list for your exact AMP version.

This repo doesn't re-document the method list — go to the two links above for that. What's here instead is what neither of those give you: **things you only find out by actually calling the API against a live instance** — auth gotchas that 400/401 you until you know the trick, permission-model surprises that aren't obvious from the spec, and a full worked example (Palworld) showing what a real create → inspect → manage → console workflow looks like end to end.

## Contents

- [`GOTCHAS.md`](./GOTCHAS.md) — confirmed-by-testing quirks: required headers, the deprecated-but-working `SESSIONID` auth pattern, per-instance permission nodes that aren't inherited from top-level role grants, and an open question around per-instance console/proxy auth (with a pointer to where CubeCoders' own community has discussed it).
- [`PALWORLD-EXAMPLE.md`](./PALWORLD-EXAMPLE.md) — a worked, end-to-end example against a real game server: find the app in the catalog, inspect a deployed instance, start/stop/restart, send console commands, and script a brand-new instance from scratch. Generalizes to any `GenericModule`-based game, not just Palworld.

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

**Two must-haves or every call fails — see GOTCHAS.md for the full list:**
- `Accept: application/json` header — omit it and you get a 400 `"Invalid accept header value"`.
- A valid session passed as `Authorization: Bearer <sessionID>`.

### 3. Get the full, current method list for your AMP version

Don't rely on a static markdown dump (things change between AMP releases) — either:
- Browse `https://your-amp-panel.example.com/API` directly in your browser, or
- Pull the auto-updated spec from [p0t4t0sandwich/ampapi](https://github.com/p0t4t0sandwich/ampapi) (`APISpec.json` / `FriendlySpec.txt`), or
- Call `POST /API/Core/GetAPISpec` yourself **with a valid authenticated session** — called anonymously it only returns a ~10-method stub (login/2FA/module-info); called authenticated it returns the full surface scoped to your session's role.

## How the notes in this repo were built

1. Logged into the AMP panel in a real browser and captured its own XHR calls via:
   ```js
   performance.getEntriesByType('resource').filter(r => r.name.includes('API/')).map(r => r.name)
   ```
   Reveals every `/API/<Module>/<Command>` the UI actually calls as you click around.
2. Called `Core/GetAPISpec` **with an authenticated admin session** to get the real method list, then cross-checked the calls that mattered against a live instance rather than trusting the spec alone — that's where the gotchas in `GOTCHAS.md` came from.
3. Walked a real deployment (Palworld) through its full lifecycle to produce `PALWORLD-EXAMPLE.md`.

If you're reverse-engineering a different undocumented panel, step 1 + "re-query a self-describing spec endpoint authenticated, not anonymous" generalizes well beyond AMP.

## Disclaimer

Unofficial, community-produced notes — not affiliated with or endorsed by CubeCoders. AMP is actively developed and this API can change without notice; always test against a non-production instance first, and keep credentials/tokens out of scripts and version control.
