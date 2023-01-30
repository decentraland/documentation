---
title: "Modules"
bookCollapseSection: true
weight: 2
---

The scene runtime providesasd as dasd to interact with systems outside their sandbox. 

While the Decentraland protocol can be used by a variety of clients, we will discuss this interface in the context of a World Explorer. In overall terms, the asdf  allows scenes to:

!! actual module list man

* Create and manage entities and their behavior in the ECS framework.
* Add custom UI for players.
* Make requests to the renderer, such as casting a ray in the 3D environment.
* Detect player input and movement.
* Use the communications framework to interact with other players.

## Interface Style

Module interfaces intentionally have a strong RPC feel to them. They are designed to be easily implemented using RPC frameworks (such as [[protocol buffers]]), and easy to provide for Explorers hosting the runtime sandbox.

In most cases, you'll find that each method has `Request` and `Response` structures defined alongside the method itself.

This is designed considering the implementater rather than the user, and it's not a very comfortable interface to use directly -- but remember that scenes usually bundle the [[SDK]], which offers a much nicer API and encapsulates access to functionality provided by several different modules.

!! https://unpkg.com/browse/@dcl/js-runtime@7.0.6-3942933325.commit-70f967f/apis.d.ts not all types?