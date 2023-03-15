
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
	**📔 Note**:  To click on a UI component, players must first unlock the cursor from the view control. They do this by pressing the _right mouse button_ and keeping it pressed, or by hitting `Esc`.
	{{< /hint >}}
- `onMouseUp`: A similar callback function that runs every the pointer button is raised while pointing at the entity. This could be used for example to build a drag-and-drop mechanic on your UI.
- `variant`: Use this property to set the style of the button as one of the defaults. `primary` and `secondary` are available.
- `color`: Background color of the button.
- `font`: Font of the text on the button.
- `textAlign`: Alignment of the text inside the button
- `uiTransform`: Positioning properties of the UI element.
<!-- - `disabled`: -->


The following example shows how to create a clickable UI button.

```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	<Button
		value= "Click me"
		variant= 'primary'
		uiTransform={{ width: 100, height: 100 }}
		variant={{ color: Color4.Green() }}
		onMouseDown={() => { console.log("Clicked on the UI") } }
	/>
))
```

You can also write the function that is executed by the click outside the UI definition, and reference it by name. This helps keep the UI code more readable, and is also useful if multiple clickable UI entities need to call the same function.

```ts
function handleClick() {
	// Do something onClick
	console.log("Clicked on the UI")
}
ReactEcsRenderer.setUiRenderer(() => (
	<Button
		value= "Click me"
		uiTransform={{ width: 100 }}
		onMouseDown={{ handleClick }}
	/>
))
```

## Button styling

Set the variant to `primary` or `secondary` to take advantage of the default styling options for buttons. `primary` makes your button red with white text, `secondary` makes your button white with red text.

```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity
		uiTransform={{
			width: 500,
			height: 230,
			margin: '16px 0 8px 270px',
			padding: 4,
			alignSelf: 'center'
		}}
		uiBackground={{ color: Color4.Gray() }}
	>
		<Button
			value="Click Me"
			variant='primary'
			uiTransform={{ width: 80, height: 20, margin: 4 }}
			onMouseDown={() => { console.log("Clicked on the UI") }}
		/>
		<Button
			value="Click Me"
			variant='secondary'
			uiTransform={{ width: 80, height: 20, margin: 4 }}
			onMouseDown={() => { console.log("Clicked on the UI") }}
		/>
	</UiEntity >
))
```

You're also free to use all of the properties on background freely. You can also set a variant and then override some of its properties.


## Making other elements clickable

Any element in the UI can be made clickable by adding an `onMouseDown` property to it, it works identically to a button. The following example adds `onMouseDown` properties to background images and text.


```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
    <UiEntity
	  onMouseDown={() => {console.log('Background clicked!')}}
      uiTransform={{
        width: 400,
        height: 230,
      }}
      uiBackground={{ color: Color4.create(0.5, 0.8, 0.1, 0.6) }}
    >
	    <Label
          onMouseDown={() => {console.log('Label clicked!')}}
          value={`Player: ${getPlayerPosition()}`}
          fontSize={18}
          uiTransform={{ width: '100%', height: 30 } }
        />
    </UiEntity>
))
```


<!--

TODO: children of an entity with OnClick aren't clickable too, right?

TODO: is there an euqivalent to isPointerBlocker?



