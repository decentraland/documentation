---
title: "SDK Client"
url: /creator/quests/sdk-client
weight: 4
---

In order to connect to the Quests Service to track users' progress, send events and receive updates of users' progress from your scenes, you need to use the [Quests Client for SDK 7](https://github.com/decentraland/quests-client).

#### What do we provide here? 

- Quests Client API to send your [Custom](/creator/quests/define#action-items) events and receive updates of users' progress.
- SDK System helpers to send [Location, Emote, Jump](/creator/quests/define#action-items) events automatically. (TODO)
- Default UI for your Quest HUD. (TODO)

## Installation 
Run this command in your scene's directory:

```bash
$ npm install @dcl/quests-client
```

## Usage

#### Quests Client methods

You can find below types defined in [Quests Client for SDK 7](https://github.com/decentraland/quests-client).

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

- `startQuest`: This function allows you as a creator to make the user start your Quest. In the background, the function will call the Quest RPC Service. The function receives a `StartQuestRequest` object that contains the Quest's id that you want to start. The function returns a `StartQuestResponse` object that contains the Quest Instance's id. Both objects are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `abortQuest`: This function allows you as a creator to allow the users to abort your Quest if they want to. In the background, the function will call the Quest RPC Service. The function receives a `AbortQuestRequest` object that contains the user's instance id. The function returns a `AbortQuestResponse` that contains the result of the request, it may be an error or a success. Both objects are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `sendEvent`: This function allows you as a creator to send a custom event to the Quest RPC Service. The function receives an `Action` (action item with its type and parameters) that the user should have done. The function returns an `EventResponse` object that contains the result of the request, it may be an error or a success. Both `Action` and `EventResponse` are defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `onStarted`: This function allows you as a creator to register multiple callbacks that will be called when the user starts a Quest. If you as a creator want to react to the start of a Quest, you can register a callback here. The callback receives a `QuestInstance` object that contains the information of the Quest that the user has started. The `QuestInstance` object has the following fields:
    - `id`: It's the id of the Quest Instance. It's a unique identifier of the user's Quest Instance.
    - `quest`: It's the Quest object defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).
    - `state`: It's the progress of the user on the Quest defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `onUpdate`: This function allows you as a creator to register multiple callback that will be called when the user makes progress on a Quest. You, as a creator, do want to react to progress to apply chanes on your scene. The callback receives a `QuestInstance` object that contains the information of the Quest that the user has made progress on. The `QuestInstance` object has the following fields:
    - `id`: It's the id of the Quest Instance. It's a unique identifier of the user's Quest Instance.
    - `quest`: It's the Quest object defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).
    - `state`: It's the progress of the user on the Quest defined in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

- `getInstances`: This function allows you as a creator to get all the Quest Instances of the user. The function returns an array of `QuestInstance` objects.

#### Setting up the client

First off, you should start by importing a `createQuestsClient` to initialize the Quests Client in your scene.

```typescript
// index.ts

//...
import { createQuestsClient } from '@dcl/quests-client'
```

The initialization of the Quests Client returns a promise that resolves when the Quests Client is ready to use, so you should run this code in async function. To run this code in async function, you could use the `executeTask` function from the SDK.

The URL to connect to [Quests API](creator/quests/overview/#services-architecture), you can use the following URLs: 
- Development: `wss://quests-rpc.decentraland.zone`
- Production: `wss://quests-rpc.decentraland.org`

Or you can set up your own Quests Service locally for development or testing. You can find more information on how to do so on [Quests Service's repository](https://github.com/decentraland/quests)

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient } from '@dcl/quests-client'

executeTask(async() => {
    const serviceUrl = 'wss://quests-rpc.decentraland.zone'

    try {
        const questsClient = await createQuestsClient(serviceUrl)
        console.log("Quests Client is ready to use!")
    } catch (e) {
        console.error("Error on connecting to Quests Service")
    }
})

```
#### React to changes on user's progress

Well so now, you have the client ready to use and it's listening to the Quests Service for new changes on logged-in user's progress. But you may want to react and apply different changes to your scene when the user makes progress on a Quest.

To do so, you can register a callback for that: 

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'

executeTask(async() => {
    const serviceUrl = 'wss://quests-rpc.decentraland.zone'

    try {
        const questsClient = await createQuestsClient(serviceUrl)
        console.log("Quests Client is ready to use!")

        client.onUpdate((quest: QuestInstance) => {
          // update your state here or react to the quest updates
        })

    } catch (e) {
        console.error("Error on connecting to Quests Service")
    }
})
```

The `onUpdate` function receives a callback that will be called when the user has made progress on a Quest. The callback receives a `QuestInstance` object that contains the information of the Quest that the user has made progress on.

The `QuestInstance` object has the following fields:

```typescript 
type QuestInstance = {
    id: string
    quest: Quest
    state: QuestState
}
```

- `id`: It's the id of the Quest Instance. It's a unique identifier of the user's Quest Instance.
- `quest`: It's the Quest object. You can find more information about the Quest object [here](/creator/quests/define).
- `state`: It's the progress of the user on the Quest. 

You can find `Quest` and `QuestState` types in the Quest's protocol file [here](https://github.com/decentraland/quests/blob/main/docs/quests.proto).

#### Trigger the Start of your Quest

Now you have the Quests Client ready to use and you are listening to the Quests Service for new changes on the user's progress. But you may want to trigger the start of a Quest when the user enters a specific area of your scene or when the user interacts with an NPC, or when the user clicks on a button. So, let's see how to do that.

To trigger the start of a Quest, you need to call the `startQuest` function from the Quests Client. This function receives the Quest's id that you want to start. But how can you do that since the `questClient` is scoped within `executeAsync` function? Well, you can make use of observables also known as event emitters in order to use the `questClient` from any part of your scene.

To do so, you can use the `mitt` library. You can find more information about this library [here](https://www.npmjs.com/package/mitt)

```bash
$ npm install mitt
```

In your scene code, you can create a new file with your event emitters. 

```typescript
// utils.ts
import mitt from 'mitt'

export const questStartEmitter = mitt<{start: boolean}>()
```

So the above code initializes a event emitter which will be used to trigger the start of a Quest. This event emitter "emits an event" called "start" with a boolean value. Now, you can import this emitter where you have the `questClient` initialized and listen to the `start` event. 

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { questStartEmitter } from './utils'

const MY_QUEST_ID = "quest-id-1234-5678-9012"

executeTask(async() => {
    const serviceUrl = 'wss://quests-rpc.decentraland.zone'

    try {
        const questsClient = await createQuestsClient(serviceUrl)
        console.log("Quests Client is ready to use!")

        client.onUpdate((quest: QuestInstance) => {
          // update your state here or react to the quest updates
        })

        questsStartEmitter.on('start', (value: boolean) => {
            questsClient.startQuest({questId: MY_QUEST_ID})
        })

    } catch (e) {
        console.error("Error on connecting to Quests Service")
    }
})
```

In the previous code, a constant value, containing the Quest ID you want the user to start, is defined. Then, the `questStartEmitter` is imported from the `utils.ts` file. Finally, the `questStartEmitter` is listening to the `start` event and when the event is emitted, the `startQuest` function is called with the Quest ID.

What it's left now is to emit the `start` event when you want the user to start the Quest. For example, you can emit the `start` event when the user clicks on a Cube mesh. Here is a pseudocode as example: 

```typescript
// cube.ts

//...
import { pointerEventsSystem, InputAction } from '@dcl/sdk/ecs'
import { questStartEmitter } from './utils'

//...
pointerEventsSystem.onPointerDown(cubeMeshEntity, (cmd) => {
    questStartObservable.emit('start', true)
}, { button: InputAction.IA_PRIMARY, hoverText: "E to Start Quest" })
//...
```