---
title: 'Quests SDK Library'
url: /creator/quests/sdk-client
weight: 4
---

Use the [Quests Client for SDK 7](https://github.com/decentraland/quests-client) library in your scenes (or portable experiences) to connect to the Quests Service to track player's progress, send events and receive updates of player's progress from your scenes.

## What the library provides

- An interface with the Quests Client API, to send your [Custom]({{< ref "/content/creator/quests/define.md#action-items" >}}) events and receive updates of the player's progress.
- SDK System helper to track [Location, Emote, and Jump]({{< ref "/content/creator/quests/define.md#action-items" >}}) actions. Passing a callback function to the helper, you can send the action to the Quests Service when relevant.
- A fully-customizable [Quest HUD UI]({{< ref "/content/creator/quests/quest-hud.md" >}}) to display the player's progress on your Quest. You can use this UI as is, or as an example to build your own. You can find the code [here](https://github.com/decentraland/quests-client/tree/main/src/hud.tsx).

## Usage

#### Installation

##### Via the VS Code Extension

Follow the steps in [Install a dependency]({{< ref "/content/creator/sdk7/libraries/manage-dependencies.md#install-a-dependency" >}}):

1. Open the Decentraland tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

2. Click the `+` icon on the header of the **Dependencies** view.

3. Visual Studio opens an input box at the top of the screen. Write `@dcl/quests-client`.

##### Via the CLI

Run this command in your scene's directory:

```bash
$ npm install @dcl/quests-client
```

## Quests Client overview

The types below are defined in [Quests Client for SDK 7](https://github.com/decentraland/quests-client).

```typescript
import { QuestInstance as QuestInstanceProtocol } from './protocol/decentraland/quests/definitions.gen'

type QuestsClient = {
	startQuest: () => Promise<boolean>
	abortQuest: () => Promise<boolean>
	sendEvent: (event: { action: Action }) => Promise<EventResponse | undefined>
	onStarted: (callback: OnStartedCallback) => void
	onUpdate: (callback: OnUpdateCallback) => void
	isQuestStarted: () => boolean
	getQuestInstance: () => QuestInstance | null
	getInstances: () => QuestInstance[]
}

type Required<T> = T & {
	[P in keyof T]: NonNullable<T[P]>
}

type QuestInstance = Required<QuestInstanceProtocol>

type OnStartedCallback = (instance: QuestInstance) => void
type OnUpdateCallback = (instance: QuestInstance) => void
```

## The Quest Instance

The `QuestInstance` type is used in several methods. The `QuestInstance` type has the same fields as `QuestInstanceProtocol` **but** with no `undefined` fields (the `undefined` are caused by `proto`, and it's impossible that these fields are `undefined`). A `QuestInstance` (or `QuestInstanceProtocol`) is an instance of a specific Quest and it contains the state (or progress) of the player in that specific Quest. The `QuestInstance` type has the following fields:

- `id`: The id of the Quest Instance. It's a unique identifier of the player's Quest Instance.
- `quest`: The Quest object defined in the Quest's protocol file [here](https://github.com/decentraland/protocol/blob/main/proto/decentraland/quests/definitions.proto).
- `state`: The progress of the player along the Quest defined in the Quest's protocol file [here](https://github.com/decentraland/protocol/blob/main/proto/decentraland/quests/definitions.proto).

## Quest client methods

The following methods are available in the Quests Client:

- `startQuest`: Use this function to make the player start your Quest. In the background, the function calls the Quest RPC Service. The function returns a `boolean`. If the Quest was started successfully, it returns `true`. If there was an error, it returns `false`.

- `abortQuest`: Use this function to abort the player's instance of the Quest. In the background, the function will call the Quest RPC Service. If the Quest was aborted successfully, it returns `true`. If there was an error, it returns `false`.

{{< hint warning >}}
**📔 Note**: Quests that are fully completed cannot be aborted, only partially completed quests. A player can't do a same quest more than once.
{{< /hint >}}

- `sendEvent`: Use this function send a custom event to the Quest RPC Service. The function receives an `Action` (action item with its type and parameters), representing an action that the player has already completed in the scene. The function returns an `EventResponse` object that contains the result of the request, both in case of an error or success. Both `Action` and `EventResponse` are defined in the Quest's protocol file [here](https://github.com/decentraland/protocol/blob/main/proto/decentraland/quests/definitions.proto).

- `onStarted`: Use this function to register one or multiple callbacks that are called when the player starts your Quest. Callbacks will only be called when the user starts the Quest that matches the Quest ID passed when creating the client instance. Use these callbacks for the scene to react to the start of your Quest. The callback receives an `QuestInstance` object that contains the information of the Quest that the player has started.

- `onUpdate`: Use this function to register one or multiple callbacks that are called whenever the player makes progress on a Quest. Callbacks will only be called when the user makes progress on the Quest that matches the Quest ID passed when you created the client instance. Use these callbacks to apply changes on your scene that correlate to this progress. The callback receives a `QuestInstance` object that contains the information of the Quest that the player has made progress on.

- `isQuestStarted`: Use this function to check if the player has started your Quest. The function returns a `boolean`. If the player has started the Quest, it returns `true`. If the player hasn't started the Quest, it returns `false`.

- `getQuestInstance`: This function allows you to get the Instance of the Quest that matches the Quest ID passed when you created the Client. The function returns a `QuestInstance` object, including data about the player's progress in that quest. If the user hasn't started the Quest, it returns `null`.

- `getInstances`: This function allows you to get all the Quest Instances of the player. The function returns an array of `QuestInstance` objects.

## Setting up the client

To initialize the Quests Client in your scene, start by importing `createQuestsClient`.

```typescript
// index.ts

//...
import { createQuestsClient } from '@dcl/quests-client'
```

Then run the function `createQuestsClient` to initialize the Quests Client. This function returns a promise that resolves when the Quests Client is ready to be used. Run this function inside an async function, for this you can use the `executeTask` function, see [asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}).

The function `createQuestsClient()` takes a parameter with the URL to connect to the [Quests API](creator/quests/overview/#services-architecture). The following options are available:

- **Development**: `wss://quests-rpc.decentraland.zone`
- **Production**: `wss://quests-rpc.decentraland.org`
- **Custom**: Set up your own Quests Service locally for development or testing. You can find more information on how to do so on [Quests Service's repository](https://github.com/decentraland/quests)

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient } from '@dcl/quests-client'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
	const serviceUrl = 'wss://quests-rpc.decentraland.zone'

	try {
		const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
		console.log('Quests Client is ready to use!')
	} catch (e) {
		console.error('Error on connecting to Quests Service')
	}
})
```

## Using observables

Since the instancing of the `questClient` is scoped within `executeAsync` function, interacting with this object from other parts of your scene's code can be a challenge. You'll likely end up having lots of parts in your scene's code needing to either make updates to the player's progress or know the player's current progress along the quest, and all of these will need to make use of the `questClient` object. The recommended approach is to use observables (also known as event emitters) to send and to listen to events anywhere.

To use observables, we recommend you use the `mitt` library. Find more information about this library [here](https://www.npmjs.com/package/mitt).

To install this library, follow the steps in [Install a dependency]({{< ref "/content/creator/sdk7/libraries/manage-dependencies.md#install-a-dependency" >}}):

1. Open the Decentraland tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

2. Click the `+` icon on the header of the **Dependencies** view.

3. Visual Studio opens an input box at the top of the screen. Write `mitt`.

To otherwise install the library via the command line, run:

```bash
$ npm install mitt
```

In its simplest form, you can use mitt like this to send and listen to events:

```ts
const event = mitt()

event.emit('start')

event.on('start', () => {
	console.log('started')
})
```

The code example below works across three files in the scene:

- In `events.ts` you simply define an event emitter. This can then be imported to other files
- In `cube.ts` you send this "start" event when the player performs an action. In this example, the `start` event is sent when the player clicks on a Cube mesh.
- In `index.ts` you listen for this "stat" after you have initialized the `questClient`. Then, when this event is listened to, the `startQuest` function is called with the Quest ID.

```typescript
// events.ts
import mitt from 'mitt'

export const startEvent = mitt()

// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { startEvent } from './events'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
	const serviceUrl = 'wss://quests-rpc.decentraland.zone'

	try {
		const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
		console.log('Quests Client is ready to use!')

		questsClient.onUpdate((quest: QuestInstance) => {
			// apply some changes on your scene to reflect the player's progress
		})

		questsClient.onStarted((quest: QuestInstance) => {
			// react to the start of your Quest by applying some change on your scene
		})

		startEvent.on('start', async () => {
			await questsClient.startQuest()
		})
	} catch (e) {
		console.error('Error on connecting to Quests Service')
	}
})

