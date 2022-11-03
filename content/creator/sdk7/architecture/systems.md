---
date: 2018-01-16
title: Systems
description: Learn how systems are used to update the scene state
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/systems/
weight: 2
---

Decentraland scenes rely on _systems_ to update any data over time, including information stored in each entity's [components]({{< ref "/content/creator/sdk7/architecture/entities-components.md" >}}).


<!-- TODO: Change image -->
![](/images/media/ecs-big-picture.png)

_systems_ are what make scenes dynamic, they're functions that are executed periodically on every tick of the scene's game loop, changing what will be rendered.

The following example shows a basic system declaration:

```ts
// Define the system
function mySystem() {

	// performed on every tick
	log("my system is running")
}

// Add system to engine
engine.addSystem(mySystem)
```

You must add a _System_ to the engine before its functions start being called. You can also declare a system and add it to the engine all in one same instruction.

```ts
// Define and add system to engine
engine.addSystem(mySystem() {

	// performed on every tick
	log("my system is running")
})
```


The function in a system can perform anything you want. Typically, it will act upon all the entities that meet certain [query]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}), following certain logic to change the values stored in the entity's components.


```ts
function moveSystem(dt: number) {
	// iterate over all entiities with a Transform
  for (const [entity] of engine.getEntitiesWith(Transform)) {

	// fetch a mutable Transform component 
	const transform = Transform.getMutable(entity)

	// update the position value
  	transform.position.x += 0.01
  }
}

engine.addSystem(moveSystem)
```

In the example above, the system `MoveSystem` is a function that runs on each tick of the game loop, changing position of every entity in the scene that has a Transform.


<!-- TODO: change image -->
![](/images/media/ecs-system.png)

<!--
> Tip: As a simpler alternative to create custom systems, you can use the helpers in the [utils library](https://github.com/decentraland/decentraland-ecs-utils). The library creates systems in the background that handle common tasks like moving or rotating entities. In most cases, this library only requires a single line of code to apply these behaviors.
-->

You can have multiple systems in your scene to decouple different behaviors, making your code cleaner and easier to scale and reuse. For example, one system might handle physics, another might make an obstacle entity move back and forth continuously, another could handle the AI of characters.

Multiple systems can act on a single entity. For example a non-player character might move on its own based on an AI, but also be affected by gravity when accidentally walking from off a cliff. In that scenario, the physics and the AI systems don't even need to know about each other. They independently reassess their current state on each tick of the game loop and implement their own separate logic.

## The system function

A system's function is executed periodically, once per every tick of the game loop. This happens automatically, you don't need to explicitly call this function from anywhere in your code.

In a Decentraland scene, you can think of the game loop as the aggregation of all the system functions in your scene.

> Note: If you add multiple instances of a same system to the engine, the function will be executed multiple times per tick of the game loop. For example, adding a system twice could result in an entity moving at twice the speed as expected, as it advances two increments on each tick.


## Handle entities by reference

Some components and systems are meant for using only on one entity in the scene. For example, on an entity that stores a game's score or perhaps a main gate that is unique in the scene. To access one of those entities within a system, you can simply refer to the entity or its components by name in the system's functions.

```ts
// create a new entity
const game = engine.addEntity()

// add component to that entity
ScoreComponent.create(game)

// Define the system
export function UpdateScore() {

	// call reference to individual entity
	const points = ScoreComponent.get(game).points
	log(points)
}

// Add system to engine
engine.addSystem(UpdateScore)
```

For larger projects, we recommend that you keep system definitions on separate files from the instancing of entities and components.


## Loop over a component query

A lot of times, your scene will have multiple entities of the same type that will have similar behaviors. For example many doors that can be opened, or many enemies that can attack the player. It makes sense to handle all of these similar entities in a single system, iterating over the list and performing the same checks on each.

You don't want a system's function to iterate over _the entire_ set of entities in the scene, as this could be very costly in terms of processing power. To avoid this, you can [query components]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}), to only iterate over the relevant entities.

For example, your scene can have a `PhysicsSystem` that calculates the effect of gravity over the entities of your scene. Some entities in your scene, such as trees, are not meant to ever move; so it would be smart to avoid calculating the effects of gravity on these. You can define a `HasPhysics` component to mark entities that could be affected by gravity, and then have `PhysicsSystem` only deal with the entities returned by this query.

