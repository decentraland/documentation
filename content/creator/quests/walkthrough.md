---
title: 'Walkthrough'
url: /creator/quests/walkthrough
weight: 6
---

To summarize the contents in this section, let's go ahead and create our first quest!

To set up the context, we are going to create a pick up quest, where the players will need to collect different items in our scene to prepare for a battle and after that move to the battle zone!

First things first, we need to set up our quest: we will go through its definition, configuration and publication; later on, we are going to dive into the code in order to wire things up in our scene; and finally we will see the results in the world!

# Define the quest

We will start off by defining our quest as seen in the [Quest Definition page]({{< ref "/content/creator/quests/define.md" >}}).

### Define the quest steps and tasks

In our case, we will need two steps:
1. Prepare for battle
2. Go to the battle zone

For the first part, the player will need to collect some items we are going to provide them, these are the 1) armor, 2) ammo and 3) medikit. As all of these can be done in any order during the step of preparation, we can model these as different independent tasks like so:
```json
[
  {
    "id": "pick-up-armor",
    "description": "Pick up the armor",
    "actionItems": ...
  },
  {
    "id": "pick-up-ammo",
    "description": "Pick up the ammo",
    "actionItems": ...
  },
  {
    "id": "pick-up-medikit",
    "description": "Pick up the medikit",
    "actionItems": ...
  }
]
```

Amazing, we have an array of tasks with their ids and description. Remember, the description will enable the client to show a friendly name for the player to understand the task at hand, so be sure to have a short and sweet name here!

Now, we are missing the actual `actionItems`, these are the events that will enable the progression through the quest to be made. In our case, we can use `CUSTOM` actions for all of them and we'll add some parameters to each of them to specify the kind of action that they mean to us, which is `PickUp` for picking up stuff, and the id of each of our items. With actions and tasks specified, our first step is complete and looks like the following:
```json
{
    "id": "prepare-for",
    "description": "Prepare for the Battle",
    "tasks": [
      {
        "id": "pick-up-armor",
        "description": "Pick up the armor",
        "actionItems": [
          {
            "type": "CUSTOM",
            "parameters": {
              "kind": "PickUp",
              "id": "armor"
            }
          }
        ]
      },
      {
        "id": "pick-up-ammo",
        "description": "Pick up the ammo",
        "actionItems": [
          {
            "type": "CUSTOM",
            "parameters": {
              "kind": "PickUp",
              "id": "ammo"
            }
          }
        ]
      },
      {
        "id": "pick-up-medikit",
        "description": "Pick up the medikit",
        "actionItems": [
          {
            "type": "CUSTOM",
            "parameters": {
              "kind": "PickUp",
              "id": "medikit"
            }
          }
        ]
      }
    ]
  }
```

Now that the player is prepared and has all the required items, they need to move to the battle zone. For this, we will create a new step, this is simpler than the previous and will only require a single task which is to move to the desired spot. In order to signal this, we can use a `LOCATION` action with the coordinates we want them to move to.
```json
{
    "id": "go-to-zone",
    "description": "Go to the Battle Zone",
    "tasks": [
      {
        "id": "go-to-battle-zone",
        "description": "Go to the Battle Zone",
        "actionItems": [
          {
            "type": "LOCATION",
            "parameters": {
              "y": "1",
              "x": "1"
            }
          }
        ]
      }
    ]
}
```

### Connect the steps in the quest

And with this, the steps for our quest are ready! Now, we still need to create the connections between them, so that the `go-to-zone` happens after the prepartion is completed. For this we will define the `connections` as follows:
```json
{
    "connections": [
      {
        "stepFrom": "prepare-for",
        "stepTo": "go-to-zone"
      }
    ]
}
```

Since `prepare-for` is not referred as a `stepTo` in any connection, it will be available as a first step in our quest.


