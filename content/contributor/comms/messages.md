---
title: "Messages"
sidebartitle: "Messages"
url: "/contributor/comms/messages"
weight: 2
---

Messages in comms are binary data _packets_, serialized using [protocol buffers](https://github.com/protocolbuffers/protobuf). They carry text and voice chat, positional updates, profile changes and other real-time interactions.

You can find all definitions in the [protocol repository](https://github.com/decentraland/protocol), or by following the link in each message type.


###### `Packet` <small>[↗ source][Packet]</small> {#Packet}

The `Packet` structure is the container for all messages.

| Field | Type | Value
| ----- | --- | --- |
| `message` | `enum` | One of `Chat`, `Voice`, `Position`, `AnnounceProfileVersion`, <br>`ProfileRequest`, `ProfileResponse`, or `Scene`.


## Text and Voice Chat

Clients chat by broadcasting text messages and audio clips to all connected peers (usually players in the same island).

Only two `Packet` types are involved, one for each use-case. Under typical circumstances, clients broadcast these messages to all other clients in their island, which is the group of nearby players they can interact with.

---
###### `Chat` <small>[↗ source][Chat]</small> {#Chat}

Sends a text chat message to other clients.


| Field | Type | Value
| ----- | --- | --- |
| `message` | `string` | Text of the message
| `timestamp` | `double` | Sender's UTC timestamp


---
###### `Voice` <small>[↗ source][Voice]</small> {#Voice}

Sends an encoded voice sample to other clients.

| Field | Type | Value
| ----- | --- | --- |
| `encoded_samples` | `bytes` | Encoded audio data
| `codec` | `enum` | Only `VC_OPUS` (no other codecs are supported for now)
| `index` | `uint32` | An incremental counter set by the sender

The `codec` field is an `enum` value. Custom codecs are not supported.


## Movement

Clients that control avatars send and receive positional updates within their island, in order to synchronize movement and posture among players.

---
###### `Position` <small>[↗ source][Position]</small> {#Position}

Updates other clients on the position and orientation of an avatar.

| Field | Type | Value
| ----- | --- | --- |
| `position_x`<br>`position_y`<br>`position_z` | `float` | Avatar position in the world map
| `rotation_x`<br>`rotation_y`<br>`rotation_z`<br>`rotation_w` | `float` | Avatar rotation quaternion
| `index` | `uint32` | An incremental counter set by the sender

Clients typically send `Position` updates with a low frequency (such as once every 1 or 2 seconds), and switch to a high frequency (several times per second) when moving or interacting.

{{< info >}}
When sending positional updates, speed is usually better than reliability. The perceived performance is better when delivery is faster, even if a `Position` message is ocasionally dropped or reordered. Some adapters (e.g. [LiveKit]({{< relref "adapters/livekit" >}})) can change between fast and reliable modes on a per-message basis.
{{< /info >}}

The low-frequency broadcasts are recommended as a simple solution for deliverying updates to clients that momentarily lost connectivity or failed to catch a message while they joined the island.

The `index` field is an incremental counter, set by the sender so receivers can sort updates that arrive out-of-order.


## Profile Sharing

Clients within an island can request the avatar information of other players, in order to render their avatars, display their names and pictures, etc.

Since profiles changes are rare (compared with positional updates, for example), the system is designed to simplify the task of maintaining a local profile cache, and only fetch profiles when needed.

There's 3 [`Packet`](#Packet) types involved: a [`ProfileRequest`](#ProfileRequest)/[`ProfileResponse`](#ProfileResponse) pair used by clients to share profiles on demand, and the [`AnnounceProfileVersion`](#AnnounceProfileVersion) message to tell peers what the latest version is, so they can decide whether to request it.

Clients typically broadcast `AnnounceProfileVersion` messages periodically, plus immediately when their profile changes. 


```goat
.----------.                   .----------.                 .----------.                            
| Client 1 |                   | Client 2 |                 | Client 3 |
'----+-----'                   '----+-----'                 '----+-----'
     |                              |                            ⋮
     o  AnnounceProfileVersion(v1)  |                            ⋮
     |                              |                            ⋮
     |                              |                            ⋮
     o  AnnounceProfileVersion(v1)  |                            ⋮
     |                              |                            |
     |                              |                            o ProfileRequest(@client 1) 
     |                              |                            |
     o ProfileResponse(v1)          |                            |
     |                              |                            |
     |                              |                            |
     o AnnounceProfileVersion(v1)   |                            |
     |                              |                            |
     |                              |                            |
     o AnnounceProfileVersion(v2)   |                            |
     |                              |                            |
     |                              o ProfileRequest(@client 1)  o ProfileRequest(@client 1) 
     |                              |                            |
     o ProfileResponse(v1)          |                            |
     |                              |                            |
     |                              |                            |
     
     
```

---
###### `AnnounceProfileVersion` <small>[↗ source][AnnounceProfileVersion]</small> {#AnnounceProfileVersion}

Signals other clients that there's a [profile entity]({{< ref "/contributor/content/entity-types/profiles" >}}) they can request.

| Field | Type | Value
| ----- | --- | --- |
| `profile_version` | `uint32` | A version number incremented with every modification.

Receivers that cache profiles can use the `profile_version` number to decide whether their local copy is up-to-date, or if they need to send a [`ProfileRequest`](#ProfileRequest).


---
###### `ProfileRequest` <small>[↗ source][ProfileRequest]</small> {#ProfileRequest}

Requests a profile of a specified version from a particular peer.

| Field | Type | Value
| ----- | --- | --- |
| `address` | string | The identifying address for the profile.
| `profile_version` | `uint32` | The wanted profile version.

Receivers can reply with [`ProfileResponse`](#ProfileResponse) messages to provide the requested profile.


---
###### `ProfileResponse` <small>[↗ source][ProfileResponse]</small> {#ProfileResponse}

Sends a profile in response to a [`ProfileRequest`](#ProfileRequest).

The `serialized_profile` field contains the JSON serialization of a [profile entity]({{< ref "/contributor/content/entity-types/profiles" >}}).

If the sender wants to recommend a content server to download entities referenced in their profile, it can set the `base_url` field.


<!--
---
###### `Scene` <small>[↗ source][Scene]</small> {#Scene}
!! TODO
-->

[Packet]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/rfc4/comms.proto#L8
[Position]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/rfc4/comms.proto#L20
[AnnounceProfileVersion]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/rfc4/comms.proto#L34
[ProfileRequest]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/rfc4/comms.proto#L41
[ProfileResponse]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/rfc4/comms.proto#L46
[Chat]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/rfc4/comms.proto#L56
[Scene]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/rfc4/comms.proto#L61
[Voice]: https://github.com/decentraland/protocol/blob/c48ea0aa00d8173084571552463a6a05a7f49636/proto/decentraland/kernel/comms/rfc4/comms.proto#L66