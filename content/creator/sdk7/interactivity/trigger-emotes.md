---
date: 2020-11-20
title: Trigger emotes
description: Make the player perform an emote
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/trigger-emotes/
weight: 4
---


To make a player perform an emote, use the `triggerEmote()` function. Note that only existing default emotes are supported for now. This function takes a single argument:

- `emote`: An emote from the `PredefinedEmote` enum.

```ts
import { triggerEmote } from "~system/RestrictedActions"

const emoter = engine.addEntity()
Transform.create(emoter, { position: { 8, 0, 8 } })
MeshRenderer.setBox(emoter)
MeshCollider.setBox(emoter)
pointerEventsSystem.onPointerDown(
  emoter,
  () => {
    triggerEmote({ predefined: "robot" })
  },
  { button: InputAction.IA_PRIMARY, hoverText: 'Dance' }
)
```

There are some default emotes available to all players:

- `wave`
- `fist_pump`
- `robot`
- `raise_hand`
- `clap`
- `money`
- `kiss`
- `tik`
- `hammer`,
- `tektonik`
- `dont_see`
- `hands_air`
- `shrug`
- `disco`
- `dab`
- `head_explode`

The emote animation is seen both by the player (in 3rd person view) and any other players around. If the player walks, runs or jumps, they will interrupt the animation and return to playing the corresponding animations for these actions.

{{< hint warning >}}
**📔 Note**:  Players can only be animated if they already are standing inside the scene's bounds, not if they are on a neighboring scene.
{{< /hint >}}


Before you can use this feature, you must add the `ALLOW_TO_TRIGGER_AVATAR_EMOTE` permission to the `scene.json` file. If not yet present, create a `requiredPermissions` property at root level in the JSON file to assign it this permission.

```json
  "requiredPermissions": [
    "ALLOW_TO_TRIGGER_AVATAR_EMOTE"
  ],
```

See [Required permissions]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#required-permissions">}}) for more details.

{{< hint warning >}}
**📔 Note**:  To prevent abusive behavior that might damage a player's experience, the ability to make a player perform an emote is handled as a permission. Currently, this permission has no effect in how the player experiences the scene. In the future, players who walk into a scene with this permission in the `scene.json` file will be requested to grant the scene the ability to play emotes on them.
{{< /hint >}}

