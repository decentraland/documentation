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

{{< hint warning >}}
**📔 Note**:  You can only define JSX UI syntax in files that have a `.tsx` extension. `.tsx` files support everything that `.ts` files support, plus UI syntax. We recommend creating a `.ui.tsx` file and defining your UI there.
{{< /hint >}}

A simple UI with static elements can look a lot like HTML, but when you add dynamic elements that respond to a change in state, you can do things that are a lot more powerful.

The default Decentraland explorer UI includes a chat widget, a map, and other elements. These UI elements are always displayed on the top layer, above any scene-specific UI. So if your scene has UI elements that occupy the same screen space as these, they will be occluded.

See [UX guidelines]({{< ref "/content/creator/sdk7/design-experience/ux-ui-guide.md" >}}) for tips on how to design the look and feel of your UI.

<!-- TODO: Should I call it JSX? any better name?? -->

When the player clicks the _close UI_ button, on the bottom-right corner of the screen, all UI elements go away.


## Render a UI

To display a UI in your scene, use the `ReactEcsRenderer.setUiRenderer()` function, passing it a valid structure of entities, described in JSX.

Each entity is defined as an HTML-like node, with properties for each of its components.

```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

export const uiMenu = () => (
	<UiEntity
		uiTransform={{
			width: 700,
			height: 400,
			margin: { top: '35px', left: '500px' }
		}}
		uiBackground={{ color: Color4.Red() }}
	/>
)

ReactEcsRenderer.setUiRenderer(uiMenu)
```

You can also define an entity structure and render it, all in one same command.

```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity
		uiTransform={{
			width: 700,
			height: 400,
			margin: { top: '35px', left: '500px' }
		}}
		uiBackground={{ color: Color4.Red() }}
	/>
))
```

{{< hint warning >}}
**📔 Note**:  All of your UI elements need to be nested into the same structure, and have one single parent at the root of the structure. You can only call `ReactEcsRenderer.setUiRenderer()` once in the scene.
{{< /hint >}}

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
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
	// parent entity
	<UiEntity
		uiTransform={{
			width: 200,
			height: 200,
			margin: { top: '250px', left: '500px' }
		}}
		uiBackground={{ color: Color4.Blue() }}
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







