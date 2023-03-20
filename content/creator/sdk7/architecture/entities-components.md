---
date: 2018-01-15
title: Entities and components
description: Learn the essentials about entities and components in a Decentraland scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/entities-components/
weight: 1
---

Decentraland scenes are built around [_entities_, _components_ and _systems_](https://en.wikipedia.org/wiki/Entity%E2%80%93component%E2%80%93system). This is a common pattern used in the architecture of several game engines, that allows for easy composability and scalability.



![](/images/media/ecs-big-picture.png)

## Overview

_Entities_ are the basic unit for building everything in Decentraland scenes. All visible and invisible 3D objects and audio players in your scene will each be an entity. An entity is nothing more than an id, that can be referenced by components. The entity itself has no properties or methods of its own, it simply serves to group several components together.

_Components_ define the traits of an entity. For example, a `Transform` component stores the entity's coordinates, rotation and scale. A `MeshRenderer` component gives the entity a visible shape (like a cube or a sphere) when rendered in the scene, a `Material` component gives the entity a color or texture. You can also create custom components to serve your scene's required data, for example a custom `health` could store an entity's remaining health value, and add it to entities that represent non-player enemies in a game.

If you're familiar with web development, think of entities as the equivalent of _Elements_ in a _DOM_ tree, and of components as _attributes_ of those elements.

{{< hint warning >}}
**📔 Note**:  In previous versions of the SDK, Entities were _objects_ that were instanced, and could be extended to add functions. As of version 7.0 of the SDK, entities are only an ID. This structure better fits the principles of [data oriented programming]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}) and can help in the scene's performance.
{{< /hint >}}

<img src="/images/media/ecs-components-new.png" alt="Armature" width="400"/>

Components like `Transform`, `Material` or any of the _shape_ components are closely tied in with the rendering of the scene. If the values in these components change, that alone is enough for the engine to change how the scene is rendered in the next frame.

The engine is the part of the scene that sits in the middle and manages all of the other parts. It determines what entities are rendered and how players interact with them. It also coordinates what functions from [systems]({{< ref "/content/creator/sdk7/architecture/systems.md">}}) are executed and when.


Components are meant to store data about their referenced entity. They can only store this data, they can't modify this data themselves. All changes to the values in the components are carried out by [Systems]({{< ref "/content/creator/sdk7/architecture/systems.md" >}}). Systems are completely decoupled from the components and entities themselves. Entities and components are agnostic to what _systems_ are acting upon them.


## Syntax for entities and components

The example below shows some basic operations for declaring, and configuring basic entities and components.

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

{{< hint warning >}}
**📔 Note**:  In previous versions of the SDK, it was necessary to manually add an entity to the engine to start rendering it. As of version 7 of the SDK, entities are implicitly added to the engine as soon as they are assigned a component.
{{< /hint >}}

When a component is created, it's always assigned to a parent entity. The component's values then affect the entity.

## Remove entities

To remove an entity from the engine, use `engine.removeEntity()`

```ts
// Create an entity
const door = engine.addEntity()

// Give the entity a visible shape via a GltfContainer component
GltfContainer.create(door)

// Remove entity
engine.removeEntity(door)
```

If a removed entity has any child entities, these change their parent back to the default `engine.RootEntity` entity, which is positioned at the scene base position, with a scale of _1_.


To remove an entity and also all of its children (and any children of its children, recurrently), use `engine.removeEntityWithChildren()`.

```ts
// Create parent entity
const door = engine.addEntity()

// Create child entity
const doorKnob = engine.addEntity()

// Give the entities a visible shape
GltfContainer.create(door, {
	src: "models/door.glb"
})
GltfContainer.create(doorKnob, {
	src: "models/doorKnob.glb"
})

// Parent
Transform.create(doorKnob, {
	parent: door
})

// Remove both parent and children
engine.removeEntityWithChildren(door)
```

{{< hint info >}}
**💡 Tip**:  Instead of removing an entity from the engine, in some cases it might be better to make it invisible, in case you want to be able to load it again without any delay. See [Make invisible]({{< ref "/content/creator/sdk7/3d-essentials/shape-components.md#make-invisible" >}})
{{< /hint >}}

### Removing entities behind the scenes

An entity is just an id that is referenced by its components. So when removing an entity you're really removing each of the components that reference this entity. This means that if you manually remove all of the components of an entity, it will have the same effect as doing `engine.removeEntity()`.

Once the entity's components are removed, that entity's id is free to be referenced by new components as a fresh new entity.


## Nested entities

An entity can have other entities as children. Thanks to this, we can arrange entities into trees, just like the HTML of a webpage.


<img src="/images/media/ecs-nested-entities-new.png" alt="nested entities" width="400"/>

To set an entity as the parent of another, the child entity must have a `Transform` component. You can then set the `parent` field with a reference to the parent entity.

```ts
// Create entities
const parentEntity = engine.addEntity()

const childEntity = engine.addEntity()

// Set parent
Transform.create(childEntity, {
	parent: parentEntity
})
```


Once a parent is assigned, it can be read off the child entity from the `parent` field on its `Transform` component.

```ts
// Get parent from an entity
const parent = Transform.get(childEntity).parent
```


If a parent entity has a `Transform` component that affects its position, scale or rotation, its children entities are also affected. Any position or rotation values are added, any scale values are multiplied.

If either the parent or child entity doesn't have a `Transform` component, the following default values are used.

- For **position**, the parent's center is _0, 0, 0_
- For **rotation** the parent's rotation is the quaternion _0, 0, 0, 1_ (equivalent to the Euler angles _0, 0, 0_)
- For **scale**, the parent is considered to have a size of _1_. Any resizing of the parent affects scale and position in proportion.

Entities with no shape component are invisible in the scene. These can be used as wrappers to handle and position multiple entities as a group.

