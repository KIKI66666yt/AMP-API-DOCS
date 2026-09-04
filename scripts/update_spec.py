#!/usr/bin/env python3
"""
Fetches AMP's live Core/GetAPISpec and ADSModule/GetSupportedApplications,
regenerates API-REFERENCE.md and APP-CATALOG.md. Run by
.github/workflows/update-spec.yml on a schedule via a self-hosted runner
with network access to an internal-only AMP panel.

Required env vars: AMP_URL, AMP_CI_USERNAME, AMP_CI_PASSWORD
"""
import json
import os
import sys
import urllib.request
import ssl
from datetime import datetime, timezone

AMP_URL = os.environ["AMP_URL"].rstrip("/")
USERNAME = os.environ["AMP_CI_USERNAME"]
PASSWORD = os.environ["AMP_CI_PASSWORD"]

# Internal self-signed cert on some homelab panels; verify=False is a
# deliberate tradeoff for an internal-only host reachable only via a
# self-hosted runner on the same trusted network.
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def api_call(module, command, session_id=None, extra=None, timeout=60):
    url = f"{AMP_URL}/API/{module}/{command}"
    body = {"SESSIONID": session_id or ""}
    if extra:
        body.update(extra)
    data = json.dumps(body).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if session_id:
        headers["Authorization"] = f"Bearer {session_id}"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, context=CTX, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def login():
    resp = api_call(
        "Core", "Login",
        extra={"username": USERNAME, "password": PASSWORD, "token": "", "rememberMe": False},
    )
    if not resp.get("success"):
        print("Login failed:", resp, file=sys.stderr)
        sys.exit(1)
    return resp["sessionID"]


def fmt_param(p):
    opt = "optional" if p.get("Optional") else "required"
    t = p.get("TypeName", "")
    name = p.get("Name", "")
    desc = p.get("Description") or ""
    s = f"`{name}`:{t} ({opt})"
    if desc:
        s += f" — {desc}"
    return s


def build_api_reference(spec: dict) -> str:
    order = [
        "Core", "ADSModule", "FileManagerPlugin", "StorePlugin",
        "EmailSenderPlugin", "WebhookPlugin", "CommonCorePlugin",
    ]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = []
    lines.append(f"# AMP API Reference (auto-generated {now})\n")
    lines.append(
        "Generated from `Core/GetAPISpec` called with an authenticated session "
        "by a scheduled GitHub Actions workflow "
        "(`.github/workflows/update-spec.yml`) running on a self-hosted runner "
        "with network access to a live AMP panel. Regenerated automatically — "
        "always current as of the commit date above, unlike a manually "
        "maintained snapshot."
    )
    lines.append(
        "The calling account here has minimal, read-only permissions — see "
        "params/permissions below for what each method needs; this doc "
        "reflects the FULL spec (permissions listed even if this particular "
        "account can't invoke a given method)."
    )
    total = 0
    for mod in order:
        methods = spec.get(mod, {})
        if not methods:
            continue
        lines.append(f"\n## {mod} ({len(methods)} methods)\n")
        for name in sorted(methods.keys()):
            m = methods[name]
            total += 1
            params = m.get("Parameters") or []
            pstr = ", ".join(fmt_param(p) for p in params) if params else "(no params)"
            perms = m.get("RequiredPermissions") or []
            permstr = ", ".join(f"`{p}`" for p in perms) if perms else "(none listed)"
            ret = m.get("ReturnTypeName") or ""
            desc = m.get("Description") or ""
            line = f"- **`{mod}.{name}`**"
            if desc:
                line += f" — {desc}"
            lines.append(line)
            lines.append(f"  - Params: {pstr}")
            lines.append(f"  - Returns: `{ret}`" if ret else "  - Returns: (none)")
            lines.append(f"  - Permissions: {permstr}")
    lines.append(f"\n\nTotal documented: {total} methods.\n")
    lines.append("\n## Call shape reminder\n")
    lines.append(
        "```\n"
        "POST /API/<Module>/<Command>\n"
        "Headers: Content-Type: application/json, Accept: application/json,\n"
        "         Authorization: Bearer <sessionID>\n"
        "Body: {\"SESSIONID\":\"<sessionID>\", <param1>:..., <param2>:...}\n"
        "```\n"
    )
    lines.append(
        "Complex-typed params (`IsComplexType: true`, e.g. `InstanceDatastore`) "
        "need a nested JSON object matching that type's shape — not "
        "discoverable from this spec dump alone. See GOTCHAS.md and "
        "PALWORLD-EXAMPLE.md for worked examples."
    )
    return "\n".join(lines) + "\n"


def build_app_catalog(apps: list) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    apps_sorted = sorted(apps, key=lambda x: (x.get("FriendlyName") or "").lower())
    lines = []
    lines.append(f"# AMP App Catalog — all supported application templates (auto-generated {now})\n")
    lines.append(
        f"AMP's `ADSModule.GetSupportedApplications` call returns every app "
        f"template the panel knows how to deploy — {len(apps)} entries as of "
        f"this commit. Each entry's `Id` is the stable per-app template "
        f"identifier: pass it as the `AppConfigId` provisioning setting when "
        f"calling `ADSModule.CreateInstance` (see PALWORLD-EXAMPLE.md for a "
        f"full worked example), and it reappears as "
        f'`DeploymentArgs["<ModuleName>.Meta.AppConfigId"]` on any instance '
        f"already deployed from this template.\n"
    )
    lines.append(
        "Regenerated automatically by `.github/workflows/update-spec.yml` on "
        "a schedule — always reflects the live catalog, not a stale "
        "snapshot.\n"
    )
    lines.append(f"**Total: {len(apps)} app templates.**\n")
    lines.append("| Friendly Name | Module | Id |")
    lines.append("|---|---|---|")
    for app in apps_sorted:
        name = (app.get("FriendlyName") or "").replace("|", "\\|")
        mod = app.get("ModuleName") or ""
        aid = app.get("Id") or ""
        lines.append(f"| {name} | `{mod}` | `{aid}` |")
    return "\n".join(lines) + "\n"


def main():
    session_id = login()
    spec = api_call("Core", "GetAPISpec", session_id=session_id)
    apps = api_call("ADSModule", "GetSupportedApplications", session_id=session_id)

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    api_ref = build_api_reference(spec)
    with open(os.path.join(repo_root, "API-REFERENCE.md"), "w") as f:
        f.write(api_ref)

    catalog = build_app_catalog(apps)
    with open(os.path.join(repo_root, "APP-CATALOG.md"), "w") as f:
        f.write(catalog)

    total_methods = sum(len(v) for v in spec.values())
    print(f"Wrote API-REFERENCE.md ({total_methods} methods) and APP-CATALOG.md ({len(apps)} apps)")


if __name__ == "__main__":
    main()
