---
title: "Overview"
sidebartitle: "Overview"
url: "/contributor/runtime/overview"
weight: 1
---

The Decentraland scene runtime is the sandboxed execution environment where a [scene]({{< relref "../content/entity-types/scenes" >}}) runs its main script.

Within the environment, scenes have access to certain [[global objects]] and can import [[modules]] from the runtime library to access a wide array of functionality. For example:

- Create entities and control their behavior
- Interact with the player
- Communicate with other players
- Inspect the state of the world
- Connect to external services
- Make web3 payments

!!chart

In practice, scenes bundle the [[SDK]] library with their code, which encapsulates the RPC interface and provides a nice and comfortable API. It implements an Entity-Component-System (ECS) framework (among other utilities) and higher-level methods to communicate with a renderer in a World Explorer.

{{< info >}}
Note that the [[SDK]] is _not_ part of the Decentraland protocol. Scenes can decide whether bundle it, or use alternative libraries that abstract some or all of the functionality.
{{< /info >}}


## Global Objects

Inside the sandboxed environment, [[scenes]] assume certain objects and functions are globally available. These are provided by the runtime and implement base functionality such as requiring modules, logging messages and scheduling callbacks.

Se [[globals]] for more details.


## Modules

The [[`require`]] global function can import modules provided from outside the sandbox. These modules allow selectively importing utilities such as the ECS or Comms systems.

See [[modules]] for a comprehensive list.


## Permissions

Sensitive functionality, such as making HTTP requests to 3rd party services, is restricted by the runtime unless certain permissions are requested by the [[scene]], and granted by the player.

See the [[permissions]] module to learn more.