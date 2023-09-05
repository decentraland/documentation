---
title: 'Quests SDK Library'
url: /creator/quests/sdk-client
weight: 4
---

Use the [Quests Client for SDK 7](https://github.com/decentraland/quests-client) library in your scenes (or portable experiences) to connect to the Quests Service to track player's progress, send events and receive updates of player's progress from your scenes,

## What the library provides

- An interface with the Quests Client API, to send your [Custom](/creator/quests/define#action-items) events and receive updates of player's progress.
- SDK System helpers to send [Location, Emote, Jump](/creator/quests/define#action-items) events automatically.
- Default UI for your Quest HUD. (TODO)

## Usage

#### Installation

##### Via the Editor

Follow the steps in [Install a dependency]({{< ref "/content/creator/sdk7/libraries/manage-dependencies.md#install-a-dependency" >}}):

1. Open the Decentraland Editor tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

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
type QuestsClient = {
  startQuest: UnaryClientMethod<StartQuestRequest, StartQuestResponse>
  abortQuest: UnaryClientMethod<AbortQuestRequest, AbortQuestResponse>
  sendEvent: (event: { action: Action }) => Promise<EventResponse | undefined>
  onStarted: (callback: OnStartedCallback) => void
  onUpdate: (callback: OnUpdateCallback) => void
  getInstances: () => QuestInstance[]
}

type QuestInstance = {
  id: string
  quest: Quest
  state: QuestState
}
type OnStartedCallback = (instance: QuestInstance) => void
type OnUpdateCallback = (instance: QuestInstance) => void
```

## The Quest instance

The `QuestInstance` type is used in several methods. A `QuestInstance` is an instance of a specific Quest and it contains the state (or progress) of the player in that specific Quest. The `QuestInstance` type has the following fields:

- `id`: The id of the Quest Instance. It's a unique identifier of the player's Quest Instance.
- `quest`: The Quest object defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).
- `state`: The progress of the player along the Quest defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

## Quest client methods

The following methods are available in the Quests Client:

- `startQuest`: Use this function to make the player start your Quest. In the background, the function calls the Quest RPC Service. The function receives a `StartQuestRequest` object that contains the Quest's id that you want to start. The function returns a `StartQuestResponse` object that contains the Quest Instance's id. Both objects are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `abortQuest`: Use this function to abort the player's instance of the Quest. In the background, the function will call the Quest RPC Service. The function receives an `AbortQuestRequest` object that contains the player's instance id. The function returns an `AbortQuestResponse` object that contains the result of the request, both in case of an error or success. Both objects are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

{{< hint warning >}}
**📔 Note**: Quests that are fully completed cannot be aborted, only partially completed quests. A player can't do a same quest more than once.
{{< /hint >}}

- `sendEvent`: Use this function send a custom event to the Quest RPC Service. The function receives an `Action` (action item with its type and parameters), representing an action that the player has already completed in the scene. The function returns an `EventResponse` object that contains the result of the request, both in case of an error or success. Both `Action` and `EventResponse` are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `onStarted`: Use this function to register one or multiple callbacks that are called when the player starts a Quest. Use this for the scene to react to the start of a Quest in any needed way. The callback receives an `QuestInstance` object that contains the information of the Quest that the player has started.

- `onUpdate`: Use this function to register one or multiple callbacks that are called whenever the player makes progress on a Quest. Use these callbacks to apply changes on your scene that correlate to this progress. The callback receives an `QuestInstance` object that contains the information of the Quest that the player has made progress on.

- `getInstances`: This function allows you to get all the Quest Instances of the player. The function returns an array of `QuestInstance` objects.

- `initActionsTracker`: Use this function to subscribe listeners to different kinds of actions, like actions of type location, emote and jump. Once the tracker is initialized, the scene will take care of updating the player's progress on any action of those types in the quest.

## Setting up the client

To initialize the Quests Client in your scene, start by importing `createQuestsClient`.

```typescript
// index.ts

//...
import { createQuestsClient } from '@dcl/quests-client'
```

Then run the function `createQuestsClient` to initialize the Quests Client. This function returns a promise that resolves when the Quests Client is ready to be used. Run this function inside an async function, for this you can use the `executeTask` function, see [asynchronous functions]({{< ref "/content/creator/scenes/programming-patterns/async-functions.md" >}}).

The function `createQuestsClient()` takes a parameter with the URL to connect to the [Quests API](creator/quests/overview/#services-architecture). The following options are available:

- Development: `wss://quests-rpc.decentraland.zone`
- Production: `wss://quests-rpc.decentraland.org`
- Custom: Set up your own Quests Service locally for development or testing. You can find more information on how to do so on [Quests Service's repository](https://github.com/decentraland/quests)

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient } from '@dcl/quests-client'

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl)
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

1. Open the Decentraland Editor tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

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
    const questsClient = await createQuestsClient(serviceUrl)
    console.log('Quests Client is ready to use!')

    questsClient.onUpdate((quest: QuestInstance) => {
      // update your state here or react to your quest updates
    })

    questsClient.onStarted((quest: QuestInstance) => {
      // react to the start of your Quest
    })

    startEvent.on('start', async () => {
      await questsClient.startQuest({ questId: MY_QUEST_ID })
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
    const questsClient = await createQuestsClient(serviceUrl)

 		await questsClient.startQuest({ questId: MY_QUEST_ID })
   })
  } catch (e) {
    console.error('Error on connecting to Quests Service')
  }
})
```

The example above initializes the quest as soon as the scene loads. You may prefer to instead start the quest as response to a player's interaction. For example when the player enters a specific area of your scene or when they interact with an NPC. For an example of how to do this, see the [Using observables](#using-observables) section above.

In the previous code, a constant value, containing the Quest ID you want the player to start, is defined and passed onto the `startQuest` function.

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
    const questsClient = await createQuestsClient(serviceUrl)
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

Come back to the `events.ts` file iny your scene, to define a type of event that sends an `Action` object. For this, you need to import the `Action` type provided by the Quests Client library and defined in the Quest's Protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

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
    const questsClient = await createQuestsClient(serviceUrl)
    console.log('Quests Client is ready to use!')

    client.onUpdate((quest: QuestInstance) => {
      // update your state here or react to the quest updates
    })

    startEvent.on('start', async (value: boolean) => {
      await questsClient.startQuest({ questId: MY_QUEST_ID })
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

For actions of type `LOCATION`, `JUMP`, and `EMOTE`, you can make use of `initActionsTracker` function from `@dcl/quests-client/dist/systemHelpers`. This function will register a set of systems to track these types of actios. You only need to call this function once, with the action types you want to track.

For example: Let's track the `LOCATION` type of action. 

First, you need to import the `initActionsTracker` function from `@dcl/quests-client/dist/systemHelpers`. After that you can the funciton passing the SDK engine constant as first parameter, a callback function as second parameter which you may want to send the acion using the `QuestClient` or using a event emitter as we see in other examples, and the type of action you want to track as third parameter.

```ts
import { initActionsTracker } from '@dcl/quests-client/dist/systemHelpers'

