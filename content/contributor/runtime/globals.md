---
title: "Globals"
sidebartitle: "Globals"
url: "/contributor/runtime/globals"
weight: 2
---

The scene runtime ensures the existence of certain objects and functions inside the sandboxed Javascript environment, in addition to the standard utilities such as `Promise`, `Date` or `Math`.

{{< info >}}
The globals described below are typical JavaScript concepts, but they are tailored to the Decentrland scene runtime and may not behave identically to their counterparts in browser or Node environments.
{{< /info >}}

## Globals

The runtime injects 7 definitions in the scene's global scope:

1. [`console`](#console): a simplified version of the typical `console` object.
2. [`exports`](#module): an object where the scene can add its [public interface]({{< relref "execution" >}}).
3. [`module`](#module): a container for the `exports` object.
4. [`require`](#module): a function to load runtime-provided modules by name.
5. [`setImmediate`](#scheduling): a function to schedule calls after all pending callbacks run.
6. [`fetch`](#http): a restricted implementation of the browser `fetch` function.
7. [`WebSocket`](#http): a restricted implementation of the browser `WebSocket` class.

All of these are defined as read-only properties, so they cannot be reassigned. Some will throw exceptions when used unless certain [permissions]({{< ref "/contributor/content/entity-types/scenes#permissions" >}}) are granted to the scene.


## Console {#console}

Scenes have access to a `console` object, much like the one provided by a browser or Node environment, though limited to only some of the methods you would normally find.

```ts
type Console = {
  log(...args: any): void
  info(...args: any): void
  debug(...args: any): void
  warning(...args: any): void
  error(...args: any): void
}
```

Just like their standard counterparts, each method takes variable arguments of any type and renders them as human-readable messages. For example, this is valid:

```js
console.log("The thing just appeared", { thing: "foo" }, [1, 2, 3])
```

The precise behavior of these methods depends on the provider, but the messages must be accessible to scene developers debugging their code.

{{< info >}}
In the Foundation's browser-based World Explorer, log messages appear in the developer tools panel.
{{< /info >}}


## Imports and Exports {#module}

Scenes can import and export objects using the traditional [CommonJS](https://wiki.commonjs.org/wiki/Modules/1.0) module interface.

```ts
exports: Object
require(moduleName: string): Object
```

The `require` function allows scenes to access runtime-provided modules (such as [EngineApi]({{< relref "modules/engine_api" >}}) or [RestrictedActions]({{< relref "modules/restricted_actions" >}})), and nothing else (it **does not** access NPM packages or modules by path).

Properties added to the `exports` object are the scene's public interface and will be exposed to the runtime. In fact, scenes _must_ expose at least one method to run properly (see [execution]({{< relref "execution" >}})).

{{< info >}}
Scenes written in languages such as TypeScript use the more modern `import` and `export` statements, which can be transpiled into CommonJS-compatible uses of `require` and `exports`.
{{< /info >}}


## Scheduling {#scheduling}

When a scene needs to schedule callbacks and have their execution controlled by the sandbox host, it can use the `setImmediate` global. 

```ts
setImmediate(fn: Function): void
```

These callbacks will be invoked immediately after all the currently pending tasks in the event loop are processed, and before the next round begins.

In a World Explorer, the `setImmediate` implementation is usually synchronized with the game engine, to execute after the [game loop tick](https://adr.decentraland.org/adr/ADR-148).


## HTTP and WebSockets {#http}

The `fetch` and `WebSocket` globals work exactly like their well-known counterparts (see [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) in MDN), but with some restrictions enforced by the runtime.

When calling the `fetch` function:

- An error is thrown if the URL doesn't begin with `https://`.
- An error is thrown if the scene doesn't have the [`USE_FETCH` permission]({{< ref "/contributor/content/entity-types/scenes#permissions" >}}).
- An implementation-defined timeout can abort the request.

When using the `WebSocket` class:

- An error is thrown if the URL doesn't begin with `wss:`
- An error is thrown if the scene doesn't have the [`USE_WEBSOCKET` permission]({{< ref "/contributor/content/entity-types/scenes#permissions" >}}).

Apart from these differences, both cases follow standard behavior.







