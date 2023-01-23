---
title: "Execution"
sidebartitle: "Execution"
url: "/contributor/runtime/execution"
weight: 3
---

The runtime treats [[scenes]] like modules. Once the sandbox is set up (i.e. all [[globals]] are injected and [[modules]] are ready to be loaded), the code of the scene will be evaluated so it can populate the [[`exports`]] object.

Two methods will be picked up by the host from `exports`: [[`onStart`]] (optional) and [[`onUpdate`]] (mandatory).

```ts
type Exports = {
  onStart?: () => Promise<void>
  onUpdate: (deltaSeconds: number) => Promise<void>
}
```

{{< info >}}
Most scenes use the [[Decentraland SDK]], which provides a higher-level interface and automatically exports these methods. However, the SDK is _not_ part of the protocol, and scene developers can decide not to use it.
{{< /info >}}

!!add nice diagram, light on detail

During the life-cycle of a scene, the runtime will ensure that calls to these methods are never made concurrently. The returned `Promise` will always be awaited before the scene receives a new call.


###### `onStart` {#onStart}

The life-cycle of a [[scene]] begins with the asynchronous `onStart` method. It's the place to make one-time initializations that must complete before the first call to [[`onUpdate`]] is made.

```ts
onStart(): Promise<void>
```

Exporting `onStart` is not required, and scenes are not expected to do anything in particular if they do. The method can be missing or do nothing and return an immediately resolved `Promise`.

{{< info >}}
Scenes using the Decentraland SDK export an empty `onStart` method, unless explicitly overridden by the developer.
{{< /info >}}

!!examples of useful things


###### `onUpdate` {#onUpdate}

While a scene is actively running, the asynchronous `onUpdate` method will be periodically invoked by the runtime to report the passage of time. This is the heart of the scene: in each successive call, entities can be updated, input processed, animations played, messages sent, UI displayed, etc.

```ts
onUpdate(deltaSeconds: number): Promise<void>
```

The `deltaSeconds` parameter is the fractional number of seconds elapsed since the last call to `onUpdate` was initiated by the runtime (regardless of when the returned `Promise` was settled). This is specific to each running scene.

Since `onUpdate` calls will never overlap, the sequence of `deltaSeconds` produces a coherent timeline.

In ideal circumstances, scenes get a chance to run `onUpdate` before each frame is rendered. However, depending on available resources, scenes running a heavy workload may not settle their `Promise` in time for the next frame. Each scene is independent in this respect: lightweight implementations of `onUpdate` may be invoked multiple times in the same period as a single, time-consuming call in another scene.

!!add nice diagram, see the ADR
!!quotas?