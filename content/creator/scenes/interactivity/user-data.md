---
date: 2018-02-22
title: Player data
description: Obtain data from players as they interact with your scene.
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/user-data/
url: /creator/development-guide/user-data
weight: 5
---

{{< hint warning >}}
**📔 Note**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/interactivity/user-data.md" >}}).
{{< /hint >}}

## Track player position and rotation

The `Camera` object exposes information about the player's point of view in your scene.

- `Camera.instance.position` returns a 3D vector with the coordinates of the avatar's center, relative to the scene. When the player is on the ground, the height of this point is approximately _1.177_ m. In 3rd person camera mode, this value refers also to the avatar's center, not to the position of the 3rd person camera.
- `Camera.instance.feetPosition` returns a 3D vector with the coordinates of the player's feet relative to the scene. When the player is at ground level, the height is nearly 0.155.
- `Camera.instance.worldPosition` returns a 3D vector with the coordinates of the player's center, relative to the whole of Genesis City. For example, if the scene is in coordinates _100,-100_, and the player is standing on the bottom-left corner of that scene, the player's world position will be about _1600, 1.177, -1600_
- `Camera.instance.rotation` returns a quaternion with the player's rotation. In 3rd person camera mode, this refers to the 3rd person camera angle, not the direction faced by the avatar.
- `Camera.instance.rotation.eulerAngles` returns a Vector3 with the player's rotation. In 3rd person camera mode, this refers to the 3rd person camera angle, not the direction faced by the avatar.

```ts
log(Camera.instance.feetPosition)
log(Camera.instance.rotation.eulerAngles)
```

The example above logs the player's position and rotation.

```ts
class CubeRotateSystem implements ISystem {
	entity: Entity
	constructor(entity: Entity) {
		this.entity = entity
	}

	update() {
		const transform = this.entity.getComponent(Transform)
		transform.rotation = Camera.instance.rotation
	}
}

const cube = new Entity()
cube.addComponent(new BoxShape())
cube.addComponent(new Transform({ position: new Vector3(5, 1, 5) }))
engine.addEntity(cube)

engine.addSystem(new CubeRotateSystem(cube))
```

The example above uses the player's rotation to set that of a cube in the scene.

{{< hint warning >}}
**📔 Note**: The `Camera.instance` data is updated at a throttled rate of 10 times per second. Due to this, positions & rotations may lag slightly in relation to the scene that runs at 30 FPS under ideal conditions.
{{< /hint >}}

<!--
See [Event Listeners](/creator/development-guide/event-listeners #player-moves) for a more efficient approach where updates are only made in the event of the player moving, and not while the player stands still.
-->

## Get player data

The following data can be fetched from a player:

- `displayName`: _(string)_ The player's user name, as others see in-world
- `userId`: _(string)_ A UUID string that identifies the player. If the player has a public key, this field will have the same value as the public key.
- `publicKey`: _(string)_ The public key of the player's Ethereum wallet. If the player logs in as a guest, with no linked wallet, this field will be `null`.
- `hasConnectedWeb3`: _(boolean)_ Indicates if the player has a public key. _True_ if the player has one.
- `avatar`: A nested object with data about the player's appearance.
- `version`: _(number)_ A version number that increases by one every time the player changes any of their settings. Use this if you encounter conflicting data, to know what version is more recent.

{{< hint warning >}}
**📔 Note**: For any Ethereum transactions with the player, always use the `publicKey` field, instead of the `userId`, to avoid dealing with non-existing wallets.
{{< /hint >}}

The `avatar` object has the following nested information:

- `wearables`: `WearableId[]` An array of identifiers for each of the wearables that the player is currently wearing. For example `urn:decentraland:off-chain:base-avatars:green_hoodie`. All wearables have a similar identifier, even if they're NFTs.
- `bodyShape`: An identifier for the avatar's general body shape. Either `urn:decentraland:off-chain:base-avatars:BaseFemale` for female or `urn:decentraland:off-chain:base-avatars:BaseMale` for male.

- `skinColor`: _ColorString_ A hex value for the player's skin color.
- `hairColor`: _ColorString_ A hex value for the player's hair color.
- `eyeColor`: _ColorString_ A hex value for the player's eye color.
- `snapshots`: A nested object with base64 representations of .jpg images of the player in various resolutions.
  - `face256`: _string_ The player's face as a 256x256 pixel image.
  - `body`: _string_ The full resolution image of the player standing straight, with 512x1024 pixels.

{{< hint danger >}}
**❗Warning**  
The snapshots of the avatar will be deprecated in the future and will no longer be returned as part of an avatar's data. The recommended approach is to use `AvatarTexture` instead, see [Avatar Portraits]({{< ref "/content/creator/scenes/3d-essentials/materials.md#avatar-portraits" >}}) ).
{{< /hint >}}

#### Data from current player

To obtain information from the current player that's running the scene, use `getUserData()`.

The example below imports the `Identity` library and runs `getUserData()`.

```ts
import { getUserData } from '@decentraland/Identity'

executeTask(async () => {
	let data = await getUserData()
	log(data)
})
```

The function returns the entire set of data described above, including address, name, wearables, snapshots, etc.

{{< hint info >}}
**💡 Tip**: When testing in preview, to avoid using a random avatar, run the scene in the browser connected with your Metamask wallet. In the Decentraland Editor, open the Decentraland tab and hover your mouse over it to display the three dots icon on the top-right. Click this icon and select **Open in browser with Web3**.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: The `getUserData()` function is asynchronous. See [Asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}) if you're not familiar with those.
{{< /hint >}}

