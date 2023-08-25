---
title: 'Quests SDK Library'
url: /creator/quests/sdk-client
weight: 4
---

Use the [Quests Client for SDK 7](https://github.com/decentraland/quests-client) library in your scenes (or portable experiences) to connect to the Quests Service to track player's progress, send events and receive updates of player's progress from your scenes,

## What does this library provide?

- An interface with the Quests Client API, to send your [Custom](/creator/quests/define#action-items) events and receive updates of player's progress.
- SDK System helpers to send [Location, Emote, Jump](/creator/quests/define#action-items) events automatically. (TODO)
- Default UI for your Quest HUD. (TODO)

## Usage

#### Installation

##### Via the Editor

Make sure you've [installed the Decentraland editor]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md#the-decentraland-editor" >}}).

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
- `state`: The progress of the player on the Quest defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

## Quest client methods

The following methods are available in the Quests Client:

- `startQuest`: Use this function to make the player start your Quest. In the background, the function calls the Quest RPC Service. The function receives a `StartQuestRequest` object that contains the Quest's id that you want to start. The function returns a `StartQuestResponse` object that contains the Quest Instance's id. Both objects are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `abortQuest`: Use this function to allow the player to abort your Quest. In the background, the function will call the Quest RPC Service. The function receives a `AbortQuestRequest` object that contains the player's instance id. The function returns a `AbortQuestResponse` that contains the result of the request, both in case of an error or success. Both objects are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `sendEvent`: Use this function send a custom event to the Quest RPC Service. The function receives an `Action` (action item with its type and parameters), representing an action that the player has already completed in the scene. The function returns an `EventResponse` object that contains the result of the request, both in case of an error or success. Both `Action` and `EventResponse` are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `onStarted`: Use this function to register one or multiple callbacks that are called when the player starts a Quest. Use this for the scene to react to the start of a Quest in any needed way. The callback receives a `QuestInstance` object that contains the information of the Quest that the player has started.

- `onUpdate`: Use this function to register one or multiple callbacks that are called whenever the player makes progress on a Quest. Use these callbacks to apply changes on your scene that correlate to this progress. The callback receives a `QuestInstance` object that contains the information of the Quest that the player has made progress on.

- `getInstances`: This function allows you as a creator to get all the Quest Instances of the player. The function returns an array of `QuestInstance` objects.

## Setting up the client

Start by importing `createQuestsClient` to initialize the Quests Client in your scene.

```typescript
// index.ts

//...
import { createQuestsClient } from '@dcl/quests-client'
```

The initialization of the Quests Client returns a promise that resolves when the Quests Client is ready to use. Run this code inside an async function. To do this, you can use the `executeTask` function, see [asynchronous functions]({{< ref "/content/creator/scenes/programming-patterns/async-functions.md" >}}).

The function `createQuestsClient()` takes a parameter containing the URL to connect to the [Quests API](creator/quests/overview/#services-architecture). The following options are available:

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

## React to changes on the player's progress

By now you have the client set up and listening to the Quests Service for changes on the current player's progress. You may want to react and apply different changes to your scene when the player makes progress on a Quest.

To react to these changes, register a callback:

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
      // update your state here or react to the quest updates
    })
  } catch (e) {
    console.error('Error on connecting to Quests Service')
  }
})
```

The `onUpdate` function receives a callback function that is called every time the player makes progress on a Quest. The callback receives a `QuestInstance` object that contains the information of the Quest that the player has made progress on.

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

## Trigger the Start of your Quest

Now you have the Quests Client ready to use and you are listening to the Quests Service for new changes on the player's progress. But you may want to trigger the start of a Quest when the player enters a specific area of your scene or when the player performs a specific action, like interacting with an NPC.

To trigger the start of a Quest, call the `startQuest` function. This function receives the id of the quest you want to start. But how can you do that since the `questClient` is scoped within `executeAsync` function? Well, you can make use of observables also known as event emitters in order to use the `questClient` from any part of your scene.

To do so, you can use the `mitt` library. You can find more information about this library [here](https://www.npmjs.com/package/mitt)

```bash
$ npm install mitt
```

In your scene code, you can create a new file with your event emitters.

```typescript
// utils.ts
import mitt from 'mitt'

