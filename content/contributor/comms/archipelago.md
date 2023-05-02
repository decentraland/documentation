---
title: "Archipelago"
sidebartitle: "Archipelago"
url: "/contributor/comms/archipelago"
weight: 2
---

Archipelago is the realm service that groups nearby players into islands, reassigning them as they move around and providing the information required to connect to the actual backend that will relay their messages.

{{< info >}}
You can see the Archipelago protocol in action and experiment with it using the [[Comms Demo Station]].
{{< /info >}}

To use the service, clients must connect to their realm's _backend-for-frontend_ (BFF) websocket RPC, authenticate and activate the comms module for their connection, as described below. They can then start exchanging messages with Archipelago.

The Archipelago protocol closely matches the comms [client life-cycle]({{< relref "overview#lifecycle" >}}), with messages to report positions, get island assignments and receive various updates.

!! prefer link to sections below over externals

Connections to the BFF (and thus Archipelago) last for the full duration of the client's session -- indeed, as far as comms is concerned, open connections _are_ the session.

All messages exchanged with the BFF and the Archipelago service are encoded using protocol buffers, as defined in the Decentraland [protocol repository](https://github.com/decentraland/protocol). There's also a complete implementation of a BFF connection in the [Foundation's World Explorer](https://github.com/decentraland/unity-renderer/blob/d19577b762db71144bc402c3af0fb599685276b8/browser-interface/packages/shared/realm/connections/BFFConnection.ts).


## Connecting {#connecting}

To begin, clients must obtain the URI for the realm's BFF through the `/about` endpoint. The response includes the following object:

```js
"bff": {
  "healthy": true,
  "publicUrl": "/bff",
  // ...other properties
}
```

By specification, the RPC interface is located at `wss://<root>/<publicUrl>/rpc`. For example, [`https://peer.decentraland.org/about`](https://peer.decentraland.org/about) reports its `publicUrl` as `/bff`, so the websocket endpoint is at `wss://peer.decentraland.org/bff/rpc`.

{{< info >}}
While the larger realms run the Archipelago service, smaller ones may choose to provide a fixed backend connection string for all players.
{{< /info >}}

<!-- !! fixed adapters -->

## Authenticating {#authenticating}

When opening a connection to the BFF, clients must begin by requesting and signing a challenge from the service to verify their identity. For this, they use the [`BffAuthenticationService`][BffAuthenticationService] RPC interface.

Clients send a [`GetChallengeRequest`][GetChallengeRequest] with the an Ethereum address (representing their public key), receive a [`GetChallengeResponse`][GetChallengeResponse] with a randomly generated string to sign, and respond with a [`SignedChallenge`][SignedChallenge].

The [`SignedChallenge`][SignedChallenge] message carries a JSON-serialized [authentication chain]({{< relref "../auth/authchain" >}}) that begins with the provided address, and ends with the challenge signature.

If the challenge signature is successfully verified by the service, the client will receive a [`WelcomePeerInformation`][WelcomePeerInformation] message.


```goat
 .-----------.                .--------.                                                            
 |    BFF    |                | Client |
 '----+------'                '---+----'
       ⋮                          |
       ⋮                  Connect |
       o - - - - - - - - - - - - -|
       |                          |
       |                          |
       |      GetChallengeRequest |
       |<-------------------------+
       +------------------------->|
       | GetChallengeResponse     |
       |                          |
       |                          |
       |          SignedChallenge |
       |<-------------------------+
       +------------------------->|
       | WelcomePeerInformation   |
       |                          |
```

Protocol failures (e.g. malformed messages) during the authentication phase will result in immediate disconnection. !!


## Sending Heartbeat {#heartbeat}

During their session with Archipelago, clients must periodically send a _heartbeat_ message to keep
the connection active, and keep Archipelago updated as needed to issue island assignments.

{{< info >}}
The recommended heartbeat frequency for comms clients is about one update per second.
{{< /info >}}

The [`Heartbeat`][Heartbeat] message includes two fields:

| Field | Type | Value
| ----- | --- | --- |
| `position` | `Position` | The 3D coordinates of the current position in the world map.
| `desired_room` | `string?` | Optional request for a specific island (e.g. to join a friend)


When given a `desired_room` parameter, Archipelago will try to honor the request and assign the
client to specified island, but it may (rarely) reject if the island population is already too large. Clients should verify their assignments.


## Getting Island Assignments {#assignment}

Shortly after the first heartbeat, Archipelago will send the client their first [`IslandChangeMessage`][IslandChangeMessage].

| Field | Type | Value
| ----- | --- | --- |
| `island_id` | `string` | The unique identifier for the island.
| `conn_str` | `string` | The connection string containing an adapter URI.
| `from_island_id` | `string?` | The previous island ID, if any.
| `peers` | `map<string, Position>` | Other players (identified by address) and their positions.


The main field is the `conn_str`, which can be used to initialize an adapter and connect to the island. Values typically look like this:

```
livekit:wss://comms.example.com?access_token=eyJhbGciOiJI...
```

The label before the first `:` is the adapter type, the rest is a specialized URI for it. It can include pre-authorized tokens or other parameters.

During the session, Archipelago may send a new assignment at any time, for a number of reasons:

1. Position changes: the client reported moving away from others in the island.
2. Island requests: the client requested being assigned to a specific island.
3. Archipelago policy: the service decided to create or divide islands to better balance the population.

Clients must listen for these assignments, closing and opening adapter connections as indicated, and
changing the type of adapter in use when required.


[SignedChallenge]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/bff/authentication_service.proto#L13
[WelcomePeerInformation]: https://github.com/decentraland/protocol/blob/e877adcab9411b13be327b1f314d04994098246a/proto/decentraland/bff/authentication_service.proto#L17
[GetChallengeRequest]: https://github.com/decentraland/protocol/blob/e877adcab9411b13be327b1f314d04994098246a/proto/decentraland/bff/authentication_service.proto#L4
[GetChallengeResponse]: https://github.com/decentraland/protocol/blob/e877adcab9411b13be327b1f314d04994098246a/proto/decentraland/bff/authentication_service.proto#L8
[BffAuthenticationService]: https://github.com/decentraland/protocol/blob/e877adcab9411b13be327b1f314d04994098246a/proto/decentraland/bff/authentication_service.proto#L24
[Heartbeat]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/v3/archipelago.proto#L62
[IslandChangedMessage]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/v3/archipelago.proto#L17