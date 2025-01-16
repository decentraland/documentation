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
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity
		uiTransform={{
			width: '200px',
			height: '100px',
			justifyContent: 'center',
			alignItems: 'center',
		}}
		uiBackground={{ color: Color4.Green() }}
	/>
))
```

## Positioning properties

The alignment of UI entities is based on the Flexbox alignment model. This is a very powerful model for dynamically organizing nested entities inside modals that may vary in size.

{{< hint info >}}
**💡 Tip**: Decentraland's UI implementation is based on that of [Yoga](https://yogalayout.com/docs/). Read [this article](https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/) for a very approachable and in-depth coverage of the properties available in Flexbox.
{{< /hint >}}

### Entity size

Use `width` and `height` to set the size of the entity. The following kinds of values are supported:

- `auto`: The size adapts to fit the content inside. This is very convenient for text that may vary in length. Write the value as "auto".
- **Percentage**: As a percentage of the parent's measurements. Write the value as a string that ends in "%", for example `10 %`.
- **Pixels**: Write the value as a number.
- **Screen width or height**: Use vw (view width) and vh (view height) can be used to indicate a fraction of the full size of the window running Decentraland. For example `10vw` refers to 10% of the window's width, `25vh` to 25% of the window's height.

Note that these properties affect the **default** size of that item, the size of the item before any flex grow and flex shrink calculations are performed. The final size may be interpreted differently based on the size of the parent entity, and the Flexbox properties that are set.

{{< hint warning >}}
**📔 Note**: In properties that support both numbers and strings, to set the value in pixels, write a number. To set these fields as a percentage of the parent's measurements, write the value as a string that ends in "%", for example `10 %`. You can also set a pixel value as a string by ending the string in `px`, for example `200px`.

- When values are expressed as a percentage, they're always in relation to the parent's container. If the entity has no parents, then the value is a percentage of the whole screen.
- If values are expressed in pixels, they are absolute, and not affected by the parent's scale.
- If values are expressed in `vh` or `vw`, they are a percentage of the full window, not affected by the parent's scale.

For the `auto` width/height to work, the following rules apply:

- The UiTransform that uses width/height as “auto” should have `alignSelf`: `“center”`/`“flex-start”`/`“flex-end”` OR `positionType: “absolute”`
- If the UiTransform of a child use `positionType: “absolute”`, the parent won’t adapt to its size/position
- If the UiTransform of a child uses any position overwrite, the parent won’t adapt to its size/position
  {{< /hint >}}

These other properties are also available to adjust size in a more advanced way:

- `maxWidth` and `maxHeight`: _number_ or string (like height and width). The maximum size that the entity may have.
- `minWidth` and `minHeight`: _number_ or string (like height and width). The minimum size that the entity may have. If the parent is too small to fit the minimum size of the entities, they will overflow from their parent.
- `flexBasis`: This is an axis-independent way of providing the default size of an item along the main axis. Setting the flex basis of a child is similar to setting the width of that child if its parent is a container with flex direction: row or setting the height of a child if its parent is a container with flex direction: column.

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity
		uiTransform={{
			alignSelf: 'center',
			alignContent: 'center',
			width: '80%',
			height: '30%',
			minWidth: 300,
			maxWidth: 2500,
			margin: { left: '10%', right: '10%' },
		}}
		uiBackground={{ color: Color4.Green() }}
	/>
))
```

<!--
TODO
examples:
```ts
``` -->

### Arranging child entities

By default, child entities are positioned in relation to the top-left corner of its parent. You can use properties like `justifyContent` and `alignItems` to change this behavior.

{{< hint info >}}
**💡 Tip**: Any properties that refer to _content_ refer to entities along the main axis (determined by `flexDirection`). Any properties that refer
{{< /hint >}}

- `flexDirection`: Flex direction controls the direction in which children of a node are laid out. This is also referred to as the main axis. The main axis is the direction in which children are laid out. The cross axis is the axis perpendicular to the main axis, or the axis which wrapping lines are laid out in. It takes its value from the `FlexDirectionType` type. The following options are available:

  - `row` (DEFAULT)
  - `row-reverse`
  - `column`
  - `column-reverse`

- `justifyContent`: This property describes how to align children within the main axis of their container. For example, you can use this property to center a child horizontally within a container with `flexDirection` set to row or vertically within a container with `flexDirection` set to column. The value of this property must be from the `AlignType` type. Possible values are:

  - `flex-start` (DEFAULT): Align children of a container to the start of the container's main axis.
  - `flex-end`: Align children of a container to the end of the container's main axis.
  - `center`: Align children of a container in the center of the container's main axis.
  - `space-between`: Evenly space of children across the container's main axis, distributing remaining space between the children.
  - `space-around`: Evenly space of children across the container's main axis, distributing remaining space around the children. Compared to space between using space around will result in space being distributed to the beginning of the first child and end of the last child.

