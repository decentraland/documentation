---
title: "Globals"
sidebartitle: "Globals"
url: "/contributor/runtime/globals"
weight: 2
---

The scene runtime ensures the existence of certain objects and functions inside the sandboxed Javascript environment, available in the global scope.

Most of them are implementations of familiar browser and/or Node concepts, such as `console` or `setImmediate`.

## Globals

The runtime injects 7 definitions in the scene's global scope:

1. [`console`](#console): a subset of the Node/browser `console` object.
2. [`module`](#module): a subset of Node's `module` object.
3. [`exports`](#module): a shortcut to `module.exports`, as in Node.
4. [`require`](#module): an implementation of Node's `require` for a curated list of modules.
5. [`setImmediate`](#scheduling): an implementation of Node's `setImmediate`.
6. [`fetch`](#http): a restricted implementation of the browser `fetch` function.
7. [`WebSocket`](#http): a restricted implementation of the browser `WebSocket` class.

All of these are defined as read-only properties, so they cannot be reassigned. Some will throw exceptions when used unless certain [permissions]({{< ref "/contributor/content/entity-types/scenes#permissions" >}}) are granted to the scene.


## Console {#console}

Scenes have access to a `console` object, much like the one provided by a browser or Node environment, though limited to the some of the methods you would normally find.

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

Scenes can import and export objects using a Node-like interface.

The `require` function provides access to optional modules that scenes can leverage. Since the `require` function is injected by the runtime, so are the module definitions and their import paths.

```ts
require(moduleName: string): { exports: Object }
```

Scenes can (and must]]) export objects by setting keys in `module.exports`, or the `exports` shortcut.

See the [execution]({{< relref "execution" >}}) page for more information.


## Scheduling {#scheduling}

When a scene needs to schedule callbacks with their execution controlled by the sandbox host, it can use the Node-like `setImmediate` global. These callbacks will queue up and be invoked before the next [[tick]].

!!Is this correct? What are the scheduling guarantees? Does it behave like Node, in the sense that callbacks are invoked on the next round of the event loop? Document exact behavior.

```ts
setImmediate(fn: Function): void
```

{{< info >}}
In the Foundation's World Explorer, scenes have a CPU quota they cannot exceed. Callbacks will run when there's computing time to spare.
!! i need to know all about this, and know very little
{{< /info >}}


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







