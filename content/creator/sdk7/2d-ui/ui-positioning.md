
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

## Positioning properties

The alignment of UI entities is based on the Flexbox alignment model. This is a very powerful model for dynamically organizing nested entities inside modals that may vary in size.

> TIP: Decentraland's UI implementation is based on that of [Yoga](https://yogalayout.com/docs/). Read [this article](https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/) for a very approachable and in-depth coverage of the properties available in Flexbox.

### Arranging child entities

By default, child entities are positioned in relation to the top-left corner of its parent. You can use properties like `justifyContent` and `alignItems` to change this behavior.

> Tip: Any properties that refer to _content_ refer to entities along the main axis (determined by `flexDirection`). Any properties that refer 

- `flexDirection`: Flex direction controls the direction in which children of a node are laid out. This is also referred to as the main axis. The main axis is the direction in which children are laid out. The cross axis is the axis perpendicular to the main axis, or the axis which wrapping lines are laid out in. It takes its value from the `YGFlexDirection` enum. The following options are available:

	- `YGFlexDirection.YGFD_ROW` (DEFAULT)
	- `YGFlexDirection.YGFD_ROW_REVERSE`
	- `YGFlexDirection.YGFD_COLUMN` 
	- `YGFlexDirection.YGFD_COLUMN_REVERSE`


- `justifyContent`: This property describes how to align children within the main axis of their container. For example, you can use this property to center a child horizontally within a container with `flexDirection` set to row or vertically within a container with `flexDirection` set to column. The value of this property must be from the `YGJustify` enum. Possible values are:

	- `YGAlign.FLEX_START` (DEFAULT): Align children of a container to the start of the container's main axis.
	- `YGAlign.FLEX_END`: Align children of a container to the end of the container's main axis.
	- `YGAlign.CENTER`: Align children of a container in the center of the container's main axis.
	- `YGAlign.SPACE_BETWEEN`: Evenly space of children across the container's main axis, distributing remaining space between the children.
	- `YGAlign.SPACE_AROUND`: Evenly space of children across the container's main axis, distributing remaining space around the children. Compared to space between using space around will result in space being distributed to the beginning of the first child and end of the last child.
	- `YGAlign.SPACE_EVENLY`: Evenly distributed within the alignment container along the main axis. The spacing between each pair of adjacent items, the main-start edge and the first item, and the main-end edge and the last item, are all exactly the same.

- `alignItems`: Describes how to align children along the cross axis of their container. Align items is very similar to justify content but instead of applying to the main axis, align items applies to the cross axis. This property requires a value from the  `YGAlign` enum. The following options are available:

	- `YGAlign.YGA_STRETCH`: (DEFAULT) Stretch children of a container to match the height of the container's cross axis.

	- `YGAlign.YGA_FLEX_START`: Align children of a container to the start of the container's cross axis.

	- `YGAlign.YGA_FLEX_END`: Align children of a container to the end of the container's cross axis.

	- `YGAlign.YGA_CENTER`: Align children of a container in the center of the container's cross axis.

	- `YGAlign.YGA_BASELINE`: Align children of a container along a common baseline. Individual children can be set to be the reference baseline for their parents.

- `alignSelf`: Align self has the same options and effect as `alignItems` but instead of affecting the children within a container, you can apply this property to a single child to change its alignment within its parent. align self overrides any option set by the parent with align items. It takes its value from `YGAlign`, see `alignItems` above for details on these options.

- `alignContent`: Align content defines the distribution of lines along the cross-axis. This only has effect when items are wrapped to multiple lines using `flexWrap`. It takes its value from the `YGAlign` enum. The following options are available:

	- `YGAlign.YGA_FLEX START`: (DEFAULT) Align wrapped lines to the start of the container's cross axis.
	- `YGAlign.YGA_FLEX END`: Align wrapped lines to the end of the container's cross axis.
	- `YGAlign.YGA_STRETCH`: Stretch wrapped lines to match the height of the container's cross axis.
	- `YGAlign.YGA_CENTER`: Align wrapped lines in the center of the container's cross axis.
	- `YGAlign.YGA_SPACE_BETWEEN`: Evenly space wrapped lines across the container's main axis, distributing remaining space between the lines.
	- `YGAlign.SPACE_AROUND`: Evenly space wrapped lines across the container's main axis, distributing remaining space around the lines. Compared to space between using space around will result in space being distributed to the begining of the first lines and end of the last line.


