---
date: 2025-01-07
title: Subscribe to changes
description: Detect changes in a component and run functions on every change
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/subscribe-to-changes/
weight: 5
---

A neat way to write your code is to subscribe to events, and running a function any time that event happens.

A number of [Event listeners]({{< ref "/content/creator/sdk7/interactivity/event-listeners.md" >}}) come predefined as part of the SDK, but you can also use the `onChange()` method on any component to achieve the same. This also works with any [Custom Component]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}) that you defined, without needing any extra work.

For example, the following function checks the `AvatarEquippedData` component on the player entity, and runs a function if the player change any of their equipped wearables or emotes. The new values of the component are passed on the function's arguments.

```ts
import { AvatarEquippedData } from '@dcl/sdk/ecs'

export function main() {
	AvatarEquippedData.onChange(engine.PlayerEntity, (equipped) => {
		if (!equipped) return
		console.log('New wearables list: ', equipped.wearableUrns)
		console.log('New emotes list : ', equipped.emoteUrns)
	})
}
```

Thanks to the `onChange()` method, it's not necessary to create a system and iteratively check for new values on every frame, it greatly simplifies this very common use case.

{{< hint warning >}}
**📔 Note**: Do not use `onChange()` inside a System, as that would subscribe a new copy of the function on every frame of the game loop, and could potentially lead to crashes.
{{< /hint >}}

The same method works out-of-the-box with [Custom Component]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}). For example:

```ts
// define component
export const MyComponent = engine.defineComponent('myComponent', {
	value1: Schemas.Boolean,
	value2: Schemas.Float,
})

// Usage
export function main() {
	// Create entities
	const myEntity = engine.addEntity()

	// Create instances of the component
	MyComponent.create(myEntity, {
		value1: true,
		value2: 10,
	})

	// Subscribe to changes
	MyComponent.onChange(myEntity, (componentData) => {
		if (!componentData) return
		console.log(componentData.value1)
		console.log(componentData.value2)
	})
}
```

You can also combine this approach with [Querying components]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}), to bulk-subscribe every entity in the scene that has a certain component to their own function.

```ts
export function main() {
	for (const [entity] of engine.getEntitiesWith(MyComponent)) {
		MyComponent.onChange(entity, (componentData) => {
			if (!componentData) return
			console.log(componentData.value1)
			console.log(componentData.value2)
		})
	}
}
```

Note that this approach will only subscribe to `onChange()` for entities that exist at the start of the scene, for example entities created via the UI of the [Creator Hub]({{< ref "/content/creator/scene-editor/get-started/about-editor.md" >}}).

{{< hint info >}}
**💡 Tip**: If you prefer to instead handle events that are not necessarily related to a component changing, we recommend importing the TypeScript library [Mitt](https://www.npmjs.com/package/mitt) into your scene. This library offers simple functions to emit and listen to events.
{{< /hint >}}
