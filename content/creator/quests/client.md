---
title: 'Quests SDK Library'
url: /creator/quests/sdk-client
weight: 4
---

Use the [Quests Client for SDK 7](https://github.com/decentraland/quests-client) library in your scenes (or portable experiences) to connect to the Quests Service to track player's progress, send events and receive updates of player's progress from your scenes.

## What the library provides

- An interface with the Quests Client API, to send your [Custom](/creator/quests/define#action-items) events and receive updates of player's progress.
- SDK System helper to track [Location, Emote, Jump](/creator/quests/define#action-items) actions. Passing a callback function to the helper, you can send the action to the Quests Service, if it's the action that your quest requires.
- A fully-customizable Quest HUD UI to display the player's progress on your Quest. You can use this UI as is, or as an example to build your own one. You can find the code [here](https://github.com/decentraland/quests-client/tree/main/src/hud.tsx).

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
  startQuest: () => Promise<boolean>
  abortQuest: () => Promise<boolean>
  sendEvent: (event: { action: Action }) => Promise<EventResponse | undefined>
  onStarted: (callback: OnStartedCallback) => void
  onUpdate: (callback: OnUpdateCallback) => void
  isQuestStarted: () => boolean
  getQuestInstance: () => QuestInstance | null
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

- `startQuest`: Use this function to make the player start your Quest. In the background, the function calls the Quest RPC Service. The function returns a `boolean`. If the Quest was started successfully, it returns `true`. If there was an error, it returns `false`.

- `abortQuest`: Use this function to abort the player's instance of the Quest. In the background, the function will call the Quest RPC Service. If the Quest was aborted successfully, it returns `true`. If there was an error, it returns `false`.

{{< hint warning >}}
**📔 Note**: Quests that are fully completed cannot be aborted, only partially completed quests. A player can't do a same quest more than once.
{{< /hint >}}

- `sendEvent`: Use this function send a custom event to the Quest RPC Service. The function receives an `Action` (action item with its type and parameters), representing an action that the player has already completed in the scene. The function returns an `EventResponse` object that contains the result of the request, both in case of an error or success. Both `Action` and `EventResponse` are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `onStarted`: Use this function to register one or multiple callbacks that are called when the player starts your Quest. Callbacks will only be called when the user starts the Quest that matches the Quest ID passed when you created the client. Use these callbacks for the scene to react to the start of your Quest in any needed way. The callback receives an `QuestInstance` object that contains the information of the Quest that the player has started.

- `onUpdate`: Use this function to register one or multiple callbacks that are called whenever the player makes progress on a Quest. Callbacks will only be called when the user makes progress on the Quest that matches the Quest ID passed when you created the client. Use these callbacks to apply changes on your scene that correlate to this progress. The callback receives an `QuestInstance` object that contains the information of the Quest that the player has made progress on.

- `isQuestStarted`: Use this function to check if the player has started your Quest. The function returns a `boolean`. If the player has started the Quest, it returns `true`. If the player hasn't started the Quest, it returns `false`.

- `getQuestInstance`: This function allows you to get the Instance of the Quest that mathches the QUest ID passed when you created the Client. The function returns a `QuestInstance` object. If the user hasn't started the Quest, it returns `null`.

- `getInstances`: This function allows you to get all the Quest Instances of the player. The function returns an array of `QuestInstance` objects.

- `initActionsTracker`: Use this function to subscribe listeners to different kinds of actions, like actions of type location, emote and jump. Once the tracker is initialized, the scene will take care of updating the player's progress on any action of those types in the quest.

## Setting up the client

To initialize the Quests Client in your scene, start by importing `createQuestsClient`.

```typescript
// index.ts

//...
import { createQuestsClient } from '@dcl/quests-client'
```

Then run the function `createQuestsClient` to initialize the Quests Client. This function returns a promise that resolves when the Quests Client is ready to be used. Run this function inside an async function, for this you can use the `executeTask` function, see [asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}).

The function `createQuestsClient()` takes a parameter with the URL to connect to the [Quests API](creator/quests/overview/#services-architecture). The following options are available:

- Development: `wss://quests-rpc.decentraland.zone`
- Production: `wss://quests-rpc.decentraland.org`
- Custom: Set up your own Quests Service locally for development or testing. You can find more information on how to do so on [Quests Service's repository](https://github.com/decentraland/quests)

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
      console.log("Quest started successfully!")
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

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
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
    })
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

## Quest HUD - an SDK UI for your Quest

The Quests Client library provides a UI (HUD) for your Quest. This displays the players their progress, listing the steps in the quest and their status.

As it was defined previously, this HUD is fully-customizable. So, let's start with the options that you have to customize it.

```typescript
type LabelProps = EntityPropTypes & UiLabelProps

export type QuestHudOptions = {
  autoRender?: boolean
  leftSidePanel?: UiTransformProps
  questBox?: {
    uiBackground?: UiBackgroundProps
    uiTransform?: UiTransformProps
  }
  questNameContainer?: {
    uiTransform?: UiTransformProps
    label?: LabelProps
  }
  stepsContainer?: {
    uiTransform: UiTransformProps
    labels?: {
      labelUiEntity?: UiTransformProps
      props?: LabelProps
    }
    showTasksButton?: {
      buttonUiEntity: UiTransformProps
      buttonProps?: UiButtonProps
    }
  }
  tasksBox?: {
    uiTransform?: UiTransformProps
    uiBackground?: UiBackgroundProps
    labels?: {
      labelUiEntity?: UiTransformProps
      props?: LabelProps
    }
  }
  nextSteps?: {
    nextTitleUiEntity?: UiTransformProps
    nextTitleProps?: LabelProps
    labels?: {
      labelUiEntity?: UiTransformProps
      props?: LabelProps
    }
  }
}
```

- `autoRender`: If `true`, the HUD will be rendered automatically. If `false`, you will need to call the `render` function to render the HUD. By default, it's **not** rendered automatically.

- `leftSidePanel`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify the `UiEntity` containing the box that contains all the Quest progress and the "Hide/Show" toggle button. In web terms, this would be the div acting as a container for the box and button.

- `questBox`: It's an object that contains two fields:
  - `uiBackground`: It's the `UiBackgroundProps` type from `@dcl/sdk/react-ecs`. You can use this to modify the background of the `UiEntity` containing the box that contains the Quest name and the steps. In web terms, this would be the `div` acting as a container for the Quest name and steps.
  - `uiTransform`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify the `UiEntity` containing the box that contains the Quest name and the steps. In web terms, this would be the `div` acting as a container for the Quest name and steps.

- `questNameContainer`: It's an object that contains two fields:
  - `uiTransform`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify the `UiEntity` containing the Quest name. In web terms, this would be the `div` acting as a container for the Quest name.
  - `label`: It's the `LabelProps` type defined in the snippet above. You can use this to modify the `Label` containing the Quest name. In web terms, this would be the `p` tag containing the Quest name.

- `stepsContainer`: It's an object that contains three fields:
  - `uiTransform`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify the `UiEntity` containing and listing the steps with their `description`. In web terms, this would be the `div` acting as a container for the steps.
  - `labels`: It's an object that contains two fields:
    - `labelUiEntity`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify all `UiEntity`s containing the step's `description` and the "Show Tasks" button. In web terms, this would be the `div` acting as a container for the step's `description` and the "Show Tasks" button.
    - `props`: It's the `LabelProps` type defined in the snippet above. You can use this to modify all `Label`s containing the step's `description`. In web terms, this would be the `p` tag containing the step's `description`.
  - `showTasksButton`: It's an object that contains two fields:
    - `buttonUiEntity`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify all `UiEntity`s containing the "Show Tasks" button. In web terms, this would be the `div` acting as a container for the "Show Tasks" button.
    - `buttonProps`: It's the `UiButtonProps` type from `@dcl/sdk/react-ecs`. You can use this to modify all the "Show Tasks" `Button`s.

- `tasksBox`: It's an object that contains three fields:
  - `uiTransform`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify all `UiEntity`s containing and listing each step tasks with their `description`. In web terms, this would be the `div` acting as a container for a step tasks.
  - `uiBackground`: It's the `UiBackgroundProps` type from `@dcl/sdk/react-ecs`. You can use this to modify the background of all `UiEntity`s containing and listing each step tasks with their `description`. In web terms, this would be the `div` acting as a container for the tasks.
  - `labels`: It's an object that contains two fields:
    - `labelUiEntity`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify all `UiEntity`s containing the task's `description`. In web terms, this would be the `div` acting as a container for the task's `description`.
    - `props`: It's the `LabelProps` type defined in the snippet above. You can use this to modify all `Label`s containing the task's `description`. In web terms, this would be the `p` tag containing the task's `description`.

- `nextSteps`: It's an object that contains three fields:
  - `nextTitleUiEntity`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify the `UiEntity` containing the "Next Steps" title. In web terms, this would be the `div` acting as a container for the "Next Steps" title.
  - `nextTitleProps`: It's the `LabelProps` type defined in the snippet above. You can use this to modify the `Label` containing the "Next Steps" title. In web terms, this would be the `p` tag containing the "Next Steps" title.
  - `labels`: It's an object that contains two fields:
    - `labelUiEntity`: It's the `UiTransformProps` type from `@dcl/sdk/react-ecs`. You can use this to modify all `UiEntity`s containing the next step's `description`. In web terms, this would be the `div` acting as a container for the next step's `description`.
    - `props`: It's the `LabelProps` type defined in the snippet above. You can use this to modify all `Label`s containing the next step's `description`. In web terms, this would be the `p` tag containing the next step's `description`.


Well now, let's explain the `QuestHUD` type returned by the `createQuestHUD` function from `@dcl/quests-client/dist/hud`:

```typescript
type QuestHUD = {
  upsert: (instance: QuestInstance) => void
  getHUDComponent: () => () => ReactEcs.JSX.Element
  render: () => void
}
```

- `upsert`: Use this function to update the Quest HUD with the player's progress, you may want to call it when the users start the Quest and when they make some progress. This function receives a `QuestInstance` object. It creates an SDK entity with this data to be used by a ReactECS UI component. This component is rendered in the scene UI, displaying the Quest progress.

- `getHUDComponent`: Use this function to get the ReactECS UI component that renders a ready-to-use Quest HUD. You may want to make use of this function when you already have an UI to render since `ReactEcsRenderer.setUiRenderer` overrides everything that previously exists when you execute it.

- `render`: Use this function to render the Quest HUD. You may want to call this function when you have the `autoRender` option set to `false` and you want to render the Quest HUD manually. (TODO: check if recalling it when entity updates is needed.)

To use it, import the `createQuestHUD` function from `@dcl/quests-client/dist/hud`. For example:

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { createQuestHUD } from '@dcl/quests-client/dist/hud'

const questHud = createQuestHUD()

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
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

The above code creates a Quest HUD object without customization, it will use the default styles for everything. You can find the defaults in the code [here](https://github.com/decentraland/quests-client/blob/main/src/hud.tsx) or you can just render the HUD to check how it looks.

When the quest is stated or it receives any player progress update, the `questHud.upsert` function is called to updates this UI. This function receives a `QuestInstace` object. It creates an SDK entity with this data to be used by a ReactECS UI component. This component is rendered in the scene UI, displaying the Quest progress, including which steps and tasks are completed or not.

###### Customizing the Quest HUD
```typescript
// index.ts

//....
const questHud = createQuestHUD({
  autoRender: true,
  leftSidePanel: {
    position: { top: '8%' }
  },
  questBox: {
    uiBackground: {
      color: Color4.fromHexString('ff2d5382')
    }
  }
})

//....
//....
```

The above code create a customized Quest HUD and it's rendered automatically so whenever the player starts the Quest or makes progress or `upsert` function is called, the Quest HUD will appear or be updated.

Also, this Quest HUD will be rendered `8%` far from the top of the screen because all the left side panel is pulled up (this will works for Worlds where there isn't a minimap), the default is `28%`. And., the Quest box will have a background color of `#ff2d5382`, which it's the primary color of Decentraland (kind of light red) with almost 50% of opacity.

You are also free to use the SDK to create your own custom UI to display quest progress based on this same information. See [Onscreen UI]({{< ref "/content/creator/sdk7/2d-ui/onscreen-ui.md" >}}) for guidance about how to do this.
