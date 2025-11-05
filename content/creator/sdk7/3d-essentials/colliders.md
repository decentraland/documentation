---
date: 2018-02-6
title: Colliders
description: Learn about the different components that give entities their 3D shape and collision.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/colliders/
---

Entities that have colliders occupy space and block a player's path, entities without colliders can be walked through by a player`s avatar.

Colliders are also needed to make an entity clickable. Button events are based on the collider shape of an entity, not on its visible shape.

There are separate collision layers for interacting with either the player's physics, or with pointer events, colliders can be configured to only interact with one or the other. They can also be configured to interact with custom layers, that can be used with [raycasts]({{< ref "/content/creator/sdk7/interactivity/raycasting.md#" >}}) to handle whatever makes sense to the scene.

{{< hint warning >}}
**📔 Note**: Colliders don't affect how other entities interact with each other, entities can always overlap. Collision settings only affect how the entity interacts with the player's avatar and button events. Decentraland doesn't have a native physics engine, so if you want entities to fall, crash or bounce, you must code this behavior into the scene, or import a library to handle that.
{{< /hint >}}

## Use the Scene Editor

The easiest way to manage an entity's colliders is to use the [Scene Editor]({{< ref "/content/creator/scene-editor/get-started/about-editor.md" >}}).

You can add a **Mesh Collider** component to your entity to assign a primitive shape (cube, plain, sphere, cylinder, or cone) to your entity. You can then pick [Collision layers](#collision-layers) from a dropdown.

You can also configure the collision layers on a **GLTF** component to change the default [Collision layers](#collision-layers) used on either the collider geometry or the visible geometry of the model. See [Add Components]({{< ref "/content/creator/scene-editor/build/components.md#add-components" >}}).

<img src="/images/editor/gltf-component.png" alt="Scene name" width="200"/>

## Colliders on primitive shapes

The `MeshCollider` component gives an entity a simple collider based on a primitive shape (boxes, spheres, planes, cylinders, or cones).

Entities that have a `MeshRenderer` component to give them a [primitive shape]({{< ref "/content/creator/sdk7/3d-essentials/shape-components.md#primitive-shapes" >}}) don't have colliders by default. You must also give the entity a `MeshCollider` component.

The following collider shapes are available on `MeshCollider`. Several shapes include optional additional fields, specific to that shape.

- **box**:

  Use `MeshCollider.setBox()`, passing the entity.

- **plane**:

  Use `MeshCollider.setPlane()`, passing the entity.

- **sphere**:

  Use `MeshCollider.setSphere()`, passing the entity.

- **cylinder**:

  Use `MeshCollider.setCylinder()`, passing the entity. Pass `radiusTop` and `radiusBottom` as additional optional fields, to modify the cylinder.

  {{< hint info >}}
  **💡 Tip**:: Set either `radiusTop` or `radiusBottom` to 0 to make a cone.
  {{< /hint >}}

This example defines a box entity that can't be walked through.

```ts
// create entity
const myCollider = engine.addEntity()

// visible shape
MeshRenderer.setBox(myCollider)

// collider
MeshCollider.setBox(myCollider)
```

The shape used by the `MeshCollider` doesn't need to necessarily match the one used by the `MeshRenderer`. You can also add a `MeshCollider` to an entity that has a 3D model from a `GLTFContainer` component, or to an entity that has no visible shape at all.

{{< hint warning >}}
**📔 Note**: The `MeshCollider` component and `ColliderLayer` must be imported via

> `import { MeshCollider, ColliderLayer } from "@dcl/sdk/ecs"`

See [Imports]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#imports" >}}) for how to handle these easily.
{{< /hint >}}

## Colliders on 3D models

3D models can be assigned colliders on two different geometry levels:

- `visibleMeshesCollisionMask`: Refers to the visible geometry of the model. By default this geometry has no colliders.
- `invisibleMeshesCollisionMask`: refers to the collider meshes, whose name end in `_collider`. By default, this geometry is treated as a collider for both physics and pointer events.

Any mesh embedded as part of a 3D model who's name ends in `_collider` is treated as part of the `invisibleMeshesCollisionMask` layer, and interpreted as a collider by default.

Defining collider geometry as a separate invisible layer allows for much greater control and is a lot less demanding on the system than using the visible geometry, as the collision object is usually a lot simpler (with less vertices) than the original model.

If a model doesn't have any collider geometry, and you want to make it affect the physics or the pointer events systems, you can either:

- Assign collision layers directly to the visible geometry, via the `visibleMeshesCollisionMask`.
  {{< hint warning >}}
  **📔 Note**: If the visible geometry of the object has many vertices, note that this may have more of a performance cost.
  {{< /hint >}}
- Give the entity a `MeshCollider` component, to give it a primitive shape collider.
- Overlay an invisible entity that has a `MeshCollider` component.
- Edit the model in an external tool like Blender to include a _collider mesh_. The collider must be named _x_collider_, where _x_ is the name of the model. So for a model named _house_, the collider must be named _house_collider_.

You might also want to assign the pointer events collision layer to the `visibleMeshesCollisionMask` in case you want the hover hints and pointer events to respond more accurately to the contour of the entity. Note that this is more demanding on performance.

{{< hint warning >}}
**📔 Note**: Make sure you don't have the same layer (physics, pointer events or custom layers) assigned to both `visibleMeshesCollisionMask` and `invisibleMeshesCollisionMask`, as that would be a very inefficient use of resources. You can have different layers on each, such as physics on the invisible layer and pointer events on the visible layer.
{{< /hint >}}

```ts
// create entity
const myEntity = engine.addEntity()

// assign GLTF shape
GltfContainer.create(myEntity, {
	src: '/models/myModel.gltf',
	invisibleMeshesCollisionMask: ColliderLayer.CL_PHYSICS,
	visibleMeshesCollisionMask: ColliderLayer.CL_POINTER,
})
```

See [3D models](/creator/3d-modeling/3d-models) for more details on how to add collider invisible geometry to a 3D model.

{{< hint warning >}}
**📔 Note**: The `GltfContainer` component and `ColliderLayer` must be imported via

> `import { GltfContainer, ColliderLayer } from "@dcl/sdk/ecs"`

See [Imports]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#imports" >}}) for how to handle these easily.
{{< /hint >}}

### Animated models

When setting colliders to use the visible geometry on a model that includes [armature-based animations]({{< ref "/content/creator/3d-modeling/animations.md" >}}), the animations aren't followed by colliders. The collider meshes keep their original shape. If an animation involves deforming a meshe's geometry, the collider meshes retain the un-animated shape while the animation plays.

When playing animations that involve moving full meshes without changing their shape, these changes are accurately reflected by colliders. For example if a platform moves as part of an animation, the platform´s collider does move with the animation.

## Collision layers

The scene can handle separate collision layers, that have different behaviors.

You can configure a `MeshCollider` component or the `GltfContainer` component to only respond to one kind of interaction, or to several of them, or none. To do this, on the `MeshCollider` set the `collisionMask` property, and on `GltfContainer` set the `visibleMeshesCollisionMask` or `invisibleMeshesCollisionMask` properties to one or several of the following values:

- `ColliderLayer.CL_PHYSICS`: Only blocks player movement (and doesn't affect pointer events)
- `ColliderLayer.CL_POINTER`: Responds only to pointer events (and doesn't block the player movement)
- `ColliderLayer.CL_CUSTOM1` through to `CL_CUSTOM8`: Can be used together with raycasts, so that a ray only detects collisions with one specific layer.
- `ColliderLayer.CL_NONE`: Doesn't respond to collisions of any kind.

{{< hint warning >}}
**📔 Note**: To disable collisions form a `MeshCollider` component, delete the component. Do not set the collision layer to `ColliderLayer.CL_NONE`. There's a known issue with the `MeshCollider` component. Instead of disabling all collisions, it makes this value equivalent to the default (`ColliderLayer.CL_PHYSICS | ColliderLayer.CL_POINTER`).
{{< /hint >}}

```ts
// create entity
const myEntity = engine.addEntity()
// visible shape
MeshRenderer.setBox(myEntity)

// create a MeshCollider component that only responds to player physics
MeshCollider.setBox(myEntity, ColliderLayer.CL_PHYSICS)
```

A single collision mask can respond to multiple collision layers. Use the `|` character as an _or_, to include as many layers as you need. The default value on a MeshCollider is `ColliderLayer.CL_PHYSICS | ColliderLayer.CL_POINTER`.

```ts
MeshCollider.setBox(
	myEntity,
	ColliderLayer.CL_CUSTOM1 |
		ColliderLayer.CL_CUSTOM3 |
		ColliderLayer.CL_PHYSICS |
		ColliderLayer.CL_POINTER
)
```

You can use the 8 different custom layers for whatever suits your scene best, for example one could be used for NPC line-of-sight calculations, whilst another for estimating trajectories of falling objects. Using different layers for different systems allows you to use less resources, as in each case you'll only be checking collisions with the relevant entities.

See [Raycasting]({{< ref "/content/creator/sdk7/interactivity/raycasting.md" >}}) for more on how to use custom collision layers.

### Cameras and colliders

When a player's camera moves in 3rd person mode, the camera might be blocked by colliders or not, depending on the collision layers assigned to the entities. Be mindful of this when designing your scene, you may want to prevent the camera from going through walls or other entities.

To avoid the camera from going through walls, you must assign both the `ColliderLayer.CL_PHYSICS` and the `ColliderLayer.CL_POINTER` layers to the entities that you want to block the camera. It's important that both layers are assigned to the same geometry on the entity. So if you assign the `ColliderLayer.CL_PHYSICS` layer to the visible layer of the entity, you must also assign the `ColliderLayer.CL_POINTER` layer to the same geometry.

For example, on the Creator Hub, the following combination of settings will prevent the camera from going through walls:

<img src="/images/colliders-camera.png" width="300" />

Both the `ColliderLayer.CL_PHYSICS` and the `ColliderLayer.CL_POINTER` layers are assigned to the same invisible layer of the geometry of the entity. If they were both assigned to the visible layer, the result would be the same. This is the default behavior, both when adding an entity via the Creator Hub or via code.

<img src="/images/colliders-no-camera.png" width="300" />

In this second example, the camera can go through the wall, because the `ColliderLayer.CL_PHYSICS` layer is assigned to the invisible layer of the entity, and the `ColliderLayer.CL_POINTER` layer is assigned to the visible layer of the entity, even if both geometries have the same overall shape.


```ts
// NO CAMERA GOING THROUGH THE WALL
// default (both pointer and physics use the invisible geometry)
GLTFContainer.create(myEntity, {
	src: '/models/myModel.gltf',
})

// NO CAMERA GOING THROUGH THE WALL
// Both use the same invisible geometry
GltfContainer.create(myEntity2, {
	src: '/models/myModel.gltf',
	invisibleMeshesCollisionMask: ColliderLayer.CL_PHYSICS | ColliderLayer.CL_POINTER,
})

// NO CAMERA GOING THROUGH THE WALL
// Both use the same visible geometry
GltfContainer.create(myEntity2, {
	src: '/models/myModel.gltf',
	visibleMeshesCollisionMask: ColliderLayer.CL_PHYSICS | ColliderLayer.CL_POINTER,
})

// YES CAMERA GOES THROUGH THE WALL
// physics and pointer are on diferent layers
GltfContainer.create(myEntity2, {
	src: '/models/myModel.gltf',
	invisibleMeshesCollisionMask: ColliderLayer.CL_PHYSICS,
	visibleMeshesCollisionMask: ColliderLayer.CL_POINTER
})

// YES CAMERA GOES THROUGH THE WALL
// physics and pointer are on diferent layers
GltfContainer.create(myEntity2, {
	src: '/models/myModel.gltf',
	invisibleMeshesCollisionMask: ColliderLayer.CL_POINTER,
	visibleMeshesCollisionMask: ColliderLayer.CL_PHYSICS
})
```

### Pointer blocking

Only shapes that have colliders can be activated with [pointer events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md" >}}). An entity also needs to have a collider to block pointer events from going through it and prevent hitting entities behind it. So for example, a player can't pick something up that is locked inside a chest, if the chest has colliders around it. The player's pointer events are only affected by meshes that are active in the `ColliderLayer.CL_POINTER` layer.

By default, a MeshCollider affects both the Physics and the Pointer layers, but you can change this value to only affect one, or neither, and to affect custom layers instead.

{{< hint warning >}}
**📔 Note**: Besides colliders, an entity also needs to have a `PointerEvents` component to respond to pointer events. The `pointerEventsSystem` helpers also take care of this requirment.
{{< /hint >}}

```ts
// only responds to player physics
// for example for an invisible wall that you can't walk through but you can click through
MeshCollider.setBox(myEntity, ColliderLayer.CL_PHYSICS)

// only responds to the player's pointer
// for example for an item you can click to pick up, but can walk right through
MeshCollider.setBox(myEntity2, ColliderLayer.CL_POINTER)
```

By default, the visible geometry of a `GLTFContainer` isn't mapped to any collision layers, but the invisible geometry affects both the Physics and the Pointer layers. You can change this value to only affect one, or neither, and to affect custom layers instead. You can also configure the visible geometry layer in the same way.

```ts
// default (both pointer and physics use the invisible geometry)
GLTFContainer.create(myEntity, {
	src: '/models/myModel.gltf',
})

// player physics uses the simpler invisible geometry
// pointer events use the full detailed contour of the visible geometry
GltfContainer.create(myEntity2, {
	src: '/models/myModel.gltf',
	invisibleMeshesCollisionMask: ColliderLayer.CL_PHYSICS,
	visibleMeshesCollisionMask: ColliderLayer.CL_POINTER,
})

// both player physics and pointer events use the full detailed contour of the visible geometry
// the simpler invisible geometry is mapped to ColliderLayer.CL_NONE to avoid calculating both
GltfContainer.create(myEntity, {
	src: '/models/myModel.gltf',
	invisibleMeshesCollisionMask: ColliderLayer.CL_NONE,
	visibleMeshesCollisionMask:
		ColliderLayer.CL_POINTER | ColliderLayer.CL_PHYSICS,
})

// don't respond to collisions of any kind, with either the visible or the invisible geometry:
GltfContainer.create(myEntity, {
	src: '/models/myModel.gltf',
	invisibleMeshesCollisionMask: ColliderLayer.CL_NONE,
})
```

## Advanced MeshCollider Syntax

The complete syntax for creating a `MeshCollider` component, without any helpers to simplify it, looks like this:

```ts
MeshCollider.create(myBox, {
	mesh: {
		$case: 'box',
		box: {},
	},
})

MeshCollider.create(myPlane, {
	mesh: {
		$case: 'plane',
		plane: {},
	},
})

MeshCollider.create(myShpere, {
	mesh: {
		$case: 'sphere',
		sphere: {},
	},
})

MeshCollider.create(myCylinder, {
	mesh: {
		$case: 'cylinder',
		cylinder: {},
	},
})
```

This is how the base protocol interprets MeshCollider components. The helper functions abstract away from this and expose a friendlier syntax, but behind the scenes they output this syntax.

The `$case` field allows you to specify one of the allowed types. Each type supports a different set of parameters.

The supported values for `$case` are the following:

- `box`
- `plane`
- `sphere`
- `cylinder`

Depending on the value of `$case`, it's valid to define the object for the corresponding shape, passing any relevant properties.
