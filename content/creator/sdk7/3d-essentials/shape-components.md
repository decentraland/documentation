---
date: 2018-02-6
title: Shape components
description: Learn about the different components that give entities their 3D shape and collision.
categories:
  - development-guide
type: Document
url: /creator/development-guide/shape-components/
weight: 2
---

Three dimensional scenes in Decentraland are based on the [Entity-Component](https://en.wikipedia.org/wiki/Entity%E2%80%93component%E2%80%93system) model, where everything in a scene is an _entity_, and each entity can include _components_ that shape its characteristics and functionality.

The rendered shape of an entity is determined by what component it uses.

<img src="/images/media/ecs-simple-components.png" alt="nested entities" width="400"/>

## Primitive shapes

Several basic shapes, often called _primitives_, can be added to an entity.

The following primitive shape components are available:

- `box`
- `sphere`
- `plane`
- `cylinder`

To apply a primitive shape to an entity, give it a `MeshRenderer` component:

```ts
const primitiveEntity = engine.addEntity()

MeshRenderer.create(primitiveEntity, { box: {} })
```


Primitive shapes don't include materials. To give it a color or a texture, you must assign a [material component]({{< ref "/content/creator/sdk7/3d-essentials/materials.md" >}}) to the same entity.

To make a primitive clickable, or to prevent players from walking through it, you must give the entity a _collider_ via a [MeshCollider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}) component.


Each of these components has certain fields that are specific to that shape, for example the _cylinder_ shape has `radiusTop` and `radiusBottom`, etc.

> Tip: You can make a cone out of a cylinder by setting the `radiusTop` or `radiusBottom` to 0.

Primitives of type `box` or `plane` include a `uvs` field that allows you to handle how to map textures to their surface. See [materials]({{< ref "/content/creator/sdk7/3d-essentials/materials.md" >}}) for more details. 


## 3D models

For more complex shapes, you can build a 3D model in an external tool like Blender and then import them in _.glTF_ or _.glb_ (binary _.glTF_). [glTF](https://www.khronos.org/gltf) (GL Transmission Format) is an open project by Khronos providing a common, extensible format for 3D assets that is both efficient and highly interoperable with modern web technologies.

To add an external model into a scene, add a `GltfContainer` component to an entity and set its `src` to the path of the glTF file containing the model.

```ts
const houseEntity = engine.addEntity()

GltfContainer.create(houseEntity, { 
	src: "models/House.gltf" 
})
```

The `src` field is required, you must give it a value when constructing the component. In the example above, the model is located in a `models` folder at root level of the scene project folder.

> Tip: We recommend keeping your models separate in a `/models` folder inside your scene.

glTF models can include their own embedded textures, materials, colliders and animations. See [3D models](/creator/3d-modeling/3d-models) for more information on this.

Keep in mind that all models, their shaders and their textures must be within the parameters of the [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}).

### Free libraries for 3D models

Instead of building your own 3D models, you can also download them from several free or paid libraries.

To get you started, below is a list of libraries that have free or relatively inexpensive content:

- [Assets from the Builder](https://github.com/decentraland/builder-assets/tree/master/assets)
- [SketchFab](https://sketchfab.com/)
- [Clara.io](https://clara.io/)
- [Archive3D](https://archive3d.net/)
- [SketchUp 3D Warehouse](https://3dwarehouse.sketchup.com/)
- [Thingiverse](https://www.thingiverse.com/) (3D models made primarily for 3D printing, but adaptable to Virtual Worlds)
- [ShareCG](https://www.sharecg.com/)
- [CGTrader](https://www.cgtrader.com/)

> Note: Pay attention to the license restrictions that the content you download has.

Note that in several of these sites, you can choose what format to download the model in. Always choose _.glTF_ format if available. If not available, you must convert them to _glTF_ before you can use them in a scene. For that, we recommend importing them into Blender and exporting as _.glTF_ from there.


### Optimize 3D models

To ensure that 3D models in your scene load faster and take up less memory, follow these best practices:

- Save your models in _.glb_ format, which is a lighter version of _.gltf_.
- If you have multiple models that share the same textures, export your models with textures in a separate file. That way multiple models can refer to a single texture file that only needs to be loaded once.
- If your scene has entities that appear and disappear, it might be a good idea to pool these entities and keep them underground, or at a scale of 0. This will help them appear faster, the trade-off is that they will occupy memory when not in use. See [entities and components]({{< ref "/content/creator/sdk7/architecture/entities-components.md#pooling-entities-and-components" >}})


## Stretching a shape

Primitive shapes and 3D models have default dimensions that you can alter by changing the scale in the entity's `Transform` component.

```ts
const primitiveEntity = engine.addEntity()

MeshRenderer.create(primitiveEntity, { box: {} })

Transform.create(primitiveEntity, {
	position: {x: 8, y:1, z: 8},
	scale: {x: 4, y:0.5, z: 4}
})
```

## Make invisible


You can make an entity invisible by giving an entity a `VisibilityComponent`, with its `visible` property set to _false_.


```ts
const myEntity = engine.addEntity()
Transform.create(myEntity, { 
  position: Vector3.create(4, 0, 4)
})
MeshRenderer.create(myEntity, { box: {} })

VisibilityComponent.create(myEntity, {visible: false})
```

The `VisibilityComponent` works the same for entities with primitive shapes and with `GLTFContainer` components.

If an entity is invisible, its collider can block a player's path and can prevent clicking entities that are behind it.


## Advanced syntax

The complete syntax for creating a `MeshRenderer` component, without any helpers to simplify it, looks like this:

```ts
MeshRenderer.create(myBox, {
    mesh: { 
      $case: 'box',
      box: { uvs: []} 
    }
  })

MeshRenderer.create(myPlane, {
    mesh: { 
      $case: 'plane',
      plane: { uvs: []} 
    }
  })

MeshRenderer.create(myShpere, {
    mesh: { 
      $case: 'sphere',
      sphere: {} 
    }
  })

MeshRenderer.create(myCylinder, {
    mesh: { 
      $case: 'cylinder',
      cylinder: {} 
    }
  })
```

This is how the base protocol interprets MeshRenderer components. The helper functions abstract away from this and expose a friendlier syntax, but behind the scenes they output this syntax.


The `$case` field allows you to specify one of the allowed types. Each type supports a different set of parameters. In the example above, the `box` type supports a `uvs` field.

The supported values for `$case` are the following:

- `box`
- `plane`
- `sphere`
- `cylinder`

Depending on the value of `$case`, it's valid to define the object for the corresponding shape, passing any relevant properties.