---
date: 2022-10-28
title: UI Button events
description: Handle button events on UI entities.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/ui-button-events/
weight: 3
---

To make a button in your UI, create a `Button` UI element. The button must have the following:

- `value`: A string with the text to display on the button.

It can also have:

- `onMouseDown`: A callback function that runs every time the user pushes the pointer button on the entity.
  {{< hint warning >}}
  **📔 Note**: To click on a UI component, players must first unlock the cursor from the view control. They do this by pressing the _right mouse button_ and keeping it pressed, or by hitting `Esc`.
  {{< /hint >}}
- `onMouseUp`: A similar callback function that runs every the pointer button is raised while pointing at the entity.
- `variant`: Use this property to set the style of the button as one of the defaults. `primary` and `secondary` are available.
- `disabled`: Boolean to set a button disabled. When disabled is set to _true_, the `onMouseDown` and `onMouseUp` actions are no longer called. Also the `apha` value of the color of both the text and the backgroun is halved, so the button is "grayed-out" and stands out less.
- `color`: Background color of the button.
- `font`: Font of the text on the button.
- `textAlign`: Alignment of the text inside the button
- `uiTransform`: Positioning properties of the UI element.
- `uiBackground`: Set the color or texture of the UI element. 

The following example shows how to create a clickable UI button.

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <Button
    value="Click me"
    variant="primary"
    uiTransform={{ width: 100, height: 100 }}
    onMouseDown={() => {
      console.log('Clicked on the UI')
    }}
  />
))
```

You can also write the function that is executed by the click outside the UI definition, and reference it by name. This helps keep the UI code more readable, and is also useful if multiple clickable UI entities need to call the same function.

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

function handleClick() {
  // Do something onClick
  console.log('Clicked on the UI')
}
ReactEcsRenderer.setUiRenderer(() => (
  <Button
    value="Click me"
    uiTransform={{ width: 100 }}
    onMouseDown={{ handleClick }}
  />
))
```

## Button styling

Set the variant to `primary` or `secondary` to take advantage of the default styling options for buttons. `primary` makes your button red with white text, `secondary` makes your button white with red text.

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: 500,
      height: 230,
      margin: '16px 0 8px 270px',
      padding: 4,
      alignSelf: 'center',
    }}
    uiBackground={{ color: Color4.Gray() }}
  >
    <Button
      value="Click Me"
      variant="primary"
      uiTransform={{ width: 80, height: 20, margin: 4 }}
      onMouseDown={() => {
        console.log('Clicked on the UI')
      }}
    />
    <Button
      value="Click Me"
      variant="secondary"
      uiTransform={{ width: 80, height: 20, margin: 4 }}
      onMouseDown={() => {
        console.log('Clicked on the UI')
      }}
    />
  </UiEntity>
))
```

You're also free to use all of the properties on background freely. You can also set a variant and then override some of its properties. This example uses the `primary` variant, but overrides the color to be green:

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <Button
      value="My Button!"
      variant="primary"
      uiTransform={{ width: 100, height: 100 }}
      onMouseDown={() => {
        console.log('Clicked on My Button!')
      }}
      uiBackground={{
      color : Color4.Green()
      }}
  />
))
```

## Togglable buttons

A common use case is to make a button toggle between two states, like a switch. The example below switches between two colors each time the button is pressed:

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

let buttonEnabled = false

ReactEcsRenderer.setUiRenderer(() => (
  <Button
      value="My Button"
      variant="primary"
      uiTransform={{ width: 100, height: 100 }}
      onMouseDown={() => {
        console.log('Clicked on My Button!')
        buttonEnabled = !buttonEnabled
        if(buttonEnabled){
          // do something
        } else {
          // do something else
        }
      }}
      uiBackground={{
        color : buttonEnabled ? Color4.Green() : Color4.Red()
      }}
    />
))
```

Note that in the example above, the color depends on a `buttonEnabled` variable. Whenever this variable's value changes, it inmediately affects the background color.

## Making other elements clickable

Any element in the UI can be made clickable by adding an `onMouseDown` property to it, it works identically to a button. The following example adds `onMouseDown` properties to background images and text.

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    onMouseDown={() => {
      console.log('Background clicked!')
    }}
    uiTransform={{
      width: 400,
      height: 230,
    }}
    uiBackground={{ color: Color4.create(0.5, 0.8, 0.1, 0.6) }}
  >
    <Label
      onMouseDown={() => {
        console.log('Label clicked!')
      }}
      value={`Player: ${getPlayerPosition()}`}
      fontSize={18}
      uiTransform={{ width: '100%', height: 30 }}
    />
  </UiEntity>
))
```

## Pointer blocking

All UI entities are non-pointer blocking by default. If an entity has an `onMouseDown`, then it becomes pointer blocking.

You can change this default behavior by changing the value of the `pointerFilter` property on the `uiTransform` component on any UI entity. For example to set an entity that has no `onMouseDown` to be pointer blocking.

The supported values for `pointerFilter` are:

- `block`: The UI element is pointer blocking, players can't click on anything behind this UI element.
- `none`: The UI element is non-pointer blocking. The element is not clickable and anything behind it can be clicked.