- `flexWrap`: The flex wrap property is set on containers and controls what happens when children overflow the size of the container along the main axis. By default children are forced into a single line (which can shrink entities). If wrapping is allowed items are wrapped into multiple lines along the main axis if needed. wrap reverse behaves the same, but the order of the lines is reversed. This property takes its value from the `YGWrap` enum.

	- `YGWrap.YGW_WRAP`
	- `YGWrap.YGW_NO_WRAP`	
	- `YGWrap.YGW_WRAP_REVERSE`

<!-- 
TODO
examples:
```ts
``` -->

### Entity size

The following fields are available to configure the size of a UI entity. Note that all of these properties affect the **default** size of that item, the size of the item before any flex grow and flex shrink calculations are performed. The final size may be interpreted differently based on the size of the parent entity, and the Flexbox properties that are set.

In properties that support both numbers and strings, to set the value in pixels, write a number. To set these fields as a percentage of the parent's measurements, write the value as a string that ends in "%", for example `10 %`. You can also set a pixel value as a string by ending the string in `px`, for example `200px`. 

When values are expressed as a percentage, they're always in relation to the parent's container. If the entity has no parents, then the value is a percentage of the whole screen. If values are expressed in pixels, they are absolute, and not affected by the parent's scale.


- `width` and `height`: The size of the entity. To set these fields in pixels, write the value as a number. To set these fields as a percentage of the parent's measurements, write the value as a string that ends in "%", for example `10 %`.

- `maxWidth` and `maxHeight`: _number_ or string (like height and width). The maximum size that the entity may have.

- `minWidth` and `minHeight`: _number_ or string (like height and width). The minimum size that the entity may have. If the parent is too small to fit the minimum size of the entities, they will overflow from their parent.

- `flexBasis`: This is an axis-independent way of providing the default size of an item along the main axis. Setting the flex basis of a child is similar to setting the width of that child if its parent is a container with flex direction: row or setting the height of a child if its parent is a container with flex direction: column. 

- `flexGrow`: This describes how any space within a container should be distributed among its children along the main axis. After laying out its children, a container will distribute any remaining space according to the flex grow values specified by its children. Flex grow accepts any floating point value >= 0, with 0 being the default value. A container will distribute any remaining space among its children weighted by the child’s flex grow value.

- `flexShrink`: Describes how to shrink children along the main axis in the case that the total size of the children overflow the size of the container on the main axis. flex shrink is very similar to flex grow and can be thought of in the same way if any overflowing size is considered to be negative remaining space. These two properties also work well together by allowing children to grow and shrink as needed. Flex shrink accepts any floating point value >= 0, with 1 being the default value. A container will shrink its children weighted by the child’s flex shrink value.

- `overflow`: Determines what happens if the size of the children of an entity overflow its parent. It uses values from the `YGOverflow` enum.

	- `YGOverflow.YGO_HIDDEN`: Overflowing entities are made invisible.
	- `YGOverflow.YGO_VISIBLE`: Overflowing entities break out of the margins of the parent.
	- `YGOverflow.YGO_SCROLL`: The parent becomes scrollable, allowing to view the full extent of the children by scrolling.


<!-- TODO: Check that scrolling really works -->

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

- `positionType`: Defines how entities are positioned. It uses a value from the `YGPositionType` enum.

	- `YGPositionType.YGPT_RELATIVE`: (DEFAULT) By default an entity is positioned relatively. This means an entity is positioned according to the normal flow of the layout, and then offset relative to that position based on the values of `top`, `right`, `bottom`, and `left`. The offset does not affect the position of any sibling or parent entities.
	- `YGPositionType.YGPT_ABSOLUTE`: When positioned absolutely, an entity doesn't take part in the normal layout flow. It is instead laid out independent of its siblings. The position is determined based on the `top`, `right`, `bottom`, and `left` values.

- `position`: The position values `top`, `right`, `bottom`, and `left` behave differently depending on the `positionType`. For a relative entity they offset the position of the entity in the direction specified. For absolute entity though these properties specify the offset of the entity's side from the same side on the parent.  The expected value is an object that contains the properties `top`, `left`, `bottom`, and `right`.

> Note: When measuring from the top, the numbers for `position` should be negative. Example: to position a component leaving a margin of 20 pixels with respect to the parent on the top and left sides, set `position` to 20, -20.


<!-- 
TODO
examples:
```ts
``` -->


### Visibility

- `display`: Determines is an entity is visible or not. To make an entity invisible, set `display` to `YGDisplay.YGD_NONE`.


<!-- 
TODO
examples:
```ts
``` -->


