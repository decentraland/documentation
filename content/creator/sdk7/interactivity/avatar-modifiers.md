---
date: 2020-09-24
title: Modifier Areas
description: Specify an area on your scene where player avatars or the camera behave differently
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/avatar-modifiers/
weight: 3
---

## Avatar Modifiers

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

## Camera modifiers

Players are normally free to switch between first and third person camera by pressing V on the keyboard. Use a `CameraModeArea` to force the camera mode to either 1st or 3rd person for all players that stand within a specific area in your scene.

```ts
const entity = engine.addEntity()

CameraModeArea.create(entity, {
	area: Vector3.create(4, 3, 4),
	mode: CameraType.CT_FIRST_PERSON,
})
```

If a player's current camera mode doesn't match that of the `CameraModeArea`, they will transition to that camera mode. A toast appears onscreen to clarify that this change is due to the scene. While inside, players can't change their camera mode. When a player leaves the `CameraModeArea`, their camera mode is restored to what they had before entering.

Use `CameraModeArea` in regions where players would have a significantly better experience by using a specific camera mode. For example, first person is ideal if the player needs to click on small object, or third person may be useful for players to notice some entity that your scene has attached over their head. Don't assume players know how to switch camera modes, many first-time players might not know they have the option, or not remember the key to do it.

{{< hint warning >}}
**📔 Note**: Camera modifier areas are affected by the _position_ and _rotation_ of the Transform component of their host entity, but they're not affected by the _scale_.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: If you overlap multiple camera modifier areas, the last one to be instanced by your scene's code will take priority over the others.
{{< /hint >}}

When creating an `CameraModeArea` component, you must provide the following:

- `area`: Size of the modifier area
- `cameraMode`: Which camera mode to force in this area, from the `CameraType` enum.

The supported camera modes are:

- `CameraType.CT_FIRST_PERSON`
- `CameraType.CT_THIRD_PERSON`

## Exclude Avatars

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

## Debug modifier areas

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