- `alignItems`: Describes how to align children along the cross axis of their container. Align items is very similar to justify content but instead of applying to the main axis, align items applies to the cross axis. This property requires a value from the `AlignType` type. The following options are available:

  - `stretch`: (DEFAULT) Stretch children of a container to match the height of the container's cross axis.
  - `flex-start`: Align children of a container to the start of the container's cross axis.
  - `flex-end`: Align children of a container to the end of the container's cross axis.
  - `center`: Align children of a container in the center of the container's cross axis.
  - `baseline`: Align children of a container along a common baseline. Individual children can be set to be the reference baseline for their parents.

- `alignSelf`: Align self has the same options and effect as `alignItems` but instead of affecting the children within a container, you can apply this property to a single child to change its alignment within its parent. align self overrides any option set by the parent with align items. It takes its value from `AlignType`, see `alignItems` above for details on these options.

- `alignContent`: Align content defines the distribution of lines along the cross-axis. This only has effect when items are wrapped to multiple lines using `flexWrap`. It takes its value from the `AlignType` type. The following options are available:

  - `flex-start`: (DEFAULT) Align wrapped lines to the start of the container's cross axis.
  - `flex-end`: Align wrapped lines to the end of the container's cross axis.
  - `stretch`: Stretch wrapped lines to match the height of the container's cross axis.
  - `center`: Align wrapped lines in the center of the container's cross axis.
  - `space-between`: Evenly space wrapped lines across the container's main axis, distributing remaining space between the lines.
  - `space-around`: Evenly space wrapped lines across the container's main axis, distributing remaining space around the lines. Compared to space between using space around will result in space being distributed to the begining of the first lines and end of the last line.

- `flexGrow`: This describes how any space within a container should be distributed among its children along the main axis. After laying out its children, a container will distribute any remaining space according to the flex grow values specified by its children. Flex grow accepts any floating point value >= 0, with 0 being the default value. A container will distribute any remaining space among its children weighted by the child’s flex grow value.

- `flexShrink`: Describes how to shrink children along the main axis in the case that the total size of the children overflow the size of the container on the main axis. flex shrink is very similar to flex grow and can be thought of in the same way if any overflowing size is considered to be negative remaining space. These two properties also work well together by allowing children to grow and shrink as needed. Flex shrink accepts any floating point value >= 0, with 1 being the default value. A container will shrink its children weighted by the child’s flex shrink value.

- `overflow`: Determines what happens if the size of the children of an entity overflow its parent. It uses values from the `OverflowType` type.

  - `hidden`: Overflowing entities are made invisible.
  - `visible`: Overflowing entities break out of the margins of the parent.
  <!-- - `scroll`: The parent becomes scrollable, allowing to view the full extent of the children by scrolling.-->

- `flexWrap`: The flex wrap property is set on containers and controls what happens when children overflow the size of the container along the main axis. By default children are forced into a single line (which can shrink entities). If wrapping is allowed items are wrapped into multiple lines along the main axis if needed. wrap reverse behaves the same, but the order of the lines is reversed. This property takes its value from the `FlexWrapType` type.

  - `wrap`
  - `no-wrap`
  - `wrap-reverse`

<!--
TODO
examples:
```ts
``` -->

### Margins and padding

- `margin`: This property affects the spacing around the outside of a node. A node with margin will offset itself from the bounds of its parent but also offset the location of any siblings. The margin of a node contributes to the total size of its parent if the parent is auto sized. Set space between the entity and its parent's margins. The expected value is an object that contains the properties `top`, `left`, `bottom`, and `right`.
- `padding`: This property affects the size of the node it is applied to. Padding in Yoga acts as if box-sizing: border-box; was set. That is padding will not add to the total size of an entity if it has an explicit size set. For auto sized nodes padding will increase the size of the node as well as offset the location of any children. The expected value is an object that contains the properties `top`, `left`, `bottom`, and `right`.

<!--
TODO
examples:
```ts
``` -->

### Fine-tune position

In Flexbox, entity positions are mostly determined by how they are parented, and what arrangement properties are set on the parent and child. You often don't have to set the `position` property at all. But if you do want to tweak that, or completely override the normal flow of Flexbox and set an absolute position, here are the relevant properties:

