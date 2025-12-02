---
date: 2025-11-16
title: The Player Avatar
description: Learn how to control the player's avatar
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/player-avatar/
weight: 5
---

There are varios ways in which you can control the player's avatar and change the gameplay experience for your players.

For dealing with avatars that are not players, see [NPC Avatars]({{< ref "/content/creator/sdk7/interactivity/npc-avatars.md" >}}).


## Move player

{{< hint info >}}
**💡 Tip**: The easiest way to move the player is to use the [Scene Editor]({{< ref "/content/creator/scene-editor/get-started/about-editor.md" >}}). Use the no-code **Move player** or the **Move player here** Actions, see [Make any item smart]({{< ref "/content/creator/scene-editor/interactivity/make-any-item-smart.md" >}}).
{{< /hint >}}


To change the player's position in the scene, use the `movePlayerTo()` function. This function takes an object with three properties:

- `newRelativePosition`: Where to position the player, expressed as a Vector3.
- `cameraTarget`: (optional) What direction to make the camera face, expressed as a Vector3 that represents the coordinates of a point in space to stare at. If no value is provided, the camera will maintain the same rotation as before moving.
- `avatarTarget`: (optional) What direction to make the avatar face, expressed as a Vector3 that represents the coordinates of a point in space to stare at. If no value is provided, the avatar will maintain the same rotation as before moving. If the player is in 1st person camera mode, the camera and avatar rotation are the same.

```ts
import { movePlayerTo } from '~system/RestrictedActions'

// create entity
const myEntity = engine.addEntity()
MeshRenderer.setBox(myEntity)
MeshCollider.setBox(myEntity)

Transform.create(myEntity, {
	position: { x: 4, y: 1, z: 4 },
})

// give entity behavior
pointerEventsSystem.onPointerDown(
	{
		entity: myEntity,
		opts: { button: InputAction.IA_POINTER, hoverText: 'Click' },
	},
	function () {
		// respawn player
		movePlayerTo({
			newRelativePosition: Vector3.create(1, 0, 1),
			cameraTarget: Vector3.create(8, 1, 8),
			avatarTarget: Vector3.create(8, 1, 8),
		})
	}
)
```

The player's movement occurs instantly, without any confirmation screens or camera transitions.

{{< hint warning >}}
**📔 Note**: Players can only be moved if they already are standing inside the scene's bounds, and can only be moved to locations that are inside the limits of the scene's bounds. You can't use `movePlayerTo()` to transport a player to another scene. To move a player to another scene, see [Teleports]({{< ref "/content/creator/sdk7/interactivity/external-links.md#teleports">}}).
{{< /hint >}}


## Play animations

You can make the player perform an animation as part of the scene's code. This can help provide more immersion, and it can also help communicate what other players are doing to each other. The avatar animations are seen both by the player (in 3rd person view) and any other players around.

Animations done by the player are overridden by the default locomotion animations, like walking and jumping. So animations played by the scene only play while the player is standing still. If the player walks or jumps, any animations are interrupted.

{{< hint warning >}}
**📔 Note**: Players can only be animated if they already are standing inside the scene's bounds, not if they are on a neighboring scene. Smart wearables can play animations anywhere.

While a player is performing an animation, they are not affected by collisions, their movements aren't constrained by the scene's physics. Also note that if an animation displaces the player from their original position, for example if the animation involves a jump, the player's Transform component will not be affected by this displacement.
{{< /hint >}}



### Use the Scene Editor

The easiest way to make a player perform an animation is to use the [Scene Editor]({{< ref "/content/creator/scene-editor/get-started/about-editor.md" >}}). Use the no-code **Play Emote** action to play a default animation, or the **Play Custom Emote** action to play an animation form a file. See [Make any item smart]({{< ref "/content/creator/scene-editor/interactivity/make-any-item-smart.md" >}}).

### Default animations

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
**💡 Tip**: If a player walks or jumps while playing the animation, they will interrupt it. If you don't want that to be possible, you can freeze the avatar with [Input Modifiers]({{< ref "/content/creator/sdk7/interactivity/player-avatar.md#freeze-the-player">}}) for the duration of the avatar animation.
{{< /hint >}}

### Custom animations

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
**💡 Tip**: If a player walks or jumps while playing the animation, they will interrupt it. If you don't want that to be possible, you can freeze the avatar with [Input Modifiers]({{< ref "/content/creator/sdk7/interactivity/player-avatar.md#freeze-the-player">}}) for the duration of the avatar animation.
{{< /hint >}}


## Restrict locomotion

You can restrict what actions the player can do in your scene. Use it to freeze the player, or to only restrict specific ways of locomotion, for example to prevent the player from jumping or running.


### Freeze the player

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

### Restricting specific kinds of locomotion

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

### Advanced syntax

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

## Locomotion Settings

You can affect the player's locomotion, like their running speed, jump height, and more. This can be altered dynamically, for example to allow a player to collect a temporary speed boost by interacting with a item, or to disable the player's ability to jump for a short period of time.

To do this, add an `AvatarLocomotionSettings` component to the `engine.PlayerEntity`.

