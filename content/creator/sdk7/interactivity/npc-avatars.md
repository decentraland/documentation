---
date: 2020-11-04
title: NPC Avatars
description: Display and control NPC avatar
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/npc-avatars/
weight: 2
---


Display an avatar as an entity in a scene.


## Create avatar


The following creates an avatar with random wearables and body shape, and name "NPC".

```ts
const myAvatar = engine.addEntity()
AvatarShape.create(myAvatar)

Transform.create(myAvatar, {
	position: Vector3.create(4, 0.25, 5)
})
```

To pass data when generating the `AvatarShape`, the following fields are required:

- `id`: (required) Internal identifier for the Avatar
- `wearables`:  (required) Array with list of URNs for wearables that the avatar currently has on. If wearables conflict (like two of them are hats), the last one in the list replaces the other.
- `emotes`:  (required) Array with list of URNs for emotes that the avatar is currently playing 

<!-- TODO: check if emotes really work like this -->


The following optional fields are also available:

- `name`: Name to display over the Avatar's head. Default: "NPC".
- `talking`: If _true_, it displays a green set of bars next to the name, like when players use voice chat in-world.
- `bodyShape`: String to define which body shape to use.
- `eyeColor`: _Color3_ for the eye color (any color is valid)
- `skinColor`: _Color3_ for the skin color (any color is valid)
- `hairColor`: _Color3_ for the hair color (any color is valid)

> TIP: See [color types]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md" >}}) for more details on how to set colors.


## Default animations

Avatars play default idle animations while still. If they change positions, they play the walk or run position while moving. If they move above the ground level they play the jump animation and if they fall, they play the falling animation.

TODO: Validate this


## Animations

To play animations on the avatar, set the `expressionTriggerId` string to the name of the animation you want to play.

```ts
const myAvatar = engine.addEntity()
AvatarShape.create(myAvatar, {
	id: "",
	emotes: [],
	wearables: [],
	expressionTriggerId: "robot"
})

Transform.create(myAvatar, {
	position: Vector3.create(4, 0.25, 5)
})
```

TODO: Should I aso set `expressionTriggerTimestamp`? is it lamport or time?