- `positionType`: Defines how entities are positioned. It uses a value from the `PositionType` enum.

  - `relative`: (DEFAULT) By default an entity is positioned relatively. This means an entity is positioned according to the normal flow of the layout, and then offset relative to that position based on the values of `top`, `right`, `bottom`, and `left`. The offset does not affect the position of any sibling or parent entities.
  - `absolute`: When positioned absolutely, an entity doesn't take part in the normal layout flow. It is instead laid out independent of its siblings. The position is determined based on the `top`, `right`, `bottom`, and `left` values.

- `position`: The position values `top`, `right`, `bottom`, and `left` behave differently depending on the `positionType`. For a relative entity they offset the position of the entity in the direction specified. For absolute entity though these properties specify the offset of the entity's side from the same side on the parent. The expected value is an object that contains the properties `top`, `left`, `bottom`, and `right`.

{{< hint warning >}}
**📔 Note** : When measuring from the top, the numbers for `position` should be negative. Example: to position a component leaving a margin of 20 pixels with respect to the parent on the top and left sides, set `position` to 20, -20.
{{< /hint >}}

<!--
TODO
examples:
```ts
``` -->

### Visibility

- `display`: Determines is an entity is visible or not. To make an entity invisible, set `display` to `none`.

<!--
TODO
examples:
```ts
``` -->

## Responsive UI size

Players with different screen sizes may see your UI layout differently. If you set the size of any UI element to a fixed number of pixels, this UI may look too small to read on retina displays, that have a much higher pixel density.

Instead of positioning and scaling UI elements in terms of screen percentages, you can also obtain the canvas dimensions and then calculate the absolute positions and sizes following your own custom logic. For example, you could chose different dialog arrangements depending on the screen size.

To obtain information about the screen's dimension, you can check the `UiCanvasInformation`, that's added by default to the scenes's root entity.

The `UiCanvasInformation` component holds the following information:

- `height`: Canvas height in pixels
- `width`: Canvas width in pixels
- `devicePixelRatio`: The ratio of the resolution in physical pixels in the device to the pixels on the canvas
- `interactableArea`: A `rect` object, detailing the size of the area designated for scene UI elements. This object contains the following fields:
  - `height`: Height of interactable area
  - `width`: Width of interactable area
  - `x`: Leftmost x position of the interactable area
  - `y`: Lowest y position of the interactable area

```ts
export function Main(){
  let canvas = UiCanvasInformation.get(engine.RootEntity)
	console.log("CANVAS DIMENSIONS: ", canvas.width, canvas.height)
})
```

The following snippet continually calculates a multiplier value based on the screen size:

```ts
import { engine, UiCanvasInformation } from "@dcl/sdk/ecs"

let timer = 0
let canvasInfoTimer = 0.5
export let scaleFactor = 1

export function UIScaleUpdate() {

  engine.addSystem((dt) => {
    timer += dt

    if (timer <= canvasInfoTimer) return
    timer = 0

    const uiCanvasInfo = UiCanvasInformation.getOrNull(engine.RootEntity)

    if (!uiCanvasInfo) return

    const newScaleFactor = Math.min(uiCanvasInfo.width / 1920, uiCanvasInfo.height / 1080)

    if (newScaleFactor !== scaleFactor) {
      scaleFactor = newScaleFactor
      console.log('NEW UI scaleFactor: ', scaleFactor)
    }
  })
}
```

The value of the `scaleFactor` variable, that this function updates, can then be used as a multiplier on any UI element in the scene, including `heigh`, `width` and `fontSize` values.

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'
import { scaleFactor } from './calculate-scale-factor'

ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity
		uiTransform={{
			width: 200 * scaleFactor,
			height: 100 * scaleFactor,
			justifyContent: 'center',
			alignItems: 'center',
			padding: 4 * scaleFactor
		}}
		uiBackground={{ color: Color4.Green() }}
	>
	  	<Label
		        value={description}
		        fontSize={18 * scaleFactor}
		        textAlign="middle-center"
		        uiTransform={{
		          width: "auto",
		          height: "auto",
		          alignSelf: "center",
		          margin: { top: 10 * scaleFactor, bottom: 10 * scaleFactor },
		        }}
	      />
	</UiEntity>
))
```

Some other best practices regarding UI sizes:

- If the width or height of any UI element is dynamic, it's good to also use the `maxWidth`, `minWidth`, `maxHeight`, and `minHeight` parameters to make sure they stay within reasonable values.
- The font size of text is relative to a fixed number of pixels, you should make it dynamic so it remains readable on retina displays. See [Responsive text size]({{< ref "/content/creator/sdk7/2d-ui/ui_text.md#responsive-text-size">}})

