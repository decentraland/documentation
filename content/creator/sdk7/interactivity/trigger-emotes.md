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

You can make the player perform an animation as part of the scene's code. This can help provide more immersion, and it can also help communicate what other players are doing to each other. The avatar animations are seen both by the player (in 3rd person view) and any other players around.

Animations done by the player are overridden by the default locomotion animations, like walking and jumping. So animations played by the scene only play while the player is standing still. If the player walks or jumps, any animations are interrupted.

{{< hint warning >}}
**📔 Note**: Players can only be animated if they already are standing inside the scene's bounds, not if they are on a neighboring scene. Portable experiences and smart wearables can play animations anywhere.
{{< /hint >}}

## Use the Scene Editor

The easiest way to make a player perform an animation is to use the [Scene Editor]({{< ref "/content/creator/scene-editor/get-started/about-editor.md" >}}). Use the no-code **Play Emote** action to play a default animation, or the **Play Custom Emote** action to play an animation form a file. See [Make any item smart]({{< ref "/content/creator/scene-editor/interactivity/make-any-item-smart.md" >}}).

## Default animations

Use the `triggerEmote()` function ro run one of the default animations that players are able to play anywhere in Decentraland. This function takes a an object with a single property as an argument:

- `predefinedEmote`: A string name for an existing emote.

```ts
import { triggerEmote } from '~system/RestrictedActions'

const emoter = engine.addEntity()
Transform.create(emoter, { position: Vector3.create(8, 0, 8) })
MeshRenderer.setBox(emoter)
MeshCollider.setBox(emoter)
pointerEventsSystem.onPointerDown(
	{
		entity: emoter,
		opts: { button: InputAction.IA_POINTER, hoverText: 'Dance' },
	},
	() => {
		triggerEmote({ predefinedEmote: 'robot' })
	}
)
```

The following emotes show feedback about player actions in your scene, all of these are valid values for the `predefinedEmote` field:

- `buttonDown`
- `buttonFront`
- `getHit`
- `knockOut`
- `lever`
- `openChest`
- `openDoor`
- `punch`
- `push`
- `swingWeaponOneHand`
- `swingWeaponTwoHands`
- `throw`
- `sittingChair1`
- `sittingChair2`
- `sittingGround1`
- `sittingGround2`

These emotes are available to all players in their default emote wheel, and can also be used in any scene.

- `wave`
- `fistpump`
- `robot`
- `raiseHand`
- `clap`
- `money`
- `kiss`
- `tik`
- `hammer`
- `tektonik`
- `dontsee`
- `handsair`
- `shrug`
- `disco`
- `dab`
- `headexplode`




{{< hint info >}}
**💡 Tip**: If a player walks or jumps while playing the animation, they will interrupt it. If you don't want that to be possible, you can freeze the avatar with [Input Modifiers]({{< ref "/content/creator/sdk7/interactivity/input-modifiers.md" >}}) for the duration of the avatar animation.
{{< /hint >}}

## Custom animations

Use the `triggerSceneEmote()` to make the player perform a custom animation, stored as a .glb file as part of the scene's asset. 

{{< hint warning >}}
**📔 Note**: The file's name **must** end in `_emote.glb` to work as an avatar animation.
{{< /hint >}}

This function takes an object as an argument with the following arguments:

- `src`: A string with a path to the emote file.
- `loop`: If true, the animation will loop continuously until the player moves or the animation is stopped. False by default.

```ts
import { triggerSceneEmote } from '~system/RestrictedActions'

const emoter = engine.addEntity()
Transform.create(emoter, { position: Vector3.create(8, 0, 8) })
MeshRenderer.setBox(emoter)
MeshCollider.setBox(emoter)
pointerEventsSystem.onPointerDown(
	{
		entity: emoter,
		opts: { button: InputAction.IA_POINTER, hoverText: 'Make snowball' },
	},
	() => {
		triggerSceneEmote({ src: 'animations/Snowball_Throw_emote.glb', loop: false })
	}
)
```

{{< hint info >}}
**💡 Tip**: If a player walks or jumps while playing the animation, they will interrupt it. If you don't want that to be possible, you can freeze the avatar with [Input Modifiers]({{< ref "/content/creator/sdk7/interactivity/input-modifiers.md" >}}) for the duration of the avatar animation.
{{< /hint >}}

## Required permissions in smart wearables and portable experiences

{{< hint warning >}}
**📔 Note**: Permissions are only relevant in [portable experiences]({{< ref "/content/creator/sdk7/projects/portable-experiences.md" >}}) and [smart wearables]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}). Normal scenes (both in parcels or in Worlds) are free to use avatar animations and are not affected by permissions.
{{< /hint >}}

Smart wearables and portable experiences are only allowed to use this functionality if they add a corresponding permissions on the `scene.json` file. This applies to both predefined and custom animations. This is granted via the `ALLOW_TO_TRIGGER_AVATAR_EMOTE` permission.

```json
  "requiredPermissions": [
    "ALLOW_TO_TRIGGER_AVATAR_EMOTE"
  ],
```

See [Required permissions]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#required-permissions">}}) for more details.