// cube.ts

//...
import { pointerEventsSystem, InputAction } from '@dcl/sdk/ecs'

//...
// create a clickable cubeMeshEntity

pointerEventsSystem.onPointerDown(
	cubeMeshEntity,
	(cmd) => {
		startEvent.emit('start')
	},
	{ button: InputAction.IA_PRIMARY, hoverText: 'E to Start Quest' }
)
//...
```

## Trigger the Start of your Quest

To trigger the start of a Quest, call the `startQuest` function. This function receives the id of the quest you want to start.

```ts
const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
	const serviceUrl = 'wss://quests-rpc.decentraland.zone'
	try {
		const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)

		const result = await questsClient.startQuest()

		if (result) {
			console.log('Quest started successfully!')
		} else {
			console.error("Quest couldn't be started")
		}
	} catch (e) {
		console.error('Error on connecting to Quests Service')
	}
})
```

The example above initializes the quest as soon as the scene loads. You may prefer to instead start the quest as response to a player's interaction. For example when the player enters a specific area of your scene or when they interact with an NPC. For an example of how to do this, see the [Using observables](#using-observables) section above.

#### React to the start of your Quest

When the player starts your Quest, you may want the scene to react to this event. You can register a callback using `onStarted` function, provided by the client:

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { startEvent } from './events'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
	const serviceUrl = 'wss://quests-rpc.decentraland.zone'

	try {
		const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
		console.log('Quests Client is ready to use!')

		client.onStarted((quest: QuestInstance) => {
			// react to the start of your Quest
		})
	} catch (e) {
		console.error('Error on connecting to Quests Service')
	}
})
```

