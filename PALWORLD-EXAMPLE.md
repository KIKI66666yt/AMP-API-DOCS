# Worked example: managing a Palworld server

A concrete walkthrough using a real game (Palworld) to show the full lifecycle: find the app, read its config, start/stop/restart it, and script a brand-new instance. Palworld happens to run under AMP's generic `GenericModule` wrapper (the same wrapper many non-native-AMP games use), so this example is a good template for other `GenericModule`-based games too.

All examples assume you already have a session — see README.md for the login call. Replace `<sessionID>` and `your-amp-panel.example.com` throughout.

## 1. Find Palworld in the app catalog

```bash
curl -sk -X POST "https://your-amp-panel.example.com/API/ADSModule/GetSupportedApplications" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>"}'
```

This returns **every** app AMP knows how to deploy (240+ entries) as one large array — don't print it raw, filter for `"FriendlyName": "Palworld"` (or similar) in the response. Each entry looks like:

```json
{
  "Id": "afacd4b2-eb92-4668-8068-9a9975651f54",
  "FriendlyName": "Palworld",
  "Description": "...",
  "ModuleName": "GenericModule",
  "Settings": { "...": "..." }
}
```

The `Id` here is the stable per-app template identifier — it reappears later as `DeploymentArgs["GenericModule.Meta.AppConfigId"]` on any deployed instance of this app, which is how you can confirm which app catalog entry an existing instance corresponds to.

## 2. Inspect an already-deployed instance

```bash
curl -sk -X POST "https://your-amp-panel.example.com/API/ADSModule/GetInstance" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>", "InstanceId":"<instance-guid>"}'
```

Key fields in the response for a Palworld instance:

```json
{
  "InstanceID": "...",
  "InstanceName": "Palworld01",
  "FriendlyName": "My Palworld Server",
  "Module": "GenericModule",
  "Running": true,
  "AppState": "Ready",
  "Metrics": { "CPU": {...}, "Memory": {...}, "Users": {...} },
  "DeploymentArgs": {
    "GenericModule.Meta.AppConfigId": "afacd4b2-eb92-4668-8068-9a9975651f54",
    "...GamePort...": 8211,
    "...RESTAPIPort...": 8212,
    "...QueryPort...": 27015,
    "...RCONPort...": 25575
  }
}
```

`ADSModule/GetInstances` (no `InstanceId` param) returns this same shape for **every** instance in one call — that's the best single call for a fleet-status dashboard, and its `Metrics` field is populated live without needing any special console session (see GOTCHAS.md — true per-instance console access is a separate, unsolved problem; this metrics polling is the practical workaround).

## 3. Start / stop / restart

All three take the instance's **name**, not its GUID:

```bash
# Start
curl -sk -X POST "https://your-amp-panel.example.com/API/ADSModule/StartInstance" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>", "InstanceName":"Palworld01"}'

# Stop
curl -sk -X POST "https://your-amp-panel.example.com/API/ADSModule/StopInstance" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>", "InstanceName":"Palworld01"}'

# Restart (stops, then auto-starts again within ~15s)
curl -sk -X POST "https://your-amp-panel.example.com/API/ADSModule/RestartInstance" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>", "InstanceName":"Palworld01"}'
```

All three return `{"Status":true,"Reason":null}` on success.

## 4. Send a console command

```bash
curl -sk -X POST "https://your-amp-panel.example.com/API/Core/SendConsoleMessage" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>", "message":"Broadcast Hello from the API"}'
```

**Important:** `Core/SendConsoleMessage` and `Core/GetUpdates` operate on whatever instance your *current session's context* is — for a top-level admin/API session that's the AMP controller itself, not an arbitrary game instance. `ADSModule.ManageInstance(InstanceId)` looks like it should switch context but does not, in testing (see GOTCHAS.md for the full writeup of that dead end). In practice this means: scripted console commands work reliably when sent from a session that is *already scoped* to that instance (e.g. the way the web UI does it internally via a proxied token) — plain top-level API sessions can reliably **poll metrics and call lifecycle actions** (start/stop/restart) but true two-way console access from outside the browser remains unsolved.

## 5. Create a brand-new Palworld instance (scripted deploy)

This is the scriptable equivalent of the "Create Instance" wizard in the UI. Three calls:

**a) Get the exact provisioning fields this module expects:**

```bash
curl -sk -X POST "https://your-amp-panel.example.com/API/ADSModule/GetProvisionArguments" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>", "ModuleName":"GenericModule"}'
```

Returns a list of `ProvisionSettingInfo` objects — the setting node names and types you'll need to populate in `ProvisionSettings` below.

**b) Confirm your target (single-node installs just need the local target):**

```bash
curl -sk -X POST "https://your-amp-panel.example.com/API/ADSModule/GetTargetInfo" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{"SESSIONID":"<sessionID>"}'
```

**c) Create the instance:**

```bash
curl -sk -X POST "https://your-amp-panel.example.com/API/ADSModule/CreateInstance" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -H "Authorization: Bearer <sessionID>" \
  -d '{
    "SESSIONID":"<sessionID>",
    "TargetADSInstance":"<target-guid-from-GetTargetInfo>",
    "NewInstanceId":"<a-new-guid-you-generate-or-get-from-Core/GetNewGuid>",
    "Module":"GenericModule",
    "InstanceName":"Palworld02",
    "FriendlyName":"My Second Palworld Server",
    "IPBinding":"0.0.0.0",
    "PortNumber":8211,
    "AdminUsername":"admin",
    "AdminPassword":"<a-strong-password>",
    "ProvisionSettings": { "GenericModule.Meta.AppConfigId": "afacd4b2-eb92-4668-8068-9a9975651f54" },
    "AutoConfigure": true,
    "StartOnBoot": true
  }'
```

`AutoConfigure: true` tells AMP to generate sane defaults for everything except Module/Target/FriendlyName — the safest starting point if you don't want to hand-populate every provisioning field yourself. Once `AutoConfigure` is off, every field `GetProvisionArguments` listed becomes your responsibility to fill in `ProvisionSettings`.

**Note:** this create call is documented from the spec and cross-checked against a real deployed instance's resulting `DeploymentArgs`, but wasn't stress-tested against every edge case (e.g. custom port ranges, non-default datastores) — treat it as a strong starting template, not a guarantee, and verify the resulting instance's config with `GetInstance` after creating it.

## Applies beyond Palworld

Anything running under `GenericModule` (rather than a game with its own dedicated AMP module) follows this exact same pattern — swap the `AppConfigId` for the target app's `Id` from `GetSupportedApplications`, and re-run `GetProvisionArguments` for that module to get the right field names.
