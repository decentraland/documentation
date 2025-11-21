---
date: 2018-02-22
title: Deprecated functions
description: Legacy functions
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/deprecated-functions/
weight: 100
---

The following functions are all legacy and should be avoided. They still work, but in the future they might stop being supported. All these examples include links to alternative ways to obtain the same information or achieve the same results.

## Player enters or leaves scene

{{< hint warning >}}
**📔 Note**: The `onEnterSceneObservable` and `onLeaveSceneObservable` events are deprecated on SDK 7.x. Use `onEnterScene` instead, see [Player enters or leaves scene]({{< ref "/content/creator/sdk7/interactivity/event-listeners.md#player-enters-or-leaves-scene" >}}).
{{< /hint >}}

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

The observables `onEnterScene` and `onLeaveScene` imported from `'@dcl/sdk/observables'` are also deprecated. The correct functions are named the same, but imported from `'@dcl/sdk/src/players'` instead. In the example below you can see both variations, first the deprecated version, then the proper one.

```ts
// DEPRECATED - imported from observables
import { onEnterScene, onLeaveScene } from '@dcl/sdk/observables'

onEnterScene.add((player) => {
	console.log('player entered scene: ', player.userId)
})

onLeaveScene.add((player) => {
	console.log('player left scene: ', player.userId)
})

// CURRENT - imported as a player function
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

## Player connects or disconnects

{{< hint warning >}}
**📔 Note**: The `getConnectedPlayers` function and the `onPlayerConnectedObservable` and `onPlayerDisconnectedObservable` events are deprecated on SDK 7.x. Use `onEnterScene` instead, see [Player enters or leaves scene]({{< ref "/content/creator/sdk7/interactivity/event-listeners.md#player-enters-or-leaves-scene" >}}). Each scene is now a distinct comms island, making it the same to be connected or on the same scene.
{{< /hint >}}

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

## Query all players in scene

{{< hint warning >}}
**📔 Note**: The `getPlayersInScene` function is deprecated on SDK 7.x. Instead, iterate over all players with a `PlayerIdentityData` component. See [Fetch all players]({{< ref "/content/creator/sdk7/interactivity/user-data.md#fetch-all-players" >}}).
{{< /hint >}}

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

## Player plays animation

{{< hint warning >}}
**📔 Note**: The `onPlayerExpressionObservable` event is deprecated on SDK 7.x. Use the `AvatarEmoteCommand` component instead, see [Player plays animation]({{< ref "/content/creator/sdk7/interactivity/event-listeners.md#player-plays-animation" >}}).
{{< /hint >}}

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

## Player changes profile

{{< hint warning >}}
**📔 Note**: The `onProfileChanged` event is deprecated on SDK 7.x. Use the `AvatarEquippedData` component instead, see [Player changes profile]({{< ref "/content/creator/sdk7/interactivity/event-listeners.md#player-changes-profile" >}}).
{{< /hint >}}

Whenever the player makes a change to their profile, the `onProfileChanged` event is called. These changes may include putting on different wearables, changing name, description, activating portable experiences, etc.

```ts
import { onProfileChanged } from '@dcl/sdk/observables'

onProfileChanged.add((profileData) => {
	console.log('Own profile data is ', profileData)
})
```

Event data includes only the ID of the player and a version number for that avatar's profile, according to the catalyst server. Every time a change is propagated, the version number increases by 1.

When this event is triggered, you can then use the [getUserData()]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-player-data">}}) function to fetch the latest version of this information, including the list of wearables that the player has on. You may need to add a slight delay before you call `getUserData()` to ensure that the version this function returns is up to date.

{{< hint info >}}
**💡 Tip**: When testing in preview with the legacy web explorer, to avoid using a random avatar, run the scene in the browser connected with your Metamask wallet.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: This event is only triggered by changes to the current player, not by changes on the profiles of other nearby players.
{{< /hint >}}

## Scene finished loading

{{< hint warning >}}
**📔 Note**: The `onSceneReadyObservable` event is deprecated from SDK v7.x. This function is no longer relevant. You can ensure that something is executed after the scene finished loading by running it inside the `Main()` function. See [Scene lifecycle]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#scene-lifecycle" >}})
{{< /hint >}}

When the scene finishes loading, the `onSceneReadyObservable` gets called. This works both if the player loads straight into the scene, or if the player walks up to the scene from somewhere else. When all of the content in the scene has finished its initial load, including heavy models, etc, this event is called.

```ts
import { onSceneReadyObservable } from '@dcl/sdk/observables'

onSceneReadyObservable.add(() => {
	console.log('SCENE LOADED')
})
```

## Deprecated player data methods

{{< hint warning >}}
**📔 Note**: The `getUserData()` and `getPlayerData()` functions are deprecated from SDK v7.4.x. Use `getPlayer()` instead. See [User data]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-user-data" >}}).
{{< /hint >}}

To obtain information from the current player that's running the scene, use `getUserData()`.

The example below imports the `~system/UserIdentity` namespace and runs `getUserData()`.

```ts
import { getUserData } from '~system/UserIdentity'

executeTask(async () => {
	let userData = await getUserData({})
	console.log(userData.data)
})
```

You can obtain data from other players that are nearby, by calling `getPlayerData()`, passing the id of a Decentraland account.

```ts
import { getPlayerData } from '~system/Players'

