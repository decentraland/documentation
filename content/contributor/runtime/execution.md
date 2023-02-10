---
title: "Execution"
sidebartitle: "Execution"
url: "/contributor/runtime/execution"
weight: 3
---

The runtime treats [scenes]({{< ref "/contributor/content/entity-types/scenes" >}}) like typical Node modules. Once the sandbox is set up (i.e. all [globals]({{< relref "" >}}) are injected and [modules]({{< relref "modules" >}}) are ready to be loaded), the code of the scene will be evaluated so it can populate the [exports]({{< relref "globals#module" >}}) object.

Two methods will be picked up by the host from `exports`: [`onStart`](#onStart) (optional) and [`onUpdate`](#onUpdate) (mandatory).

```ts
type Exports = {
  onStart?: () => Promise<void>
  onUpdate: (deltaSeconds: number) => Promise<void>
}
```

During the life-cycle of a scene, the runtime will ensure that calls to these methods are never made concurrently. The returned `Promise` will always be awaited before the scene receives a new call.

```goat
.---------.              .----------.
| onStart +------------> | onUpdate +-----.
'---------'   await      '----------'     |                                         
                               ^   await  |
                               +----------'
```

{{< info >}}
Most scenes use the [Decentraland SDK]({{< ref "/creator/sdk7/getting-started/sdk-101" >}}), which provides a higher-level interface and automatically exports these methods. However, the SDK is _not_ part of the protocol, and scene developers can decide not to use it.
{{< /info >}}

###### `onStart` {#onStart}

The life-cycle of a scene begins with the asynchronous `onStart` method. It's the place to make one-time initializations that must complete before the first call to [`onUpdate`](#onUpdate) is made.

```ts
onStart(): Promise<void>
```

Exporting `onStart` is not required, and scenes are not expected to do anything in particular if they do. The method can be missing or do nothing and return an immediately resolved `Promise`.

{{< info >}}
Scenes using the Decentraland SDK export a default `onStart` method that obtains the initial state of the [basic entities]({{< relref "entities" >}}).
{{< /info >}}


###### `onUpdate` {#onUpdate}

While a scene is actively running, the asynchronous `onUpdate` method will be periodically invoked by the runtime to report the passage of time. This is the heart of the scene: in each successive call, entities can be updated, input processed, animations played, messages sent, UI displayed, etc.

```ts
onUpdate(deltaSeconds: number): Promise<void>
```

The `deltaSeconds` parameter is the fractional number of seconds elapsed since the last call to `onUpdate` was initiated by the runtime (regardless of when the returned `Promise` was settled). This is specific to each running scene.

Since `onUpdate` calls will never overlap, the sequence of `deltaSeconds` produces a coherent timeline.

In ideal circumstances, scenes get a chance to run `onUpdate` before each frame is rendered. However, depending on available resources, scenes running a heavy workload may not settle their `Promise` in time for the next frame. Each scene is independent in this respect: lightweight implementations of `onUpdate` may be invoked multiple times in the same period as a single, time-consuming call in another scene.

See [ADR-148](https://adr.decentraland.org/adr/ADR-148) for details.


## Running Multiple Scenes

The World Explorer must not only support running several sandboxed scenes, it should be doing so at all times. There's two reasons for this:

First, when players explore the world, their sight reaches beyond the geographical limits of the scene they are standing on. Nearby scenes (up to an arbitrary or configurable distance) must be running to generate the content players should be able to see.

Second, scenes don't just run inside their own, non-overlapping boundaries. They can also be layered on top of each other, affecting the area around the player but providing different functionality.

This is the case for two kinds of scenes in particular: the avatar scene, and portable experiences.


### The Avatar Scene {#avatarScene}

From the moment the player enters the world, a global scene tasked with rendering the avatars of other players starts running.

This scene is not limited by geographical boundaries, and can display its entities (as well as UI widgets for communication) regardless of the player's location.


### Portable Experiences

Decentraland allows wearables to have their own behavior, which runs in its own scene context. These scenes are centered around the player, and can enrich the experience by adding entities or showing UI widgets.

They start running when the wearable is equipped, and stop when it's removed.
