---
date: 2018-02-15
title: 2D UI
description: Learn how to create a UI for players in your scene. This is useful, for example, to display game-related information.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/onscreen-ui/
weight: 1
---


You can build a UI for your scene, to be displayed in the screen's fixed 2D space, instead of in the 3D world space.

UI elements are only visible when the player is standing inside the scene's LAND parcels, as neighboring scenes might have their own UI to display. Parts of the UI can also be triggered to open when certain events occur in the world-space, for example if the player clicks on a specific place.

Build a UI by defining a structure of `UIEntity` in JSX. The syntax used for UIs is very similar to that of [React](https://reactjs.org/) (a very popular javascript-based framework for building web UIs).

> Note: You can only define JSX UI syntax in files that have a `.tsx` extension. `.tsx` files support everything that `.ts` files support, plus UI syntax. We recommend creating a `.ui.tsx` file and defining your UI there. 

A simple UI with static elements can look a lot like HTML, but when you add dynamic elements that respond to a change in state, you can do things that are a lot more powerful.

The default Decentraland explorer UI includes a chat widget, a map, and other elements. These UI elements are always displayed on the top layer, above any scene-specific UI. So if your scene has UI elements that occupy the same screen space as these, they will be occluded.

See [UX guidelines]({{< ref "/content/creator/sdk7/design-experience/ux-ui-guide.md" >}}) for tips on how to design the look and feel of your UI.

<!-- TODO: Should I call it JSX? any better name?? -->

When the player clicks the _close UI_ button, on the bottom-right corner of the screen, all UI elements go away.


## Render a UI

To display a UI in your scene, use the `renderUi()` function, passing it a valid structure of entities, described in JSX.

Each entity is defined as an HTML-like node, with properties for each of its components.

```ts
export const uiMenu = () => (
	<UiEntity
		uiTransform={{
			width: 700,
			height: 400,
			margin: { top: '35px', left: '500px' }
		}}
		uiBackground={{ backgroundColor: Color4.Red() }}
	/>
)

renderUi(uiMenu)
```

You can also define an entity structure and render it, all in one same command.

```ts
renderUi(() => (
	<UiEntity
		uiTransform={{
			width: 700,
			height: 400,
			margin: { top: '35px', left: '500px' }
		}}
		uiBackground={{ backgroundColor: Color4.Red() }}
	/>
))
```

> Note: All of your UI elements need to be nested into the same structure, and have one single parent at the root of the structure. You can only call `renderUi()` once in the scene.

## UI Entities

Each element in the UI must be defined as a separate `UiEntity`, wether it's an image, text, an invisible alignment box, etc. Just like in the scene's 3D space, each `UiEntity` has its own components to give it a position, color, etc.

The React-like syntax allows you to specify each component as a property within the `UiEntity`, this makes the code shorter and more readable.

The components used in a `UiEntity` are different from those used in regular entities. You cannot apply a UI component to a regular entity, nor a regular component to a UI entity.

The following components are available to use in the UI:

- `uiTransform`
- `uiBackground`
- `uiText`
- `onClick`

Like with HTML tags, you can define components as self-closing or nest one within another.

```ts
renderUi(() => (
	// parent entity
	<UiEntity
		uiTransform={{
			width: 200,
			height: 200,
			margin: { top: '250px', left: '500px' }
		}}
		uiBackground={{ backgroundColor: Color4.Blue() }}
	>
		// self-closing child entity
		<UiEntity
			uiTransform={{
				width: 400,
				height: 400,
				margin: { top: '35px', left: '500px' }
			}}
			uiText={{ value: `Hello world!`, fontSize: 40 }}
		/>
	// closing statement for the parent entity
	</UiEntity>
))
```

A JSX statement can only have one parent-level entity. You can define as many other entities as you want, but they must all fit inside a structure with one single parent at the top.

TODO: Can I have multiple JSX statements in a scene?







<!-- 
## Images from an image atlas

TODO: Wait for textures in UI

You can use an image atlas to store multiple images and icons in a single image file. You then display rectangular parts of this image file in your UI based on pixel positions, pixel width, and pixel height inside the source image.

Below is an example of an image atlas with multiple icons arranged into a single file.

![](/images/media/UI-atlas.png)

The `UIImage` component has the following fields to crop a sub-section of the original image:

- `sourceTop`: the _y_ coordinate, in pixels, of the top of the selection
- `sourceLeft`: the _x_ coordinate, in pixels, of the left side of the selection.
- `sourceWidth`: the width, in pixels, of the selected area
- `sourceHeight`: the height, in pixels, of the selected area

When constructing a `UIImage` component, you must pass a `Texture` component as an argument. Read more about `Texture` components in [materials]({{< ref "/content/creator/sdk7/3d-essentials/materials.md" >}}).

```ts
let imageAtlas = "images/image-atlas.jpg"
let imageTexture = new Texture(imageAtlas)

const canvas = new UICanvas()

const playButton = new UIImage(canvas, imageTexture)
playButton.sourceLeft = 26
playButton.sourceTop = 128
playButton.sourceWidth = 128
playButton.sourceHeight = 128

const startButton = new UIImage(canvas, imageTexture)
startButton.sourceLeft = 183
startButton.sourceTop = 128
startButton.sourceWidth = 128
startButton.sourceHeight = 128

const exitButton = new UIImage(canvas, imageTexture)
exitButton.sourceLeft = 346
exitButton.sourceTop = 128
exitButton.sourceWidth = 128
exitButton.sourceHeight = 128

const expandButton = new UIImage(canvas, imageTexture)
expandButton.sourceLeft = 496
expandButton.sourceTop = 128
expandButton.sourceWidth = 128
expandButton.sourceHeight = 128
```

You can change the texture being used by an existing `UIImage` component, set the `source` field.

```ts
playButton.source = imageTexture2
``` -->


<!-- 


## Input text

Input boxes can be added to the UI to provide a place to type in text. You add a text box with an `UIInputText` component. Players must first click on this box before they can write into it.

```ts
const canvas = new UICanvas()

const textInput = new UIInputText(canvas)
textInput.width = "80%"
textInput.height = "25px"
textInput.vAlign = "bottom"
textInput.hAlign = "center"
textInput.fontSize = 10
textInput.placeholder = "Write message here"
textInput.placeholderColor = Color4.Gray()
textInput.positionY = "200px"
textInput.isPointerBlocker = true

textInput.onTextSubmit = new OnTextSubmit((x) => {
  const text = new UIText(textInput)
  text.value = "<USER-ID> " + x.text
  text.width = "100%"
  text.height = "20px"
  text.vAlign = "top"
  text.hAlign = "left"
})
```

Here are some of the main properties you can set:

- `focusedBackground`: You can change the background color to indicate that the input box is currently selected. Use this field to set an alternative color.

- `placeholder`: Set placeholder text to display on the box by default.

- `placeholderColor`: Make the placeholder a different color, to tell it apart. You'll usually want to make it a paler shade of the color of text that the player writes.

When the player interacts with the component, you can use the following events to trigger the execution of code:

- `OnFocus()`: The player clicked on the UI component and has a cursor on it.
- `OnBlur()`: The player clicked away and the cursor is gone.
- `OnChanged()`: The player typed or deleted something to change the string on the component.
- `OnTextSubmit()`: The player hit the `Enter` key to submit this string.

```ts
textInput.onChanged = new OnChanged((data: { value: string }) => {
  inputTextState = data.value
})
``` 
-->

<!-- 
## Open the UI

You can have the code of your scene make the UI visible when specific events occurs, for example at the end of a game to display the final score.

To do this, simply set the `visible` property of the main `UICanvas` component that wraps the UI to _true_ or _false_.

If the UI is clickable, or has clickable parts, you should also set the `isPointerBlocker` property to _true_ or _false_, so that the player can freely click in the world space when the UI is not on the way.

The following code adds a cube to the world-space of the scene that opens the UI when clicked.

```ts
const uiTrigger = new Entity()
const transform = new Transform({
  position: new Vector3(5, 1, 5),
  scale: new Vector3(0.3, 0.3, 0.3),
})
uiTrigger.addComponent(transform)

uiTrigger.addComponent(
  new OnPointerDown(() => {
    canvas.visible = true
    canvas.isPointerBlocker = true
  })
)

MeshRenderer.create(myEntity, { box: {} })
engine.addEntity(uiTrigger)
```

Players can close the UI by clicking the icon on the top-right corner. Note that when closing the UI in this way, they won't see any more UI components appear in your scene, even if the code sets them to visible.

It's a good practice to add a button on your UI elements for closing them in a way that doesn't prevent other UI components from being visible in the future.

You might also want to close the UI automatically when a specific event occurs, for example when a new match of a game starts.

To do this, simply set the `visible` property of the main `UIScreenSpace` component that wraps the UI to _false_.

If the UI is clickable, or has clickable parts, you should also set the `isPointerBlocker` property to _false_, so that the player can freely click in the world space.

```ts
const canvas = new UICanvas()

const close = new UIImage(canvas, new Texture("icon.png"))
close.name = "clickable-image"
close.width = "120px"
close.height = "30px"
close.sourceWidth = 92
close.sourceHeight = 91
close.vAlign = "bottom"
close.isPointerBlocker = true
close.onClick = new OnClick(() => {
  log("clicked on the close image")
  canvas.visible = false
  canvas.isPointerBlocker = false
})
```


TODO:  How do I define a type and reuse it???



TODO: what is `key` for?  to give an element a searchable name?
-->