#### Data from nearby players

You can obtain data from other players that are nearby, by calling `getPlayerData()`, passing the id of a Decentraland account.

```ts
import { getPlayerData } from '@decentraland/Players'

executeTask(async () => {
	let data = await getPlayerData({ userId: '0x….' })
	log(data)
})
```

The function returns the entire set of data described above, including address, name, wearables, snapshots, etc.

{{< hint info >}}
**💡 Tip**: The `getPlayerData()` function is asynchronous. See [Asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}) if you're not familiar with those.
{{< /hint >}}

`getPlayerData()` can only fetch data from players who are currently nearby. They don't have to be necessarily standing in the same scene, but in visual range, that's because this information is being fetched from the local engine that's rendering these avatars. To try this out in preview, open a second tab and log in with a different account.

{{< hint warning >}}
**📔 Note**: User IDs must always be lowercase. If copying a wallet address, make sure all the characters are set to lowercase.
{{< /hint >}}

To know what players are being rendered in the surroundings, use `getConnectedPlayers()`. This function returns an array with the ids of all the players that are currently being rendered, which are all eligible to call with `getPlayerData()`. You can pair this with listening for new players connecting and disconnecting by using `onPlayerConnectedObservable` and `onPlayerDisconnectedObservable`.

```ts
import { getConnectedPlayers } from '@decentraland/Players'

// Get already connected players
executeTask(async () => {
	let players = await getConnectedPlayers()
	players.forEach((player) => {
		log('player is nearby: ', player.userId)
	})
})

// Event when player connects
onPlayerConnectedObservable.add((player) => {
	log('player entered: ', player.userId)
})

// Event when player disconnects
onPlayerDisconnectedObservable.add((player) => {
	log('player left: ', player.userId)
})
```

As an alternative, you can use `getPlayersInScene()` to only fetch the players that are standing within the scene boundaries and also being rendered. You can pair this with listening to new players entering and leaving the scene by using `onEnterSceneObservable` and `onLeaveSceneObservable`.

```ts
import { getPlayersInScene } from '@decentraland/Players'

// Get all players already in scene
executeTask(async () => {
	let players = await getPlayersInScene()
	players.forEach((player) => {
		log('player is nearby: ', player.userId)
	})
})

// Event when player enters scene
onEnterSceneObservable.add((player) => {
	log('player entered scene: ', player.userId)
})

// Event when player leaves scene
onLeaveSceneObservable.add((player) => {
	log('player left scene: ', player.userId)
})
```