initActionsTracker(
  engine,
  (action) => {
    client.sendEvent(action)
  },
  'location'
)
```

If you want to track more than one action, you can keep adding them as parameters. For example:

```ts
import { initActionsTracker } from '@dcl/quests-client/dist/systemHelpers'

initActionsTracker(
  engine,
  (action) => {
    client.sendEvent(action)
  },
  'location',
  'jump'
)
```

Or the three action types:

```ts
import { initActionsTracker } from '@dcl/quests-client/dist/systemHelpers'

initActionsTracker(
  engine,
  (action) => {
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

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl)
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
- `quest`: The Quest object. Find more information about the Quest object [here](/creator/quests/define).
- `state`: The progress of the player on the Quest.

Find details about the `Quest` and `QuestState` types in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

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
import { createQuestsClient, QuestInstance, questProgress } from '@dcl/quests-client'

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl)
    console.log('Quests Client is ready to use!')

  	questsClient.onUpdate((quest: QuestInstance) => {
        for (let step of quest.state.stepsCompleted) {
            switch (step) {
                case "my_step_1":
                    questProgress.emit("step", 1)
                case "my_step_2":
                    questProgress.emit("step", 2)
                case "my_step_3":
                    questProgress.emit("step", 3)
            }
        }
  } catch (e) {
    console.error('Error on connecting to Quests Service')
  }
})


// cube.ts
import { questProgress } from '@dcl/quests-client'

  //...

	questProgress.on("step", (stepNumber: number)=>{
		if(stepNumber >= 2){
			console.log("we're ready for step 3!")
		}
	})
```

## Quest HUD, a SDK UI for your Quest

You may be wondering how to display the player's progress on the Quest. The Quests Client library provides a basic UI for your Quest. 

To make use of it, you have to import the `createQuestHUD` function from `@dcl/quests-client/dist/hud`. Let's see an example:

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { createQuestHUD } from '@dcl/quests-client/dist/hud'

const questHud = createQuestHud();

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl)
    console.log('Quests Client is ready to use!')

    client.onStarted((quest: QuestInstance) => {
        // react to the start of your Quest
        questHud.upsert(quest)
    })

    client.onUpdate((quest: QuestInstance) => {
        // update your state here to react to the quest updates
        questHud.upsert(quest)
    })
  } catch (e) {
    console.error('Error on connecting to Quests Service')
  }
})
```

What does the above code do? It creates a Quest HUD object, and automatically renders the UI when detect that a Quest is being played, by starting it off or by receiving Quest progress update.

`questHud.upsert` function, receives a QuestInstace object and creates an SDK entity wit its data to be used by a ReactECS component. This component will be rendered in the scene, and will display the Quest progress: steps and tasks completed or not. Under the hood, this function is calling `ReactEcsRenderer.setUiRenderer` from `@dcl/sdk/react-ecs` library.