---
date: 2020-11-20
title: Trigger emotes
description: Make the player perform an emote
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/trigger-emotes/
url: /creator/development-guide/trigger-emotes
weight: 4
---

{{< hint danger >}}
**❗Warning**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/interactivity/trigger-emotes.md" >}}).
{{< /hint >}}

To make a player perform an emote, use the `triggerEmote()` function. Note that only existing default emotes are supported for now. This function takes a single argument:

- `emote`: An emote from the `PredefinedEmote` enum.

```ts
import { triggerEmote, PredefinedEmote } from '@decentraland/RestrictedActions'

const emoter = new Entity()
emoter.addComponent(new BoxShape())
emoter.addComponent(new Transform({ position: new Vector3(8, 0, 8) }))
emoter.addComponent(
	new OnPointerDown(
		(e) => {
			triggerEmote({ predefined: PredefinedEmote.ROBOT })
		},
		{ hoverText: 'Dance' }
	)
)

engine.addEntity(emoter)
```

Only the emotes in the `PredefinedEmote` enum are currently supported. This list includes the following:

- 'WAVE'
- 'FIST_PUMP'
- 'ROBOT'
- 'RAISE_HAND'
- 'CLAP'
- 'MONEY'
- 'KISS'
- 'TIK'
- 'HAMMER',
- 'TEKTONIK'
- 'DONT_SEE'
- 'HANDS_AIR'
- 'SHRUG'
- 'DISCO'
- 'DAB'
- 'HEAD_EXPLODE'

The emote animation is seen both by the player (in 3rd person view) and any other players around. If the player walks, runs or jumps, they will interrupt the animation and return to playing the corresponding animations for these actions.

{{< hint warning >}}
**📔 Note**: Players can only be animated if they already are standing inside the scene's bounds, not if they are on a neighboring scene.
{{< /hint >}}

Before you can use this feature, you must add the `ALLOW_TO_TRIGGER_AVATAR_EMOTE` permission to the `scene.json` file. If not yet present, create a `requiredPermissions` property at root level in the JSON file to assign it this permission.

```json
"requiredPermissions": [
    "ALLOW_TO_TRIGGER_AVATAR_EMOTE"
  ],
```

See [Required permissions]({{< ref "/content/creator/scenes/projects/scene-metadata.md#required-permissions" >}}) for more details.

{{< hint warning >}}
**📔 Note**: To prevent abusive behavior that might damage a player's experience, the ability to make a player perform an emote is handled as a permission. Currently, this permission has no effect in how the player experiences the scene. In the future, players who walk into a scene with this permission in the `scene.json` file will be requested to grant the scene the ability to play emotes on them.
{{< /hint >}}
