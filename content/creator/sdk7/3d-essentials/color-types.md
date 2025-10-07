---
date: 2022-10-19
title: Color types
description: How to define color values
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/color-types/
weight: 8
---

Color values can passed as properties of different components, like [Materials]({{< ref "/content/creator/sdk7/3d-essentials/materials.md" >}}), [Text]({{< ref "/content/creator/sdk7/3d-essentials/text.md" >}}) or different properties of [UI entities]({{< ref "/content/creator/sdk7/2d-ui/onscreen-ui.md" >}}). Color values can either be of type `Color3` or `Color4`.

`Color3` contains three properties, _red_, _green_, and _blue_. `Color4` has those same three plus `alpha`, for transparency values.

## Set a color

You can make a color by using the `Color3.create()` or the `Color4.create()` functions.

```ts
// Red color
const red3 = Color3.create(1, 0, 0)
const red4 = Color4.create(1, 0, 0, 1)
```

You can also create certain predetermined colors that are part of the `Color3` and `Color4` namespaces.

```ts
const red = Color3.Red()
const blue = Color3.Blue()
const black = Color3.Black()
```

{{< hint info >}}
**💡 Tip**: Write `Color3.` or `Color4.` and Visual Studio should suggest all the possible values in an intelligent dropdown.
{{< /hint >}}

You can otherwise pick a random color using the following function:

```ts
const randomColor = Color3.Random()
```

If you prefer to describe a color in hexadecimal, use `Color3.fromHexString()`.

```ts
const red = Color3.fromHexString('FD350A')
const blue = Color3.fromHexString('0A0CFD')
```

Any object value that includes numeric values for `r`, `g`, and `b` can be interpreted as a `Color3` value. Likewise, any object that includes those properties plus an `a` value can be interpreted as a `Color4` value. This allows you to also use the following syntax:

```ts
// Red color
const red3 = { r: 1, g: 0, b: 0 }
const red4 = { r: 1, g: 0, b: 0, a: 1 }
```

The following example uses a color property as part of a `TextShape` component, to set the text color.

```ts
const myEntity = engine.addEntity()

Transform.create(myEntity, {
  position: Vector3.create(4, 1, 4),
})

TextShape.create(myEntity, {
  text: 'this text is RED',
  textColor: Color4.create(1, 0, 0, 1),
})
```

{{< hint warning >}}
**📔 Note**: `Color3` and `Color4` must be imported via

> `import { Color3, Color4 } from "@dcl/sdk/math"`

See [Imports]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#imports" >}}) for how to handle these easily.
{{< /hint >}}

## Transparency

Use the _alpha_ property of `Color4` to make a color translucid.

If alpha is 1, the color will be completely opaque, if it's 0 it will be completely invisible. Anything in between results in a partially transparent tone.

```ts
// Completely opaque
const opaque = Color4.create(1, 1, 1, 1)

// Half way
const half = Color4.create(1, 1, 1, 0.5)

// Almost invisible
const half = Color4.create(1, 1, 1, 0.1)
```

## Lerp

Use the `Color3.lerp()` or the `Color4.lerp()` function to define a color that's somewhere between two other colors. These functions work similar to the `Vector3.lerp()` function.

Both `Color3.lerp()` or the `Color4.lerp()` take the following arguments:

- `left`: The first color to use as reference
- `right`: The second color to use as reference
- `amount`: A number from 0 to 1 to define how much of the _left_ color to use in the mix. The closer to 0, the closer to the _left_ color.

```ts
const orange = Color3.lerp(Color3.Red(), Color3.Yellow(), 0.3)
```

You can use a system to gradually change the `amount` parameter, to create a smooth transition.

```ts
// Systems
var pulseState: number = 0
const color1 = Color4.Red()
const color2 = Color4.Yellow()

export function PulseSystem(dt: number) {
  pulseState += dt
  const entitiesWithMaterial = engine.getEntitiesWith(Material)

  // iterate over the entities of the group
  for (const [entity] of entitiesWithMaterial) {
    const material = Material.getMutable(entity)
    material.albedoColor = Color4.lerp(color1, color2, Math.sin(pulseState))
  }
}

engine.addSystem(PulseSystem)
```
