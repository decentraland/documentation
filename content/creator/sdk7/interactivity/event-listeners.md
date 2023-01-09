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

## Player connects or disconnects

Get the full list of currently connected players from `getConnectedPlayers`.

```ts
import { getConnectedPlayers } from "~system/Players"

executeTask(async () => {
  let connectedPlayers = await getConnectedPlayers({})
  connectedPlayers.players.forEach((player) => {
    console.log("player was already here: ", player.userId)
  })
})
```

{{< hint warning >}}
**📔 Note**   The `onPlayerConnectedObservable` and `onPlayerDisconnectedObservable` events are deprecated on SDK 7.x. Instead, track the list of connected players, from `getConnectedPlayers()`. This is a more [data oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}) and should result in better performance.
{{< /hint >}}


Whenever another player starts or stops being rendered by the local engine, this creates an event you can listen to. Players may or may not be standing on the same scene as you, but must be within visual range (not necessarily in sight). The `onPlayerConnectedObservable` detects both when a player newly connects nearby or comes close enough to be in visual range, likewise the `onPlayerDisconnectedObservable` detects when a player ends their session or or walks far away.

```ts
onPlayerConnectedObservable.add((player) => {
  console.log("player entered: ", player.userId)
})

onPlayerDisconnectedObservable.add((player) => {
  console.log("player left: ", player.userId)
})
```

Keep in mind that if other players are already being rendered in the surroundings before the player has loaded your scene, this event won't notify the newly loaded scene of the already existing players. If you need to keep track of all current players, you can query for existing players upon scene loading, and then listen to this event for updates.

## Player enters or leaves scene

Whenever an avatar steps inside or out of the parcels of land that make up your scene, or teleports in or out, this creates an event you can listen to. This event is triggered by all avatars, including the player's.

```ts
onEnterSceneObservable.add((player) => {
  console.log("player entered scene: ", player.userId)
})

onLeaveSceneObservable.add((player) => {
  console.log("player left scene: ", player.userId)
})
```

{{< hint warning >}}
**📔 Note**   This event only responds to players that are currently being rendered locally. In large scenes where the scene size exceeds the visual range, players entering in the opposite corner may not be registered. If the number of players in the region exceeds the capabilities of an island on Decentraland servers, players that are not sharing a same island aren't visible and are not tracked by these events either.
{{< /hint >}}


#### Only current player

You can filter out the triggered events to only react to the player's avatar, rather than other avatars that may be around.

```ts
import { getUserData } from "~system/UserIdentity"

executeTask(async () => {
  let myPlayer = await getUserData({})

  onEnterSceneObservable.add((player) => {
    console.log("player entered scene: ", player.userId)
    if (player.userId === myPlayer.data?.userId) {
      console.log("I entered the scene!")
    }
  })

  onLeaveSceneObservable.add((player) => {
    console.log("player left scene: ", player.userId)
    if (player.userId === myPlayer.data?.userId) {
      console.log("I left the scene!")
    }
  })
})
```

This example first obtains the player's id, then subscribes to the events and compares the `userId` returned by the event to that of the player.

#### Query all players in scene

You can also get the full list of players who are currently on your scene and being rendered by calling `getPlayersInScene()`.

```ts
import { getPlayersInScene } from "~system/Players"

executeTask(async () => {
  let connectedPlayers = await getPlayersInScene({})
  connectedPlayers.players.forEach((player) => {
    console.log("player was already here: ", player.userId)
  })
})
```

## Player changes camera mode

Knowing the camera mode can be very useful to fine-tune the mechanics of your scene to better adjust to what's more comfortable using this mode. For example, small targets are harder to click when on 3rd person.

The following system regularly checks the player's camera mode:

```ts
let previousCameraMode: CameraType

engine.addSystem(function cameraModeCheck() {
  let cameraEntity = CameraMode.get(engine.CameraEntity)

  if (!cameraEntity) return

  if (cameraEntity.mode !== previousCameraMode) {
    previousCameraMode = cameraEntity.mode
    if (cameraEntity.mode == CameraType.CT_THIRD_PERSON) {
      console.log("The player is using the 3rd person camera")
    } else {
      console.log("The player is using the 1st person camera")
    }
  }
})
```

