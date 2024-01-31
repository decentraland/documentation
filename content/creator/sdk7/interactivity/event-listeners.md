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
		console.log('ENTERED SCENE', player)
	})

	onLeaveScene((player) => {
		console.log('LEFT SCENE', player)
	})
}
```

### Only current player

You can filter out the triggered events to only react to the player's avatar, rather than other avatars that may be around.

```ts
import { getPlayer, onEnterScene, onLeaveScene } from '@dcl/sdk/src/players'

export function main() {
	let myPlayer = getPlayer()

	onEnterScene((player) => {
		console.log('ENTERED SCENE', player)

		if (myPlayer && player.userId == myPlayer.userId) {
			console.log('THIS IS ME')
		}
	})

	onLeaveScene((player) => {
		console.log('LEFT SCENE', player)

		if (myPlayer && player.userId == myPlayer.userId) {
			console.log('THIS IS ME')
		}
	})
}
```

This example first obtains the player's id, then subscribes to the events and compares the `userId` returned by the event to that of the player.

#### Query all players in scene

Go over the full list of players who are currently on your scene by looking iterating over all entities with a `PlayerIdentityData` component.

```ts
import { getPlayersInScene } from '~system/Players'

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

Use the `onChange` function on the `AvatarEquippedData` to fire an event each time the player changes one of their wearables, or their listed emotes on the quick access wheel. Similarly, use the `onChange` function on the `AvatarBase` to fire an event each time the player changes their base avatar properties, like hair color, skin color, avatar shape, or name.

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
**💡 Tip**: When testing in preview, to avoid using a random avatar, run the scene in the browser connected with your Metamask wallet. In the Decentraland Editor, open the Decentraland tab and hover your mouse over it to display the three dots icon on the top-right. Click this icon and select **Open in browser with Web3**.
{{< /hint >}}

You can also detect changes on the profiles of other players in the scene, simply pass a reference to the other player instead of `engine.PlayerEntity`.

## Deprecated functions

#### Player clicks on another player

Whenever the player clicks on another player, you can detect an event.

```ts
import { onPlayerClickedObservable } from '@dcl/sdk/observables'

onPlayerClickedObservable.add((clickEvent) => {
	console.log('Clicked ', clickEvent.userId, ' details: ', clickEvent.ray)
})
```

{{< hint warning >}}
**📔 Note**: The `onPlayerClickedObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: Both the player performing the click and the player being clicked must be standing within the parcels of the scene. This listener only detects events of the current player clicking on other players, not those of clicks performed by other players.
{{< /hint >}}

The event includes the following data:

- `userId`: The id of the clicked player
- `ray`: Data about the ray traced by the click
  - `direction`: _Vector3_ A normalized Vector3 that represents the direction from the point of origin of the click to the hit point of the click.
  - `distance`: _number_ The distance in meters from the point of origin to the hit point.
  - `origin`: _Vector3_ The point of origin of the click, the position of the player who did the click, relative to the scene.

{{< hint info >}}
**💡 Tip**: The default behavior of clicking on another player is opening the player passport, where you can see additional information about that player, add them as a friend, etc. You can disable the opening of this UI so that it doesn't get in the way of the experience you want to build by adding an [Avatar Modifier Area]({{< ref "/content/creator/sdk7/interactivity/avatar-modifiers.md" >}}).
{{< /hint >}}

#### Player locks/unlocks cursor

Players can switch between two cursor modes: _locked cursor_ mode to control the camera or _unlocked cursor_ mode for moving the cursor freely over the UI.

Players unlock the cursor by clicking the _Right mouse button_ or pressing the _Esc_ key, and lock the cursor back by clicking anywhere in the screen.

This `onPointerLockedStateChange` event is activated each time a player switches between these two modes, while near the scene.

```ts
import { onPointerLockedStateChange } from '@dcl/sdk/observables'

onPointerLockedStateChange.add(({ locked }) => {
	if (locked) {
		console.log('Pointer has been locked')
	} else {
		console.log('Pointer has been unlocked')
	}
})
```

{{< hint warning >}}
**📔 Note**: The `onPointerLockedStateChange` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: This event is triggered even if the player is not standing directly inside the scene.
{{< /hint >}}

The `locked` property from this event is a boolean value that is _true_ when the player locks the cursor and _false_ when the player unlocks the cursor.

This event is useful if the player needs to change cursor modes and may need a hint for how to lock/unlock the cursor.

This can also be used in scenes where the player is expected to react fast, but the action can take a break while the player has the cursor unlocked.

#### Player changes realm or island

Players in decentraland exist in separate _realms_, and in separate _islands_ within each realm. Players in different realms or islands cant see each other, interact or chat with each other, even if they're standing on the same parcels.

Each time the player changes realms or island, the `onRealmChangedObservable` event gets called.

```ts
import { onRealmChangedObservable } from '@dcl/sdk/observables'

onRealmChangedObservable.add((realmChange) => {
	console.log('PLAYER CHANGED ISLAND TO ', realmChange.room)
})
```

{{< hint warning >}}
**📔 Note**: The `onRealmChangedObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}

This event includes the following fields:

- **serverName**: _string_; The catalyst server name.
- **room**: _string_; The island name.
- **displayName**: _string_; The catalyst server name followed by a _-_ and the island name. For example `unicorn-x011`.
- **domain**: _string_; The url to the catalyst server being used.

As players move through the map, they may switch islands to be grouped with those players who are now closest to them. Islands also shift their borders dynamically to fit a manageable group of people in each. So even if a player stands still they could be changed island as others enter and leave surrounding scenes.

