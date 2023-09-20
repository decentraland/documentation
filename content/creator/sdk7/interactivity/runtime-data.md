---
date: 2023-06-19
title: Runtime data
description: Obtain data from the context where your scene is running and the scene itself.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/runtime-data/
weight: 5
---

## Get Decentraland Time

Decentraland follows a day/night cycle that takes 2 hours to be completed, so there are 12 full cycles every day. Players can also change the settings to experience a specific fixed time of day, for example to always see Decentraland with a 10pm night sky. For this reason, Decentraland time may vary from one player to another.

Use `getWorldTime()` to fetch the time of day that the player is experiencing inside Decentraland.

```ts
import { getWorldTime } from '~system/Runtime'

executeTask(async () => {
  let time = await getWorldTime({})
  console.log(time.seconds)
})
```

{{< hint info >}}
**💡 Tip**: The `getWorldTime()` function is asynchronous. See [Asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}) if you're not familiar with those.
{{< /hint >}}

`getWorldTime()` returns an object with a `seconds` property. This property indicates how many seconds have passed (in Decentraland time) since the start of the day, assuming the full cycle lasts 24 hours. Divide the seconds value by 60 to obtain minutes, and by 60 again to obtain the hours since the start of the day. For example, if the `seconds` value is _36000_, it corresponds to _10 AM_.

In Decentraland time, the sun always rises at 6:15 and sets at 19:50.

You could use this information to change the scene accordingly, for example to play bird sounds when there's daylight and crickets when it's dark, or to turn the emissive materials on street lamps when it's dark.

```ts
import { getWorldTime } from '~system/Runtime'

executeTask(async () => {
  let time = await getWorldTime({})
  console.log(time.seconds)
  if (time.seconds < 6.25 * 60 * 60 || time.seconds > 19.85 * 60 * 60) {
    // night time
    console.log('playing cricket sounds')
  } else {
    // day time
    console.log('playing bird sounds')
  }
})
```

## Get realm data

Players in decentraland exist in several separate _realms_. Players in different realms can't see each other, interact or chat with each other, even if they're standing on the same parcels. Dividing players like this allows Decentraland to handle an unlimited amount of players without running into any limitations. It also pairs players who are in close regions, to ensure that ping times between players that interact are acceptable.

If your scene sends data to a [3rd party server]({{< ref "/content/creator/sdk7/networking/remote-scene-considerations.md" >}}) to sync changes between players in real time, then it's often important that changes are only synced between players that are on the same realm. You should handle all changes that belong to one realm as separate from those on a different realm. Otherwise, players will see things change in a spooky way, without anyone making the change.

```ts
import { getRealm } from '~system/Runtime'

executeTask(async () => {
  const { realmInfo } = await getRealm({})
  console.log(`You are in the realm: `, realmInfo.realmName)
})
```

{{< hint info >}}
**💡 Tip**: The `getRealm()` function is asynchronous. See [Asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}) if you're not familiar with those.
{{< /hint >}}

Decentraland handles its communications between players (including player positions, chat, messageBus messages and smart item state changes) through a decentralized network of communication servers, each of these servers is called a **Realm**. Each one of these servers can support multiple separate **rooms** (also called **islands**), each grouping a different set of players that are near each other on the Decentraland map.

The `getRealm()` function returns the following information:

- `baseUrl`: _(string)_ The domain of the realm server
- `realmName`: _(string)_ The name of the realm server
- `networkId`: _(number)_ The Ethereum network
- `commsAdapter`: _(string)_ Comms adapter, removing all query parameters (credentials)
- `preview`: _(boolean)_ True if the scene is running as a local preview, instead of published in Decentraland.

{{< hint warning >}}
**📔 Note**: The `layer` property is deprecated, and should be avoided.
{{< /hint >}}

As players move through the map, they may switch rooms to be grouped with those players who are now closest to them. Rooms also shift their borders dynamically to fit a manageable group of people, so even if a player stands still, as players enter and leave the world, the player could find themselves on another room. Players in a same `room` are communicated, and will share messages across the MessageBus even if they;re too far to see each other. Players in a same server but in different rooms are not currently communicating, but they might get communicated as they move around the map and change rooms.

See [onRealmChangedObservable]({{< ref "/content/creator/sdk7/interactivity/event-listeners.md#player-changes-realm-or-island">}}) for how to detect changes regarding the player's realm or island.

{{< hint warning >}}
**📔 Note**: When the scene first loads, there might not yet be a room assigned for the player. The explorer will eventually assign a room to the player, but this can sometimes occur a couple of seconds after the scene is loaded.
{{< /hint >}}

## Get player platform

Players can access Decentraland via various platforms, currently via the browser or via the native desktop app.

Use `getPlatform()` to know what platform the current player is running Decentraland on.

```ts
import { getPlatform } from '~system/EnvironmentAPI'

executeTask(async () => {
  let data = await getPlatform()
  console.log(data.platform)
  if (data.platform === Platform.BROWSER) {
    console.log('In browser')
  } else if (data.platform === Platform.DESKTOP) {
    console.log('In native desktop app')
  }
})
```

Players using the desktop app are likely to have a much smoother experience than those on the browser, since the browser imposes performance limitations on how much of the machine's processing power the browser tab can use. You could use this information to render higher quality materials or other performance-heavy improvements only for players on desktop, as they are less likely to suffer bad frame rate from the extra content.

## The EngineInfo Component

The `EngineInfo`component keeps track of data about the scene's lifecycle, which can sometimes be useful to tell when an event is occurring, relative to the scene's initialization.

This component is added to the `engine.RootEntity`.

```ts
engine.addSystem((deltaTime) => {
  const engineInfo = EngineInfo.getOrNull(engine.RootEntity)
  if (!engineInfo) return

  console.log(
    '--------------' +
      '\nframeNumber: ' +
      engineInfo.frameNumber +
      '\ntickNumber: ' +
      engineInfo.tickNumber +
      '\ntotalRuntime: ' +
      engineInfo.totalRuntime +
      '\n--------------'
  )
})
```

The `EngineInfo`component holds the following data:

- `frame_number`: Frame counter of the engine
- `total_runtime`: Total runtime of this scene in seconds
- `tick_number`: Tick counter of the scene as per [ADR-148](https://adr.decentraland.org/adr/ADR-148)