```ts
// Define the system
export function PhysicsSystem() {
	// iterate over all entiities with a HasPhysics
  for (const [entity] of engine.getEntitiesWith(HasPhysics)) {

	// fetch a mutable Transform component 
	const transform = Transform.getMutable(entity)

	// Calculate effect of physics
  }
}

// Add system to engine
engine.addSystem(PhysicsSystem)
```


## Delta time between frames

The function in a system can optionally include an argument called `dt`, of type `number` (representing _delta time_).

```ts
function MySystem(dt: number) {

	// Udate scene
	log("time since last tick: ", dt)
}

engine.addSystem(MySystem)
```

_delta time_ represents time that passed since the last tick of the game loop, in seconds.

Decentraland scenes are updated by default at 30 ticks per second. This means that the `dt` argument passed to all systems will tend to equal to _1/30_ (0.0333...).

If the processing of a frame takes less time than this interval, then the engine will wait the remaining time to keep updates regularly paced and `dt` will remain equal to _1/30_ .

![](/images/media/ecs-framerate.png)

If the processing of a frame takes longer than _1/30_ seconds, the drawing of that frame is delayed. The engine then tries to finish that frame and show it as soon as possible. It then proceeds to the next frame and tries to show it _1/30_ seconds after the last frame. It doesn't compensate for the previous delay.

![](/images/media/ecs-framerate-heavy.png)

Ideally, you should avoid your scene dropping frames, as it impacts the quality of the player's experience. Since this is dependant on the processing power of the player's machine, it's always a possibility that your scene should be ready to handle gracefully.

The `dt` variable is useful when frame processing exceeds the default time. Assuming that the current frame will take as much time as the previous one, this information may be used to calculate how much to adjust a gradual change, so that the rate of change appears steady and in proportion to the lag between frames.

See [entity positioning]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md" >}}) for examples of how to use `dt` to make movement smoother.


## Loop at a timed interval

If you want a system to execute something at a regular time interval, you can do this by combining the `dt` argument with a timer.

```ts
let timer: number = 10

function LoopSystem(dt: number) {
  if (timer > 0) {
      timer -= dt
    } else {
      timer = 10
      // DO SOMETHING
    }
}

engine.addSystem(LoopSystem)
```

For more complex use cases, where there may be multiple delays and loops being created dynamically, it may be worth defining a custom component to store an individual timer value for each entity. See [Custom components]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}).


## System execution order

In some cases, when you have multiple systems running, you might care about what system is executed first by your scene.

For example, you might have a _physics_ system that updates the position of entities in the scene, and another _boundaries_ system that ensures that none of the entities are positioned outside the scene boundaries. In this case, you want to make sure that the _boundaries_ system is executed last. Otherwise, the _physics_ system could move entities outside the bounds of the scene but the _boundaries_ system won't find out till it's executed again in the next frame.

When adding a system to the engine, set an optional `priority` field to determine when the system is executed in relation to other systems.

```ts
engine.addSystem(PhysicsSystem, 1)
engine.addSystem(BoundariesSystem, 5)
```

Systems with a lower priority number are executed first, so a system with a priority of _1_ is executed before one of priority _5_.

Systems that aren't given an explicit priority have a default priority of _0_, so these are executed first.

If two systems have the same priority number, there's no way to know for certain which of them will be executed first.


## Remove a system

An instance of a system can be added or removed from the engine to turn it on or off.

If a system is defined but isn't added to the engine, its function isn't called by the engine.

To remove a system, you must first create a pointer to it when adding it to the engine, so that you can refer to the system later.

```ts
// declare system
function mySystem(dt: number){
	log("delay since last tick: ", dt)
}

// add system (making a pointer)
const mySystemInstance = engine.addSystem(mySystem)

// remove system
engine.removeSystem(mySystemInstance)
```

Note that to remove the system you need a pointer to the _instance_ of the system, not to the system's class. In the above example, `engine.removeSystem()` is not being passed `mySystem` (the system class declaration). It's being passed `mySystemInstance` (the instance that was added to the engine). A scene can potentially have multiple instances of a same system running together, so you need to tell the engine which one of those to remove.