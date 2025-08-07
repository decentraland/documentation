---
date: 2025-08-01
title: Lights
description: Learn how to use lights in your scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/lights/
weight: 5
---

Lights are a fundamental part of 3D graphics. They are used to illuminate the scene and create a sense of depth and realism, and can be used to create different moods and atmospheres.

By default, the scene is lit with a single directional light. This is a light that shines in a specific direction, and is used to simulate the sun or the moon. See [Skybox Control]({{< ref "/content/creator/sdk7/interactivity/skybox-control.md" >}}) for more information.

You can add up to 1 light per parcel in your scene.

There are two supported types of lights:

- Point light: A light that shines in all directions from a specific point.
- Spot light: A light that shines in a specific direction, and covers only a cone-shaped area.


## Adding a light

To add a light to your scene, you need to create a light entity and add the `LightSource` component to it.

```ts
import { engine, LightSource } from '@dcl/sdk/ecs'

const light = engine.addEntity()

Transform.create(light, {
  position: Vector3.create(10, 3, 10),
})

LightSource.create(light, {
  type: {
            $case: 'point',
            point: {}
        }
})
```

{{< hint warning >}}
**📔 Note**: A light with the default brightness will be hardly visible with the midday sun, like in the real world. You can use the [Skybox Control]({{< ref "/content/creator/sdk7/interactivity/skybox-control.md" >}}) to force the skybox to night time, or increase the brightness by setting the `intensity` property of the `LightSource` component to a higher value.
{{< /hint >}}


## Spot lights

Spot lights are lights that shine in a specific direction, and cover a specific cone-shaped area. The direction of the light is defined by the entity's Transform component. The aperture of the cone is defined by the `innerAngle` and `outerAngle` properties of the `LightSource` component. 

```ts
import { engine, LightSource } from '@dcl/sdk/ecs'

const light = engine.addEntity()

Transform.create(light, {
  position: Vector3.create(10, 3, 10),
  rotation: Quaternion.fromEulerDegrees(-90, 0, 0),
})

LightSource.create(light, {
	type: {
            $case: 'spot',
            spot: {
                innerAngle: 20,
                outerAngle: 120
            }
        },
	shadow: true
})
```

The `innerAngle` is the angle of the inner cone, where the light is at full brightness, and the `outerAngle` is the angle of the outer cone, where the light gradually fades out towards the edges of the cone. You can play with these values to create different effects, for lights that are more focused or more diffuse.

## Intensity and color

All lights, both point and spot, have a color and an intensity. The color is defined by the `color` property of the `LightSource` component, and the intensity is defined by the `intensity` property.

```ts
import { engine, LightSource } from '@dcl/sdk/ecs'

const light = engine.addEntity()

Transform.create(light, {
  position: Vector3.create(10, 3, 10),
})

LightSource.create(light, {
  type: {
            $case: 'point',
            point: {}
        },
  color: Color3.Red(),
  intensity: 1000,
})
```

The color is a `Color3` object, if not specified it will be white. You can set this to any color you want, which can have a big impact on the mood of the scene.

The intensity is expressed in candels (lumens/m^2 at 1 m distance, or lumens divided by 4*pi).

The defualt intensity is 100, this is the brightness of an average lightbulb in the real world and can be seen up to around 10 meters away from the light source. If you need the light to be visible from further away, or during the day, you can increase the intensity.

The distance at which the light is visible is the square root of the intensity value.

- At an intensity of 100, the light is visible up to around 10 meters away.
- At an intensity of 1000, the light is visible up to around 31 meters away.
- At an intensity of 10000, the light is visible up to around 100 meters away.


## Shadows

Each light can cast shadows or not. By default they don't, but you can enable them by setting the `shadow` property of the `LightSource` component to `true`.

```ts
import { engine, LightSource } from '@dcl/sdk/ecs'

const light = engine.addEntity()

Transform.create(light, {
  position: Vector3.create(10, 3, 10),
  rotation: Quaternion.fromEulerDegrees(-90, 0, 0),
})

LightSource.create(light, {
	type: {
            $case: 'spot',
            spot: {
                innerAngle: 20,
                outerAngle: 120
            }
    },
	shadow: true
})
```

{{< hint warning >}}
**📔 Note**: 	Shadows are only supported for spot lights. Point lights don't support shadows. If there are multiple lights in the scene, some of them may not be casting shadows, see [Light optimization](#light-optimization) for more information.
{{< /hint >}}



## Switching a light on and off

The LightSource component has a `active` property that can be used to switch a light on and off. This is useful if you want to turn a light off without removing it from the scene, or without setting the `intensity` to 0 and losing reference of what the original intensity was.

