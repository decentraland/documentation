---
date: 2022-10-28
title: UI Background
description: Set a background color on a UI entity.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/ui-background/
weight: 4
---

## uiBackground

A `uiBackground` component gives color or a texture an entity's area. It uses the size and position defined by the entity's `uiTransform`.

The following fields can be configured, all of them are optional:

- `color`: The color to use on the entity, as a [Color4]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md">}}) value.

{{< hint info >}}
**💡 Tip**: Make an entity semi-transparent by setting the 4th value of the `Color4` to less than 1.
{{< /hint >}}

- `texture`: The texture to display on the entity, this takes an object with various parameters about the texture. The same properties are available as in textures in [materials on 3D entities]({{< ref "/content/creator/sdk7/3d-essentials/materials.md#using-textures" >}}).

  - `src`: The path to the image file to use as a texture. (string)
  - `filterMode`: _(optional)_ Determines how pixels in the texture are stretched or compressed when rendered. . See [Texture Scaling]({{< ref "/content/creator/sdk7/3d-essentials/materials.md#texture-scaling" >}}).
    (FilterMode = 'point' | 'bi-linear' | 'tri-linear')
  - `wrapMode`: _(optional)_ Determines how a texture is tiled onto an entity. This takes a value from the `TextureWrapMode` enum. See [Texture Wrapping](({{< ref "/content/creator/sdk7/3d-essentials/materials.md#texture-wrapping" >}}).
    (WrapMode = 'repeat' | 'clamp' | 'mirror' | 'mirror-once')

  > Tip: You can combine both `texture` and `color` properties on a single `uiBackground` component to produce a tinted texture.

- `textureMode`: Selects how you want the texture to adapt to the size of the entity that it's applied to. (TextureMode = 'nine-slices' | 'center' | 'stretch')enum, which supports the following vales:

  - `center`: The texture is not stretched, it's positioned centered on the entity and parts of it may be cropped depending on the entity's size.
  - `stretch`: The texture is stretched to match the entire surface of the entity.
  - `nine-slices`: Parts of the texture are stetched to match the entire surface of the entity, leaving margins unstretched. See [nine-slice textures](#nine-slice-textures).

- `avatarTexture`: Display an avatar profile thumbnail, based on an avatar ID. See [Avatar Portraits](({{< ref "/content/creator/sdk7/3d-essentials/materials.md#avatar-portraits" >}}).
- `textureSlices`: Determine the margins to use when using the nine-slice texture mode, see [nine-slice textures](#nine-slice-textures). Set a number smaller than 1, as a fraction of the total width or height of the image.
<!-- - `uvs`: TODO -->

Simple color:

```ts
import ReactEcs, { ReactEcsRenderer, UiEntity } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: 700,
      height: 400
    }}
    uiBackground={{
		color: Color4.create(0.5, 0.8, 0.1, 0.6)
	}}
  >
))
```

Repeated texture pattern:

```ts
import ReactEcs, { ReactEcsRenderer, UiEntity } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: 700,
      height: 400
    }}
    uiBackground={{
		textureMode: 'center'
		texture: {
			src: "images/brick-wall-texture.png",
			wrapMode: 'repeat'
		}
	}}
  >
))
```

## Nine-slice textures

You can use [9-slice scaling](https://en.wikipedia.org/wiki/9-slice_scaling) with your textures, to ensure that corners and margins don't get stretched unevenly.

With this popular technique, you slice an image into 9 segments, that will be stretched in different ways to preserve the proportions of the margins and corners. For example, use this to define rounded-corner backgrounds that easily adapt to any size. Consider the following image (borrowed from [Wikipedia](https://en.wikipedia.org/wiki/9-slice_scaling#/media/File:Traditional_scaling_vs_9-slice_scaling.svg)):

![](/images/media/9-slice.png)

In this image we see the orginal texture (top-left), and the result of scaling it in a traditional way (top-right); notice how the corners get deformed. Below that, we see the texture segmented into 9 slices (bottom-left), and then the result of stretching the image according to the 9-slice method (bottom-right).

Here's how each segment is affected, using the above image as reference.

- Segment 5 is the only part of the image that is fully stretched on both x and y axis.
- Segments 1,3, 7, and 9 (the corneres) arent stetched at all.
- Segments 2 and 8 are only stetched horizontally
- Segments 4 and 6 are only stegched vertically.

To use nine-slice stretching on an entity, set the `textureMode` to `BackgroundTextureMode.NINE_SLICES`. You can optionally also set a width for the margin on each side in `textureSlices`.

```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{ width: 700, height: 400 }}
    uiBackground={{
		textureMode: 'nine-slices',
		texture: {
			src: 'images/rounded_alpha_square.png'
		},
		textureSlices: {
      top: 0.2,
      bottom: 0.2,
      left: 0.2,
      right: 0.2
    }
	}}
  >
))
```

<!--
## Images from an image atlas

TODO: Wait for textures in UI

You can use an image atlas to store multiple images and icons in a single image file. You then display rectangular parts of this image file in your UI based on pixel positions, pixel width, and pixel height inside the source image.

Below is an example of an image atlas with multiple icons arranged into a single file.

![](/images/media/UI-atlas.png)

The `UIImage` component has the following fields to crop a sub-section of the original image:

- `sourceTop`: the _y_ coordinate, in pixels, of the top of the selection
- `sourceLeft`: the _x_ coordinate, in pixels, of the left side of the selection.
- `sourceWidth`: the width, in pixels, of the selected area
- `sourceHeight`: the height, in pixels, of the selected area

When constructing a `UIImage` component, you must pass a `Texture` component as an argument. Read more about `Texture` components in [materials]({{< ref "/content/creator/sdk7/3d-essentials/materials.md" >}}).

```ts
let imageAtlas = "images/image-atlas.jpg"
let imageTexture = new Texture(imageAtlas)

const canvas = new UICanvas()

const playButton = new UIImage(canvas, imageTexture)
playButton.sourceLeft = 26
playButton.sourceTop = 128
playButton.sourceWidth = 128
playButton.sourceHeight = 128

const startButton = new UIImage(canvas, imageTexture)
startButton.sourceLeft = 183
startButton.sourceTop = 128
startButton.sourceWidth = 128
startButton.sourceHeight = 128

const exitButton = new UIImage(canvas, imageTexture)
exitButton.sourceLeft = 346
exitButton.sourceTop = 128
exitButton.sourceWidth = 128
exitButton.sourceHeight = 128

const expandButton = new UIImage(canvas, imageTexture)
expandButton.sourceLeft = 496
expandButton.sourceTop = 128
expandButton.sourceWidth = 128
expandButton.sourceHeight = 128
```

You can change the texture being used by an existing `UIImage` component, set the `source` field.

```ts
playButton.source = imageTexture2
``` -->
