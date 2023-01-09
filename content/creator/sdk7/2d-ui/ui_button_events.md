
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


Make a UI entity clickable by giving it an `onMouseDown` component. The `onMouseDown` component references a function that runs every time the user pushes the pointer button on the entity. There's also a similar `onMouseUp` component, that detects when the button is raised while pointing at the entity.


> Note: To click on a UI component, players must first unlock the cursor from the view control. They do this by pressing the _right mouse button_ and keeping it pressed, or by hitting `Esc`.

The following example shows how to create a clickable UI entity. 

```ts
ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity 
		uiTransform = {{ width: 100, height: 100 }} 
		uiBackground={{ backgroundColor: Color4.Green() }}
		onMouseDown = { ()=>{ console.log("Clicked on the UI")} } 
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
	<UiEntity 
		uiTransform = {{ width: 100 }} 
		onClick = {{handleClick}} 
	/>
))
```




<!--

TODO: children of an entity with OnClick aren't clickable too, right?

TODO: is there an euqivalent to isPointerBlocker?

> Tip: If you want to add text over a button, keep in mind that the text needs to have the `isPointerBlocker` property set to `false`, otherwise players might be clicking the text instead of the button.
 -->

## Dropdown

Create a `Dropdown` entity to allow users to expand and select an item from a list.

A `Dropdown` entity must have at least the following properties:

- `options`: What values to display when the dropdown is expanded. Provide an object containting an arraw with a string value for each option. The first value in the array is displayed as the default option.
- `onChange`: A function that is executed every time that a value is selected in the dropdown, using 

You can also configure other comopnents of the `Dropdown` entity, like a `uiTransform`, as in other UI entities.

```ts
function selectOption(index: number) {
  switch(index){
    case 0:
      textColor = Color4.Red()
      break
    case 1:
      textColor = Color4.Blue()
      break
    case 2:
      textColor = Color4.Green()
      break
  } 
}

let textColor: Color4Type = Color4.Red()

ReactEcsRenderer.setUiRenderer(() => {
  return (
    <UiEntity
      uiTransform={{
        width: "200px",
        height: "100px",
        alignContent: YGAlign.YGA_AUTO,
        flexDirection: YGFlexDirection.YGFD_COLUMN,
        alignSelf: YGAlign.YGA_CENTER

      }}
    >
      <Label value="Select a color"  
        fontSize={18} 
        color={textColor}
        uiTransform={{
          width: "140px",
          height: "40px",
        }}
      />
      <Dropdown 
        options= {[`Red`, `Blue`, `Green`]}
        onChange={selectOption} 
        uiTransform={{
          width: "100px",
          height: "40px",
        }}
      />
    </UiEntity>
  )
})

```
<!-- 
## Input box

TODO -->