## Send Custom Actions to the Quests Service

When an action is of type `CUSTOM`, you must use the `sendEvent` function to update the quest service.

Like with other functions from the quest client, you can use an event emitter to route events from anywhere in your scene's code to the context where the quest client object is initialized. A good practice is to define an "action" event with mitt that includes all of the data about the action. That way you only need to create a single listener, that handles all the actions from your scene.

Come back to the `events.ts` file iny your scene, to define a type of event that sends an `Action` object. For this, you need to import the `Action` type provided by the Quests Client library and defined in the Quest's Protocol file [here](https://github.com/decentraland/protocol/blob/main/proto/decentraland/quests/definitions.proto).

```typescript
// events.ts
import mitt from 'mitt'
import { Action } from '@dcl/quests-client'

export const startEvent = mitt()
export const actionEvents = mitt<{ action: Action }>()
```

The above code initializes an event emitter used to send events to the Quests Service. This event emitter emits an event called "action", and includes an `Action` object. Import this emitter on the file where you have the `questClient` initialized and listen to the `action` event.

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { startEvent, actionEvents } from './events'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
	const serviceUrl = 'wss://quests-rpc.decentraland.zone'

	try {
		const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
		console.log('Quests Client is ready to use!')

		client.onUpdate((quest: QuestInstance) => {
			// apply some changes on your scene to reflect the player's progress
		})

		startEvent.on('start', async (value: boolean) => {
			await questsClient.startQuest()
		})

		actionEvents.on('action', async (action: Action) => {
			await questsClient.sendEvent({ action })
		})
	} catch (e) {
		console.error('Error on connecting to Quests Service')
	}
})
```

The code above includes the `actionEvents` emitter listening to the `action` event. When this event is listened to, the quest client's `sendEvent` function is called, using the data from the `Action` object that was passed with this event.

With this set up, you can emit events with the `actionEvents` emitter from any part of your code, and they will be forwarded to the Quest Service. Below is some pseudocode example:

```typescript
// another-file.ts

//...

import { actionEvents } from './events'

//...

actionEvents.emit('action', {
	type: 'CUSTOM',
	parameters: { id: 'my-custom-action-id' },
})
```

## Sending other types of actions

For actions of type `LOCATION`, `JUMP`, and `EMOTE`, you can make use of the `initActionsTracker` function. This function registers a set of systems to track these types of actions. You only need to call this function once, with the action types you want to track.

For example: to track the `LOCATION` type of action.

1. Import the `initActionsTracker` function from `@dcl/quests-client/dist/systemHelpers` and call it, passing the following parameters:
   a. The SDK `engine` constant.
   b. A callback function. You may use it to send the action using the `QuestClient` or using a event emitter, as covered in other examples.
   c. The type of action you want to track.

```ts
import { initActionsTracker } from '@dcl/quests-client/dist/systemHelpers'

initActionsTracker(
	engine,
	(action) => {
		// You can add a check here to only send the action if the player has started the quest
		// Also, you can add a check here to only send the action if the action itself meets some criteria or condition.
		// Or it's indeed a valid action for the quest so that you don't send invalid actions to the Quests Service.
		client.sendEvent(action)
	},
	'location'
)
```

To track more than one action, list them as additional parameters. For example:

```ts
import { initActionsTracker } from '@dcl/quests-client/dist/systemHelpers'

initActionsTracker(
	engine,
	(action) => {
		// You can add a check here to only send the action if the player has started the quest
		// Also, you can add a check here to only send the action if the action itself meets some criteria or condition.
		// Or it's indeed a valid action for the quest so that you don't send invalid actions to the Quests Service.
		client.sendEvent(action)
	},
	'location',
	'jump'
)
```

Or all three action types:

```ts
import { initActionsTracker } from '@dcl/quests-client/dist/systemHelpers'

