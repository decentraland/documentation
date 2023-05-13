---
title: "Overview"
sidebartitle: "Overview"
url: "/contributor/comms/overview"
weight: 1
---

The Decentraland communications system, or simply _comms_, is the real-time messaging protocol that handles interaction between players in a realm.

Some of these interactions are initiated by players, others are automatically handled by clients under the hood. Some examples:

* Text and voice chat
* Position updates as players move around
* Avatar updates when players change their appearance

{{< info >}}
You can see the comms protocol in action and experiment with it using the open-source [[Comms Demo Station]].
{{< /info >}}

Since most of this functionality requires broadcasting messages to all nearby players, they are automatically grouped into proximity-based clusters named _islands_. Each player is assigned to a single island at a time, which changes as they travel the world and move relative to others.

The realm service that manages and assigns players to islands is called _Archipelago_. It takes care of creating islands as they are needed, keeping their population at a reasonable number and dynamically reassigning players in response to their movements.


```goat
.----------------------------------------------------------------------------.                      
| Realm                                                                      |
|                                                     .------------------.   |
|                                              +---> | Island 1 | * * * * |  |
| .-------------------.                        |      '------------------'   |
| |                   |    .---------------.   |      .------------------.   |
| |      Players      +----+  Archipelago  +---+---> | Island 2 | * * o o |  |
| | * * * * * * * * * |    '---------------'   |      '------------------'   |
| '-------------------'                        |                ⋮            |
|                                              |      .------------------.   |
|                                              +---> | Island n | * * * o |  |
|                                                     '------------------'   |
|                                                                            |
'----------------------------------------------------------------------------'
```

When assigned to an island, clients are given an island-specific URI to connect to the actual backend that will relay messages between them. This connection lasts until Archipelago reassigns the client to a different island.

This means that, in addition to the [Archipelago]({{< relref "archipelago" >}}) protocol, clients must implement a number of _transports_, each wrapping one of the supported backends in a unified interface.

## Client Life-cycle {#lifecycle}

The life-cycle of a comms client can be summarized in a few steps:

1. **Select a realm**: obtain a URI for the [Archipelago]({{< relref "archipelago" >}}) service.
2. **Join Archipelago**: open a persistent connection with the service.
3. **Get an island (re)assignment**: report the current position and obtain an island-specific URI.
4. **Connect a transport**: open a second connection to the island-specific backend.
5. **Repeat**: continue going through steps 3 and 4, periodically reporting new positions.

When the client ends their session, they simply disconnect from the Archipelago service. They will be automatically removed from their current island.

```goat
.-------------.         .--------.         .----------------.                                       
| Archipelago |         | Client |         | Island Backend |
'-----+-------'         '---+----'         '-------+--------'
      ⋮                     |                      ⋮
      ⋮             Connect |                      ⋮
      o - - - - - - - - - - |                      ⋮
      |                     |                      ⋮
      |                     |                      ⋮
      |        Authenticate |                      ⋮
      |<--------------------+                      ⋮
      +-------------------->|                      ⋮
      | Accept              |                      ⋮
      |                     |                      ⋮
      |                     |                      ⋮
      |     Report position |                      ⋮
      |<--------------------+                      ⋮
      +-------------------->|                      ⋮
      | Assign island       |                      ⋮
      |                     |                      ⋮
      |                     | Connect transport    ⋮
      |                     |- - - - - - - - - - - o
      |                     |                      |
      |                     |                      |
      |                     | Authenticate         |
      |                     +--------------------->|
      |                     |<---------------------+
      |                     |               Accept |
      |                     |                      |
      |                     |                      |
      |                     | Player messages…     |
      |                     +--------------------->|
      |                     |<---------------------+
      |                     |     Player messages… |
      |                     |                      |
      |                     |                      |
      |     Update position |                      |
      |<--------------------+                      |
      +-------------------->|                      |
      | Reassign island     |                      |
      |                     |                      |
      |                     | Disconnect transport |
      |                     |- - - - - - - - - - - o
      |                     |                      ⋮                      
      |                     |                      ⋮ 
    --------------------- Repeat ---------------------
```


## Connections

Comms connections are mainly websocket-based, although some transports may use other strategies.

Go to the [Transports]({{< relref "transports" >}}) or [Archipelago]({{< relref "archipelago" >}}) sections to learn more, or a specific transport page for details about it.


## Authentication

Connections to comms are authenticated by having clients sign a server-provided challenge, using the scheme described in the [authentication chain]({{< relref "../auth/authchain" >}}) section.

Head over to the [Archipelago]({{< relref "archipelago" >}}) page or see a specific transport to learn more about authentication flows.


## Islands

Islands are highly dynamic groups of players that can broadcast messages among themselves, created and maintained by [Archipelago]({{< relref "archipelago" >}}) in response to their movements in the world.

There is no predefined area or central point for an island. They are not stable geographical features, only temporary associations of nearby players. If an island can be said to cover a region, it's only because its members are currently spread in that zone.

There can be zero islands in a region without players, and several overlapping islands in densly populated areas, where assigning everyone to the same group would make real-time broadcasting impossible.

Each server in the Decentraland network can configure the maximum island population and the distance at which players are considered to be nearby. By default, islands can host up to 100 players within 100 meters of each other.

The flow for getting assigned to an island and joining it is detailed in the [Archipelago]({{< relref "archipelago" >}}) section.


## Messages

Messages in the comms protocol are binary blobs serialized using [protocol buffers](https://github.com/protocolbuffers/protobuf), wrapped in a [Packet]({{< relref "messages#Packet" >}}) structure.

{{< info >}}
When using the word _message_ in the context of comms, we'll always be referring to the binary message protocol, not to chat messages exchanged between players.
{{< /info >}}

There are several different message types, for a variety of real-time interaction flows. Head over to the [messages]({{< relref "messages" >}}) section to learn more.