```ts
import { engine, LightSource } from '@dcl/sdk/ecs'

const light = engine.addEntity()

Transform.create(light, {
  position: Vector3.create(10, 3, 10),
  rotation: Quaternion.fromEulerDegrees(-90, 0, 0),
})

LightSource.create(light, {
	type: {
            $case: 'spot',
            spot: {
                innerAngle: 20,
                outerAngle: 120
            }
        },
	shadow: true
})

const switch = engine.addEntity()

Transform.create(switch, {
  position: Vector3.create(8, 1, 10),
})

MeshRenderer.setBox(switch, {})

MeshCollider.setBox(switch, {})

pointerEventsSystem.onPointerDown(
	{
		entity: switch,
		opts: {
			button: InputAction.IA_POINTER,
			hoverText: 'Click',
		},
	},
	function () {
		LightSource.getMutable(light).active = !LightSource.getMutable(light).active
	}
)
```

## Light optimization

Light sources can have a pretty big impact on the performance of your scene. For this reason, the engine will automatically optimize the scene by disabling some of the lights or their shadows, starting with the ones that are further away.

The number allowed active lights in a scene is capped at one per parcel, and beyond that it depends on the user´s selected quality settings.

- Low quality: Maximum 4 lights (in a scene with enough parcels)
- Medium quality: Maximum 6 lights (in a scene with enough parcels)
- High quality: Maximum 10 lights (in a scene with enough parcels)

If there are more lights than allowed, the engine will automatically disable lights based on proximity of the light source to the player. As the player moves, the engine will re-enable lights that are close enough to the player.

In all cases, the engine will only render shadows for up to 3 light sources. If there are more lights with shadows than 3, the engine will automatically disable shadows for the remaining lights that are further away.

Besides the maximum number of allowed lights, shadows also depend on distance from the player.

- Less than 10 meter away: Shadows are rendered as soft shadows (high quality)
- Between 10 and 20 meters away: Shadows are rendered as hard shadows (low quality)
- Between 20 and 40 meters away: Shadows aren't rendered
- More than 40 meters away: Light sources are not rendered at all

It's also important to note that lights are only rendered if the player is standing inside the scene. If the player is outside the scene, the lights will not be rendered.

## Light range


The lightSource component has a `range` property that can be used to set the maximum distance at which the light is visible. By default, the value of the `range` property is -1, which means that the light range depends on the intensity of the light.

- At an intensity of 100, the range is 10 meters.
- At an intensity of 1000, the range is 31 meters.
- At an intensity of 10000, the range is 100 meters.

The default setting ensures that the dropoff curve is smooth and looks natural. But in case you want to limit the range of the light, you can set the `range` property to a positive number.


```ts
import { engine, LightSource } from '@dcl/sdk/ecs'

const light = engine.addEntity()

Transform.create(light, {
  position: Vector3.create(10, 3, 10),
})

LightSource.create(light, {
  type: {
            $case: 'point',
            point: {}
        },
  intensity: 1000,
  range: 20,
})
```

{{< hint warning >}}
**📔 Note**: Setting the `range` property to a positive number will abruptly cut the light at the provided distance. This is useful if you want to create a light that is only visible in a specific area, or to optimize the performance of your scene.
Setting the `range` to a value that is larger than what the light can actually reach with its current intensity will not have any effect.
{{< /hint >}}


## Light masks

You can use a light mask to produce some interesting effects. Instead of illuminating the entire area, you can apply a texture to be used as a filter that will only illuminate parts of the area.

Masks are more typically used with spot lights, but they can also be used with point lights. Below is an example of a spot light with a mask applied.

```ts
import { engine, LightSource } from '@dcl/sdk/ecs'

const light = engine.addEntity()

Transform.create(light, {
  position: Vector3.create(10, 3, 10),
})

LightSource.create(light, {
	type: {
            $case: 'spot',
            spot: {
                innerAngle: 20,
                outerAngle: 120
            }
        },
	shadow: true
	shadowMaskTexture: Material.Texture.Common({src: "assets/scene/images/lightmask1.png"})         
})
```

For example, you can apply the image below to produce a fun effect where the light is only visible in the areas where the texture is white. You can can use this with lights of any color and intensity.

<img src="/images/lightmask1.png" width="500" />

With a black and white image, the light is either hitting an area or not. It's also possible to pass an image with colors, and these colors will tint your light on each area, this can be used to project a colored logo or image onto a surface.

{{< hint warning >}}
**📔 Note**: The image used as a mask must have a height and width in pixels that is a power of 2 (eg: 1024, 512, 256). This feature doesn't work for images that have different dimensions.
{{< /hint >}}

When applying a mask to a point light, the texture will be wrapped as a cube around the light source. If you want to avoid having visible edges between the sides of the cube, make sure the texture has continuity in the edges.


```ts
import { engine, LightSource } from '@dcl/sdk/ecs'

const light = engine.addEntity()

Transform.create(light, {
  position: Vector3.create(10, 3, 10),
})

LightSource.create(light, {
	type: {
            $case: 'point',
            point: {}
        },
	shadowMaskTexture: Material.Texture.Common({src: "assets/scene/images/point-light-mask1.png"})         
})
```

For example, the image below displays each of the letters on different sides of the cube (Y on top, -Y on the bottom, X on the right, -X on the left, Z on the front, -Z on the back).

<img src="/images/point-light-mask1.png" width="500" />






