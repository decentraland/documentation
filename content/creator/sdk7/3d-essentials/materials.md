---
date: 2018-02-7
title: Materials via code
description: Learn how to add materials and textures to entities with primitive shapes.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/materials/
weight: 3
---

## Materials

Materials can be applied to entities that use primitive shapes (cube, sphere, plane, etc) by adding a `Material` component. This component has several fields that allow you to configure the properties of the material, add a texture, etc.

You can't add material components to _glTF_ models. _glTF_ models include their own materials that are implicitly imported into a scene together with the model.

When importing a 3D model with its own materials, keep in mind that not all shaders are supported by the Decentraland engine. Only standard materials and PBR (physically based rendering) materials are supported. See [external 3D model considerations](/creator/3d-modeling/materials) for more details.

There are different types of supported materials:

- PBR (Physically Based Rendering): The most common kind of material in Decentraland. It supports plain colors or textures, and different properties like metallic, emissive, transparency, etc. Read more about [PBR](https://en.wikipedia.org/wiki/Physically_based_rendering).
- Basic materials: They don't respond to lights and shadows, which makes them ideal for displaying billboard images.

## Add a material

The following example creates a PBR material and sets some of its fields to give it a red color and metallic properties. This material is added to an entity that also has a box shape, so it will color the box with this material.

```ts
//Create entity and assign shape
const meshEntity = engine.addEntity()
Transform.create(meshEntity, {
  position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(meshEntity)

//Create material and configure its fields
Material.setPbrMaterial(meshEntity, {
  albedoColor: Color4.Red(),
  metallic: 0.8,
  roughness: 0.1,
})
```

To change the material of an entity that already has a `Material` component, run `Material.setPbrMaterial()` or any of the other helper functions and it will overwrite the original material. There's no need to remove the original `Material` or to use the advanced syntax.

```ts
//Create entity and assign shape
const meshEntity = engine.addEntity()
Transform.create(meshEntity, {
  position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(meshEntity)

//Create material and configure its fields
Material.setPbrMaterial(meshEntity, {
  albedoColor: Color4.Red(),
})

//Overwrite with new material component
Material.setPbrMaterial(meshEntity, {
  albedoColor: Color4.Blue(),
})
```

{{< hint warning >}}
**📔 Note**: The `Material` component must be imported via

> `import { Material } from "@dcl/sdk/ecs"`

See [Imports]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#imports" >}}) for how to handle these easily.
{{< /hint >}}

## Material colors

Give a material a plain color. In a PBR Material, you set the `albedoColor` field. Albedo colors respond to light and can include shades on them.

Color values are of type `Color4`, composed of _r_, _g_ and _b_ values (red, green, and blue). Each of these takes values between 0 and 1. By setting different values for these, you can compose any visible color. For black, set all three to 0. For white, set all to 1.

{{< hint warning >}}
**📔 Note**: If you set any color in `albedoColor` to a value higher than _1_, it will appear as _emissive_, with more intensity the higher the value. So for example, `{r: 15, g: 0, b: 0}` produces a very bright red glow.
{{< /hint >}}

See [color types]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md" >}}) for more details on how to set colors.

You can also edit the following fields in a PBR Material to fine-tune how its color is perceived:

- _emissiveColor_: The color emitted from the material.
- _reflectivityColor_: AKA _Specular Color_ in other nomenclature.

To create a plain color material that is not affected by light and shadows in the environment, create a basic material instead of a PBR material.

```ts
Material.setBasicMaterial(myEntity, {
  diffuseColor: Color4.Black(),
})
```

## Using textures

Set an image file as a texture on a material by setting the `texture` parameter.

```ts
//Create entity and assign shape
const meshEntity = engine.addEntity()
Transform.create(meshEntity, {
  position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(meshEntity)

//Create material and configure its fields
Material.setPbrMaterial(meshEntity, {
  texture: Material.Texture.Common({
    src: 'materials/wood.png',
  }),
})
```

In the example above, the image for the material is located in a `materials` folder, which is located at root level of the scene project folder.

{{< hint info >}}
**💡 Tip**: We recommend keeping your texture image files separate in a `/materials` folder inside your scene.
{{< /hint >}}

While creating a texture, you can also pass additional parameters:

- `filterMode`: Determines how pixels in the texture are stretched or compressed when rendered. This takes a value from the `TextureFilterMode` enum. See [Texture Scaling](#texture-scaling).
- `wrapMode`: Determines how a texture is tiled onto an object. This takes a value from the `TextureWrapMode` enum. See [Texture Wrapping](#texture-wrapping).

```ts
Material.setPbrMaterial(myEntity, {
  texture: Material.Texture.Common({
    src: 'materials/wood.png',
    filterMode: TextureFilterMode.TFM_BILINEAR,
    wrapMode: TextureWrapMode.TWM_CLAMP,
  }),
})
```

To create a texture that is not affected by light and shadows in the environment, create a basic material instead of a PBR material.

```ts
Material.setBasicMaterial(myEntity, {
  texture: Material.Texture.Common({
    src: 'materials/wood.png',
  }),
})
```

#### Textures from an external URL

You can point the texture of your material to an external URL instead of an internal path in the scene project.

```ts
Material.setBasicMaterial(myEntity, {
  texture: Material.Texture.Common({
    src: 'https://wearable-api.decentraland.org/v2/collections/community_contest/wearables/cw_tuxedo_tshirt_upper_body/thumbnail',
  }),
})
```

The URL must start with `https`, `http` URLs aren't supported. The site where the image is hosted should also have [CORS policies (Cross Origin Resource Sharing)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) that permit externally accessing it.

#### Multi-layered textures

You can use several image files as layers to compose more realistic textures, for example including a `bumpTexture` and a `emissiveTexture`.

```ts
Material.setPbrMaterial(myEntity, {
  texture: Material.Texture.Common({
    src: 'materials/wood.png',
  }),
  bumpTexture: Material.Texture.Common({
    src: 'materials/woodBump.png',
  }),
})
```

#### Texture wrapping

If you want the texture to be mapped to specific scale or alignment on your entities, then you need to configure _uv_ properties on the [MeshRenderer component]({{< ref "/content/creator/sdk7/3d-essentials/shape-components.md" >}}).

You set _u_ and _v_ coordinates on the 2D image of the texture to correspond to the vertices of the shape. The more vertices the entity has, the more _uv_ coordinates need to be defined on the texture, a plane for example needs to have 8 _uv_ points defined, 4 for each of its two faces.

```ts
const meshEntity = engine.addEntity()
Transform.create(meshEntity, {
  position: Vector3.create(4, 1, 4),
})
MeshRenderer.setPlane(
  meshEntity,
  [
    0, 0.75,

    0.25, 0.75,

    0.25, 1,

    0, 1,

    0, 0.75,

    0.25, 0.75,

    0.25, 1,

    0, 1,
  ]
)

Material.setPbrMaterial(myEntity, {
  texture: Material.Texture.Common({
    src: 'materials/wood.png',
    wrapMode: TextureWrapMode.TWM_REPEAT,
  }),
})
```

The following example includes a function that simplifies the setting of uvs. The `setUVs` function defined here receives a number of rows and columns as parameters, and sets the uvs so that the texture image is repeated a specific number of times.

```ts
const meshEntity = engine.addEntity()
Transform.create(meshEntity, {
  position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(meshEntity, setUVs(3, 3))

Material.setPbrMaterial(myEntity, {
  texture: Material.Texture.Common({
    src: 'materials/atlas.png',
    wrapMode: TextureWrapMode.TWM_REPEAT,
  }),
})

function setUVs(rows: number, cols: number) {
  return [
    // North side of unrortated plane
    0, //lower-left corner
    0,

    cols, //lower-right corner
    0,

    cols, //upper-right corner
    rows,

    0, //upper left-corner
    rows,

    // South side of unrortated plane
    cols, // lower-right corner
    0,

    0, // lower-left corner
    0,

    0, // upper-left corner
    rows,

    cols, // upper-right corner
    rows,
  ]
}
```

For setting the UVs for a `box` mesh shape, the same structure applies. Each of the 6 faces of the cube takes 4 pairs of coordinates, one for each corner. All of these 48 values are listed as a single array.

You can also define how the texture is tiled if the mapping spans more than the dimensions of the texture image. The `texture` object lets you configure the wrapping mode by setting the `wrapMode` field. This property takes its values from the `TextureWrapMode` enum, which allows for the following values:

- `TextureWrapMode.TWM_CLAMP`: The texture is only displayed once in the specified size. The rest of the surface of the mesh is left transparent.
- `TextureWrapMode.TWM_REPEAT`: The texture is repeated as many times as it fits in the mesh, using the specified size.
- `TextureWrapMode.TWM_MIRROR`: As in wrap, the texture is repeated as many times as it fits, but the orientation of these repetitions is mirrored.

```ts
Material.setPbrMaterial(myEntity, {
  texture: Material.Texture.Common({
    src: 'materials/atlas.png',
    wrapMode: TextureWrapMode.TWM_MIRROR,
  }),
})
```

The example above sets the wrapping mode to `TWM_MIRROR`.

{{< hint warning >}}
**📔 Note**: Uv properties are currently only available on `plane` and on `box` shapes.
{{< /hint >}}

#### Texture scaling

When textures are stretched or shrinked to a different size from the original texture image, this can sometimes create artifacts. In a 3D environment, the effects of perspective cause this naturally. There are various [texture filtering](https://en.wikipedia.org/wiki/Texture_filtering) algorithms that exist to compensate for this in different ways.

The `Material` object uses the _bilinear_ algorithm by default, but it lets you configure it to use the _nearest neighbor_ or _trilinear_ algorithms instead by setting the `samplingMode` property of the texture. This takes a value from the `TextureFilterMode` enum:

- `TextureFilterMode.TFM_POINT`: Uses a "nearest neighbor" algorithm. This setting is ideal for pixel art style graphics, as the contours will remain sharply marked as the texture is seen larger on screen instead of being blurred.
- `TextureFilterMode.TFM_BILINEAR`: Uses a bilinear algorithm to estimate the color of each pixel.
- `TextureFilterMode.TFM_TRILINEAR`: Uses a trilinear algorithm to estimate the color of each pixel.

```ts
Material.setPbrMaterial(myEntity, {
  texture: Material.Texture.Common({
    src: 'materials/atlas.png',
    filterMode: TextureFilterMode.TFM_BILINEAR,
  }),
})
```

## Avatar Portraits

To display a thumbnail image of any player, use `Material.Texture.Avatar` when setting the texture of your material, passing the address of an existing player. This creates a texture from a 256x256 image of the player, showing head and shoulders. The player is displayed wearing the set of wearables that the current server last recorded.

```ts
Material.setPbrMaterial(myEntity, {
  texture: Material.Texture.Avatar({
    userId: '0x517....',
  }),
})
```

![](/images/avatarTexture.png)

You can fetch the portrait of any Decentraland player, even if they're not currently connected, and even if they don't have a claimed Decentraland name.

The following properties are supported within the object you pass as an argument:

- `userId`: ID of the user who's profile you want to display
- `filterMode`: Determines how pixels in the texture are stretched or compressed when rendered. This takes a value from the `TextureFilterMode` enum. See [Texture Scaling](#texture-scaling).
- `wrapMode`: Determines how a texture is tiled onto an object. This takes a value from the `TextureWrapMode` enum. See [Texture Wrapping](#texture-wrapping).

## Transparent materials

To make a material with a plain color transparent, simply define the color as a `Color4`, and set the 4th value to something between _0_ and _1_. The closer to _1_, the more opaque it will be.

```typescript
let transparentRed = Color4.create(1, 0, 0, 0.5)

Material.setPbrMaterial(meshEntity, {
  albedoColor: transparentRed,
})
```

To make a material with a texture only transparent in regions of the texture:

- Set an image in `alphaTexture`.

  > Note: This must be a single-channel image. In this image use the color red to determine what parts of the real texture should be transparent.

- Optionally set the texture normally, and set the `transparencyMode` to field.

The `transparencyMode` takes its value from the `MaterialTransparencyMode` enum, that can have the following values:

- `MaterialTransparencyMode.MTM_OPAQUE`: No transparency at all
- `MaterialTransparencyMode.MTM_ALPHA_TEST`: Each pixel is either completely opaque or completely transparent, based on a threshold.
- `MaterialTransparencyMode.MTM_ALPHA_BLEND`: Intermediate values are possible based on the value of each pixel.
- `MaterialTransparencyMode.MTM_ALPHA_TEST_AND_ALPHA_BLEND`: Uses a combination of both methods.
- `MaterialTransparencyMode.MTM_AUTO`: Determines the method based on the provided texture.

<!-- TODO: Confirm that auto really works like that!! -->

If you set the `transparencyMode` to `MaterialTransparencyMode.MTM_ALPHA_TEST`, you can fine tune the threshold used to determine if each pixel is transparent or not. Set the `alphaTest` property between _0_ and _1_. By default its value is _0.5_.

```ts
// Using alpha test
Material.setPbrMaterial(meshEntity1, {
  texture: Material.Texture.Common({
    src: 'images/myTexture.png',
  }),
  transparencyMode: MaterialTransparencyMode.MTM_ALPHA_TEST,
  alphaTest: 1,
})

// Using a alpha blend
Material.setPbrMaterial(meshEntity1, {
  texture: Material.Texture.Common({
    src: 'images/myTexture.png',
  }),
  transparencyMode: MaterialTransparencyMode.MTM_ALPHA_BLEND,
})
```

<!--
## Casting no shadows

 TODO: not currently working


To prevent a material from casting shadows over other objects, use the `castShadows` property set to _false_. This property is always _true_ by default.

```ts
Material.create(meshEntity3, {
  albedoColor: Color4.Red(),
  castShadows: true
})
```
-->
<!--
## Video playing

 TODO: feature missing
To stream video from a URL into a material, or play a video from a file stored in the scene, see [video playing]({{< ref "/content/creator/sdk7/media/video-playing.md" >}}).

The video is used as a texture on a material, you can set any of the other properties of materials to alter how the video screen looks.

-->

## Advanced syntax

The complete syntax for creating a `Materials` component, without any helpers to simplify it, looks like this:

```ts
Material.create(myEntity, {
  texture: {
    tex: {
      $case: 'texture',
      texture: {
        src: 'images/scene-thumbnail.png',
      },
    },
  },
})

Material.create(myEntity, {
  texture: {
    tex: {
      $case: 'avatarTexture',
      avatarTexture: {
        userId: '0x517....',
      },
    },
  },
})
```

This is how the base protocol interprets Materials components. The helper functions abstract away from this and expose a friendlier syntax, but behind the scenes they output this syntax.

The `$case` field allows you to specify one of the allowed types. Each type supports a different set of parameters. In the example above, the `box` type supports a `uvs` field.

The supported values for `$case` are the following:

- `texture`
- `avatarTexture`

Depending on the value of `$case`, it's valid to define the object for the corresponding shape, passing any relevant properties.

To add a `Material` component to an entity that potentially already has an instance of this component, use `Material.createOrReplace()`. The helper functions like `MeshRenderer.setPbrMaterial()` handle overwriting existing instances of the component, but running `Material.create()` on an entity that already has this component returns an error.
