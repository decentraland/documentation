---
date: 2022-10-28
title: UI special types
description: Special entitiy types for the UI, including dropdowns and input boxes.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/ui-special-elements/
weight: 10
---

There are certain special entity types that allow for some special kinds of interactions.

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


## Input text


Create an `Input` entity to allow users to to type in text. Players must first click on this box before they can write into it.

A `Input` entity must have at least the following properties:

- `onChange`: A function that is executed every time that a value in the input text is changed. As the player types into the box, this function is executed once for each character that is added or removed.


It can also include the following properties, most of them similar to those present in `Label` entities:


- `placeHolder`: String to display before the player starts inputing anything. It's useful to make this text a hint about what they should write.
- `placeHolderColor`: The color to use for the placeholder text, as a [Color4]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md">}}). 
Normally use a paler shade of the color of text that the player writes.
- `fontSize`: The size of the text, as a number.
	> NOTE: The `fontSize` is not affected by the size of its entity or parent entities.
- `color`: The color of the text the player writes, as a [Color4]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md">}}).
 Make sure you use a different color from the `placeHolderColor`.
- `font`: The font to use, taking a value from the `Font` enum. Supported values are:
	- `Font.T_SERIF`
	- `Font.T_SANS_ERIF` _(default)_
	- `Font.T_MONOSPACE`
- `textAlign`: How the text will align with its parent. It takes a value from the `TextAlignMode` enum. 


You can also configure other comopnents of the `Dropdown` entity, like a `uiTransform`, `OnMouseDown` as in other UI entities.



