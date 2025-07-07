---
date: 2024-10-08
title: Input Modifiers
description: Change what actions players can perform
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/input-modifiers/
weight: 8
---

You can restrict what actions the player can do in your scene. Use it to freeze the player, or to only restrict specific ways of locomotion, for example to prevent the player from jumping or running.

{{< hint warning >}}
**📔 Note**: Input Modifiers are a feature that's only supported in the DCL 2.0 desktop client.
{{< /hint >}}

## Freeze the player

You can freeze the player so that none of the input keys can move the avatar. This can be useful for many game mechanics. It's also a good practice to freeze a player while performing an important animation that shouldn't be interrupted by movement, or while a [Virtual Camera]({{< ref "/content/creator/sdk7/3d-essentials/camera.md" >}}) points away from the avatar and you don't want the player to move blindly.

Use the `InputModifier` component on the `engine.PlayerEntity` to prevent the player's inputs from affecting the avatar's locomotion. The avatar will remain still, the player will only be able to rotate the camera.

```ts
import {InputModifier, engine} from '@dcl/sdk/ecs'

InputModifier.create(engine.PlayerEntity, {
	mode: InputModifier.Mode.Standard({
		disableAll: true,
	}),
})
```

Keep the following considerations in mind:

- While the player's interactions are disabled, their avatar is still affected by external forces, like gravity or moving platforms.
- The `InputModifier` component can only be used with the `engine.PlayerEntity` entity. It can only affect the current player, it can't affect other players.
- This component only affects the player while the avatar is within your scene's bounds. Their locomotion stops being restricted as soon as they're out.
- While the player's interactions are disabled, the player can't perform emotes freely, but the scene can trigger animations on the avatar.
- Player inputs don't affect the avatar, but the [global input events]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md#global-input-events" >}}) can still be listened by the scene. You could use these to control a vehicle, or use a [Virtual Camera]({{< ref "/content/creator/sdk7/3d-essentials/camera.md" >}}) to follow another entity as it moves, treating it as an alternative avatar.

## Restricting locomotion

Instead of entirely freezing the player, you can restrict certain specific forms of locomotion of the player. The `InputModifier` includes the following options:

- `disableWalk`: Player can't walk slowly (pressing control). If the player tries to walk, they will jog or run if allowed.
- `disableRun`: Player can't run (pressing shift). If the player tries to run, they will jog or run if allowed.
- `disableJog`: Player can't jog (this is the default movement speed). If the player tries to jog, they will run or walk if allowed.
- `disableJump`: Player can't jump.
- `disableEmote`: Player can't perform emotes voluntarily. The scene is able to trigger animations on the player's avatar.
- `disableAll`: The player can't perform any of the above actions.

```ts
import {InputModifier, engine} from '@dcl/sdk/ecs'

InputModifier.create(engine.playerEntity, {
	mode: InputModifier.Mode.Standard({
		disableAll: false,
		disableWalk: false,
		disableRun: true,
		disableJog: true,
		disableJump: true,
		disableEmote: true,
	}),
})
```

## Advanced syntax

To use the component without any helpers, you can use the following syntax:

```ts
import {InputModifier, engine} from '@dcl/sdk/ecs'

InputModifier.createOrReplace(engine.PlayerEntity, {
	mode: {
		$case: 'standard',
		standard: {
			disableAll: false,
			disableWalk: false,
			disableRun: true,
			disableJog: true,
			disableJump: true,
			disableEmote: true,
		},
	},
})
```