```ts
import {AvatarLocomotionSettings, engine} from '@dcl/sdk/ecs'

AvatarLocomotionSettings.create(engine.PlayerEntity, {
	runSpeed: 10,
	jumpHeight: 2,
})
```

The following properties are available:

- `walkSpeed`: The speed at which the player walks, in meters per second. On the desktop client, players walk by pressing the control key.
- `jogSpeed`: The speed at which the player jogs, in meters per second. This is the default way in which the player moves.
- `runSpeed`: The speed at which the player runs, in meters per second. On the desktop client, players run by pressing the shift key.
- `jumpHeight`: The height at which the player jumps, in meters.
- `runJumpHeight`: The height at which the player jumps after running, in meters.
- `hardLandingCooldown`: The cooldown after a hard landing, in seconds. This is the time that the player has to wait before they can move again after landing from a high fall.

For reference, here are the default values for those properties:

- `walkSpeed`: 1.5 m/s
- `jogSpeed`: 8 m/s
- `runSpeed`: 10 m/s
- `jumpHeight`: 1 m
- `runJumpHeight`: 1.5 m
- `hardLandingCooldown`: 0.75 s

{{< hint info >}}
**💡 Tip**: None of these properties can be lower than 0. If you set one of them to a negative value, it will be clamped to 0. Setting these values to zero will have the same effect as using the `InputModifier` to block the use of certain keys.

You can only affect the player's locomotion if they are inside the scene's bounds. To affect other player's avatars, you must run the code that affects their locomotion on their own instance.
{{< /hint >}}

You can create a [smart wearable]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}) that makes the player always run faster or jump higher. If both the scene and a smart wearable define different values for these parameters, the scene values are always used.

To ensure nobody has unfair advantages at a parkour scene, you can enforce the default parameters by explicitly adding their default values in your scene:

```ts
import {AvatarLocomotionSettings, engine} from '@dcl/sdk/ecs'

AvatarLocomotionSettings.create(engine.PlayerEntity, {
	runSpeed: 10,
	walkSpeed: 1.5,
	jogSpeed: 8 ,
	jumpHeight: 1,
	runJumpHeight: 1.5,
	hardLandingCooldown: 0.75
})
```

## Avatar modifier areas

Avatars behave and look consistently throughout Decentraland as they walk across scenes. However, you can add an `AvatarModifierArea` to a region of your scene to affect how player avatars behave when they enter that area.

{{< hint danger >}}
**❗Warning**  
Please limit the amount of `AvatarModifierAreas` you use in your scene to just a couple. If you use too many of them, it may have a significant impact on performance.
{{< /hint >}}

### Placing Avatar Modifier Areas

Add an entity with an `AvatarModifierArea` component and position this entity by using a `Transform` component.

```ts
const entity = engine.addEntity()

AvatarModifierArea.create(entity, {
	area: Vector3.create(4, 3, 4),
	modifiers: [AvatarModifierType.AMT_HIDE_AVATARS],
	excludeIds: []
})

Transform.create(entity, {
	position: Vector3.create(8, 0, 8),
})
```

When creating an `AvatarModifierArea` component, you must provide the following:

- `area`: Size of the modifier area
- `modifiers`: An array listing the modifiers to implement in the area. This property uses values from the `AvatarModifierType` enum.

The supported modifiers are:

- `AvatarModifierType.AMT_HIDE_AVATARS`
- `AvatarModifierType.AMT_DISABLE_PASSPORTS`

All the effects of an `AvatarModifierArea` only take place within the region of their area. Players return to normal when they walk out of the area.

An `AvatarModifierArea` affects only players that are inside the area, entering the area doesn't affect how other players that are outside the area are perceived.

The effects of an `AvatarModifierArea` are calculated locally for each player. You can have an `AvatarModifierArea` that is only present in the scene for some of the players and not for others. For example, you could make a "marco polo" game, where only one player in the scene has a modifier area that hides all of the other players. All the other players that don't have this modifier area in their local version of the scene are able to see each other normally.
If the area hides avatars, then the players that don't have the area in their local version of the scene will see all avatars normally. Even those that experience themselves as hidden. Players that do have the area will experience themselves and all other avatars as affected by the area when they enter it.

{{< hint warning >}}
**📔 Note**: Avatar modifier areas are affected by the _position_ and _rotation_ of the Transform component of their host entity, but they're not affected by the _scale_.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: The `AvatarModifierArea`component must be imported via

> `import { AvatarModifierArea } from "@dcl/sdk/ecs"`

See [Imports]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#imports" >}}) for how to handle these easily.
{{< /hint >}}

### Hide avatars

When a player walks into an `AvatarModifierArea` that has the `AvatarModifierType.AMT_HIDE_AVATARS` modifier, the player's avatar stops being rendered. This applies both for the player in 3rd person view, and for when other players walk into the area.

```ts
const entity = engine.addEntity()

AvatarModifierArea.create(entity, {
	area: Vector3.create(4, 3, 4),
	modifiers: [AvatarModifierType.AMT_HIDE_AVATARS],
	excludeIds: []
})

Transform.create(entity, {
	position: Vector3.create(8, 0, 8),
})
```

