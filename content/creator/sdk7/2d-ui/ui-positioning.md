
---
date: 2022-10-28
title: UI Positioning
description: Set the position, scale, padding and other properties of UI entities.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/ui-positioning/
weight: 3
---


For all kinds of UI content, use the `uiTransform` component to set the size, position, and other properties related to the entity's alignment.

The `uiTransform` component works in the screen's 2d space very much like the `Transform` component works in the the scene's 3D space.

```ts
ReactEcsRenderer.setUiRenderer(() => (
      <UiEntity
       uiTransform={{
          width: '200px',
          height: '100px',
          justifyContent: YGJustify.YGJ_CENTER,
          alignItems: YGAlign.YGA_CENTER,
        }}
        uiBackground={{ backgroundColor: Color4.Green() }}
      />
))
```

The following fields are available to configure:

- `width` and `height`: The size of the entity. To set these fields in pixels, write the value as a number. To set these fields as a percentage of the parent's measurements, write the value as a string that ends in "%", for example `10 %`.
- `justifyContent`: Value from the `YGJustify` enum. This property defines how to align children within a parent. Possible values are:

- `alignItems`: YGAlign.YGA_CENTER,
- `alignContent`:
- `alignSelf`:
- `direction`:
- `display`:YGDisplay.YGD_FLEX
- `flex`:
- `flexBasis`:
- `flexDirection`:
- `flexGrow`:
- `flexShrink`:
- `flexWrap`:
- `maxHeight`:
- `maxWidth`:
- `overflow`:
- `padding`:
- `position`:
- `positionType`:
- `margin`: An object that can contain the following properties.
	- `top`, `bottom`, `left`, and `right`:  Set space between the entity and its parent's margins.



> Note: In properties that support both numbers and strings, to set the value in pixels, write a number. To set these fields as a percentage of the parent's measurements, write the value as a string that ends in "%", for example `10 %`. You can also set a pixel value as a string by ending the string in `px`, for example `200px`. 

> TIP: Decentraland's UI implementation is based on that of [Yoga](https://yogalayout.com/docs/). You might find their documentation and support issues useful to troubleshoot UI in your Decentraland scenes.

When values are expressed as a percentage, they're always in relation to the parent's container. If the entity has no parents, then the value is a percentage of the whole screen. If values are expressed in pixels, they are absolute, and not affected by the parent's scale.

By default, child entities are positioned in relation to the top-left corner of its parent. You can use properties like `justifyContent` and `alignItems` to change this behavior.

> Tip: When measuring from the top, the numbers for `position` should be negative. Example: to position a component leaving a margin of 20 pixels with respect to the parent on the top and left sides, set `position` to 20, -20.

<!-- 
examples:
```ts
``` -->