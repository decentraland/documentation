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
  - `serif`
  - `sans-serif` _(default)_
  - `monospace`
- `textAlign`: How the text will align with its parent. It takes a value from the `TextAlingType` type. TextAlignType = 'top-left' | 'top-center' | 'top-right' | 'middle-left' | 'middle-center' | 'middle-right' | 'bottom-left' | 'bottom-center' | 'bottom-right';
- `textWrap`: If the text uses line-breaks to ensure it all fits in the maximum width allowed. It takes a value from the `TextWrap` type: 'TW_WRAP' | 'TW_NO_WRAP'

{{< hint warning >}}
**📔 Note**: The `fontSize` is not affected by the size of its entity or parent entities.
{{< /hint >}}

A `Label` entity can also have other common components found on other types of UI entities, like `uiTransform` and `uiBackground`.

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity uiTransform={{ width: 'auto', height: 'auto' }}>
		<Label
			value="This is a label"
			color={Color4.Red()}
			fontSize={29}
			font="serif"
			textAlign="top-left"
		/>
	</UiEntity>
))
```

<!-- TODO: examples with textAlign -->

If a line of text is too long to fit in the assigned width, or the maximum width of its container, the text will continue on the next line. You can disable this by changing the value of the `textWrap` property.

You can also force a line break by explicitly adding `\n` to the string.

```ts
import { ReactEcsRenderer } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity uiTransform={{ width: 700, height: 400 }}>
		<Label value="Hello World!\nThis other bit is quite long. It probably won't fit in a single line, so it will include a line break somewhere.\nFourth line" />
	</UiEntity>
))
```

If no explicit `height` or `width` is set on the `uiTransform` of the container, the container will use the value `auto`, which adjusts to fit all the text. You can set a `maxWidth` and a `maxHeight` to ensure it doesn't exceed certain limits. You can also use `minWidth` and `minHeight` to ensure the container does't grow too small, even if the text is shorter.

```ts
import { ReactEcsRenderer, UiEntity } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity
		uiTransform={{
			minWidth: 100,
			maxWidth: 300,
			height: 'auto',
			alignSelf: 'center',
			padding: 10,
		}}
		uiBackground={{
			color: Color4.Red(),
		}}
		uiText={{
			value: 'Hello world!',
			fontSize: 18,
		}}
	/>
))
```

## Responsive text size

Use the `scaleFontSize()` function to provide font values that adjust to the player's screen size. When setting the `fontSize` property of a text UI entity, pass this function instead of a single number.

```ts
import { ReactEcsRenderer, UiEntity } from '@dcl/sdk/react-ecs'
import { scaleFontSize } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: 'auto',
      height: 'auto',
      alignSelf: 'center',
      padding: 10,
    }}
    uiText={{
      value: 'Hello world!',
      fontSize={scaleFontSize(15)}
    }}
  />
))
```

The `scaleFontSize()` function requires two parameters:

- `fontSize`: The base font size to use.
- `scaleUnit` _(optional)_: The scaling factor. This determines if the text should be adjusted based on the screen width or the height, and a multiplier for how much to adapt. Default: `"0.39vh"`. Values can be:
  - _Number_: A simple number, in this case it gets interpreted as relative to _width_
  - _String ending in **vw**_: This makes the number relative to the view width. For example `"0.8vw"`
  - _String ending in **vh**_: This makes the number relative to the view height. For example `"0.8vh"`

{{< hint info >}}
**💡 Tip**: This function works similar to the CSS `calc()` function.
{{< /hint >}}

The value of `scaleUnit` is a percentage of the window's width or height. So a `scaleUnit` of `"100vw"` is 100% of the width of the screen, a value of `"0.5vw"` is 0.5% of the width of the screen.

The formula that `scaleFontSize()` follows is it multiples the screen width or height by the `scaleUnit` and adds to that the `fontSize` passed in the first parameter.

```ts
final font = fontSize + (screen width * scaleUnit / 100 )
```

For example, in the snippet below uses a `scaleUnit` value of 0.8. If the screen width is _1280px_ that will result in text of size of **26.84**, having followed the equation `15 + (1280 * 0.8 / 100)`.

```ts
import { ReactEcsRenderer, UiEntity } from '@dcl/sdk/react-ecs'
import { scaleFontSize } from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: 'auto',
      height: 'auto',
      alignSelf: 'center',
      padding: 10,
    }}
    uiText={{
      value: 'Hello world!',
      fontSize={scaleFontSize(15, 0.8)}
    }}
  />
))
```

{{< hint info >}}
**💡 Tip**: If you don't have different screen sizes to test, you can try resizing the window where you run the preview. The text will adjust instantly every time you change the window.
{{< /hint >}}