Filling out a couple more details in our quest the final configuration looks as follows:
```json
{
    "name": "Prepare for Battle",
    "image_url": "https://raw.githubusercontent.com/decentraland/sdk7-goerli-plaza/main/Gnark/images/scene-thumbnail.png",
    "definition": {
        "steps": [
          {
            "id": "prepare-for",
            "description": "Prepare for the Battle",
            "tasks": [
              {
                "id": "pick-up-armor",
                "description": "Pick up the armor",
                "actionItems": [
                  {
                    "type": "CUSTOM",
                    "parameters": {
                      "kind": "PickUp",
                      "id": "armor"
                    }
                  }
                ]
              },
              {
                "id": "pick-up-ammo",
                "description": "Pick up the ammo",
                "actionItems": [
                  {
                    "type": "CUSTOM",
                    "parameters": {
                      "kind": "PickUp",
                      "id": "ammo"
                    }
                  }
                ]
              },
              {
                "id": "pick-up-medikit",
                "description": "Pick up the medikit",
                "actionItems": [
                  {
                    "type": "CUSTOM",
                    "parameters": {
                      "kind": "PickUp",
                      "id": "medikit"
                    }
                  }
                ]
              }
            ]
          },
          {
            "id": "go-to-zone",
            "description": "Go to the Battle Zone",
            "tasks": [
              {
                "id": "go-to-battle-zone",
                "description": "Go to the Battle Zone",
                "actionItems": [
                  {
                    "type": "LOCATION",
                    "parameters": {
                      "y": "1",
                      "x": "1"
                    }
                  }
                ]
              }
            ]
          }
        ],
        "connections": [
          {
            "stepFrom": "prepare-for",
            "stepTo": "go-to-zone"
          }
        ]
    }
}
```

### Upload the quest

Having our quest defined, we are going to save it to disk as `pickup-scene.json` and the next step is to upload it to the Quests server. For this task, we are going to take advantage of the official [Quests CLI]({{< ref "/content/creator/quests/cli.md#create-a-new-quest-with-a-json-file" >}}).

Jump into your terminal of choice and execute the following command:
```bash
npx @dcl/sdk-commands quests --create-from-json <absolute_base_path>/pickup-scene.json
```

This will open up a new tab your default browser showing the confirmation of the new quest to be uploaded. Sign in with your wallet and submit your quest to the server. Back in the terminal a message will be waiting for you with the confirmation of the new quest created and activated. **Remember the quest id provided here as it will be important later on to connect the definition with our scene logic.**

# Wire things up on the scene

With our newly created quest already uploaded, we can move forward and wire things up in the scene. In this step, we will be creating the components and interactions necessary to make our quest come to life!

### Connect the quest client and HUD

To start off, let's create a client to connect with our scene. [You can review the documentation for it here]({{< ref "/content/creator/quests/client.md" >}}).

```typescript
const ws = 'wss://quests-rpc.decentraland.org'

// replace <QUEST_ID> below with the id returned by the CLI in the uploading quest phase
const quests = await createQuestsClient(ws, '<QUEST_ID>')

```

We will use the client returned to react to events coming from the server:
```typescript
quests.onStarted((questInstance) => {
  if (questInstance.quest.id === QUEST_ID) {
    questInstanceId = questInstance.id
    updateFromState(questInstance.state)
    hud.upsert(generateQuestUI(questInstance))
    questStarted = true
  }
})

quests.onUpdate((questInstance) => {
  if (questInstance.id === questInstanceId) {
    updateFromState(questInstance.state)
    hud.upsert(generateQuestUI(questInstance))
  }
})
```

*Note:* In the above example we are also using the HUD described [in the SDK section as well]({{< ref "/content/creator/quests/client.md#quest-hud---an-sdk-ui-for-your-quest" >}}).

And we will do the opposite to send events to the server whenever the player acts on our scene. For this we will use the `mitt` lib [as described here]({{< ref "/content/creator/quests/client.md#using-observables" >}}) to generate events in our scene code.
```typescript
export const questEventsObservable = mitt<{ message: Action }>()

questEventsObservable.on('message', async (action) => {
  await quests.sendEvent({ action })
})

questStartObservable.on('start', async () => {
  await quests.startQuest()
})
```