See [Check player's camera mode]({{< ref "/content/creator/sdk7/interactivity/user-data.md#check-the-players-camera-mode">}}).

## Player plays animation

Whenever the player plays an emote (dance, clap, wave, etc), you can detect this event.

```ts
onPlayerExpressionObservable.add(({ expressionId }) => {
  console.log("Expression: ", expressionId)
})
```

The event includes the following information:

- expressionId: Name of the emote performed (ie: _wave_, _clap_, _kiss_)

{{< hint warning >}}
**📔 Note**   This event is triggered any time the player makes an emote and the scene is loaded. The player could be standing in a nearby scene when this happens.
{{< /hint >}}


{{< hint warning >}}
**📔 Note**   The `onPlayerExpressionObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}


## Player clicks on another player

Whenever the player clicks on another player, you can detect an event.

```ts
onPlayerClickedObservable.add((clickEvent) => {
  console.log("Clicked ", clickEvent.userId, " details: ", clickEvent.ray)
})
```

{{< hint warning >}}
**📔 Note**   The `onPlayerClickedObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}


{{< hint warning >}}
**📔 Note**   Both the player performing the click and the player being clicked must be standing within the parcels of the scene. This listener only detects events of the current player clicking on other players, not those of clicks performed by other players.
{{< /hint >}}


The event includes the following data:

- `userId`: The id of the clicked player
- `ray`: Data about the ray traced by the click
  - `direction`: _Vector3_ A normalized Vector3 that represents the direction from the point of origin of the click to the hit point of the click.
  - `distance`: _number_ The distance in meters from the point of origin to the hit point.
  - `origin`: _Vector3_ The point of origin of the click, the position of the player who did the click, relative to the scene.

Tip: The default behavior of clicking on another player is opening the player passport, where you can see additional information about that player, add them as a friend, etc. You can disable the opening of this UI so that it doesn't get in the way of the experience you want to build by adding an [Avatar Modifier Area]({{< ref "/content/creator/sdk7/interactivity/avatar-modifiers.md" >}}).

## Player locks/unlocks cursor

Players can switch between two cursor modes: _locked cursor_ mode to control the camera or _unlocked cursor_ mode for moving the cursor freely over the UI.

Players unlock the cursor by clicking the _Right mouse button_ or pressing the _Esc_ key, and lock the cursor back by clicking anywhere in the screen.

This `onPointerLockedStateChange` event is activated each time a player switches between these two modes, while near the scene.

```ts
onPointerLockedStateChange.add(({ locked }) => {
  if (locked) {
    console.log("Pointer has been locked")
  } else {
    console.log("Pointer has been unlocked")
  }
})
```

{{< hint warning >}}
**📔 Note**   The `onPointerLockedStateChange` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}


{{< hint warning >}}
**📔 Note**   This event is triggered even if the player is not standing directly inside the scene.
{{< /hint >}}


The `locked` property from this event is a boolean value that is _true_ when the player locks the cursor and _false_ when the player unlocks the cursor.

This event is useful if the player needs to change cursor modes and may need a hint for how to lock/unlock the cursor.

This can also be used in scenes where the player is expected to react fast, but the action can take a break while the player has the cursor unlocked.

## Player goes idle

Whenever the player is inactive for a full minute, without interacting with any input being picked up by the Decentraland explorer, we can consider the player to be idle. Whenever this happens, it creates an event that you can listen to.

```ts
onIdleStateChangedObservable.add(({ isIdle }) => {
  console.log("Idle State change: ", isIdle)
})
```

