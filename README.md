# AMP-API-DOCS

Field notes and worked examples for [CubeCoders AMP](https://cubecoders.com/AMP)'s HTTP API — the real-world quirks, permission gotchas, and end-to-end workflows you hit once you go past "here's the method list."

## This is a companion, not a duplicate

There's a community project for AMP's raw API surface:

**→ [p0t4t0sandwich/ampapi](https://github.com/p0t4t0sandwich/ampapi)** — `APISpec.json` / `FriendlySpec.txt`, a `ModuleInheritance.json` mapping which plugin modules each instance type (GenericModule, Minecraft, Rust, srcds, FiveM, ADS) actually inherits, and client libraries in C#, Node, Python, Java, Go, and Rust.

**⚠️ Stale as of this writing:** its last commit was May 31, 2025, pinned to AMP v2.6.2.0 — several versions behind current AMP releases (v2.8.0.4+). The repo's `update_spec.yml` GitHub Actions workflow that's supposed to auto-refresh the spec on a schedule has its trigger **commented out**, so despite the README's "automagically updates" claim, it isn't actually being kept current. Still useful for the `ModuleInheritance.json` mapping and the client libraries, but **don't trust its `APISpec.json`/`FriendlySpec.txt` as current** — pull the spec live instead (see step 3 below), which always matches your exact installed AMP version.

**Also worth knowing:** your own AMP panel serves built-in interactive API docs at `https://<your-panel>/API` (the "AMP API Browser") — no separate tooling needed, and it's guaranteed to match your exact AMP version.

This repo doesn't try to be a static method-list dump (those go stale, as above) — it's what a snapshot alone doesn't give you: **things you only find out by actually calling the API against a live instance** — auth gotchas that 400/401 you until you know the trick, permission-model surprises that aren't obvious from any spec, and a full worked example (Palworld) showing what a real create → inspect → manage → console workflow looks like end to end.

## Contents

- [`SKILL.md`](./SKILL.md) — a self-contained, portable skill file for AI coding agents (Claude, Cursor, etc.) — drop it into your agent's skills directory and it'll know how to authenticate, call the API, avoid the gotchas below, and set up a least-privilege service account, without needing the rest of this repo loaded.
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

Don't rely on a static markdown dump (things change between AMP releases, and third-party mirrors can go stale — see the p0t4t0sandwich/ampapi note above). In order of freshness:
- Call `POST /API/Core/GetAPISpec` yourself **with a valid authenticated session** — called anonymously it only returns a ~10-method stub (login/2FA/module-info); called authenticated it returns the full surface scoped to your session's role, guaranteed to match your exact running AMP version.
- Browse `https://your-amp-panel.example.com/API` directly in your browser (same guarantee, human-readable).
- [p0t4t0sandwich/ampapi](https://github.com/p0t4t0sandwich/ampapi)'s `APISpec.json`/`FriendlySpec.txt` — useful for the module-inheritance mapping, but check its last-commit date before trusting the spec itself as current.

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
