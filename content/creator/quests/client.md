---
title: "SDK Client"
url: /creator/quests/sdk-client
weight: 4
---

In order to connect to the Quests Service to track users' progress, send events and receive updates of users' progress from your scenes, you need to use the [Quests Client for SDK 7](https://github.com/decentraland/quests-client).

#### What do we provide here? 

- Quests Client API to send your [Custom](/creator/quests/define#action-items) events and receive updates of users' progress.
- SDK System helpers to send [Location, Emote, Jump](/creator/quests/define#action-items) events automatically.
- Default UI for your Quest HUD. 

## Installation 
Run this command in your scene's directory:

```bash
$ npm install @dcl/quests-client
```

## Usage

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

You can find this types on Quest's protocol file. TODO: ATTACH IT HERE