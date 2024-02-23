---
title: "Archipelago"
sidebartitle: "Archipelago"
url: "/contributor/comms/archipelago"
weight: 3
---

Archipelago is the realm service that groups nearby players into islands, reassigning them as they move around and providing the information required to connect to the actual backend that will relay their messages.

{{< info >}}
You can see the Archipelago protocol in action and experiment with it using the open-source [Comms Station](https://decentraland.github.io/comms-station/).
{{< /info >}}

To use the service, clients must connect to their realm's Archipelago websocket endpoint and authenticate to begin their session. They can then start sending positional updates and receiving island assignments (see the [client life-cycle]({{< relref "overview#lifecycle" >}})).

All messages exchanged with the Archipelago service are encoded using protocol buffers, as defined in the Decentraland [protocol repository](https://github.com/decentraland/protocol).


## Connecting {#connecting}

To begin, clients must open a secure websocket connection (`wss:`) to the `/archipelago/ws` endpoint of the realm.

Once connected, clients have a time window defined by realm policy (60 seconds, by default) to send each message of the [authentication](#authenticating) flow.

**Fixed Adapters**<br>!!
!!While the larger realms run the Archipelago service, smaller ones may choose to provide a fixed backend connection string for all players. The URI, if present, can be found in the `comms.fixedAdapter` property of the realm's `/about`.!!

In these cases, dynamic island assignment won't be available, and the realm's RPC interface should not be used for that purpose.


## Authenticating {#authenticating}

After opening a connection to Archipelago, clients must begin by requesting and signing a challenge from the service to verify their identity.

The first message a client sends is a [`ChallengeRequestMessage`](ChallengeRequestMessage) with their Ethereum address (i.e. their public key). They will receive a [`ChallengeResponseMessage`](ChallengeResponseMessage) with a randomly generated string to sign, and must respond with a [`SignedChallengeMessage`](#SignedChallengeMessage).

The [`SignedChallengeMessage`](#SignedChallengeMessage) carries a JSON-serialized [authentication chain]({{< relref "../auth/authchain" >}}) that begins with the provided address, and ends with the challenge signature.

If the signature is successfully verified by the service, the client is authenticated and will receive a [`WelcomeMessage`](#WelcomeMessage).


```goat
 .-------------.                  .--------.                                                        
 | Archipelago |                  | Client |
 '----+--------'                  '---+----'
       ⋮                              |
       ⋮                  Connect     |
       o - - - - - - - - - - - - - - -|
       |                              |
       |                              |
       |      ChallengeRequestMessage |
       |<-----------------------------+
       +----------------------------->|
       | ChallengeResponseMessage     |
       |                              |
       |                              |
       |       SignedChallengeMessage |
       |<-----------------------------+
       +----------------------------->|
       | WelcomeMessage               |
       |                              |
```


## Sending Heartbeat {#heartbeat}

During their session, clients must periodically send a [`Heartbeat`](#Heartbeat) message to keep Archipelago updated with the necessary information to issue island assignments.

{{< info >}}
The recommended heartbeat frequency for comms clients is about one update per second.
{{< /info >}}

If a client stops sending [`Heartbeat`](#Heartbeat) messages, Archipelago (depending on its current policy) may close the connection.


## Getting Island Assignments {#assignment}

Shortly after the first heartbeat, Archipelago will send the client their first [`IslandChangedMessage`][IslandChangedMessage].

The main field is `conn_str`, which can be used to initialize a transport and connect to the island. Values typically look like this:

```
livekit:wss://comms.example.com?access_token=eyJhbGciOiJI...
```

The label before the first `:` is the transport type, the rest is a specialized URI for it. It can include pre-authorized tokens or other parameters.

During the session, Archipelago may send a new assignment at any time, for a number of reasons:

1. Position changes: the client reported moving away from others in the island.
2. Island requests: the client requested being assigned to a specific island.
3. Archipelago policy: the service decided to create or divide islands to better balance the population.

Clients must listen for these assignments, closing and opening transport connections as indicated, and changing the type of transport in use when required.


## Client Messages

###### `ChallengeRequestMessage` <small>[↗ source][ChallengeRequestMessage]</small> {#ChallengeRequestMessage}

Sent by the client as the first message of a session, to start the authentication flow.

| Field | Type | Value
| ----- | --- | --- |
| `address` | `string` | The user's address.

The `address` field must be derived from the first private key of the [authentication chain]({{< relref "../auth/authchain" >}}) that will be presented.


---
###### `SignedChallengeMessage` <small>[↗ source][SignedChallengeMessage]</small> {#SignedChallengeMessage}

Sent by the client after receiving a [`ChallengeResponseMessage`](#ChallengeResponseMessage), to complete the authentication flow.

| Field | Type | Value
| ----- | --- | --- |
| `auth_chain_json` | `string` | A JSON-serialized [authentication chain]({{< relref "../auth/authchain" >}}) ending with the challenge signature.

The first key in the [authentication chain]({{< relref "../auth/authchain" >}}) must correspond to the address sent in the original [`ChallengeRequestMessage`](#ChallengeRequestMessage).


---
###### `Heartbeat` <small>[↗ source][Heartbeat]</small> {#Heartbeat}

Sent by the client at regular intervals (typically once per second), to update Archipelago on their position and/or request an island assignment.

| Field | Type | Value
| ----- | --- | --- |
| `position` | `Position` | The client's 3D position in the world map
| `desired_room` | `string?` | The ID of an island the client would like to be assigned to

The first `Heartbeat` message a client sends is quickly followed by an [`IslandChangedMessage`](#IslandChangedMessage) from Archipelago. Subsequent updates, however, are independent of island assignments. Clients should not expect a `Heartbeat` to be responded.

When the `desired_room` parameter is included, the service will attempt to honor the request, but a reassignment to that island is not guaranteed. It depends on Archipelago's policy (e.g. limits on island population).


## Server Messages

###### `ChallengeResponseMessage` <small>[↗ source][ChallengeResponseMessage]</small> {#ChallengeResponseMessage}

Sent by Archipelago in response to a [`ChallengeRequestMessage`](#ChallengeRequestMessage)

| Field | Type | Value
| ----- | --- | --- |
| `challenge_to_sign` | `string` | A generated string to sign and create an [authentication chain]({{< relref "../auth/authchain" >}})
| `already_connected` | `bool` | Whether an existing connection for this user's key


---
###### `WelcomeMessage` <small>[↗ source][WelcomeMessage]</small> {#WelcomeMessage}

Sent by Archipelago after successful authentication.

| Field | Type | Value
| ----- | --- | --- |
| `peer_id` | `string` | A unique identifier for the authenticated client (typically their address)


---
###### `IslandChangedMessage` <small>[↗ source][IslandChangedMessage]</small> {#IslandChangedMessage}

Sent by Archipelago when the client is (re)assigned to an island.

Description.

| Field | Type | Value
| ----- | --- | --- |
| `island_id` | `string` | The ID of the new island
| `from_island_id` | `string?` | The ID of the old island, if this is a reassignment
| `conn_str` | `string` | The connection string for the island [transport]({{< relref "transports" >}}).
| `peers` | `map<string, Position>` | Description.

Clients that receive an `IslandChangedMessage` should end their connection to the island backend, and connect to the one given in `conn_str`.

The `peers` field contains the current identities and positions of all peers in the island, so that clients can populate their initial set. After this point, they should rely on messages received via the island [transport]({{< relref "transports" >}}) to get positional updates.


---
###### `KickedMessage` <small>[↗ source][KickedMessage]</small> {#KickedMessage}

Sent by Archipelago before closing a connection.

| Field | Type | Value
| ----- | --- | --- |
| `reason` | `KickedReason` | Archipelago's reason for closing the connection


The standard values for the `reason` field are:

* `KR_NEW_SESSION`: another connection authenticated with the same key.

---
###### `JoinIslandMessage` <small>[↗ source][JoinIslandMessage]</small> {#JoinIslandMessage}

Sent by Archipelago when a peer is assigned to the client's island.

| Field | Type | Value
| ----- | --- | --- |
| `island_id` | `string` | The identifier for the island
| `peer_id` | `string` | The unique identifier for the peer (typically their address)

The `island_id` field will match the client's current assignment.


---
###### `LeftIslandMessage` <small>[↗ source][LeftIslandMessage]</small> {#LeftIslandMessage}

Sent by Archipelago when a peer is removed from the client's island.

| Field | Type | Value
| ----- | --- | --- |
| `island_id` | `string` | The identifier for the island
| `peer_id` | `string` | The unique identifier for the peer (typically their address)

The `island_id` field will match the client's current assignment.




[WelcomeMessage]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L13
[IslandChangedMessage]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L17
[LeftIslandMessage]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L24
[JoinIslandMessage]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L29
[KickedReason]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L34
[KickedMessage]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#LL37C1-L38C1
[ChallengeRequestMessage]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L54
[SignedChallengeMessage]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L58
[Heartbeat]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L62
[ChallengeResponseMessage]: https://github.com/decentraland/protocol/blob/9a568b16b2eafb134177329ba670c1451be8a169/proto/decentraland/kernel/comms/v3/archipelago.proto#L8