If your scene relies on an [3rd party server]({{< ref "/content/creator/sdk7/networking/authoritative-servers.md" >}}) to sync changes between players in real time, then you may want to only share data between players that are grouped in a same realm+island, so it's a good practice to change rooms in the 3rd party server whenever players change island.

### Player connects or disconnects

Get the full list of currently connected players from `getConnectedPlayers`.

```ts
import { getConnectedPlayers } from '~system/Players'

executeTask(async () => {
	let connectedPlayers = await getConnectedPlayers({})
	connectedPlayers.players.forEach((player) => {
		console.log('player was already here: ', player.userId)
	})
})
```

{{< hint warning >}}
**📔 Note**: The `onPlayerConnectedObservable` and `onPlayerDisconnectedObservable` events are deprecated on SDK 7.x. Instead, track the list of connected players, from `getConnectedPlayers()`.
{{< /hint >}}

Whenever another player starts or stops being rendered by the local engine, this creates an event you can listen to. Players may or may not be standing on the same scene as you, but must be within visual range (not necessarily in sight). The `onPlayerConnectedObservable` detects both when a player newly connects nearby or comes close enough to be in visual range, likewise the `onPlayerDisconnectedObservable` detects when a player ends their session or or walks far away.

```ts
import {
	onPlayerConnectedObservable,
	onPlayerDisconnectedObservable,
} from '@dcl/sdk/observables'

onPlayerConnectedObservable.add((player) => {
	console.log('player entered: ', player.userId)
})

onPlayerDisconnectedObservable.add((player) => {
	console.log('player left: ', player.userId)
})
```

Keep in mind that if other players are already being rendered in the surroundings before the player has loaded your scene, this event won't notify the newly loaded scene of the already existing players. If you need to keep track of all current players, you can query for existing players upon scene loading, and then listen to this event for updates.

### Player enters or leaves scene

Whenever an avatar steps inside or out of the parcels of land that make up your scene, or teleports in or out, this creates an event you can listen to. This event is triggered by all avatars, including the player's.

```ts
import {
	onEnterSceneObservable,
	onLeaveSceneObservable,
} from '@dcl/sdk/observables'

onEnterSceneObservable.add((player) => {
	console.log('player entered scene: ', player.userId)
})

onLeaveSceneObservable.add((player) => {
	console.log('player left scene: ', player.userId)
})
```

{{< hint warning >}}
**📔 Note**: This event only responds to players that are currently being rendered locally. In large scenes where the scene size exceeds the visual range, players entering in the opposite corner may not be registered. If the number of players in the region exceeds the capabilities of an island on Decentraland servers, players that are not sharing a same island aren't visible and are not tracked by these events either.
{{< /hint >}}

#### Query all players in scene

You can also get the full list of players who are currently on your scene and being rendered by calling `getPlayersInScene()`.

```ts
import { getPlayersInScene } from '~system/Players'

executeTask(async () => {
	let connectedPlayers = await getPlayersInScene({})
	connectedPlayers.players.forEach((player) => {
		console.log('player was already here: ', player.userId)
	})
})
```

#### Player plays animation

Whenever the player plays an emote (dance, clap, wave, etc), you can detect this event.

```ts
import { onPlayerExpressionObservable } from '@dcl/sdk/observables'

onPlayerExpressionObservable.add(({ expressionId }) => {
	console.log('Expression: ', expressionId)
})
```

The event includes the following information:

- expressionId: Name of the emote performed (ie: _wave_, _clap_, _kiss_)

{{< hint warning >}}
**📔 Note**: This event is triggered any time the player makes an emote and the scene is loaded. The player could be standing in a nearby scene when this happens.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: The `onPlayerExpressionObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}

#### Player changes profile

Whenever the player makes a change to their profile, the `onProfileChanged` event is called. These changes may include putting on different wearables, changing name, description, activating portable experiences, etc.

```ts
import { onProfileChanged } from '@dcl/sdk/observables'

onProfileChanged.add((profileData) => {
	console.log('Own profile data is ', profileData)
})
```

{{< hint warning >}}
**📔 Note**: The `onProfileChanged` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}

Event data includes only the ID of the player and a version number for that avatar's profile, according to the catalyst server. Every time a change is propagated, the version number increases by 1.

When this event is triggered, you can then use the [getUserData()]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-player-data">}}) function to fetch the latest version of this information, including the list of wearables that the player has on. You may need to add a slight delay before you call `getUserData()` to ensure that the version this function returns is up to date.

{{< hint info >}}
**💡 Tip**: When testing in preview, to avoid using a random avatar, run the scene in the browser connected with your Metamask wallet. In the Decentraland Editor, open the Decentraland tab and hover your mouse over it to display the three dots icon on the top-right. Click this icon and select **Open in browser with Web3**.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: This event is only triggered by changes to the current player, not by changes on the profiles of other nearby players.
{{< /hint >}}

#### Scene finished loading

When the scene finishes loading, the `onSceneReadyObservable` gets called. This works both if the player loads straight into the scene, or if the player walks up to the scene from somewhere else. When all of the content in the scene has finished its initial load, including heavy models, etc, this event is called.

```ts
import { onSceneReadyObservable } from '@dcl/sdk/observables'

onSceneReadyObservable.add(() => {
	console.log('SCENE LOADED')
})
```

{{< hint warning >}}
**📔 Note**: The `onSceneReadyObservable` event is deprecated from SDK v7.x. This function is no longer relevant. You can ensure that something is executed after the scene finished loading by running it inside the `Main()` function. See []
{{< /hint >}}