executeTask(async () => {
	let userData = await getPlayerData({ userId: '0x….' })
	console.log(userData)
})
```

Both `getUserData()` and `getPlayerData()` return the same data structure available via the content API. See [Data from any player]({{< ref "/content/creator/sdk7/interactivity/user-data.md#data-from-any-player">}})

`getPlayerData()` can only fetch data from players who are currently nearby. They don't have to be necessarily standing in the same scene, but in visual range, that's because this information is being fetched from the local engine that's rendering these avatars. To try this out in preview, open a second tab and log in with a different account.

{{< hint warning >}}
**📔 Note**: User IDs must always be lowercase. If copying a wallet address, make sure all the characters are set to lowercase.
{{< /hint >}}

The `getUserPublicKey()` and `getUserAccount()` functions are also deprecated. Please use `getPlayer()` instead. See [User data]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-user-data" >}}).

## Get skybox time

{{< hint warning >}}
**📔 Note**: The `getDecentralandTime()` function is deprecated from SDK v7.x.x. Use `getWorldTime()` instead. See [Get Decentraland Time]({{< ref "/content/creator/sdk7/interactivity/runtime-data.md#get-decentraland-time" >}}).
{{< /hint >}}

```ts
import { getDecentralandTime } from '~system/EnvironmentApi'

executeTask(async () => {
	let time = await getDecentralandTime({})
	console.log(time)
})
```

## Get realm

{{< hint warning >}}
**📔 Note**: The `getCurrentRealm()` function is deprecated from SDK v7.x.x. Use `getRealm()` instead. See [Get Realm Data]({{< ref "/content/creator/sdk7/interactivity/runtime-data.md#get-realm-data" >}}).
{{< /hint >}}

```ts
import { getCurrentRealm } from '@decentraland/EnvironmentAPI'

async function fetchPlayerData() {
	const playerRealm = await getCurrentRealm()

	console.log(playerRealm.domain)
}

fetchPlayerData()
```

## Is preview mode

{{< hint warning >}}
**📔 Note**: The `isPreviewMode()` function is deprecated from SDK v7.x.x. Use `getRealm()` instead, which contains a `preview` property. See [Get Realm Data]({{< ref "/content/creator/sdk7/interactivity/runtime-data.md#get-realm-data" >}}).
{{< /hint >}}

```ts
import { isPreviewMode } from '~system/EnvironmentAPI'

executeTask(async () => {
	const preview: boolean = await isPreviewMode({})

	if (preview) {
		console.log('Running in preview')
	}
})
```

## Player clicks on another player

Whenever the player clicks on another player, you can detect an event.

```ts
import { onPlayerClickedObservable } from '@dcl/sdk/observables'

onPlayerClickedObservable.add((clickEvent) => {
	console.log('Clicked ', clickEvent.userId, ' details: ', clickEvent.ray)
})
```

{{< hint warning >}}
**📔 Note**: The `onPlayerClickedObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.

As an alternative, you can attach an invisible collider to the player and detect clicks against this.
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
**💡 Tip**: The default behavior of clicking on another player is opening the player passport, where you can see additional information about that player, add them as a friend, etc. You can disable the opening of this UI so that it doesn't get in the way of the experience you want to build by adding an [Avatar Modifier Area]({{< ref "/content/creator/sdk7/interactivity/player-avatar.md#disable-passport-popup">}}).
{{< /hint >}}

## Player locks/unlocks cursor

{{< hint warning >}}
**📔 Note**: The `onPointerLockedStateChange` event is deprecated from SDK v7.x. See [Event listeners]({{< ref "/content/creator/sdk7/interactivity/event-listeners.md#player-locks-or-unlocks-cursor" >}}) for a non-deprecated alternative.
{{< /hint >}}

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
**📔 Note**: This event is triggered even if the player is not standing directly inside the scene.
{{< /hint >}}

## Player changes realm or island

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

## Crypto functions

{{< hint warning >}}
**📔 Note**: The functions `requirePayment()`, `signMessage()`, `convertMessageToObject()` are deprecated. Use the `sendAsync()` function instead. See [Scene blockchain operations]({{< ref "/content/creator/sdk7/blockchain/scene-blockchain-operations.md#" >}}). There are also libraries that can help simplify some common use cases with these functions.
{{< /hint >}}

## Video Events

{{< hint warning >}}
**📔 Note**: The `onVideoEvent` event is deprecated from SDK v7.x. See [Event listeners]({{< ref "/content/creator/sdk7/media/video-playing.md#video-events" >}}) for a non-deprecated alternative.
{{< /hint >}}

When a video changes its playing status, the `onVideoEvent` observable receives an event.

```ts
onVideoEvent.add((data) => {
	log('New Video Event ', data)
})
```

The input of a video event contains the following properties:

- `videoClipId` ( _string_): The ID for the entity that changed status.
- `componentId` (_string_): The ID of the entity that changed status.
- `currentOffset` (_number_): The current value of the `seek` property on the video. This value shows seconds after the video's original beginning. _-1_ by default.
- `totalVideoLength` (_number_ ): The length in seconds of the entire video. _-1_ if length is unknown.
- `videoStatus`: The value for the new video status of the `VideoTexture`, expressed as a value from the `VideoStatus` enum. This enum can hold the following possible values:

- `VideoStatus.NONE` = 0,
- `VideoStatus.ERROR` = 1,
- `VideoStatus.LOADING` = 2,
- `VideoStatus.READY` = 3,
- `VideoStatus.PLAYING` = 4,
- `VideoStatus.BUFFERING` = 5
