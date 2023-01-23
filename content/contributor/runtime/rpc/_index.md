---
title: "RPC Interface"
sidebartitle: "RPC Interface"
url: "/contributor/runtime/rpc"
weight: 2
---

The scene runtime provides an RPC interface for scenes to interact with systems outside their sandbox. 

While the Decentraland protocol can be used by a variety of clients, we will discuss this interface in the context of a World Explorer. In overall terms, the RPC allows scenes to:

* Create and manage entities and their behavior in the ECS framework.
* Add custom UI for players.
* Make requests to the renderer, such as casting a ray in the 3D environment.
* Detect player input and movement.
* Use the communications framework to interact with other players.

The interface is defined using [[protocol buffers]], which auto-generates code for the object model in various programming languages.

Note that scene creators will usually work with higher-level code by using the SDK, which wraps the protocol layer and offers a much simpler API.

## Messages

!!The [[protocol buffer definition]] contains a number of action messages and structures that model the parameters and responses for each call.

## Managing Entities

Scenes can instruct the renderer to create, !!

The top-level `message` is [[`EntityAction`]], which has a `type` and a polymorphic `payload` that depends on it.

| Field | Type | Value |
| --- | --- | --- |
| `type` | `enum EAType` | An identifier for the kind of `payload` (see below).
| `payload` | `Payload` | Data specific to the `type` (see below).
| `tag` | `optional string` | !!



### Payloads

The `Payload` structure contains a series of `optional` fields, one for each `EAType`, with only one present in any given case. The `type` field of `EntityAction` indicates which of these fields will be present.