To separate a child entity from its parent, you can assign the entity's parent to `null`.

```ts
const mutableChildTransform = Transform.get(childEntity)
mutableChildTransform.parent = null
```


## Get an entity by ID

Every entity in your scene has a unique number _id_. You can retrieve a component that refers to a specific entity from the engine based on this ID.

```typescript
// fetch a Transform component
Transform.get(1000 as Entity)
```

{{< hint warning >}}
**📔 Note**:  The entity ids between _0_ and _511_ are reserved by the engine for fixed entities, like the player avatar, the base scene, etc.
{{< /hint >}}

For example, if a player's click or a [raycast]({{< ref "/content/creator/sdk7/interactivity/raycasting.md" >}}) hits an entity, this will return the id of the hit entity, and you can use the command above to fetch the Transform component of the entity that matches that id. You can also fetch any other component of that entity in the same way.


## Add or replace a component

Each entity can only have one component of a given kind. For example, if you attempt to assign a Transform to an entity that already has one, this will cause an error.

To prevent this error, you can use `.createOrReplace` instead of `.create`. This command overwrites any existing components of the same kind if they exists, otherwise it creates a new component just like `.create`.


```ts
Transform.createOrReplace(door, {
	position: Vector3.create(5, 1, 5)
})
```

{{< hint warning >}}
**📔 Note**:  Since `.createOrReplace` runs an additional check before creating the component, it's always more performant to use `.create`. If you're sure that the entity doesn't already have a component like the one you're adding, use `.create`.
{{< /hint >}}


## Access a component from an entity

You can access components of an entity by using the entity's `.get()` or the `getMutable()` functions.

```ts
// Create entity
const box = engine.addEntity()

// Create and add component to that entity
Transform.create(box)

// Get read-only version of component
let transform = Transform.get(box)

// Get mutable version of component
let transform = Transform.getMutable(box)
```

The `get()` function fetches a read-only reference to the component. You cannot change any values from this reference of the component.

If you wish to change the values of the component, use the `getMutable()` function instead. If you change the values in the mutable version of the component, you're directly affecting the entity that component belongs to.

See [mutable data]({{< ref "/content/creator/sdk7/programming-patterns/mutable-data.md" >}}) for more details.

{{< hint warning >}}
**📔 Note**:  Only use `getMutable()` if you're actually going to make changes to the component's values. Otherwise, always use `get()`. This practice follows the principles of [data oriented programming]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}), and can significantly help in the scene's performance.
{{< /hint >}}

```ts
// Get mutable version of component
let transform = Transform.getMutable(box)

// change a value of the component
transform.scale.x = 5
```

The example above directly modifies the value of the _x_ scale on the Transform component.

If you're not entirely sure if the entity does have the component you're trying to retrieve, use `getOrNull()` or `getMutableOrNull()`.

{{< hint warning >}}
**📔 Note**:  Avoid using `getOrNull()` or `getMutableOrNull()` when possible, as these functions involve additional checks that and are therefore less efficient than `.get()` and `getMutable()`.
{{< /hint >}}


```ts
//  getOrNull
const transformOrNull = Transform.getOrNull(myEntity)

//  getMutableOrNull
const mutableTransformOrNull = Transform.getMutableOrNull(myEntity)
```

If the component you're trying to retrieve doesn't exist in the entity:

- `get()` and `getMutable()` returns an error.
- `getOrNull()` and `getMutableOrNull()` returns `Null`.


## Remove a component from an entity

To remove a component from an entity, use the entity's `deleteFrom()` method of the component type.

```ts
Transform.deleteFrom(myEntity)
```

If you attempt to remove a component that doesn't exist in the entity, this action won't raise any errors.

{{< hint warning >}}
**📔 Note**:  To remove all the components of an entity at once, see [this section](#remove-entities)
{{< /hint >}}

## Check for a component

You can check if an entity owns an instance of a certain component by using the `has()` function. This function returns _true_ if the component is present, and _false_ if it's not. This can be very handy for using in conditional logic in your scene.

```ts
const hasTransform = Transform.has(myEntity)
```


{{< hint info >}}
**💡 Tip**:  You can also [query components]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}) to fetch a full list of components that hold a specific component, or a specific set of components. Do not iterate over all entities in the scene manually to check each with a `has()`, that approach is a lot less efficient. 
{{< /hint >}}

## Reserved entities

Certain entity ids are reserved for special entities that exist in every scene. They can be accessed via the following aliases:

- `engine.RootEntity`
- `engine.PlayerEntity`
- `engine.CameraEntity`

{{< hint warning >}}
**📔 Note**: Avoid referring to these entities on the initial scene loading, because that can result in errors if the entities are not initialized yet. To avoid this problem, encapsulate the behavior in an async [`executeTask` block]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md#the-executetask-function" >}}).

If you refer to these entities in a system, they will always be available, because the first execution of the system is called once the scene is already properly initialized.
{{< /hint >}}

### The root entity

All entities in the scene are children of the root entity, directly or indirectly.

### The player entity

The `engine.PlayerEntity` entity represents the player's avatar. Fetch the player's `Transform` component to get the player's current position and rotation, see [user data]({{< ref "/content/creator/sdk7/interactivity/user-data.md" >}}). You can also modify this Transform to move the player, see [move player]({{< ref "/content/creator/sdk7/interactivity/move-player.md" >}}).

### The camera entity

The `engine.CameraEntity` entity represents the player's camera. 
Fetch the camera's `Transform` component to get the camera's position and rotation. You can also fetch the camera's `CameraMode` component to know know if the player is using 1st or 3rd person camera mode, see [camera mode]({{< ref "/content/creator/sdk7/interactivity/user-data.md#check-the-players-camera-mode">}}).