{{< hint info >}}
**💡 Tip**: Read more about `onPlayerConnectedObservable` and `onPlayerDisconnectedObservable` in [Player connects or disconnects]({{< ref "/content/creator/scenes/interactivity/event-listeners.md#player-connects-or-disconnects" >}}) and about about `onEnterSceneObservable` and `onLeaveSceneObservable` in [Player enters or leaves scene]({{< ref "/content/creator/scenes/interactivity/event-listeners.md#player-enters-or-leaves-scene" >}}).
{{< /hint >}}

Listen for events when players connect and disconnect
As more players connect and disconnect, you can pic

#### Data from any player

To obtain information from any player, make a [REST API call]({{< ref "/content/creator/scenes/networking/network-connections.md#call-a-rest-api" >}}) to the content servers. This returns the same information as the `getUserData()` and `getPlayerData()` functions, detailed at the start of the section.

This information is exposed in the following URL, appending the player's user id to the url parameter.

`https://peer.decentraland.org/lambdas/profile/<player user id>`

{{< hint info >}}
**💡 Tip**: Try the URL out in a browser to see how the response is structured.
{{< /hint >}}

Unlike `getPlayerData()`, this option is not limited to just the players who are currently being rendered in the surroundings. With this approach you can fetch data from any player that has logged onto the servers in the past.

If you know which server the player you want to query is connected to, you can get more up-to-date data by sending your requests to that specific server. For example, if the player changes clothes, this information will be available instantly in the player's server, but will likely take a couple of minutes to propagate to the `peer.decentraland.org` server.

`https://<player server>/lambdas/profile/<player user id>`

{{< hint info >}}
**💡 Tip**: You can obtain the current player's server by doing `getCurrentRealm().domain`.
{{< /hint >}}

This example combines `getUserData()` and `getCurrentRealm()` to obtain the player's data directly from the server that the player is on:

```ts
import { getUserData } from '@decentraland/Identity'
import { getCurrentRealm } from '@decentraland/EnvironmentAPI'

async function fetchPlayerData() {
	const userData = await getUserData()
	const playerRealm = await getCurrentRealm()

	let url = `{playerRealm.domain}/lambdas/profile/{userData.userId}`.toString()
	log('using URL: ', url)

	try {
		let response = await fetch(url)
		let json = await response.json()

		log('full response: ', json)
		log('player is wearing :', json[0].metadata.avatars[0].avatar.wearables)
		log('player owns :', json[0].metadata.avatars[0].inventory)
	} catch {
		log('an error occurred while reaching for player data')
	}
}

fetchPlayerData()
```

## Get player's public Ethereum key

As an alternative to `getUserData()`, you can obtain a player's public Ethereum key by using `getUserPublicKey()`. You can then use this information to send payments to the player, or as a way to recognize players.

The example below imports the `Identity` library and runs `getUserPublicKey()` to get the public key of the player's Ethereum account and log it to console. The player must be logged into their Metamask account on their browser for this to work.

```ts
import { getUserPublicKey } from '@decentraland/Identity'

const publicKeyRequest = executeTask(async () => {
	const publicKey = await getUserPublicKey()
	log(publicKey)
	return publicKey
})
```

{{< hint info >}}
**💡 Tip**: The `getUserPublicKey()` function is asynchronous. See [Asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}) if you're not familiar with those.
{{< /hint >}}

## Get Decentraland Time

Decentraland follows a day/night cycle that takes 2 hours to be completed, so there are 12 full cycles every day. Players can also change the settings to experience a specific fixed time of day, for example to always see Decentraland with a 10pm night sky. For this reason, Decentraland time may vary from one player to another.

Use `getDecentralandTime()` to fetch the time of day that the player is experiencing inside Decentraland.

```ts
import { getDecentralandTime } from '@decentraland/EnvironmentAPI'

executeTask(async () => {
	let time = await getDecentralandTime()
	log(time.seconds)
})
```

{{< hint info >}}
**💡 Tip**: The `getDecentralandTime()` function is asynchronous. See [Asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}) if you're not familiar with those.
{{< /hint >}}

`getDecentralandTime()` returns an object with a `seconds` property. This property indicates how many seconds have passed (in Decentraland time) since the start of the day, assuming the full cycle lasts 24 hours. Divide the seconds value by 60 to obtain minutes, and by 60 again to obtain the hours since the start of the day. For example, if the `seconds` value is _36000_, it corresponds to _10 AM_.

