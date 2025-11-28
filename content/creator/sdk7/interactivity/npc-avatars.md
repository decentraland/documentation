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

## Create an avatar

The following snippet creates an avatar with random wearables and body shape, and name "NPC".

```ts
const myAvatar = engine.addEntity()
AvatarShape.create(myAvatar)

Transform.create(myAvatar, {
	position: Vector3.create(4, 0.25, 5),
})
```

When passing data to generate an `AvatarShape`, the following fields are required:

- `id`: (required) Internal identifier for the Avatar

The following optional fields are also available:

- `name`: Name to display over the Avatar's head. Default: "NPC".
- `bodyShape`: String to define which body shape to use.
- `wearables`: Array with list of URNs for wearables that the avatar currently has on. If wearables conflict (like two of them are hats), the last one in the list replaces the other.
- `emotes`: Array with list of URNs for NFT emotes that the avatar is capable of playing
- `eyeColor`: _Color3_ for the eye color (any color is valid)
- `skinColor`: _Color3_ for the skin color (any color is valid)
- `hairColor`: _Color3_ for the hair color (any color is valid)
- `talking`: If _true_, it displays a green set of bars next to the name, like when players use voice chat in-world.
- {{< hint info >}}
  **💡 Tip**: See [color types]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md" >}}) for more details on how to set colors.
  {{< /hint >}}

{{< hint warning >}}
**📔 Note**: The `AvatarShape`component must be imported via

> `import { AvatarShape } from "@dcl/sdk/ecs"`

See [Imports]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#imports" >}}) for how to handle these easily.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: The URN fields must follow the same format used for [NFTShapes]({{< ref "/content/creator/sdk7/media/display-a-certified-nft.md" >}}): `urn:decentraland:<CHAIN>:<CONTRACT_STANDARD>:<CONTRACT_ADDRESS>:<TOKEN_ID>`
{{< /hint >}}

## Animations

Avatars play default idle animations while still.

To play animations on the avatar, set the `expressionTriggerId` string to the name of the animation you want to play.

```ts
const myAvatar = engine.addEntity()
AvatarShape.create(myAvatar, {
	id: '',
	emotes: [],
	wearables: [],
	expressionTriggerId: 'robot',
})

Transform.create(myAvatar, {
	position: Vector3.create(4, 0.25, 5),
})
```

The `expressionTriggerId` field supports all [default animations]({{< ref "/content/creator/sdk7/interactivity/player-avatar.md#default-animations">}}), as well as custom animations [from a scene file]({{< ref "/content/creator/sdk7/interactivity/player-avatar.md#custom-animations">}}), and even URNs from emotes that are published to the marketplace.

### Looping Animations

Animations on an `AvatarShape` play once, if you want the avatar to keep looping an animation, you should create a system that tells it to play the animation again every couple of seconds.

Use the `expressionTriggerTimestamp` to replay a same emote. The value of this field is a [lamport timestamp](https://en.wikipedia.org/wiki/Lamport_timestamp), meaning that it's not a time value, but rather an index that is raised by 1 for each repetition of the emote. 

So the first time you play an emote, you set `expressionTriggerTimestamp` to _0_. To play the emote again, you must update this value to 1. That's how the engine knows that this is a new instruction, and not an instruction it already acted upon.

The following snippet creates a system that runs a same emote every 2 seconds:

```ts
const myAvatar = engine.addEntity()
AvatarShape.create(myAvatar, {
	id: '',
	emotes: [],
	wearables: [],
	expressionTriggerId: 'clap',
    expressionTriggerTimestamp: 0
})

Transform.create(myAvatar, {
	position: Vector3.create(4, 0.25, 5),
})

let clapTimer = 0
let emoteDuration = 2  // 2 seconds

// system
engine.addSystem((dt: number) => {
    clapTimer += dt
      
    if (clapTimer >= emoteDuration) {
        // Trigger the clap emote
        AvatarShape.getMutable(wearable).expressionTriggerTimestamp =+ 1 
        
        clapTimer = 0 // Reset timer
    }
})
```

{{< hint info >}}
**💡 Tip**: You must know the duration of the emote, and make that the duration of the system. If you create an emote that fixes the avatar still in a same pose, it's recommendable to make the duration of the emote longer than the system. That way, you can make sure that there are no artifacts when finishing and resetting the animation. 
{{< /hint >}}

## Copy wearables from player

The following snippet changes the wearables and other characteristics of an NPC avatar to match those that the player currently has on. This could be used in a scene as a manequin, to show off a particular wearable or emote combined with the player's current outfit.

```ts
import { getPlayer } from '@dcl/sdk/src/players'


export function swapAvatar(avatar: Entity) {

  let userData = getPlayer()
  console.log(userData)

  if (!userData || !userData.wearables) return

  const mutableAvatar = AvatarShape.getMutable(avatar)

  mutableAvatar.wearables = userData.wearables
  mutableAvatar.bodyShape = userData.avatar?.bodyShapeUrn
  mutableAvatar.eyeColor = userData.avatar?.eyesColor
  mutableAvatar.skinColor = userData.avatar?.skinColor
  mutableAvatar.hairColor = userData.avatar?.hairColor
  
}
```


## Display only wearables

Use the `showOnlyWearables` field to display only the listed wearables of an avatar. The rest of the avatar's body will be invisible.

```ts
const myAvatar = engine.addEntity()
AvatarShape.create(myAvatar, {
	id: '',
	emotes: [],
	wearables: [
    'urn:decentraland:matic:collections-v2:0x90e5cb2d673699be8f28d339c818a0b60144c494:0'
  ],
	showOnlyWearables: true,
})

Transform.create(myAvatar, {
	position: Vector3.create(4, 0.25, 5),
})
```

This is useful for displaying wearables, for example in a store.

{{< hint info >}}
**💡 Tip**: If a wearable is rather small, try setting the `scale` of the `Transform` to a larger value.
{{< /hint >}}


## Attach an entity to an NPC

You can use the `AvatarAttach` feature to fix an entity to one of the bones of an NPC avatar, for example so that the NPC is holding an object on their hand. The entity will move together with the avatar when it animates.

To use this feature, use the `id` property on the `AvatarShape` to assign an arbitrary id to this avatar, and then reference that id on the `AvatarAttach`. The id can be any string you want.

```ts
// Create NPC, with an ID
const myAvatar = engine.addEntity()
Transform.create(myAvatar, {
  position: Vector3.create(8, 0.25, 8),
})
AvatarShape.create(myAvatar, {
  id: "my-avatar-id", 
  wearables: [],
  emotes: []
})

// Create object to attach to NPC
const attachedEntity = engine.addEntity()
Transform.create(attachedEntity, {
    position: Vector3.create(4, 2, 4),
    scale: Vector3.create(0.15,0.15,0.15)
})
MeshRenderer.setBox(attachedEntity)
Material.setBasicMaterial(attachedEntity, { diffuseColor: Color4.Blue() })
AvatarAttach.create(attachedEntity, {
    avatarId: "my-avatar-id",
    anchorPointId: AvatarAnchorPointType.AAPT_LEFT_HAND
})
```

Learn more about the `AvatarAttach` component [here]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md#attach-an-entity-to-an-avatar">}}).