initActionsTracker(
	engine,
	(action) => {
		// You can add a check here to only send the action if the player has started the quest
		// Also, you can add a check here to only send the action if the action itself meets some criteria or condition.
		// Or it's indeed a valid action for the quest so that you don't send invalid actions to the Quests Service.
		client.sendEvent(action)
	},
	'location',
	'jump',
	'emote'
)
```

The order of the action type parameters is not relevant here. Each action type that you pass as parameter will be tracked by the system.

## React to changes on the player's progress

You may want to react and apply different changes to your scene when the player makes progress on a Quest. To react to these changes, register a callback with `onUpdate`:

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
	const serviceUrl = 'wss://quests-rpc.decentraland.zone'

	try {
		const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
		console.log('Quests Client is ready to use!')

		client.onUpdate((quest: QuestInstance) => {
			// update your state here to react to the quest updates
		})
	} catch (e) {
		console.error('Error on connecting to Quests Service')
	}
})
```

The `onUpdate` function receives a callback function that is called every time the player makes progress on a Quest. The callback receives a `QuestInstance` object that contains information about the Quest that the player has made progress on.

The `QuestInstance` object has the following fields:

```typescript
type QuestInstance = {
	id: string
	quest: Quest
	state: QuestState
}
```

- `id`: The id of the Quest Instance. It's a unique identifier of the player's Quest Instance.
- `quest`: The Quest object. Find more information about the Quest object [here]({{< ref "/content/creator/quests/define.md" >}}).
- `state`: The progress of the player on the Quest.

Find details about the `Quest` and `QuestState` types in the Quest's protocol file [here](https://github.com/decentraland/protocol/blob/main/proto/decentraland/quests/definitions.proto).

{{< hint info >}}
**💡 Tip**: When there are changes to the scene's state that reflect the player's progress throughout the quest, always make the changes via this function, rather than as a direct consequence of the player's action. That way, if for whatever reason the quest service is not successful, the scene will remain in a consistent state with the player's progress.
{{< /hint >}}

Once again, it's recommended to use event emitters so that the effects of a change in the quest progress can make changes anywhere in your code.

```typescript
// events.ts
import mitt from 'mitt'
import { Action } from '@dcl/quests-client'

export const startEvent = mitt()
export const actionEvents = mitt<{ action: Action }>()
export const questProgress = mitt<{ step: number }>()

// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import {
	createQuestsClient,
	QuestInstance,
	questProgress,
} from '@dcl/quests-client'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
	const serviceUrl = 'wss://quests-rpc.decentraland.zone'

	try {
		const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
		console.log('Quests Client is ready to use!')

		questsClient.onUpdate((quest: QuestInstance) => {
			for (let step of quest.state.stepsCompleted) {
				switch (step) {
					case 'my_step_1':
						questProgress.emit('step', 1)
					case 'my_step_2':
						questProgress.emit('step', 2)
					case 'my_step_3':
						questProgress.emit('step', 3)
				}
			}
		})
	} catch (e) {
		console.error('Error on connecting to Quests Service')
	}
})

// cube.ts
import { questProgress } from '@dcl/quests-client'

//...

questProgress.on('step', (stepNumber: number) => {
	if (stepNumber >= 2) {
		console.log("we're ready for step 3!")
	}
})
```

## Check for progress in other sessions

The player might be coming back to your scene after having started the quest before. The quest server keeps track of how far they got, but your scene might have to load changes that reflect the past actions of the player. For example, you might have to hide items that were already collected, unlock doors that were already opened, etc. You should also update the quest UI to reflect their initial progress.

Use the `getQuestInstance()` function to fetch a `QuestInstance` object, which contains a `stepsCompleted` array.

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
	const serviceUrl = 'wss://quests-rpc.decentraland.zone'

	try {
		const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
		console.log('Quests Client is ready to use!')

		const currentProgress = questsClient.getQuestInstance()
		if (currentProgress) {
			sendQuestUpdates(currentProgress)
		}

		questsClient.onUpdate((quest: QuestInstance) => {
			sendQuestUpdates(quest)
		})
	} catch (e) {
		console.error('Error on connecting to Quests Service')
	}
})

function sendQuestUpdates(questInstance: QuestInstance) {
	for (let step of questInstance.state.stepsCompleted) {
		switch (step) {
			case 'my_step_1':
				questProgress.emit('step', 1)
			case 'my_step_2':
				questProgress.emit('step', 2)
			case 'my_step_3':
				questProgress.emit('step', 3)
		}
	}
}
```

The example above defines a function `sendQuestUpdates` to handle both the initial state of the quest when the scene loads, obtained from `getQuestInstance()`, and any updates done later, obtained from `onUpdate()`. The scene can then react to these messages that are emitted and change the states of relevant things.
