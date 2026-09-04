# AMP App Catalog — all supported application templates (auto-generated 2026-09-04)

AMP's `ADSModule.GetSupportedApplications` call returns every app template the panel knows how to deploy — 243 entries as of this commit. Each entry's `Id` is the stable per-app template identifier: pass it as the `AppConfigId` provisioning setting when calling `ADSModule.CreateInstance` (see PALWORLD-EXAMPLE.md for a full worked example), and it reappears as `DeploymentArgs["<ModuleName>.Meta.AppConfigId"]` on any instance already deployed from this template.

Regenerated automatically by `.github/workflows/update-spec.yml` on a schedule — always reflects the live catalog, not a stale snapshot.

**Total: 243 app templates.**

| Friendly Name | Module | Id |
|---|---|---|
| Abiotic Factor | `GenericModule` | `2cd58de5-88a4-49f8-a71a-b09d08d1fd5e` |
| American Truck Simulator | `GenericModule` | `00732a94-88f5-43b8-b211-458ccb83062e` |
| ANEURISM IV | `GenericModule` | `0be856ec-0190-4186-92e1-7f0d20504662` |
| Archean | `GenericModule` | `d10ddf53-3b4b-496f-9e85-1f6d079c5021` |
| ARK: Survival Ascended | `GenericModule` | `218120ac-08ee-466e-9f60-5ba605436e11` |
| ARK: Survival Ascended (Minimal) | `GenericModule` | `03e2b339-49b5-428f-9cfb-6161684e6653` |
| ARK: Survival Evolved | `GenericModule` | `216356ee-197d-4eec-852d-d22256613b59` |
| ARK: Survival Evolved (Minimal with Server API) | `GenericModule` | `902f0fa7-da27-4d83-9899-e962b57c115e` |
| ARK: Survival Evolved (Minimal) | `GenericModule` | `e7892e8e-6b8f-4ce8-a34b-c5178f9f5899` |
| Arma 3 | `GenericModule` | `22f6f6c7-57c1-41aa-82c1-30875df9ff09` |
| Arma Reforger | `GenericModule` | `23e04f07-dab1-4741-a6e9-e9d0d292c8f1` |
| ASKA | `GenericModule` | `d0722498-28c5-4306-992e-afb198233966` |
| Assetto Corsa | `GenericModule` | `25c90491-a76b-4c57-8620-6fd9116e2cae` |
| Assetto Corsa Competizione | `GenericModule` | `27bf55ba-c744-42b1-ac5d-e6aaeacc9e85` |
| Astro Colony | `GenericModule` | `27e85739-18a4-4613-ab70-5a185d32eb4a` |
| Astroneer | `GenericModule` | `2a9f3285-5adc-4574-8a5b-d6ef39e8b7a0` |
| Avorion | `GenericModule` | `2b7ce232-f1db-44b3-847b-0379f6a99884` |
| Barotrauma | `GenericModule` | `2bb03c90-d662-4e3c-beca-ad136aac973b` |
| BeamMP | `GenericModule` | `2cab46a3-651b-49be-bbd1-51a5d098924a` |
| Beasts of Bermuda | `GenericModule` | `e79b39ca-9383-4713-9333-7f78960c4a19` |
| Black Mesa | `GenericModule` | `9e92924b-0032-4e70-b19a-7636731567de` |
| Blackwake | `GenericModule` | `2d46f35d-6703-4ef9-8240-c9d45bd42dbd` |
| Broke Protocol | `GenericModule` | `2fcb1ab6-7ca6-4a78-af34-db7f6185c1db` |
| Bun App Runner | `GenericModule` | `01bc40d4-5fe5-44e5-ac91-a3153cab947f` |
| Call of Duty 4: Modern Warfare | `GenericModule` | `31213330-971c-4538-aebb-6abb44c3d9d2` |
| Call of Duty: Black Ops (Plutonium Mod) | `GenericModule` | `90d45ec8-5c9b-4929-bcbe-c87c0f4c5249` |
| Call of Duty: Black Ops II (Plutonium Mod) | `GenericModule` | `33c34501-5f7b-492c-9fb8-b33402471950` |
| Call of Duty: Modern Warfare 2 (2009) | `GenericModule` | `31ce3972-13ec-40cc-a902-32272363dc3c` |
| Call of Duty: Modern Warfare 3 (2011 - Plutonium Mod) | `GenericModule` | `a2c8ed86-117d-4f85-a2a1-069e6a75bc69` |
| Call of Duty: Modern Warfare 3 (2011) | `GenericModule` | `3228d505-03f2-4a5a-88b0-a695cf3caf42` |
| Call of Duty: World at War (Plutonium Mod) | `GenericModule` | `8fa2eeea-23c6-44e3-a25f-389f036b9518` |
| Carrier Command 2 | `GenericModule` | `32342459-46ae-444f-95dd-58de5fefcbc1` |
| Chivalry: Medieval Warfare | `GenericModule` | `32ddc446-605f-44f1-9a9c-e946ff4d2fa9` |
| Clone Hero | `GenericModule` | `e5b3efbb-a83c-4d1d-af69-5c186cea8ddb` |
| code-server | `GenericModule` | `7d3f9192-9467-4c0d-b003-d0d5365342ee` |
| Colony Survival | `GenericModule` | `8c56d7d3-fb12-48ee-b124-7814df6a9b34` |
| Conan Exiles (Legacy) | `GenericModule` | `33716b55-127d-43b1-a764-f9467ee5da1f` |
| Conan Exiles Enhanced | `GenericModule` | `95ab603e-0f31-463c-8d1b-c9a5338a65a2` |
| Core Keeper | `GenericModule` | `338b48a0-21ae-498e-864f-6b91e583f31e` |
| Counter-Strike 1.6 | `GenericModule` | `081b373a-90d8-437b-ae32-0781f6eed658` |
| Counter-Strike 2 | `GenericModule` | `3446bb16-65ea-45fc-993b-cac42f15bd2b` |
| Counter-Strike: Condition Zero | `GenericModule` | `e868f70d-8042-4c55-8ae5-283f8bb0569d` |
| Counter-Strike: Global Offensive | `GenericModule` | `49f9ced8-621b-47c8-ab4f-8a6bcc430dd3` |
| Counter-Strike: Source | `GenericModule` | `09832de0-ca96-49a6-a1b5-f1d6b333f2ad` |
| Craftopia | `GenericModule` | `345b28dd-a777-4f34-b3d5-f99f540dbb7f` |
| Creativerse | `GenericModule` | `34fc091c-f0bf-4a36-a792-1e05928ce816` |
| CryoFall | `GenericModule` | `371ff279-889a-4fa0-ac43-b422adb2802c` |
| Cube 2: Sauerbraten | `GenericModule` | `6fddd2e7-c28c-4f4f-9681-7c7a9889e5ee` |
| Cubic Odyssey | `GenericModule` | `96725b82-a751-460b-b47b-b1b748e0fa84` |
| Custom Application | `Generic` | `d0e52be7-e0b7-444a-9be3-0101e5ef2591` |
| Day of Defeat | `GenericModule` | `44e92a01-51d4-4fa0-9434-936d684a6f63` |
| Day of Defeat: Source | `GenericModule` | `43647b2f-753a-4efd-bf0e-631a83f3f0eb` |
| Day of Dragons | `GenericModule` | `3a686aaa-471c-4d9a-ad7b-12c37e4f81a5` |
| DayZ (Experimental) | `GenericModule` | `3f142716-638e-4b63-91a2-cf8eda4c1370` |
| DayZ (Stable) | `GenericModule` | `4241cc0f-4604-4600-b103-80134f949278` |
| Dead Matter | `GenericModule` | `4241cc0f-4604-4600-b103-80134f970978` |
| DeadPoly | `GenericModule` | `a6dc3bb1-58a5-4489-a676-ede0e81761e9` |
| Deno App Runner | `GenericModule` | `948fa5ab-5a0a-427f-ab4d-9edbd2269ae5` |
| Desynced | `GenericModule` | `32917856-06d8-4ffb-bef2-6d0142b03891` |
| Don't Starve Together | `GenericModule` | `447da625-361c-4177-b6c6-91672712eb37` |
| DOOM II (Zandronum Mod) | `GenericModule` | `cefb36aa-67d2-44ee-aefc-403b1181eb2c` |
| Dota 2 | `GenericModule` | `a7fe57f3-ad6f-434b-8889-41caf54edb86` |
| Dotnet App Runner | `GenericModule` | `412fd058-1289-4f69-9ee3-6923d763c4ac` |
| Dummy Module | `Dummy` | `660c5ac4-795f-4ad5-94ba-4fbeb3c1dee8` |
| Dune Awakening | `GenericModule` | `8d7e92b1-1f4a-4a26-9c7e-fdc3a04b1ce0` |
| E.Y.E: Divine Cybermancy | `GenericModule` | `1a94df2a-36b5-4d53-8989-1710945a94ae` |
| Eco | `GenericModule` | `45876689-7f1f-4144-8c18-3ef93db2076f` |
| Empyrion Galactic Survival | `GenericModule` | `4628ba74-b008-4a39-b481-126d2c1e8c22` |
| Enshrouded | `GenericModule` | `473ef3af-bc0b-4555-a42b-9f6393ffd29f` |
| ET: Legacy | `GenericModule` | `9af43196-9319-480e-b2db-c3c3bd7101eb` |
| Euro Truck Simulator 2 | `GenericModule` | `47516b74-5a4c-4acf-b68b-e06f5a268d97` |
| EXFIL | `GenericModule` | `5cbe1ebc-dcc5-4852-8232-7eded2073fac` |
| Factorio | `GenericModule` | `50882765-e275-413b-91a6-28f0fd821fde` |
| Farming Simulator 19 | `GenericModule` | `c0014aac-0359-43de-9548-f51b7d8a2737` |
| Farming Simulator 22 | `GenericModule` | `d5daa870-c0a2-430a-b289-bc59a8e5d7a5` |
| Farming Simulator 25 | `GenericModule` | `0245cfc5-5fb5-4919-9cb8-c51cccbe31ae` |
| Fistful of Frags | `GenericModule` | `8ad0565c-2fb9-4303-b43d-479c0b915030` |
| FiveM - Grand Theft Auto V Server | `GenericModule` | `aa5de5cd-d1b4-4432-906f-07c0360280de` |
| FOUNDRY | `GenericModule` | `56105756-01a5-4658-b9c7-643ffedc4766` |
| Foundry Virtual Tabletop | `GenericModule` | `4a86aad1-8b35-4744-9a5e-5dd65f976329` |
| Frozen Flame | `GenericModule` | `4e7c416b-858c-4dc5-a329-5bdb57779e42` |
| Garry's Mod | `GenericModule` | `3d7b363b-888e-4807-bd0c-93f03ceb8fde` |
| Garry's Mod (64 Bit) | `GenericModule` | `d148de8d-77b6-4087-a8fb-080cd5a9667a` |
| Geyser | `GenericModule` | `54b81b0a-ad03-4cc2-afa1-703c73f15456` |
| Ground Branch | `GenericModule` | `58804602-3a83-43c4-a05b-815e61c6cbf4` |
| Half-Life | `GenericModule` | `c02078b4-82bc-458d-9cb0-b6972dcdedbd` |
| Half-Life 2: Deathmatch | `GenericModule` | `841df43e-8253-4054-ab0e-348e7a588300` |
| Half-Life Deathmatch: Source | `GenericModule` | `3cad9437-4952-41c4-8a19-951e6e7afa6a` |
| Half-Life: Opposing Force | `GenericModule` | `6dc4036e-f3eb-4983-8a76-29cc8a0ccfae` |
| HumanitZ | `GenericModule` | `5c3e6051-0fcf-4988-b6da-bde28bce4fb1` |
| Hurtworld | `GenericModule` | `5e743431-f467-4540-ab6b-983e5f9978e0` |
| Hytale | `GenericModule` | `36d2e805-a54d-4a40-acc9-c101c720ae05` |
| Icarus | `GenericModule` | `630a4794-6466-4de6-956d-91393d6f48e1` |
| Impostor - Among Us Server | `GenericModule` | `651bda41-8294-4964-a6b8-e7a8dff4c310` |
| Insurgency Sandstorm | `GenericModule` | `684b4b01-ddbc-4079-9e76-1520c61fb487` |
| Java App Runner | `GenericModule` | `521c9ad3-f8cd-40b2-9026-9122f9490406` |
| Just Cause 3 Multiplayer Mod | `GenericModule` | `6d39cdca-d89e-4f8f-9069-eb10edb408cd` |
| Kaboom! | `GenericModule` | `73ffb6d5-50e1-4c59-bce1-4469c9814544` |
| Killing Floor | `GenericModule` | `e9faea21-5663-42bc-9f6d-0f7dfdf1befa` |
| Killing Floor 2 | `GenericModule` | `75f76d07-e6a2-4b45-868a-8fc7e9bea137` |
| Last Oasis | `GenericModule` | `7e924ac7-911d-481a-8d56-e34e3f12a78a` |
| Left 4 Dead | `GenericModule` | `99544eaf-cce1-4608-b0d9-144ea11a073d` |
| Left 4 Dead 2 | `GenericModule` | `eba6a05b-2b75-4ac5-a631-21a7134027d5` |
| Longvinter | `GenericModule` | `8257700a-6174-4dca-8c7f-b47f5b31d291` |
| Longvinter (Linux Wine) | `GenericModule` | `4298f6bb-9ae0-413b-9803-a1741b0d8ffd` |
| Luanti | `GenericModule` | `b3a98938-d2ba-4018-9cf7-17ad8c73ef89` |
| MariaDB | `GenericModule` | `dbc03533-2478-4262-a262-49231c1dca7f` |
| McMyAdmin 3 (MCMA2 Licence Keys Only) | `McMyAdmin` | `75686943-2ff3-4a6f-96f5-98609fb6291c` |
| Mindustry | `GenericModule` | `83353a75-65b5-469e-8ba8-b5c04b360f0e` |
| Minecraft Bedrock | `GenericModule` | `f5e21acb-3c6d-4480-9c92-7395bd0c1cbd` |
| Minecraft BungeeCord Proxy | `Minecraft` | `d0b27f07-bcef-4b6d-863b-a8ddcc4f8793` |
| Minecraft Java Edition | `Minecraft` | `6d4005de-ee53-429c-8940-8d2e0f7ae62e` |
| Minetest (Legacy) | `GenericModule` | `87ad16e1-30ee-49c4-8916-8e29adeb688f` |
| Miscreated | `GenericModule` | `a0ee7e94-a28a-4694-9f95-24f7508b91ac` |
| MongoDB | `GenericModule` | `ac96d196-861c-4c32-9014-62d33e0d3935` |
| Mordhau | `GenericModule` | `87af5cd3-3521-4eb7-a3e3-fa3cf8203947` |
| Mount & Blade II: Bannerlord | `GenericModule` | `88800028-6407-49ad-876a-37fa7f6dc4cf` |
| Multi Theft Auto: San Andreas | `GenericModule` | `d8cf52eb-32a0-4cca-9b2f-af2d87888fe4` |
| MX Bikes | `GenericModule` | `5303d616-c8e6-4794-9b52-ca1314b770db` |
| MySQL | `GenericModule` | `28c2dbb4-8fab-47ae-a50f-64f2d2a62469` |
| Myth of Empires | `GenericModule` | `45783c08-8ad8-4027-b45a-60a48c171d9c` |
| NEBULOUS: Fleet Command | `GenericModule` | `8b2dba1e-7448-4299-be82-607fe4da7429` |
| Necesse | `GenericModule` | `8b4b5d2d-c5fe-419f-8106-647a5a236fd0` |
| Night of the Dead | `GenericModule` | `8bbcc16d-38b6-45bb-a9e4-cc13b6d49b38` |
| Nightingale | `GenericModule` | `21d3b934-c789-40e7-bc53-5181d7e618ea` |
| No More Room in Hell | `GenericModule` | `75b09896-73b0-458f-b3e4-811d64bffd9c` |
| No One Survived | `GenericModule` | `8ee4dcd5-e3e4-486a-9272-9070c9b32606` |
| Node.js App Runner | `GenericModule` | `fff18432-bef2-462d-b209-e346d6b3a1e7` |
| Nuclear Option | `GenericModule` | `71a84ca4-afd1-4fc3-91f4-fa9335a9ea79` |
| Nukkit | `GenericModule` | `04b2978f-1595-41d2-81c1-4d5e823b236b` |
| Open World - RimWorld Server | `GenericModule` | `aabc8955-be70-4361-8024-45b1a1f3a7f0` |
| open.mp - Grand Theft Auto: San Andreas Server | `GenericModule` | `8de4b186-921c-4a3d-89a3-6b1c9019cd78` |
| OpenRA - Dune 2000 | `GenericModule` | `8f92deb8-04c1-4ffb-ac30-59886563346d` |
| OpenRA - Red Alert | `GenericModule` | `90715f92-951f-4740-9539-e47f11175d53` |
| OpenRA - Tiberian Dawn | `GenericModule` | `92f606b9-11ac-420c-ad5d-9d7d85dcc2dc` |
| OpenRCT2 | `GenericModule` | `9ac30173-aff1-438a-ba5c-29bd09e0c7dd` |
| OpenStarbound | `GenericModule` | `0370e4cc-b62f-42df-ac54-078e8c754a2e` |
| OpenTTD | `GenericModule` | `a2993b11-652a-4717-b826-e4916774c309` |
| Operation: Harsh Doorstop | `GenericModule` | `ae028804-06ef-4924-addf-5a4a2dcbf15f` |
| Palworld | `GenericModule` | `afacd4b2-eb92-4668-8068-9a9975651f54` |
| Palworld (Modded) | `GenericModule` | `aa4a646a-f7bd-49ce-9042-ddb0573f0087` |
| Path of Titans | `GenericModule` | `b7a9a499-80a5-4f04-b781-92c11f72ed9a` |
| Pavlov VR | `GenericModule` | `bc724dfb-6d14-4698-8a19-66511731e7c1` |
| Pirates, Vikings, & Knights II | `GenericModule` | `292b7f25-3f48-4d87-9e29-660a214ac90e` |
| PixARK | `GenericModule` | `79bb4c35-7e34-4ce7-b685-ccded8c4f1d7` |
| Plains of Pain | `GenericModule` | `4b2fa406-6285-4ad0-a64f-fd79b2ba6c5a` |
| PocketMine-MP | `GenericModule` | `c756e383-7603-4d29-8929-cd0b03dea3c2` |
| Portal Knights | `GenericModule` | `be7abe76-5350-4519-8746-0f3e0d7c5ec6` |
| PostgreSQL | `GenericModule` | `d9f557e2-7b9c-429f-a8a5-8a2fd75c2956` |
| Pre-Fortress 2 | `GenericModule` | `4eb7bcbb-4804-4338-a490-872d8fb00cb9` |
| Project 5: Sightseer | `GenericModule` | `c032ed6f-3f44-43e7-b091-b91899588836` |
| Project Zomboid | `GenericModule` | `c2b4163c-cf2a-4d67-b6bb-5fee166b4d33` |
| Puck | `GenericModule` | `f0b1a8cd-da69-4907-a844-a191d7587e21` |
| Pumpkin | `GenericModule` | `c7ab5772-934a-4f9b-a822-1776f4817815` |
| Python App Runner | `GenericModule` | `c4cb3198-7b63-469d-959f-17a965d061ac` |
| Quake III Arena | `GenericModule` | `c53aa8ff-6ae9-47a2-892c-71e9640f7fc1` |
| Quake Live | `GenericModule` | `44743d77-688a-4f7e-aa56-9a06dd8c7d2b` |
| RAGE:MP - Grand Theft Auto V Server | `GenericModule` | `bb8773de-7ce7-42fc-a5be-3871e467b2cf` |
| RedM - Red Dead Redemption 2 Server | `GenericModule` | `5bc891bd-ce22-43f6-a05b-e508079818f0` |
| Reign Of Kings | `GenericModule` | `e89c7bc6-cff2-414c-8568-f995c0ce07d6` |
| Renown | `GenericModule` | `3a94e6c8-e0f9-4008-afc8-903c7e372bad` |
| Rimworld Together - RimWorld Server | `GenericModule` | `c63ac544-9a15-4063-9fd1-3af1ad4ca3fd` |
| Rising Storm 2: Vietnam | `GenericModule` | `e5c0aab3-7731-42d1-bb89-fa06a2741fc0` |
| Rising World (Unity Version) | `GenericModule` | `14d98639-b462-430f-ab3a-62447f231d9c` |
| Romestead | `GenericModule` | `8c2abb25-fda3-4514-9e49-75db2fa58a20` |
| RuneScape: Dragonwilds | `GenericModule` | `f3b46437-6928-4fc3-8646-62e4a43cd2fc` |
| Rust | `Rust` | `ee3e0d6d-1425-4463-8ff6-51557d58af28` |
| San Andreas Multiplayer | `GenericModule` | `c85544d6-8e56-44c7-bf23-00a9fcdaa19f` |
| Sapiens | `GenericModule` | `96a4d023-a381-424b-8cfc-404d932be4ff` |
| Satisfactory | `GenericModule` | `c9eabe8e-5219-4c16-8692-14740d5f8e92` |
| SCP: Secret Laboratory | `GenericModule` | `d26e2770-d31f-4cb6-8ca5-c5031c091fe4` |
| SCUM | `GenericModule` | `721f4476-0b57-4765-9f36-21cbae019e46` |
| Seven Days To Die | `GenericModule` | `d2bef27b-ca22-4528-bc94-29fe3825b4a1` |
| SinusBot | `GenericModule` | `78e4f069-edb6-4eda-864b-6c447e27dc8a` |
| Skyrim Together Reborn | `GenericModule` | `d467f2ce-fc4f-41c5-8b5c-0fe031beea9b` |
| Smalland: Survive the Wilds | `GenericModule` | `da75c6a6-0791-4734-ac6a-33c43d46f89e` |
| Soldat | `GenericModule` | `201ba50c-ad18-42d3-9ae8-891c7b5cb831` |
| Sons Of The Forest | `GenericModule` | `da9e2786-d2b8-4c1f-bc9d-b1ec844bd70d` |
| Soulmask | `GenericModule` | `d9cf5fcb-d4b3-4157-8b18-016b58cdbefe` |
| Space Engineers | `GenericModule` | `db79e8ff-33aa-41e9-ac5e-0fc7be43118e` |
| Space Engineers (Torch) | `GenericModule` | `c4d7ecad-c1dd-4b11-86a7-f6f2b9bbd491` |
| Spellmasons | `GenericModule` | `1a088c8c-7fa1-47ce-9a33-003f75905836` |
| Squad | `GenericModule` | `ddb38381-7434-43e2-8919-3c394b1932b1` |
| Squad 44 | `GenericModule` | `c006c56b-790a-4813-8ef4-71589516247e` |
| STAR WARS Jedi Knight - Jedi Academy | `GenericModule` | `15765dd8-56dc-4c3a-a376-3719ed41485f` |
| Starbound | `GenericModule` | `e6039009-631b-4a7e-b93c-7a66769c9ba8` |
| Stardew Valley | `GenericModule` | `f55ef901-d6bf-4ee2-a625-7aff0c3f873a` |
| Starmade | `GenericModule` | `e831989f-f6a9-418e-b9ac-04a169327c69` |
| StarRupture | `GenericModule` | `054884dc-e560-4efe-8e91-fca3478da59d` |
| Stationeers | `GenericModule` | `e8a7327f-2b8d-4af7-8b98-38026fb60885` |
| Staxel | `GenericModule` | `e8d63df4-2767-4032-9000-e8fc8fc5c94c` |
| Stormworks | `GenericModule` | `eb5e3105-cc52-4c7e-bea7-9acb00cb8924` |
| Subnautica (Nitrox Mod) | `GenericModule` | `4fc619ca-1562-43ff-9c06-1e547d019423` |
| Subsistence | `GenericModule` | `5eb09982-8804-4e9c-bc81-79338b5308bb` |
| Sunkenland | `GenericModule` | `ecfcaabc-f77c-4c10-a386-7aad24271417` |
| Sven Co-op | `GenericModule` | `f0742555-a94a-437b-a4de-65f7a4646c6b` |
| Swords 'n Magic and Stuff | `GenericModule` | `f2001731-339a-446e-90ad-f345eaf74bbd` |
| Synergy | `GenericModule` | `1a2b1d98-04f3-4b5c-b573-d61b3322da9c` |
| Tarkov (Fika Mod) (Legacy) | `GenericModule` | `f6d61670-52d9-4480-b889-5acba1afb555` |
| Tarkov (Fika Mod) 4.0.0+ | `GenericModule` | `ed44da25-4075-4e31-b563-540a1559bf28` |
| Tarkov (Fika Mod) 4.1.0+ | `GenericModule` | `f27f1374-5fbc-4870-836b-b01e393d6e1e` |
| Team Fortress 2 | `GenericModule` | `1fe85447-6ec1-46e2-9f8c-2b6b2dda7c6a` |
| Team Fortress 2 (64 Bit) | `GenericModule` | `1fe85447-6ec1-46e2-9f8c-2b6b2dda7c6b` |
| Team Fortress 2 Classified | `GenericModule` | `dc696aa5-db45-4339-8162-7e659375ee66` |
| Team Fortress Classic | `GenericModule` | `d1336d3f-cea2-43a7-ad04-28602de5842c` |
| TeamSpeak 3 | `GenericModule` | `f249d165-d473-4e52-8c9a-9181c6907f60` |
| TeamSpeak 6 | `GenericModule` | `abb20bca-3c7e-4f74-9bd6-ff9a21a04aef` |
| TeaSpeak | `GenericModule` | `aca10e5c-0dcb-4e8a-a92b-24375074ab01` |
| Teeworlds | `GenericModule` | `c4021427-e349-48ef-9afe-99b3bc3560b3` |
| Terraria | `GenericModule` | `f40e763f-9d98-4773-bcc8-1b9424ff0671` |
| TerraTech Worlds | `GenericModule` | `5936cadc-a3cd-43f0-b06a-df8e829f665f` |
| TES3MP - The Elder Scrolls III: Morrowind Server | `GenericModule` | `1a00b3e2-b8f1-45ce-ba14-478cc79f0c1c` |
| The Forest | `GenericModule` | `f4864f21-507e-430c-84d5-077c99c79493` |
| The Front | `GenericModule` | `f50fa0ca-b155-447c-9e43-adf702a416cf` |
| The Isle (EVRIMA) | `GenericModule` | `f92c4ed8-de69-4a2d-a558-087b91cf2572` |
| The Isle (Legacy) | `GenericModule` | `fd6456b1-c0a8-429a-b0ab-e6d03c46aff8` |
| The Lord of the Rings: Return to Moria | `GenericModule` | `057d8d45-4ba2-49ef-a555-c9e506cf3ca6` |
| Titanfall 2 | `GenericModule` | `7fbe40b3-2c28-45c6-aa97-be2673fc3a1b` |
| tModLoader (Legacy) | `GenericModule` | `fd699a6e-30db-446c-9879-3c36474c5f84` |
| tModLoader 1.4+ | `GenericModule` | `fdc54950-3d99-4343-9bb7-a0f2051e1092` |
| Tower Unite | `GenericModule` | `c3417ee8-328b-4bc7-9a50-44c3cc12fb89` |
| TShock - Terraria Server | `GenericModule` | `ffc05d27-8104-4235-81ec-4120cf254c17` |
| Turbo Sliders Unlimited | `GenericModule` | `b0cd5dba-437c-4d06-9bcf-2409559641d2` |
| txAdmin | `GenericModule` | `7f7c01fc-8c2b-4d64-b47d-85f3a416cc72` |
| Unreal Tournament 2004 | `GenericModule` | `1d67b152-c82c-4271-94a9-ce7ead121d2f` |
| Unreal Tournament 99 | `GenericModule` | `047a26bb-498f-4aef-9384-766e0b469388` |
| Unturned | `GenericModule` | `1f00f476-2adf-4a4f-a748-846c40fa4f31` |
| V Rising | `GenericModule` | `0ff28908-3b0b-4cd4-b9bd-0d468d676032` |
| Valheim | `GenericModule` | `1b7a66b4-6a89-47e3-9d18-5afa37a4634e` |
| VEIN | `GenericModule` | `e4161021-bd97-4306-a8e7-ec1c32947e0f` |
| Veloren | `GenericModule` | `18c71931-6fb7-48ac-bde6-f729fd2195c8` |
| Vintage Story (Legacy) | `GenericModule` | `176e6c0d-a9a6-471e-9804-d09c4268a760` |
| Vintage Story 1.18.8+ | `GenericModule` | `161f1dcd-f9c5-47d8-b191-f9dceecd4fc6` |
| Voyagers of Nera | `GenericModule` | `a530b939-e389-494a-95df-efa1d0e90d9f` |
| Windrose | `GenericModule` | `719703a2-78d0-45fc-86c7-3d548aba1706` |
| Windward | `GenericModule` | `0df3f578-aa36-4bf1-9f8e-faa07331cab3` |
| Windward Horizon | `GenericModule` | `a67da478-c59c-4d80-8fee-50b27dd55713` |
| Wolfenstein: Enemy Territory | `GenericModule` | `0d5c6d2d-655e-46f3-8ef3-68d932ca1864` |
| Wreckfest | `GenericModule` | `0cc5d165-c521-473b-aa8b-b6f7a9b2d281` |
| Wreckfest 2 | `GenericModule` | `17f9ff01-e66e-4562-ae32-911bc011373f` |
| Wurm Unlimited | `GenericModule` | `09442f29-bba9-40fe-bae8-332c8ea631b2` |
| Xonotic | `GenericModule` | `02440481-2c3d-4098-8c5f-8690bd62c442` |
| Zombie Panic! Source | `GenericModule` | `5f2f5cb2-0e21-4a9c-963e-51b4eb379add` |
