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

## uiText

Ad text to your UI by giving entities a `uiText` component.

The following fields can be configured:

- `value`: The string to display
- `fontSize`: The size of the text, as a number.
- `color`: The color of the text, as a [Color4]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md">}}).
- `font`: 
- `textAlign`: 

<!-- TODO: what value for font?? (not the same as text)
what about text align, TextAlignMode not valid either -->


> TIP: A single entity can have both `uiText` and `uiBackground` components.

> NOTE: The `fontSize` is not affected by the size of its entity or parent entities.

```ts
renderUi(() => (
  <UiEntity
    uiTransform={{
      width: 700,
      height: 400
    }}
    uiText={{ value: 'SDK 7', fontSize: 80, color: Color4.Red()  }}
  >
))
```

<!-- TODO: examples with textAlign -->



For multi-line text, you can add line breaks into the string, using `\n`.


```ts
renderUi(() => (
  <UiEntity
    uiText={{ 
		value:  "Hello World,\nthis message is quite long and won't fit in a single line.\nI hope that's not a problem." 
	}}
  >
))
```