export const questStartEmitter = mitt<{ start: boolean }>()
```

So the above code initializes a event emitter which will be used to trigger the start of a Quest. This event emitter "emits an event" called "start" with a boolean value. Now, you can import this emitter where you have the `questClient` initialized and listen to the `start` event.

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { questStartEmitter } from './utils'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl)
    console.log('Quests Client is ready to use!')

    client.onUpdate((quest: QuestInstance) => {
      // update your state here or react to the quest updates
    })

    questsStartEmitter.on('start', async (value: boolean) => {
      await questsClient.startQuest({ questId: MY_QUEST_ID })
    })
  } catch (e) {
    console.error('Error on connecting to Quests Service')
  }
})
```

In the previous code, a constant value, containing the Quest ID you want the player to start, is defined. Then, the `questStartEmitter` is imported from the `utils.ts` file. Finally, the `questStartEmitter` is listening to the `start` event and when the event is emitted, the `startQuest` function is called with the Quest ID.

What it's left now is to emit the `start` event when you want the player to start the Quest. For example, you can emit the `start` event when the player clicks on a Cube mesh. Here is a pseudocode as example:

```typescript
// cube.ts

//...
import { pointerEventsSystem, InputAction } from '@dcl/sdk/ecs'
import { questStartEmitter } from './utils'

//...
pointerEventsSystem.onPointerDown(
  cubeMeshEntity,
  (cmd) => {
    questStartObservable.emit('start', true)
  },
  { button: InputAction.IA_PRIMARY, hoverText: 'E to Start Quest' }
)
//...
```

#### React to the start of your Quest

After your player starts your Quest, you may want to react to this event. So in order to do so, you can register a callback using `onStarted` function provided by the client:

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { questStartEmitter } from './utils'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl)
    console.log('Quests Client is ready to use!')

    client.onUpdate((quest: QuestInstance) => {
      // update your state here or react to your quest updates
    })

    client.onStarted((quest: QuestInstance) => {
      // react to the start of your Quest
    })

    questsStartEmitter.on('start', async (value: boolean) => {
      await questsClient.startQuest({ questId: MY_QUEST_ID })
    })
  } catch (e) {
    console.error('Error on connecting to Quests Service')
  }
})
```

#### Sending Events to the Quests Service

You may be asking how you can send your custom events when the player performs an action that it's needed to make progress. Well, as we did it with the `startQuest` function, we can use an event emitter to send events to the Quests Service.

Let's go back to our `utils.ts` file and add a new event emitter to send events to the Quests Service. Also, we need to import the `Action` type provided by the Quests Client library and defined in the Quest's Protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

```typescript
// utils.ts
import mitt from 'mitt'
import { Action } from '@dcl/quests-client'

export const questStartEmitter = mitt<{ start: boolean }>()
export const questEventEmitter = mitt<{ action: Action }>()
```

So the above code initializes a event emitter which will be used to send events to the Quests Service. This event emitter "emits an event" called "action" with an `Action` object. Now, you can import this emitter where you have the `questClient` initialized and listen to the `action` event.

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { questStartEmitter, questEventEmitter } from './utils'

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl)
    console.log('Quests Client is ready to use!')

    client.onUpdate((quest: QuestInstance) => {
      // update your state here or react to the quest updates
    })

    questsStartEmitter.on('start', async (value: boolean) => {
      await questsClient.startQuest({ questId: MY_QUEST_ID })
    })

    questEventEmitter.on('action', async (action: Action) => {
      await questsClient.sendEvent({ action })
    })
  } catch (e) {
    console.error('Error on connecting to Quests Service')
  }
})
```

In the previous code, we've added the `questEventEmitter` and it's listening to the `action` event and when the event is emitted, the `sendEvent` function is called with the `Action` object.

After that, you can make use of the `questEventEmitter` in any part of your code to send events to the Quests Service, just importing it and emiting the `action` event. Here it's a pseudocode example:

```typescript
// another-file.ts

//...

import { questEventEmitter } from './utils'

//...

questEventEmitter.emit('action', {
  type: 'CUSTOM',
  parameters: { id: 'my-custom-action-id' },
})
```