This allows you to replace the default Decentraland avatar with any custom avatar you might want to show in your scene. Note that if you want to see other players with custom avatars, you should handle the syncing of player positions yourself.

### Disable Passport Popup

When a player walks into an `AvatarModifierArea` that has the `AvatarModifierType.AMT_DISABLE_PASSPORTS` modifier, clicking on them no longer opens up the passport UI that shows the player bio, inventory, etc.

```ts
const entity = engine.addEntity()

AvatarModifierArea.create(entity, {
	area: Vector3.create(4, 3, 4),
	modifiers: [AvatarModifierType.AMT_DISABLE_PASSPORTS],
	excludeIds: []
})

Transform.create(entity, {
	position: Vector3.create(8, 0, 8),
})
```

This is especially useful in games where accidentally opening this UI could interrupt the flow of a game, for example in a multiplayer shooter game.


### Exclude Avatars

You can exclude a list of players from being affected by a modifier area by adding their player Ids to an array in the `excludeIds` property of the modifier area.

This example hides all avatars in an area, except those of players with specific IDs. You could use this for example on a live event, to only show the event hosts on the stage, and hide any other players that jump onto the stage.

```ts
const entity = engine.addEntity()

AvatarModifierArea.create(entity, {
	area: Vector3.create(4, 3, 4),
	modifiers: [AvatarModifierType.AMT_HIDE_AVATARS],
	excludeIds: ['0xx1...', '0xx2...'],
})

Transform.create(entity, {
	position: Vector3.create(8, 0, 8),
})
```

{{< hint warning >}}
**📔 Note**: Make sure the player IDs are all written with lower-case letters. Use `.toLowerCase()` if necessary.
{{< /hint >}}

Modifier areas run locally on each player's instance, the list of excluded IDs can be different for each player. In the example below, each player excludes their own ID from a modifier that hides avatars, so that they each view their own avatar and no others.

```ts
import { getPlayer } from '@dcl/sdk/src/players'

export function main() {
	let userData = getPlayer()
	if (!userData) return

	const entity = engine.addEntity()

	AvatarModifierArea.create(entity, {
		area: Vector3.create(16, 5, 16),
		modifiers: [AvatarModifierType.AMT_HIDE_AVATARS],
		excludeIds: [userData.userId],
	})

	Transform.create(entity, {
		position: Vector3.create(8, 0, 8),
	})
}
```

{{< hint danger >}}
**❗Warning**  
If the list of excluded IDs is going to be periodically changed (for example based on players entering or leaving an area), make sure that the list is kept in order. Perform a `.sort()` on the array, so that the list remains in the same order each time it's passed. In that way, only the changes to the list are be computed. This can otherwise have a significant impact on the scene's performance.

```ts
AvatarModifierArea.create(entity, {
	area: Vector3.create(16, 5, 16),
	modifiers: [AvatarModifierType.AMT_HIDE_AVATARS],
	excludeIds: [myAvatarList.sort()],
})
```

{{< /hint >}}

### Debug modifier areas

It can be tough to know exactly what parts of the scene your modifier areas cover based on the code. Visual feedback helps a lot to confirm that they're well placed.

To verify the positions of a `AvatarModifierArea` or a `CameraModeArea`, give the entity holding it a `MeshRenderer` component with a `box` shape, and set the scale to the same size as the `area` of the modifier area.

{{< hint warning >}}
**📔 Note**: Modifier areas aren't affected by the `scale` property of the transform, their size is based on their `area` property.
{{< /hint >}}

```ts
const entity = engine.addEntity()
const areaSize = Vector3.create(8, 3, 8)

AvatarModifierArea.create(entity, {
	area: areaSize,
	modifiers: [AvatarModifierType.AMT_HIDE_AVATARS],
  	excludeIds: []
})

Transform.create(entity, {
	position: Vector3.create(8, 0, 8),
	scale: areaSize,
})

MeshRenderer.setBox(entity)
Material.setPbrMaterial(entity, {
	albedoColor: Color4.create(0.5, 0.5, 0.5, 0.5),
})
```

To activate the effects of the modifier area, the player's head or torso should enter the area. It won't take effect if only the feet of the player are covered. Make sure the player can't easily evade the area by jumping.

{{< hint warning >}}
**📔 Note**: The full area should fit inside the limits of your scene.
{{< /hint >}}


## Change an avatar's appearance

You can't change what wearables the player's avatar is wearing, but you can instead swap the player's avatar for an NPC avatar that you can fully customize.

See [NPC Avatars]({{< ref "/content/creator/sdk7/interactivity/npc-avatars.md" >}}) for more details.

{{< hint warning >}}
**📔 Note**: To allow the player to have full control over that avatar, you should listen to button events to detect when they press a button, and then trigger the corresponding animation on the NPC avatar. See [Button Events]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}) for more details.

The fludity of control may not be perfect while doing this, you may want to use this only on very specific.
{{< /hint >}}
