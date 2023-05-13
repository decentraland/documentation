---
title: "Transports"
sidebartitle: "Transports"
url: "/contributor/comms/transports"
weight: 4
---

A _transport_ is an interface that encapsulates the wire protocol of a real-time comms backend, providing a unified API across all variants.

{{< info >}}
You can see the comms protocol in action and experiment with it using the open-source [[Comms Demo Station]].
{{< /info >}}

There are 5 defined transport types:

* [Websocket]({{< relref "transport-types/websocket" >}}) (`ws-room`) uses the standard websocket protocol.
* [LiveKit]({{< relref "transport-types/livekit" >}}) (`livekit`) uses the open-source LiveKit framework.
* [SignedLogin]({{< relref "transport-types/signed_login" >}}) (`signed-login`)makes a signed HTTPs request to obtain a new transport from a server.
* [Offline]({{< relref "transport-types/offline" >}}) (`offline`) is a dummy transport indicates there are no comms in the current environment.
* [Simulator]({{< relref "transport-types/simulator" >}}) (`simulator`) is a dummy transport with completely custom behavior, mainly for developers to debug their implementations.

Messages sent and received through a transport interface are always the same (see [messages]({{< relref "messages" >}} or the )), although some transports may wrap them in control structures for transmission. In the end, as long as a transport can send and receive comms messages, it is free to leverage any wire protocol or delivery strategy under the hood.

To illustrate, this is a `Transport` interface defined in Typescript:


## Creating a Transport

Transports are created using a single connection string, which is a URI of the form:

```
<transport type>:<connection parameters>
```

The `transport type` corresponds to one listed above, and `connection parameters` is dependent on the specific transport. It can be a URL, an opaque token, or even arbitrary data. 

The [LiveKit]({{< relref "transport-types/livekit" >}}) transport, for example, uses a `wss` URL with an `access_token` parameter to establish an authenticated connection:

```
livekit:wss://comms.example.com?access_token=eyJhbGciOiJI...
```

For comparison, the [Websocket]({{< relref "transport-types/websocket" >}}) transport also uses a `wss` URL, but without a pre-generated token. It requires an authentication flow once connected.


## Connecting, Sending and Receiving

The specifics of each transport implementation are left to developers, so they can adapt to the constraints of any particular framework, language or environment. However, some functionality should always be present in a `Transport` interface.

To illustrate, this is a minimal but reasonable TypeScript interface:

```ts
interface Transport {
  // Open a connection using the paramters in the transport URI:
  connect(connParams: string): Promise<void>

  // Close the connection:
  disconnect(): Promise<void>

  // Send an arbitrary payload:
  send(data: Uint8Array): Promise<void>

  // Subscribe to incoming messages:
  on(event: 'message', callback: (packet: Packet) => void): void
}
```

## Client Requirements

Clients may choose to implement only some of the specified adapters, according to their use-case and the servers they expect to interact with.

For versatile clients, such as a World Explorer, it's recommended to implement at least the [websocket]({{< relref "transport-types/websocket" >}}) and [LiveKit]({{< relref "transport-types/livekit" >}}) transports, which are currently used by all major realms.