In Decentraland time, the sun always rises at 6:15 and sets at 19:50.

You could use this information to change the scene accordingly, for example to play bird sounds when there's daylight and crickets when it's dark, or to turn the emissive materials on street lamps when it's dark.

```ts
import { getDecentralandTime } from '@decentraland/EnvironmentAPI'

executeTask(async () => {
	let time = await getDecentralandTime()
	log(time.seconds)
	if (time.seconds < 6.25 * 60 * 60 || time.seconds > 19.85 * 60 * 60) {
		// night time
		log('playing cricket sounds')
	} else {
		// day time
		log('playing bird sounds')
	}
})
```

## Get player realm data

Players in decentraland exist in several separate _realms_. Players in different realms can't see each other, interact or chat with each other, even if they're standing on the same parcels. Dividing players like this allows Decentraland to handle an unlimited amount of players without running into any limitations. It also pairs players who are in close regions, to ensure that ping times between players that interact are acceptable.

If your scene sends data to a [3rd party server]({{< ref "/content/creator/scenes/networking/remote-scene-considerations.md" >}}) to sync changes between players in real time, then it's often important that changes are only synced between players that are on the same realm. You should handle all changes that belong to one realm as separate from those on a different realm. Otherwise, players will see things change in a spooky way, without anyone making the change.

```ts
import { getCurrentRealm } from '@decentraland/EnvironmentAPI'

executeTask(async () => {
	let realm = await getCurrentRealm()
	log(`You are in the realm: `, realm.displayName)
})
```

{{< hint warning >}}
**📔 Note**: The `getCurrentRealm()` function is asynchronous. See [Asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}) if you're not familiar with those.
{{< /hint >}}

Decentraland handles its communications between players (including player positions, chat, messageBus messages and smart item state changes) through a decentralized network of communication servers, each of these servers is called a **Realm**. Each one of these servers can support multiple separate **rooms** (also called **islands**), each grouping a different set of players that are near each other on the Decentraland map.

The `getCurrentRealm()` function returns the following information:

- `displayName`: _(string)_ The full address of the realm, composed of the server + the room
- `domain`: _(string)_ The URL of the server the player is connected to
- `serverName`: _(string)_ The name of the server the player is connected to
- `room`: _(string)_ The name of the room the player is connected to, in some versions of comms, this is a 1-to-1 map to the island name

{{< hint warning >}}
**📔 Note**: The `layer` property is deprecated, and should be avoided.
{{< /hint >}}

As players move through the map, they may switch rooms to be grouped with those players who are now closest to them. Rooms also shift their borders dynamically to fit a manageable group of people, so even if a player stands still, as players enter and leave the world, the player could find themselves on another room. Players in a same `room` are communicated, and will share messages across the MessageBus even if they;re too far to see each other. Players in a same server but in different rooms are not currently communicating, but they might get communicated as they move around the map and change rooms.

See [onRealmChangedObservable]({{< ref "/content/creator/scenes/interactivity/event-listeners.md#player-changes-realm-or-island" >}}) for how to detect changes regarding the player's realm or island.

{{< hint warning >}}
**📔 Note**: When the scene first loads, there might not yet be a room assigned for the player. The explorer will eventually assign a room to the player, but this can sometimes occur a couple of seconds after the scene is loaded.
{{< /hint >}}

## Get player platform

Players can access Decentraland via various platforms, currently via the browser or via the native desktop app.

Use `getPlatform()` to know what platform the current player is running Decentraland on.

```ts
import { getPlatform, Platform } from '@decentraland/EnvironmentAPI'

executeTask(async () => {
	let data = await getPlatform()
	log(data)
	if (data === Platform.BROWSER) {
		log('In browser')
	} else if (data === Platform.DESKTOP) {
		log('In native desktop app')
	}
})
```

Players using the desktop app are likely to have a much smoother experience than those on the browser, since the browser imposes performance limitations on how much of the machine's processing power the browser tab can use. You could use this information to render higher quality materials or other performance-heavy improvements only for players on desktop, as they are less likely to suffer bad frame rate from the extra content.

