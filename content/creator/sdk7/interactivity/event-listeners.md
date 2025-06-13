---
date: 2018-02-22
title: Event listeners
description: Events that the scene can track, related to player actions and scene changes.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/event-listeners/
weight: 8
---

There are several events that the scene can subscribe to, to know the actions of the player while in or near the scene.

For button and click events performed by the player, see [Button events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md" >}}).

## Player enters or leaves scene

Whenever an avatar steps inside or out of the parcels of land that make up your scene, or teleports in or out, this creates an event you can listen to.

This event is triggered by all avatars, including the player's.

```ts
import { onEnterScene, onLeaveScene } from '@dcl/sdk/src/players'

export function main() {
	onEnterScene((player) => {
		if (!player) return
		console.log('ENTERED SCENE', player)
	})

	onLeaveScene((userId) => {
		if (!userId) return
		console.log('LEFT SCENE', userId)
	})
}
```

On the `onEnterScene` event, the function can access all of the data returned by [get player data]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-player-data">}}) via the `player` property.
On the `onLeaveScene` event, the function only has access to the player's ID.

### Only current player

You can filter out the triggered events to only react to the player's avatar, rather than other avatars that may be around.

```ts
import { getPlayer, onEnterScene, onLeaveScene } from '@dcl/sdk/src/players'

export function main() {
	let myPlayer = getPlayer()

	onEnterScene((player) => {
		if (!player) return
		console.log('ENTERED SCENE', player)

		if (myPlayer && player.userId == myPlayer.userId) {
			console.log('I CAME IN')
		}
	})

	onLeaveScene((userId) => {
		if (!userId) return
		console.log('LEFT SCENE', userId)

		if (myPlayer && userId == myPlayer.userId) {
			console.log('I LEFT')
		}
	})
}
```

This example first obtains the player's id, then subscribes to the events and compares the `userId` returned by the event to that of the player.

### Query all players in scene

Go over the full list of players who are currently on your scene by iterating over all entities with a `PlayerIdentityData` component.

```ts
import { PlayerIdentityData, Transform } from '@dcl/sdk/ecs'

export function main() {
	for (const [entity, data, transform] of engine.getEntitiesWith(
		PlayerIdentityData,
		Transform
	)) {
		console.log('PLAYER: ', { entity, data, transform })
	}
}
```

## Player changes camera mode

Knowing the camera mode can be very useful to fine-tune the mechanics of your scene to better adjust to what's more comfortable using this mode. For example, small targets are harder to click when on 3rd person.

The following snippet uses the `onChange` function to fire an event each time the camera changes. It also fires an event when the scene loads, with the player's initial camera mode.

```ts
export function main() {
	CameraMode.onChange(engine.CameraEntity, (cameraComponent) => {
		if (!cameraComponent) return
		console.log('Camera mode changed', cameraComponent?.mode)
		// 0 = first person
		// 1 = third person
	})
}
```

See [Check player's camera mode]({{< ref "/content/creator/sdk7/interactivity/user-data.md#check-the-players-camera-mode">}}).

## Player plays animation

Use the `onChange` function on the `AvatarEmoteCommand` component to fire an event each time the player plays an emote. This includes both base emotes (dance, clap, wave, etc) and emotes from tokens.

```ts
import { AvatarEmoteCommand } from '@dcl/sdk/ecs'

export function main() {
	AvatarEmoteCommand.onChange(engine.PlayerEntity, (emote) => {
		if (!emote) return
		console.log('Emote played: ', emote.emoteUrn)
	})
}
```

The event includes the following information:

- `emoteUrn`: Name of the emote performed (ie: _wave_, _clap_, _kiss_)
- `loop`: If the emote is looping or playing once
- `timestamp`: When the emote was triggered.

You can also detect emotes form other players in the scene, simply pass a reference to the other player instead of `engine.PlayerEntity`.

## Player changes profile

Use the `onChange` function on the `AvatarEquippedData` component to fire an event each time the player changes one of their wearables, or their listed emotes on the quick access wheel. Similarly, use the `onChange` function on the `AvatarBase` to fire an event each time the player changes their base avatar properties, like hair color, skin color, avatar shape, or name.

```ts
import { AvatarEquippedData, AvatarBase } from '@dcl/sdk/ecs'

export function main() {
	AvatarEquippedData.onChange(engine.PlayerEntity, (equipped) => {
		if (!equipped) return
		console.log('New wearables list: ', equipped.wearableUrns)
		console.log('New emotes list : ', equipped.emoteUrns)
	})

	AvatarBase.onChange(engine.PlayerEntity, (body) => {
		if (!body) return
		console.log('New eyes color: ', body.eyesColor)
		console.log('New skin color: ', body.skinColor)
		console.log('New hair color: ', body.hairColor)
		console.log('New body URN: ', body.bodyShapeUrn)
	})
}
```

The event on `AvatarEquippedData` includes the following information:

- `wearableUrns`: The list of wearables that the player currently has equipped.
- `emoteUrns`: The list of emotes that the player currently has equipped in the quick access wheel.

The event on `AvatarBase` includes the following information:

- `name`: The player's name.
- `bodyShapeUrn`: The ids corresponding to male or female body type.
- `skinColor`: Player skin color as a `Color4`
- `eyeColor`: Player eye color as a `Color4`
- `hairColor`: Player hair color as a `Color4`

You can also detect changes in wearables or avatars form other players in the scene, simply pass a reference to the other player instead of `engine.PlayerEntity`.

{{< hint info >}}
**💡 Tip**: When testing in preview with the legacy web editor, to avoid using a random avatar, run the scene in the browser connected with your Metamask wallet.
{{< /hint >}}

You can also detect changes on the profiles of other players in the scene, simply pass a reference to the other player instead of `engine.PlayerEntity`.

## Player locks or unlocks cursor

Players can switch between two cursor modes: _locked cursor_ mode to control the camera or _unlocked cursor_ mode for moving the cursor freely over the UI.

Players unlock the cursor by clicking the _Right mouse button_ or pressing the _Esc_ key, and lock the cursor back by clicking anywhere in the screen.

Use the `onChange` function on the `PointerLock` component to fire an event each time the player changes between the two cursor modes.

```ts
export function main() {
	PointerLock.onChange(engine.CameraEntity, (pointerLock) => {
		if (!pointerLock) return
		console.log('Pointer lock changed', pointerLock.isPointerLocked)
	})
}
```

Checking for this component is useful if the player needs to change cursor modes and may need a hint for how to lock/unlock the cursor. This can also be used in scenes where the player is expected to react fast, but the action can take a break while the player has the cursor unlocked.
