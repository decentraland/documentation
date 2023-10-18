---
date: 2018-02-11
title: Text shapes
description: How to add text to your scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/text/
weight: 6
---

Add text to a scene using the `TextShape` component. This text sits in a position

Text in Decentraland supports all _utf8_ characters, this includes oriental and special characters.

{{< hint warning >}}
**📔 Note**:  This component is useful for in-world labels and UIs that exist in the 3D space of the scene, not for the player's 2D HUD UI.
{{< /hint >}}

The `TextShape` component is mutually exclusive with other shape components like primitive shapes and glTF 3D models, see [Shape components]({{< ref "/content/creator/sdk7/3d-essentials/shape-components.md" >}}) for more details.

To add text as a label on an existing entity, you create a second entity that has the `TextShape` component and set it as a child of the other entity.

## Create a text component

The following example shows how to create a `TextShape` component and add it to an entity.

```ts
const sign = engine.addEntity(true)

Transform.create(sign,{
    position: Vector3.create(8, 1 ,8) 
  })

TextShape.create(sign,{
    text: 'Hello World'
  })
```

{{< hint warning >}}
**📔 Note**:  If the entity with the text component is a child of another entity, then it will be affected by the parent's scale. If the parent is scaled unevenly along its axis, this will result in the text also being stretched or compressed.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**:  `TextShape` components aren't clickable. `PointerEvents` comopnents aren't activated when used on entites that have a `TextShape` component.
{{< /hint >}}

## Change the text value

When creating a new text component, you assign it a string to display. This string is stored in the `text` field.

If you want to change the string displayed by the component, you can do so at any time by changing the `text` field on a [mutable version]({{< ref "/content/creator/sdk7/programming-patterns/mutable-data.md" >}}) of the component.

```ts
const mutableText = TextShape.getMutable(myEntity)

mutableText.text = "new string"
```


## Basic text properties

The `TextShape` component has several properties that can be set to style the text. Below are some of the most common:

- `font`: Value from the enum `Font`.
- `fontSize`: _number_.
- `textColor`: _Color4_ object. _Color4_ objects store an _RBG_ color as three numbers from 0 to 1, plus _alpha_ for transparency. See [color types]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md" >}}) for more details.
- `opacity`: _number_. Set it to less than 1 to make the text translucid.

```ts
TextShape.create(sign,{
    text: 'Hello World',
	textColor: { r: 1, g: 0, b: 0, a:1 },
	fontSize: 5,
	font: Font.F_SANS_SERIF
  })
```



## Fonts


Text shapes can use fonts from the enum `Font`. This enum currently includes the following fonts:

- `Font.F_LIBERATION_SANS`
- `Font.F_SANS_SERIF`. 

By default uses it uses `Font.F_LIBERATION_SANS`.


```ts
TextShape.create(sign,{
    text: 'Hello World',
	textColor: { r: 1, g: 0, b: 0 },
	fontSize: 5,
	font: Font.F_SANS_SERIF
  })
```

{{< hint info >}}
**💡 Tip**:  If using VS studio or some other IDE, type `Font.` and you should see a list of suggestions with all of the available fonts.
{{< /hint >}}

## Text alignment and padding properties

The `TextShape` component creates a text box that has a size, padding, etc.

- `textAlign`: Select a value from the `TextAlignMode` enum. Possible values include all combinations between vertical (_top_, _bottom_, _center_) and horizontal (_left_, _right_, _center_) alignment.
- `width`: _number_. The width of the text box.
- `height`: _number_. The height of the text box.
- `paddingTop`: _number_. Space between the text and the outline of the text box.
- `paddingRight`: _number_. Space between the text and the outline of the text box.
- `paddingBottom`: _number_. Space between the text and the outline of the text box.
- `paddingLeft`: _number_. Space between the text and the outline of the text box.
- `zIndex`: _number_. Useful for when multiple flat entities occupy the same space, it determines which one to show in front.

{{< hint info >}}
**💡 Tip**:  If a text is meant to float in space, it's a good idea to add a [`Billboard` component]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md#face-the-user">}}) so that the text rotates to always face the player and be legible.
{{< /hint >}}

## Text shadow and outline properties

The text has no shadow by default, but you can set the following values to give it a shadow-like effect.

- `shadowBlur`: _number_
- `shadowOffsetX`: _number_
- `shadowOffsetY`: _number_
- `shadowColor`: _Color3_ object. _Color3_ objects store an _RBG_ color as three numbers from 0 to 1.

```ts
TextShape.create(sign,{
    text: 'Text with shadow',
	shadowColor: { r: 1, g: 0, b: 0 },
	shadowOffsetY: 1,
	shadowOffsetX: -1
  })
```

The letters in the text can also have an outline in a different color surrounding its perimeter.

- `outlineWidth`: _number_. How many pixels wide the text outline will be, in all directions. By default _0_, which makes it invisible.
- `outlineColor`: _Color3_ object. _Color3_ objects store an _RBG_ color as three numbers from 0 to 1.

## Multiple lines

If you want your text to span multiple lines, use `\n` as part of the string. The following example has two separate lines of text:

```ts
TextShape.create(sign,{
    text: "This is one line. \nThis is another line"
  })
```

You can also set up the following properties related to texts with multiple lines:

- `lineCount`: _number_. How many lines of text to fit into the textbox as a maximum. By default _1_. The `textWrapping` property must be _true_ to use more than one line.
- `lineSpacing`: _string_. How much space between each line, expressed as a string. For example "30px".
