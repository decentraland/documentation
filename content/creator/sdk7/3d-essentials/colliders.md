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

{{< hint warning >}}
**📔 Note**:  Colliders don't affect how other entities interact with each other, entities can always overlap. Collision settings only affect how the entity interacts with the player's avatar and button events. Decentraland doesn't have a native physics engine, so if you want entities to fall, crash or bounce, you must code this behavior into the scene, or import a library to handle that.
{{< /hint >}}

## Colliders on primitive shapes

Entities that have a `MeshRenderer` component to give them a [primitive shape]({{< ref "/content/creator/sdk7/3d-essentials/shape-components.md#primitive-shapes" >}})(boxes, spheres, planes etc) don't have colliders by default. You must also give the entity a `MeshCollider` component.


The following collider shapes are available. Several shapes include optional additional fields, specific to that shape.

- **box**:

	Use `MeshRenderer.setBox()`, passing the entity.

- **plane**:

	Use `MeshRenderer.setPlane()`, passing the entity.

- **sphere**:

	Use `MeshRenderer.setSphere()`, passing the entity. 

- **cylinder**:

	Use `MeshRenderer.setCylinder()`, passing the entity. Pass `radiusTop` and `radiusBottom` as additional optional fields, to modify the cylinder.

	TIP: Set  either `radiusTop` or `radiusBottom` to 0 to make a cone.


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

## Colliders on 3D models

3D models can include their own colliders as part of a _.glTF_ or _.glb_ file. Any mesh in the model who's name ends in `_collider` is interpreted as a collider.

A _collider_ is a set of geometric shapes or planes that define which parts of the model are collided with. This allows for much greater control and is a lot less demanding on the system than using the visible geometry, as the collision object is usually a lot simpler (with less vertices) than the original model.

If a model doesn't have collisions, you can either:

- Give the entity a `MeshCollider` component, to give it a primitive shape collider.
- Overlay an invisible entity that has a `MeshCollider` component.
- Edit the model in an external tool like Blender to include a _collider mesh_. The collider must be named _x_collider_, where _x_ is the name of the model. So for a model named _house_, the collider must be named _house_collider_.


See [3D models](/creator/3d-modeling/3d-models) for more details on how to add colliders to a 3D model.



## Pointer blocking

Only shapes that have colliders can be activated with [pointer events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md" >}}). An entity also needs to have a collider to block pointer events on entities behind it. So for example, a player can't pick something up that is locked inside a chest, if the chest has colliders around it. The player's pointer events are only affected by collider meshes, not by the model's visible geometry.

You can configure a `MeshCollider` component to only respond to one kind of interaction. To do this, set the `collisionMask` property to one of the following values:

- `ColliderLayer.CL_PHYSICS`: Only blocks player movement (and doesn't affect pointer events)
- `ColliderLayer.CL_POINTER`: responds only to pointer events (and doesn't block the player movement)


```ts
// create entity
const myEntity = engine.addEntity()

// visible shape
MeshRenderer.setBox(myEntity)

// create a MeshCollider component that only responds to player physics
MeshCollider.setBox(myEntity, ColliderLayer.CL_PHYSICS)
```

The example above creates a `MeshCollider` component that is configured to only respond to player physics. With this configuration, you could for example have an invisible wall that players can't walk through, but that does allow them to click on items on the other side of the wall.


## Advanced Syntax


The complete syntax for creating a `MeshCollider` component, without any helpers to simplify it, looks like this:

```ts
MeshCollider.create(myBox, {
    mesh: { 
      $case: 'box',
      box: {} 
    }
  })

MeshCollider.create(myPlane, {
    mesh: { 
      $case: 'plane',
      plane: {} 
    }
  })

MeshCollider.create(myShpere, {
    mesh: { 
      $case: 'sphere',
      sphere: {} 
    }
  })

MeshCollider.create(myCylinder, {
    mesh: { 
      $case: 'cylinder',
      cylinder: {} 
    }
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