### Create the items in each step

Now that we are connected to the Quests server and receiving updates on new events and the progress of the user, let's instantiate the required entities and components based on the current step of the user.

```typescript
export function updateFromState(state: QuestState) {
  if (state.stepsLeft === 0) {
    onQuestComplete()
  } else if (state.stepsCompleted.length === 0) {
    onQuestStart()
  } else if (state.stepsCompleted.includes('prepare-for')) {
    onAllItemsPickedUp()
  }
}

export function onQuestStart() {
  if (step !== 'prepare-for') {
    spawnItemsToPickup()
    step = 'prepare-for'
  }
}

export function onAllItemsPickedUp() {
  if (step !== 'go-to-zone') {
    spawnZone()
    step = 'go-to-zone'
  }
}

export function onQuestComplete() {
  if (step !== 'completed') {
    step = 'completed'
  }
}

export function spawnItemsToPickup() {
  const redBaseEntity = engine.addEntity()
  GltfContainer.create(redBaseEntity, {
    src: 'models/spawnBaseRed.glb'
  })
  Transform.create(redBaseEntity, {
    position: Vector3.create(4, 0, 6)
  })

  const greenBaseEntity = engine.addEntity()
  GltfContainer.create(greenBaseEntity, {
    src: 'models/spawnBaseGreen.glb'
  })
  Transform.create(greenBaseEntity, {
    position: Vector3.create(8, 0, 10)
  })

  const blueBaseEntity = engine.addEntity()
  GltfContainer.create(blueBaseEntity, {
    src: 'models/spawnBaseBlue.glb'
  })
  Transform.create(blueBaseEntity, {
    position: Vector3.create(12, 0, 6)
  })

  instantiatePickableItem('models/medikit.glb', Vector3.create(4, 0.75, 6), 'sounds/medikitPickup.mp3', 'medikit')
  instantiatePickableItem('models/ammo.glb', Vector3.create(8, 0.75, 10), 'sounds/ammoPickup.mp3', 'ammo')
  instantiatePickableItem('models/armor.glb', Vector3.create(12, 0.75, 6), 'sounds/armorPickup.mp3', 'armor')
}

export function spawnZone() {
  const tileEntity = engine.addEntity()

  MeshRenderer.setPlane(tileEntity)

  Transform.create(tileEntity, {
    position: Vector3.create(13.25, 0.1, 13.25),
    rotation: Quaternion.fromEulerDegrees(90, 0, 0),
    scale: Vector3.create(4, 4, 4)
  })

  Material.setPbrMaterial(tileEntity, {
    albedoColor: { a: 0.9, r: 1, g: 0.0, b: 0.0 },
    metallic: 0
  })

  Zone.create(tileEntity, {
    playerDetectionArea: Vector3.create(3.5, 2, 3.5)
  })

  VisibilityComponent.create(tileEntity).visible = true
  AudioSource.create(tileEntity, {
    audioClipUrl: 'sounds/ready.mp3',
    playing: false,
    loop: false
  })
}
```

With our quests client integrated in our scene, using the default HUD and acting on the user interactions to keep track of the progress we finish the scene by setting the needed systems.

You can check and try the whole example scene [in the public repository for the pick up scene](https://github.com/decentraland/pickup-quest-scene).

### Publish your scene

Now that we have both our quest definition published and our scene code ready, we just need to [follow the steps to publish it to our desired environment](/creator/development-guide/sdk7/publishing).

```bash
npm run deploy -- --target peer-testing.decentraland.org
```

Verify that your scene was correctly deployed given the feedback of the command.

# Try it out!

The quest is ready and the scene is wired up and published as well, it's time to try it!

Log in to Explorer and go to your scene location and test it out!

<img src="/images/quests/quests-screenshot.png" alt="Quests screenshot" width="600"/>
