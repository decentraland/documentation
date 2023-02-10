---
title: "Overview"
sidebartitle: "Overview"
url: "/contributor/runtime/overview"
weight: 1
---

The Decentraland scene runtime is the sandboxed execution environment where a [scene]({{< relref "../content/entity-types/scenes" >}}) runs its main script.

Each scene runs inside its own isolated runtime. Within it, it has access to certain [global objects]({{< relref "globals" >}}) and can import [modules]({{< relref "modules" >}}) from the runtime library.

 
```goat
.-----------------------------------------------------'
.                                                     '
|                   World Explorer                    |
|                                                     |
|  .---------+---.  .---------+---.  .---------+---.  | 
|  | Runtime     |  | Runtime     |  | Runtime     |  |  
|  |             |  |             |  |             |  |  
|  |  .------+   |  |  .------+   |  |  .------+   |  |  
|  |  |       |  |  |  |       |  |  |  |       |  |  |  
|  |  | Scene |  |  |  | Scene |  |  |  | Scene |  |  |  
|  |  |       |  |  |  |       |  |  |  |       |  |  |  
|  |  '---+---'  |  |  '---+---'  |  |  '---+---'  |  |  
|  |      |      |  |      |      |  |      |      |  |  
|  '------+------'  '------+------'  '------+------'  |   
|         |                |                |         |
|         v                v                v         |
|  .-----------------------------------------------.  |
|  |            Runtime module library             |  |
|  '--------------------------+----------------+---'  |
'-----------------------------------------------------'
```

By importing modules from the runtime library, scenes have access a wide array of functionality, including:

- Create entities and control their behavior
- Interact with the player
- Communicate with other players
- Inspect the state of the world
- Connect to external services
- Make web3 payments


In practice, scenes bundle the [Decentraland SDK]({{< ref "/creator/sdk7/getting-started/sdk-101" >}}) with their code, which encapsulates the RPC-style interface of the runtime library and provides a nicer and more comfortable API.

{{< info >}}
Note that the SDK is _not_ part of the Decentraland protocol. Scenes can decide whether bundle it, or use alternative libraries that abstract some or all of the functionality.
{{< /info >}}


## Global Objects

Inside the sandboxed environment, [scenes]({{< relref "../content/entity-types/scenes" >}}) assume certain objects and functions are globally available. Some are standard ES-2020 objects (like `Date` or `Math`), and others are injected by the runtime to implement functionality such as requiring modules, logging messages and scheduling callbacks.

Se [globals]({{< relref "globals" >}}) for more details.


## Modules

The [`require`]({{< relref "globals#module" >}}) global function can import modules provided by the [runtime library]({{< relref "execution" >}}). These modules allow selectively importing utilities such as the ECS or Comms systems.

See the runtime modules section for a comprehensive list.


## Execution

The runtime requires that scenes implement a specific set of methods, and guarantees they will be called according to certain rules.

See [execution]({{< relref "execution" >}}) for more on this.


## Permissions

Sensitive functionality, such as making HTTP requests to 3rd party services, is restricted by the runtime unless certain permissions are requested by the [scene]({{< relref "../content/entity-types/scenes" >}}), and granted by the player.

See [permissions]({{< relref "permissions" >}}) to learn more.