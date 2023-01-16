---
date: 2022-10-28
title: UI Text
description: Write text in UI entities.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/ui-text/
weight: 3
---


Ad text to your UI by creating a `Label` entity.

A `Label` entity has the following fields that can be configured:

- `value`: The string to display
- `fontSize`: The size of the text, as a number.
	> NOTE: The `fontSize` is not affected by the size of its entity or parent entities.
- `color`: The color of the text, as a [Color4]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md">}}).
- `font`: The font to use, taking a value from the `Font` enum. Supported values are:
	- `Font.T_SERIF`
	- `Font.T_SANS_ERIF` _(default)_
	- `Font.T_MONOSPACE`
- `textAlign`: How the text will align with its parent. It takes a value from the `TextAlignMode` enum. 

<!-- TODO: what value for font?? (not the same as text)
what about text align, TextAlignMode not valid either -->

A `Label` entity can also have other common components found on other types of UI entities, like `uiTransform` and `uiBackground`.



```ts
ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: 700,
      height: 400
    }}
  >
	<Label 
		value="This is a label" color={Color4.Red()} 
		fontSize={29} 
		font={Font.F_SANS_SERIF}
        textAlign={TextAlignMode.TAM_TOP_LEFT}
	/>
  </UiEntity>
))
```

<!-- TODO: examples with textAlign -->



For multi-line text, you can add line breaks into the string, using `\n`.

```ts
ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: 700,
      height: 400
    }}
  >
	<Label
		value:  "Hello World,\nthis message is quite long and won't fit in a single line.\nI hope that's not a problem."
	/>
  </UiEntity> 
))
```