## Get Portable Experiences

Portable experiences are essentially scenes that are not constrained to parcels of land. Players can carry these with them anywhere they go in Decentraland, adding a new layer of content over the world. Smart Wearables are examples of portable experiences. You may want to know if a player is wearing one of these, since a smart wearable may enable players to have abilities that could be considered cheating in a competitive game. For example, in a platform game, a player that wears a jetpack has a very unfair advantage over others.

As a scene creator, you may want to limit what players wearing portable experiences can do in your scene. Use `getPortableExperiencesLoaded()` to check if the player has any portable experiences currently activated.

```ts
executeTask(async () => {
	let portableExperiences = await getPortableExperiencesLoaded()
	log(portableExperiences)
})
```

`getPortableExperiencesLoaded()` returns an array of objects, each of these objects includes an `id` attribute. In the case of wearables, the id is the wearable's URN.

## Get detailed info about a player's wearables

The `getUserData()` and `getPlayerData()` return only a list of wearable ids, without information about each wearable. If instead of individual wearables you want to check for any wearable of a specific category (eg: hats), or any wearable of a specific rarity (eg: Mythic), then you'll need to fetch more detailed information about the player's wearables.

Make a [REST API call]({{< ref "/content/creator/scenes/networking/network-connections.md#call-a-rest-api" >}}) to the following URL, to obtain a full updated list of all wearables that are currently usable, with details about each.

`${playerRealm.domain}/lambdas/collections/wearables-by-owner/${userData.userId}?includeDefinitions`

{{< hint warning >}}
**📔 Note**: To construct this URL, you must obtain the realm (likely with with `getCurrentRealm()`) and the player's id (likely with `getUserData()`)
{{< /hint >}}

This feature could be used together with fetching info about the player, to for example only allow players to enter a place if they are wearing any wearable from the halloween collection, or any wearable that is of _legendary_ rarity.

{{< hint info >}}
**💡 Tip**: Try the URL out in a browser to see how the response is structured.
{{< /hint >}}

```ts
import { getUserData } from '@decentraland/Identity'
import { getCurrentRealm } from '@decentraland/EnvironmentAPI'

async function fetchWearablesData() {
	try {
		let player = await getUserData()
		const playerRealm = await getCurrentRealm()

		let url =
			`${playerRealm.domain}/lambdas/collections/wearables-by-owner/${userData.userId}?includeDefinitions`.toString()
		log('using URL: ', url)

		let response = await fetch(url)
		let json = await response.json()

		log('full response: ', json)
	} catch {
		log('an error occurred while reaching for wearables data')
	}
}

executeTask(fetchWearablesData)
```

## Check the player's camera mode

{{< hint warning >}}
**📔 Note**: `Camera.instance.cameraMode` is currently deprecated and is not always reliable. The recommended approach is to track camera change events with `onCameraModeChangedObservable`. This event is fired once when the scene first obtains information about the player's current camera mode, and then any time the player changes camera mode while in or around your scene. See [Event Listeners]({{< ref "/content/creator/scenes/interactivity/event-listeners.md#player-changes-camera-mode" >}}).
{{< /hint >}}

Players can either be using a 1st or 3rd person camera when exploring Decentraland. Check which of these the player is using by checking the value `Camera.instance.cameraMode`.

The value of this property can either be `CameraMode.FirstPerson` or `CameraMode.ThirdPerson`.

```ts
if (Camera.instance.cameraMode == CameraMode.FirstPerson) {
	log('The player is using the 1st person camera')
} else {
	log('The player is using the 3rd person camera')
}
```

The `Camera.instance.cameraMode` property is read-only, you can't force the player to change camera mode.

{{< hint info >}}
**💡 Tip**: To encourage players to use a particular camera mode in your scene, display a UI message advising them to switch modes whenever they use the wrong one.
{{< /hint >}}

Knowing the camera mode can be very useful to fine-tune the mechanics of your scene to better adjust to what's more comfortable using this mode. For example, small targets are harder to click when in 3rd person.
