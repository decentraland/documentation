---
date: 2018-01-01
title: Coding essentials
description: This set will help you understand how things work in the client and SDK of decentraland.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/coding-scenes/
weight: 1
---

## The development tools

At a very high level, the Decentraland **Software Development Kit** (SDK) allows you to do the following:

- Generate a default _project_ containing a Decentraland scene, including all the assets needed to render and run your content.
- Build, test, and preview the content of your scene locally in your web browser - completely offline, and without having to make any Ethereum transactions or own LAND.
- Write TypeScript code using the Decentraland API to add interactive and dynamic behavior to the scene.
- Upload the content of your scene to the content server.
- Link your LAND tokens to the URL of the content you have uploaded.

Our SDK includes the following components:

<!--
- **The Decentraland Editor**: Use it to create and preview Decentraland scenes. You don't need to download any software to your machine, the editor runs entirely on your browser.
-->

- **The Decentraland CLI** (Command Line Interface): Use it to [generate]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md" >}}) new Decentraland scenes locally on your own machine, preview them and upload them to the content server.
- **The Decentraland ECS**: A TypeScript package containing the library of helper methods that allows you to create interactive experiences. Use it to create and manipulate objects in the scene and also to facilitate in-world transactions between players or other applications. ( [latest ECS reference](https://github.com/decentraland/ecs-reference/blob/master/docs-latest/decentraland-ecs.md))

- **Scene examples**: Take inspiration and coding best practices from the [scene examples](https://github.com/decentraland-scenes/Awesome-Repository#examples).

## Requirements

To develop a scene locally, you don't need to own LAND tokens. Developing and testing a scene can be done completely offline, without the need to deploy a scene to the Ethereum network (the system Decentraland uses to establish ownership of LAND), or the content server.

You must have the following:

- **npm** (Node package manager): Used in the terminal to handle scene dependencies, required to install the Decentraland CLI. [Download link](nodejs.org)

- **The Decentraland CLI**: Used to build, preview and upload scenes. See [Installation guide]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md" >}})

- **A source code editor**: Helps you create scenes a lot faster and with less errors. A source code editor marks syntax errors, autocompletes while you write and even shows you smart suggestions that depend on the context that you're in. You can also click on an object in the code to see the full definition of its class and what attributes it supports. We recommend [Visual Studio Code](https://code.visualstudio.com/), which is a free tool with a rich ecosystem of helpful extensions.


## Supported languages and syntax

### TypeScript

Decentraland employs [TypeScript (.ts)](https://www.typescriptlang.org/docs/handbook/jsx.html) as the default language for writing scenes.

TypeScript is a superset of JavaScript, so if you're familiar with JavaScript you'll find it's almost the same, but TypeScript includes type declarations. Thanks to type declarations, it's possible to have features like autocomplete better debugging hints, these speed up development times and allow for the creation of a more solid codebase. These features are all key components to a positive developer experience.

When a scene is built, the Typescript code you wrote is compiled into minified Javascript, to make it lighter. The original source code in Typescript is never uploaded to the servers, only the compiled Javascript version.

### Other languages

You can use another tool or language instead of TypeScript and compile it into JavaScript, as long as your compiled scripts are contained within a single JavaScript file named _game.js_. All provided type declarations are made in TypeScript, and other languages and transpilers are not officially supported.

## Scenes

The content you deploy to your LAND is called a **scene**. A scene is an interactive program that renders 3D content, this could be a game, an interactive experience, an art gallery, whatever you want!

Scenes are deployed to virtual LAND in Decentraland. LAND is a scarce and non-fungible asset maintained in an Ethereum smart contract. Deploy to a single **parcel**, a 16 meter by 16 meter plot of LAND, or to multiple adjacent parcels.

When players visit Decentraland, they download and render the content of each scene as they walk through the map. They unload scenes as they walk away from them.

You can also run a scene locally on your machine by running a preview from the CLI. You can also [upload a preview]({{< ref "/content/creator/sdk7/publishing/deploy-third-party.md" >}}) to run remotely on a 3rd party server to easily share your work with others.

## Entities and Components

Three dimensional scenes in Decentraland are based on an [Entity-Component-System](https://en.wikipedia.org/wiki/Entity%E2%80%93component%E2%80%93system) architecture, where everything in a scene is an _entity_. Entities have _components_, each component gives the entity it belongs to specific properties. A door entity is likely to have at least a Transform component (that sets position, rotation & scale) and another to provide it a shape. Components are just a place to store data, they don’t carry out any actions. 

<img src="/images/media/ecs-components-new.png" alt="nested entities" width="400"/>


```ts
// Create an entity
const door = engine.addEntity()

// Give the entity a position via a transform component
Transform.create(door, {
	position: Vector3.create(5, 1, 5)
})

// Give the entity a visible shape via a GltfContainer component
GltfContainer.create(door)
```
 
The default set of components are interpreted by the engine and have direct consequences on how the entity will look, its position, if it emits sounds, etc. You can also define custom components to store data that might be useful to the mechanics in your scene. The engine won't directly interpret what the values on these components mean, but you can write logic in your scene's code to monitor these values and respond to them.


For example, I can define a custom “doorState” component to track the door’s open/closed/locked state. In this case, the component is nothing more than a place to store a value that keeps track of this state, I have to implement the logic that interprets these values separately. 


Entities may be nested inside other entities to form a tree structure. If you're familiar with web development, you might find it useful to think of entities as elements in a DOM tree and of components as the attributes of each of these elements.

<img src="/images/media/ecs-nested-entities-new.png" alt="nested entities" width="400"/>

Entities are an abstract concept. An entity is just an id, that is used as a reference to group different components.


See [Entities and components]({{< ref "/content/creator/sdk7/architecture/entities-components.md" >}}) for an in-depth look of both these concepts and how they're used by Decentraland scenes.

## The game loop

The [game loop](http://gameprogrammingpatterns.com/game-loop.html) is the backbone of a Decentraland scene's code. It cycles through part of the code at a regular interval and does the following:

- Listen for player input
- Update the scene
- Re-render the scene

In most traditional software programs, all events are triggered directly by player actions. Nothing in the program's state will change until the player clicks on a button, opens a menu, etc.

But interactive environments and games are different from that. Not all changes to the scene are necessarily caused by a player's actions. Your scene could have animated objects that move on their own or even non-player characters that have their own AI. Some player actions might also take multiple ticks to be completed, for example if the opening of a door needs to take a whole second, the door's rotation must be incrementally updated about 30 times as it moves.

We call each iteration over the loop a _tick_. Decentraland scenes are rendered at 30 ticks per second, whenever possible. If the machine is struggling to render each tick, it may result in less frequent updates.

In each tick, the scene is updated; then the scene is re-rendered, based on the updated values.

In Decentraland scenes, there is no explicitly declared game loop, but rather the [Systems]({{< ref "/content/creator/sdk7/architecture/systems.md" >}}) of the scene make up the game loop.

The compiling and rendering of the scene is carried out in the backend, you don't need to handle that while developing your scene.

## Systems

Entities and components are places to store information about the objects in a scene. _Systems_ hold functions that change the information that's stored in components over time.

Systems are where we implement game logic, they carry out the actions that need to be updated or checked periodically on every tick of the game loop. 

A system is a pure and simple function that gets called once on every tick (up to 30 times a second), following the [_update pattern_](http://gameprogrammingpatterns.com/update-method.html).

```ts
// Basic system
function mySystem() {
  console.log("my system is running")
}

engine.addSystem(mySystem)

// System with dt
function mySystemDT(dt: number) {
  console.log("time since last frame:  ", dt)
 }
 
engine.addSystem(mySystemDT)
```

A single scene can have 0 or many systems running at the same time. Systems can be turned on or off at different moments during the scene’s duration. It’s generally a good practice to keep independent behaviors in separate systems.

See [Systems]({{< ref "/content/creator/sdk7/architecture/systems.md" >}}) for more details about how systems are used in a scene.

## Querying components

You can [query components]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}) with the method `engine.getEntitiesWith(...components)` to keep track of all entities in the scene that have certain components.

It often makes sense to query components within a [system]({{< ref "/content/creator/sdk7/architecture/systems.md" >}}), to then loop over each of the returned entities and perform a same set of actions on each.

If you attempt to iterate over all the entities in the scene on every tick of the game loop, that could have a significant cost in performance. By referring only to the entities returned by a query, you ensure you're only dealing with those that are relevant.

```ts
// Define a System
function boxHeightSystem(dt: number) {

  // query for entities that include both MeshRenderer and Transform components	
  for (const [entity] of engine.getEntitiesWith(MeshRenderer, Transform)) {
    const transform = Transform.get(entity)
    console.log("a box is at height:  ", transform.position.y)
  }
}

// Add the system to the engine
engine.addSystem(rotationSystem)
```


## Mutability

You can choose to deal with mutable or with immutable (read-only) versions of a component. The `.get()` function in a component returns an immutable version of the component. You can only read its values, but can't change any of the properties on it.

The `.getMutable()` function returns representation of the component that allows you to change its values. Use mutable versions only when you plan to make changes to a component. Dealing with immutable versions of components results in a huge gain in performance.

```ts
// fetch an immutable version (read-only)
const immutableTransform = Transform.get(myEntity)

// the following does NOT work:
// 	immutableTransform.position.y = 2

const mutableTransform = Transform.getMutable(myEntity)

// the following DOES change the entity's position
mutableTransform.position.y = 2
```

See [mutable data]({{< ref "/content/creator/sdk7/programming-patterns/mutable-data.md" >}}) for more details.


## Putting it all together

The _engine_ is what sits in between _entities_, and _components_ on one hand and _systems_ on the other.

![](/images/media/ecs-big-picture.png)

All of the values stored in the components in the scene represent the scene's state at that point in time. With every tick of the game loop, the engine runs the functions of each of the systems to update the values stored in the components.

After all the systems run, the components on each entity will have new values. When the engine renders the scene, it will use these new updated values and players will see the entities change to match their new states.

```ts

// Create an entity
const cube = engine.addEntity()

// Give the entity a position via a transform component
Transform.create(cube, {
	position: Vector3.create(5, 1, 5)
})

// Give the entity a visible shape via a MeshRenderer component
MeshRenderer.setBox(cube)

// Define a System
function rotationSystem(dt: number) {

  // query for entities that include both MeshRenderer and Transform components	
  for (const [entity] of engine.getEntitiesWith(MeshRenderer, Transform)) {
    const transform = Transform.getMutable(entity)
    transform.rotation = Quaternion.multiply(transform.rotation, Quaternion.fromAngleAxis(dt * 10, Vector3.Up()))
  }
}

// Add the system to the engine
engine.addSystem(rotationSystem)
```

In the example above, a `cube` entity and a `rotationSystem` system are added to the engine. The `cube` entity has a `Transform`, and a `MeshRenderer` component. In every tick of the game loop, the `rotationSystem` system is called, and it changes the rotation values in the `Transform` component of the `cube` entity.

Note that most of the code above is executed just once, when loading the scene. The exception is the `rotationSystem` system, which is called on every tick of the game loop.

## Scene Decoupling

Your scenes don't run in the same context as the engine
(a.k.a. the main thread). We created the SDK in a way that is
entirely decoupled from the rendering engine. We designed it to be like this for both safety and performance reasons.

Because of this decoupling, your scene's code doesn't have access to the DOM or the `window` object, so you can't access data like the player's browser or geographical location.

The decoupling works by using RPC protocol, this protocol assigns a small part of the client to only render the scene and control events.

We have also abstracted the communication protocol. This allows us to run the scenes locally in a WebWorker.

We don't want developers to intervene with the internals of the engine or even need to know what lies inside the engine. We need to ensure a consistent experience for players throughout the Decentraland map, and mistakes are more likely to happen at that "low" level. 

This decoupling is also important to prevent neighbor scenes from interfering with the experience of players while they're on someone else's scene. A player might have multiple nearby scenes loaded at the same time, each running their own code. Some actions (like opening external links, or moving the player) are only permitted when the player is standing on that particular scene, not if the scene is loaded but the player is outside.
