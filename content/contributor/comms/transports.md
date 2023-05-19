---
title: "Transports"
sidebartitle: "Transports"
url: "/contributor/comms/transports"
weight: 4
---

A _transport_ is a client-side interface that can connect to a comms URI and exchange real-time messages with peers or services. 

{{< info >}}
You can see the comms protocol in action and experiment with it using the open-source [[Comms Demo Station]].
{{< /info >}}

Clients are free to implement transports as they see fit (as long as they follow the protocol expected by other clients and services), but the [recommended design](#recommended) described below has been tested in practice and proven to integrate well with different projects.`

## Standard Transports {#types}

There are 5 transport types defined by the protocol:

* [Websocket]({{< relref "transport-types/websocket" >}}) (`ws-room`) uses a standard websocket stream.
* [LiveKit]({{< relref "transport-types/livekit" >}}) (`livekit`) uses the open-source LiveKit framework, based on WebRTC.
* [SignedLogin]({{< relref "transport-types/signed_login" >}}) (`signed-login`) makes a signed HTTPs request to obtain a dynamically assigned transport from a server.
* [Offline]({{< relref "transport-types/offline" >}}) (`offline`) is a dummy transport indicates there are no comms in the current environment.
* [Simulator]({{< relref "transport-types/simulator" >}}) (`simulator`) is a dummy transport with completely custom behavior, mainly for developers to debug their implementations.

Messages sent and received through a transport interface are always the same (see [messages]({{< relref "messages" >}})). Some transports may wrap them in control structures for transmission, but these should be unpacked before crossing the `Transport` interface.


## Recommended Design {#recommended}

This is a minimal `Transport` interface written in TypeScript:

```ts
interface Transport {
  // Initialize the Transport with a URI:
  constructor(private uriWithConnectionParams: string)

  // Open a connection using the URI given in the constructor:
  connect(): Promise<void>

  // Close the connection:
  disconnect(): Promise<void>

  // Send an arbitrary payload to the service and all peers:
  send(packet: Packet): Promise<void>

  // Subscribe to incoming messages from both the service and all peers:
  on(event: 'receive', callback: (packet: Packet) => void): void
}
```

Actual implementations commonly extend this, adding connection/disconnection and join/leave events, non-broadcast sending, stricter typing or language-specific adaptations.

### Transport URIs

The values of `uriWithConnectionParams` are always of the form:

```
<type>:<type connection parameters>
```

The `<type>` corresponds to one listed above, and the format for `<type connection parameters>` is dependent on the specific transport. It can be a URL, an opaque token, or any arbitrary data.

The [LiveKit]({{< relref "transport-types/livekit" >}}) transport, for example, uses a `wss` URL with an `access_token` parameter to establish an authenticated connection:

```
livekit:wss://comms.example.com?access_token=eyJhbGciOiJI...
```

For comparison, the [Websocket]({{< relref "transport-types/websocket" >}}) transport also uses a `wss` URL, but without a pre-generated token. It requires an authentication flow once connected.


### Creating Transports

Since each `Transport` class will support a particular kind of URI, it's a good idea to have a factory method that either returns a valid `Transport` or fails immediately. For example:

```ts
function createTransport(uriWithConnectionParams: string) {
  const type = getPrefix(urlWithConnectionParams)

  switch (type) {
    case 'ws-room': return new WsRoomTransport(uriWithConnectionParams)
    case 'livekit': return new LiveKitTransport(uriWithConnectionParams)
    // ... other supported implementations...
  }

  throw new Error(`Unsupported transport type: ${type}`)
}
```

Clients are not required to implement all standard transports. If they intend to only use a subset of the defined types without aiming to handle all URIs, they are free to reject types they don't support.

More featured clients, such as a World Explorer, are advised to implement at least the [websocket]({{< relref "transport-types/websocket" >}}) and [LiveKit]({{< relref "transport-types/livekit" >}}) transports, which are currently in use by all major realms.


## Learn more

Head over to a [specific transport type](#types) section, read about the different [message types]({{< relref "messages" >}}) or check out the [[Comms Demo Station]].