{{< hint warning >}}
**📔 Note**   The `onIdleStateChangedObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}


The `isIdle` property is a boolean value that is _true_ when the player enters the idle mode and _false_ when the player leaves the idle mode.

This event is especially useful for multiplayer scenes, when you might want to disconnect from the server players who are likely away from the machine or left Decentraland in a tab in the background.

{{< hint warning >}}
**📔 Note**   The idle state is inferred based on the player not using the keyboard or mouse for a full minute. This can of course produce false positives, for example a player might be watching other players interact or watching a video stream, standing still but fully engaged. Be mindful of these corner cases and what the experience is like for a player who stands still for a while.
{{< /hint >}}


## Player changes profile

Whenever the player makes a change to their profile, the `onProfileChanged` event is called. These changes may include putting on different wearables, changing name, description, activating portable experiences, etc.

```ts
onProfileChanged.add((profileData) => {
  console.log("Own profile data is ", profileData)
})
```

{{< hint warning >}}
**📔 Note**   The `onProfileChanged` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}


Event data includes only the ID of the player and a version number for that avatar's profile, according to the catalyst server. Every time a change is propagated, the version number increases by 1.

{{< hint info >}}
**💡 Tip**:  When this event is triggered, you can then use the [getUserData()]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-player-data">}}) function to fetch the latest version of this information, including the list of wearables that the player has on. You may need to add a slight delay before you call `getUserData()` to ensure that the version this function returns is up to date.
{{< /hint >}}

When testing in preview, run the scene with `dcl start --web3` so that you connect with your wallet. Otherwise, you will be using a random avatar.

{{< hint warning >}}
**📔 Note**   This event is only triggered by changes to the current player, not by changes on the profiles of other nearby players.
{{< /hint >}}


## Scene finished loading

When the scene finishes loading, the `onSceneReadyObservable` gets called. This works both if the player loads straight into the scene, or if the player walks up to the scene from somewhere else. When all of the content in the scene has finished its initial load, including heavy models, etc, this event is called.

```ts
onSceneReadyObservable.add(() => {
  console.log("SCENE LOADED")
})
```

{{< hint warning >}}
**📔 Note**   The `onSceneReadyObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}


## Video playing

When a `VideoTexture` changes its playing status, the `onVideoEvent` observable receives an event.

```ts
onVideoEvent.add((data) => {
  console.log("New Video Event ", data)
})
```

{{< hint warning >}}
**📔 Note**   The `onVideoEvent` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}


The input of a video event contains the following properties:

- `videoClipId` ( _string_): The ID for the `VideoTexture` component that changed status.
- `componentId` (_string_): The ID of the `VideoTexture` component that changed status.
- `currentOffset` (_number_): The current value of the `seek` property on the video. This value shows seconds after the video's original beginning. _-1_ by default.
- `totalVideoLength` (_number_ ): The length in seconds of the entire video. _-1_ if length is unknown.
- `videoStatus`: The value for the new video status of the `VideoTexture`, expressed as a value from the `VideoStatus` enum. This enum can hold the following possible values:

- `VideoStatus.NONE` = 0,
- `VideoStatus.ERROR` = 1,
- `VideoStatus.LOADING` = 2,
- `VideoStatus.READY` = 3,
- `VideoStatus.PLAYING` = 4,
- `VideoStatus.BUFFERING` = 5

Learn more about playing videos in Decentraland in [Video Playing]({{< ref "/content/creator/sdk7/media/video-playing.md" >}}).

## Player changes realm or island

Players in decentraland exist in separate _realms_, and in separate _islands_ within each realm. Players in different realms or islands cant see each other, interact or chat with each other, even if they're standing on the same parcels.

Each time the player changes realms or island, the `onRealmChangedObservable` event gets called.

```ts
onRealmChangedObservable.add((realmChange) => {
  console.log("PLAYER CHANGED ISLAND TO ", realmChange.room)
})
```

{{< hint warning >}}
**📔 Note**   The `onRealmChangedObservable` event is deprecated from SDK v7.x. Future versions will allow for a more [data-oriented approach]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), based on regularly querying data rather than events.
{{< /hint >}}


This event includes the following fields:

- **serverName**: _string_; The catalyst server name.
- **room**: _string_; The island name.
- **displayName**: _string_; The catalyst server name followed by a _-_ and the island name. For example `unicorn-x011`.
- **domain**: _string_; The url to the catalyst server being used.

As players move through the map, they may switch islands to be grouped with those players who are now closest to them. Islands also shift their borders dynamically to fit a manageable group of people in each. So even if a player stands still they could be changed island as others enter and leave surrounding scenes.

If your scene relies on a [3rd party server]({{< ref "/content/creator/sdk7/networking/remote-scene-considerations.md" >}}) to sync changes between players in real time, then you may want to only share data between players that are grouped in a same realm+island, so it's a good practice to change rooms in the 3rd party server whenever players change island.
