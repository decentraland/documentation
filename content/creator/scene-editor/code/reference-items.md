---
date: 2024-07-25
title: Reference items in code
description: Reference items in your code by name or by tag.
categories:
  - scene-editor
type: Document
url: /creator/scene-editor/code/reference-items
weight: 2
---

You can reference items that are added via the Creator Hub drag-and-drop interface in your code. This is useful to add sophisticated behavior to those items, or to reference them from other parts of your code.

## Fetch by name

When using the Creator Hub and adding entities by dragging them into the canvas, each entity has a unique name. Use the
`engine.getEntityOrNullByName()` function to reference one of these entities from your code.

Use the `EntityNames` enum to easily access the names of the entities that you added via the Creator Hub, or write the name as a string as written on the scene's entity tree view in the Scene Editor.


```ts
import { EntityNames } from '../assets/scene/entity-names'

function main() {

	// Use the EntityNames enum
	const door1 = engine.getEntityOrNullByName(EntityNames.Door_1)

	// Write the name as a string
	const door2 = engine.getEntityOrNullByName('Door 2')

	// Ensure both doors exsist in the scene
	(if door1 && door2){
		// 
	}

}
```

<img src="/images/editor/door-names.png" width="600" />

The `EntityNames` enum contains the full list of entities added by the Creator Hub and is updated immediately as soon as you make any changes.
If you import `EntityNames.` into your code, your IDE will present you with a dropdown including all the names of the entities available.

<img src="/images/editor/EntityNames.png" width="300" />


