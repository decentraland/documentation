---
date: 2018-01-10
title: Authoritative servers
description: Using a server to sync changes in the scene for all players
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/authoritative-server/
weight: 3
---

Decentraland runs scenes locally in a player's browser. By default, players are able to see each other and interact directly, but each one interacts with the environment independently. Changes in the environment aren't shared between players by default. You need to implement this manually.

Allowing all players to see a scene as having the same content in the same state is extremely important to for players to interact in more meaningful ways. Without this, if a player opens a door and walks into a house, other players will see that door as still closed, and the first player will appear to walk directly through the closed door to other players.

- **Mark an entity as synced**: The easiest option. See [Marked an entity as synced]({{< ref "/content/creator/sdk7/networking/serverless-multiplayer.md#mark-an-entity-as-synced" >}})
- **Send Explicit MessageBus Messages**: Manually send and listen for specific messages. See [Send explicit MessageBus messages]({{< ref "/content/creator/sdk7/networking/serverless-multiplayer.md#send-explicit-messagebus-messages" >}})
- **Use a Server**: This document deals with this option. This option is more work to set up, but is recommendable if there are incentives to exploit your scene.

## Types of authoritative servers

An authoritative server may have different levels of involvement with the scene:

- API + DB: This is useful for scenes where changes don't happen constantly and where it's acceptable to have minor delays in syncing. When a player changes something, it sends an HTTP request to a REST API that stores the new scene state in a data base. Changes remained stored for any new player that visits the scene at a later date. The main limitation is that new changes from other players aren't notified to players who are already there, messages can't be pushed from the server to players. Players must regularly send requests the server to get the latest state.

{{< hint info >}}
**💡 Tip**: It's also possible to opt for a hybrid approach where changes are notified between players via Messagebus messages, but the final state is also stored via an API for future visitors.
{{< /hint >}}

- Websockets: This alternative is more robust, as it establishes a two-way communications channel between player and server. Updates can be sent from the server, you could even have game logic run on or validated on the server. This enables real time interaction and makes more fast paced games possible. It's also more secure, as each message between player and server is part of a session that is opened, no need to validate each message.

## Example scenes with authoritative server

- [API + DB](https://github.com/decentraland-scenes/Awesome-Repository#use-an-api-as-db)

- [Websockets](https://github.com/decentraland-scenes/Awesome-Repository#websockets)

## Preview scenes with authoritative servers

To preview a scene that uses an authoritative server, you must run both the scene and the server it relies on. The server can be run locally in the same machine as the preview, as an easier way to test it.

To start the server, go to the `/server` folder and run `npm run start`.

Once the server is running, either remotely or locally, you can run `npm run start` on the scene as you normally do for local scenes.

Once the scene preview is running, you can open multiple browser tabs pointing at the same local address. Each tab will instantiate a separate player in the same scene, these players will share the same scene state as the scene changes.

See [preview a scene]({{< ref "/content/creator/sdk7/getting-started/preview-scene.md" >}}) for more details.

## Separate realms

Players in decentraland exist in many separate _realms_. Players in different realms cant see each other, interact or chat with each other, even if they're standing on the same parcels. Dividing players like this allows Decentraland to handle an unlimited amount of players without running into any limitations. It also pairs players that are in close regions, to ensure that ping times between players that interact are acceptable.

If your scene sends data to a 3rd party server to sync changes between players in real time, then it's important that changes are only synced between players that are on the same realm. You should handle all changes that belong to one realm as separate from those on a different realm. Otherwise, players will see things change in a spooky way, without anyone making the change.

See how to obtain the realm for each player in [get player data]({{< ref "/content/creator/sdk7/interactivity/user-data.md" >}})

## Multiplayer persistance

Unlike local scenes that are newly mounted each time a player walks into them, scenes that use authoritative servers have a life span that extends well beyond when the player enters and leaves the scene.

You must therefore design the experience taking into account that player won't always find the scene in the same initial state.
Any changes made to the scene will linger on for other players to find, you must make sure that these don't interfere with future player's experiences in an undesired way.

### Reset the state

When loading the scene, make sure its built based on the shared information stored in the server, and not in a default state.

In some cases, it makes sense to include some kind of reset button in the scene. Pressing the reset button would reset the scene gracefully.

Sometimes, this just implies setting the variables in the scene state back to default values. But resetting the scene might also involve unsubscribing listeners and stopping loops in the server side. If empty loops remain each time the scene is reset, these would keep piling up and will have an ill effect on the scene's performance.