You can also use the `engine.getEntityByName<EntityNames>()` function, passing `<EntityNames>` as a [TypeScript generic](https://www.typescriptlang.org/docs/handbook/2/generics.html), to validate that an entity by that name really exists in your scene. If the referenced entity is renamed on the Creator Hub, this method will warn you with an error. As the output of this function can't be `null`, you can avoid checking that the entity exists.

```ts
import { EntityNames } from '../assets/scene/entity-names'

function main() {

	const door1 = engine.getEntityByName<EntityNames>(EntityNames.Door_1)

	// Ne need to check for null
	console.log(Transform.get(door1).position.x)

}
```


{{< hint warning >}}
**📔 Note**: Make sure you only use `engine.getEntityOrNullByName()` and `engine.getEntityByName()` inside the `main()` function, in functions that run after `main()`, or in a system. If used outside one of those contexts, the entities created in the Scene Editor may not yet be instanced.
{{< /hint >}}

Once you fetched a reference to an entity with any of the above methods, you're free to perform any action with it, like add or remove components, modify values of existing components, or even remove the entity from the engine.

```ts
import { EntityNames } from '../assets/scene/entity-names'

function main() {
	// fetch entity
	const door = engine.getEntityOrNullByName(EntityNames.Door_3)
	// verify that the entity exists
	if (door) {
		// add a pointer events callback
		pointerEventsSystem.onPointerDown(
			{
				entity: door,
				opts: { button: InputAction.IA_PRIMARY, hoverText: 'Open' },
			},
			function () {
				// open door
			}
		)
	}
}
```

All the entities added via the Scene Editor have a `Name` component, you can also iterate over all of them like this:

```ts
function main() {
	for (const [entity, name] of engine.getEntitiesWith(Name)) {
		console.log({ entity, name })
	}
}
```

## Fetch by Tag

You can also fetch entities by their tags. Tags are a way to group entities together, and are useful to identify entities that have the same purpose or behavior.

Add Tags to an entity via the **Tags** section at the top of the item's properties panel. You can pick from the generic tags like **Tag Group 1** through to **Tag Group 4**, or create your own with a more specific name. 

<img src="/images/editor/tags.png" width="600" />

{{< hint info >}}
**💡 Tip**: A single entity can have multiple tags assigned to it.

<img src="/images/editor/tags-multiple.png" width="600" />

{{< /hint >}}

You can then fetch all entities that have a specific tag by using the `engine.getEntitiesByTag()` function. This is ideal for when you want to iterate over a group of entities that have the same purpose or behavior.

```ts
import { engine } from '@dcl/sdk/ecs'

export function main() {
	const taggedEntities = engine.getEntitiesByTag('myTag')
  
	for (const entity of taggedEntities) {
      // Do something with each entity
    }
}
```

You can also add or remove tags to an entity from your code. This is useful if you want to change tags based on some logic, or to spawn entities dynamically that have specific tags.

```ts
import { Tags } from '@dcl/sdk/ecs'

Tags.remove(entity, tagName);
Tags.add(entity, tagName);
```

## Fetch all the children of an item

You can also write a script that lets you deal with all of the items that are grouped as children of a certain item on the entity tree on the left of the screen.
The following script iterates over all entities that have a Transform and a parent, and checks if the name of the parent matches the name `some-parent` in this case. You can then apply any custom logic you want to those specific entities.

```ts
import { engine, Entity, Transform, Name } from '@dcl/sdk/ecs'
import { EntityNames } from '../assets/scene/entity-names'

function main() {
	// get parent entity
	const parent = engine.getEntityByName<EntityNames>(EntityNames.ParentEntity)
	
	// obtain all children entities of that parent
	const childEntities = getChildren(parent)
	
	// loop over each child
	for(const entity of childEntities){
		// handle entity
	}

}

// reusable function to obtain all the child entities of a parent
function getChildren(parent: Entity): Entity[] {
	const childEntities: Entity[] = []
	for (const [entity, transform] of engine.getEntitiesWith(Transform)) {
		if (transform.parent === parent) {
			childEntities.push(entity)
		}
	}
	return childEntities
}
```


## Smart item triggers

You can detect a smart item's **Trigger events**, and respond to these with custom code. For example, you could place a button smart item, and activate custom code when the button is clicked.

Use `getTriggerEvents` to fetch an object that can handle trigger events on from a particular smart item, then use the `.on()` function of the returned object to subscribe a callback function. This callback function gets executed every time that the trigger event happens.

For example, if a scene has a button with the following generic **On Click** event, you can write the code below to run custom code whenever the button is activated.

<img src="/images/editor/restart-button.png" width="600" />

```ts
import { engine } from '@dcl/sdk/ecs'
import { getTriggerEvents, getActionEvents } from '@dcl/asset-packs/dist/events'
import { TriggerType } from '@dcl/asset-packs'
import { EntityNames } from '../assets/scene/entity-names'

function main() {
	const restart = engine.getEntityOrNullByName(EntityNames.Restart_Button)
	if (restart) {
		const restart_event = getTriggerEvents(restart)
		restart_event.on(TriggerType.ON_CLICK, () => {
			// restartGame()
		})
	}
}
```

You can similarly subscribe to any other type of trigger events, like **ON_PLAYER_ENTERS_AREA**, **ON_SPAWN**, **ON_TWEEN_END**, etc.

<!--
You can also use custom code to activate trigger events based on your own custom logic. The following example triggers a door's **On Click** trigger event. Any actions called by that event will be executed. In this case, the door will open or close.

<img src="/images/editor/door-triggers.png" width="600" />

```ts
import { engine } from '@dcl/sdk/ecs'
import { getTriggerEvents, getActionEvents } from '@dcl/asset-packs/dist/events'
import { TriggerType } from '@dcl/asset-packs'

function main() {
	const door = engine.getEntityOrNullByName('Wooden Door')
	if (door) {
		const door_events = getTriggerEvents(door)
		door_events.emit(TriggerType.ON_CLICK)
	}
}
``` -->

## Smart item actions

You can detect the activation of a smart item's **Actions**, and respond to these with custom code. For example, you could place a door smart item, and run custom code whenever the **Open** action gets called.

Use `getActionEvents` to fetch an object for handling the actions of a specific smart item. Then you can use the `.on()` function of the returned object to subscribe a callback function. This callback function gets executed every time that the action happens, regardless of if the action was activated by another smart item, or even by custom code of your own.

For example, if a scene has a door with the following default **Open** action, you can write the code below to run custom code whenever the door is opened.

<img src="/images/editor/door-actions.png" width="600" />

```ts
import { engine } from '@dcl/sdk/ecs'
import { getTriggerEvents, getActionEvents } from '@dcl/asset-packs/dist/events'
import { TriggerType } from '@dcl/asset-packs'
import { EntityNames } from '../assets/scene/entity-names'

function main() {
	const door = engine.getEntityOrNullByName(EntityNames.Wooden_Door)
	if (door) {
		// detect actions
		const actions = getActionEvents(door)
		actions.on('Open', () => {
			console.log('Door opened!!')
			// custom code
		})

		// detect triggers
		const triggers = getTriggerEvents(door)
		triggers.on(TriggerType.ON_CLICK, () => {
			console.log('Door clicked!!')
			// custom code
		})
	}
}
```

You can also emit action events from your code, this allows you to take advantage of actions that are already defined inside the smart item's Action component. The following snippet calls the "Open" action on a door smart item whenever a button smart item is triggered.

```ts
import { engine } from '@dcl/sdk/ecs'
import { getTriggerEvents, getActionEvents } from '@dcl/asset-packs/dist/events'
import { TriggerType } from '@dcl/asset-packs'
import { EntityNames } from '../assets/scene/entity-names'

function main() {
	const button = engine.getEntityOrNullByName(EntityNames.Red_Button)
	const door = engine.getEntityOrNullByName(EntityNames.Wooden_Door)
	if (button && door) {
		// references to actions and triggers
		const buttonTriggers = getTriggerEvents(button)
		const doorActions = getActionEvents(door)

		// detect triggers on button
		buttonTriggers.on(TriggerType.ON_INPUT_ACTION, () => {
			// open door
			doorActions.emit('Open', {})
		})
	}
}
```

{{< hint info >}}
**💡 Tip**: If you're not trying to do something very complicated, instead of writing code you can also create a custom smart item to handle the actions you want to perform. See [Making any item smart]({{< ref "/content/creator/scene-editor/interactivity/make-any-item-smart.md" >}}).
{{< /hint >}}

## Other smart item components

Smart items can include special components that are part of the asset-packs library, like `States` or `Counter`. These components are not part of the Decentraland SDK, but they can be fetched via the `getComponents()` function from the library. You can then read or write values to these components from your scene's code, to have an even tighter integration between smart item behavior and code.

The example below reads and logs the value of a State component of a chest smart item, whenever the chest's actions are triggered.

```ts

import { engine } from '@dcl/sdk/ecs'
import { getComponents } from '@dcl/asset-packs'
import { getTriggerEvents } from '@dcl/asset-packs/dist/events'
import { TriggerType } from '@dcl/asset-packs'
import { EntityNames } from '../assets/scene/entity-names'


export function main() {

    const chest = engine.getEntityByName<EntityNames>(EntityNames.chest)
 
    if (chest) {

        const chestTriggers = getTriggerEvents(chest)

        chestTriggers.on(TriggerType.ON_INPUT_ACTION, () => {
            const { States } = getComponents(engine)
            let state = States.getMutableOrNull(chest)?.currentValue
            console.log( "chest new state ", state)
        })
    }
}
```