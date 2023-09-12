---
title: 'Defining a Quest'
url: /creator/quests/define
weight: 2
---

Below is the full Quest schema as a Typescript type:

```typescript
{
    name: string,
    description: string,
    imageUrl: string,
    definition: {
        steps: {
            id: string,
            description: string,
            tasks: {
                id: string,
                description: string,
                actionItems: {
                    type: string,
                    parameters: {[key: string]: string]}
                }[]
            }[]
        }[],
        connections: {
            stepFrom: string,
            stepTo: string
        }[]
    },
    reward: {
        hook: {
            webhookUrl: string,
            requestBody: { [key: string]: string } | null
        },
        items: {
            name: string,
            imageLink: string
        }[]
    } | null,
}
```

## Basic fields

- `name`: The name of the Quest. This name is displayed in Decentraland.
- `description`: A short description of the Quest, to give the player some idea of what the Quest is about.
- `imageUrl`: URL to an image to display in Decentraland along with the quest.

## Steps definition section

The `definition` field is the most important section, as it defines the actual steps and their order.

- `steps`: An array of steps. Each step has an `id`, a `description` and an array of `tasks`. Steps are **ordered**, which means that a player will need to go through each of them, fulfilling each of their tasks in other to advance to the next one in the definition.
  - `id`: A unique identifier of the step.
  - `description`: A short description of the step. This information is suitable to be used as a display name or human friendly label for the current step to be seen by players of the quest through the HUD.
  - `tasks`: An array of tasks that the player has to complete to consider the step as done. Each task has an `id`, a `description` and an array of `actionItems`. The order of the tasks in a step is not important, the player will need to fulfill each of them to advance to the next one.
    - `id` A unique identifier of the task.
    - `description` A short description of the task. This information is suitable to be used as a display name or human friendly label for the current task to be seen by players of the quest through the HUD.

    - `actionItems`: An array of action items that the player has to complete to consider the task as done. *The order of the actions defined is not important*, the player is able to fulfill each of the different items in a single task in any order. Each action item has a `type` and a `parameters` field.
      - `type`: The type of the action item. Find the supported types [here]({{< ref "/content/creator/quests/define.md#action-items" >}}).
      - `parameters`: An object with the parameters needed to complete the action item. The parameters are depend on the type of the action item. Find the supported parameters [here]({{< ref "/content/creator/quests/define.md#action-items" >}}).

      **Note:** `actionItems` **will not be publicly available** for anyone but the owner of the quest.
- `connections`: An array of connections. Each connection has a `stepFrom` and a `stepTo` field. The connections define the order of the steps. Steps that don't have a `stepFrom` in this array are considered the starting steps of the Quest. Steps that don't have a `stepTo` in this array are considered the ending steps of the Quest. Note that one step can lead to multiple steps at once.
  - `stepFrom`: The `id` of the step where the connection starts.
  - `stepTo`: The `id` of the step where the connection ends.

The relation between steps, tasks, and action items is as follows:

- A **Quest** may have multiple **Steps**
- Each **Step** can may have multiple **Tasks**
- Each **Task** may have multiple **Action items**.

To complete each of these:

- To complete a **Quest**, you must complete all ending steps (steps with no `stepTo` field in the `connections` section).
- To complete a **Step**, you must complete all its **Tasks**
- To complete a **Task**, you must complete all its **Action items**

## Rewards section

Finally, let's take a look at the `reward` section. This section defines the reward that players will receive after completing the quest. It's not mandatory for a Quest to give a reward to the player, this section is optional.

- `hook`: An object with two fields: `webhookUrl` and `requestBody`.
  - `webhookUrl`: The URL of the webhook that is called when the Quest is completed.
  - `requestBody`: An optional object with parameters that are sent to the webhook. The webhook is called via a POST request with the `requestBody` as the body of the request.
- `items`: An array of items. Each items is a reward that the Quest gives to each player after completing the Quest. Each item has a `name` and an `imageLink` field.
  - `name`: The name of the item.
  - `imageLink`: The URL of the image that is used to display the item on Decentraland.

Read more about the Quest's rewards [here]({{< ref "/content/creator/quests/rewards.md" >}}).

## Action Items

Action items are the smallest unit of work that the player must complete. All action items in a task must be completed to consider the task as done.

The following set of types are supported, each with their corresponding parameters.

- **Location**: This action item is used to check if the player is at specific coordinates. This action is detected by the Quest Client library's system helpers. The `parameters` are the coordinates of a parcel of LAND on the Decentraland map. The `parameters` are:

  - `x`: The x coordinate of the location.
  - `y`: The y coordinate of the location.

```typescript
    {
        type: "LOCATION",
        parameters: { "x": string, "y": string }
    }
```

- **Jump**: This action item is used to check if the player has jumped. This action is detected by the Quest Client library's system helpers. The `parameters` are the coordinates of parcel of LAND on the Decentraland map where the player has to jump. The `parameters` are:

  - `x`: The x coordinate of the location.
  - `y`: The y coordinate of the location.

```typescript
    {
        type: "JUMP",
        parameters: { "x": string, "y": string }
    }
```

- **Emote**: This action item is used to check if the player has played an emote. This action is detected by the Quest Client library's system helpers. The `parameters` are the coordinates of the parcel of LAND on the Decentraland map where the player has to play the emote, and the `emote_id` of the emote that the player has to play. The `parameters` are:

  - `x`: The x coordinate of the location.
  - `y`: The y coordinate of the location.
  - `emote_id`: The `emote_id` of the emote that the player has to play.

```typescript
    {
        type: "EMOTE",
        parameters: { "x": string, "y": string, "emote_id": string }
    }
```

- **Custom**: This action item is used to check if the player has completed a custom action. This action is a "third-party" action, so the Quest Creator is responsible for sending the event to the Quest Service when it occurs. There is only one field within `parameters`. The field is:

  - `id`: The `id` of the custom action that the player has to complete.

```typescript
    {
        type: "CUSTOM",
        parameters: { "id": string }
    }
```

An example of a `CUSTOM` action item could be a "click a box", or "kill 10 zombies". The Quest Creator is responsible for sending the event to the Quest Service when the player has completed the action.

{{< hint info >}}
**💡 Tip**: If the player must repeat a same action multiple times, add the same action item more than once within the `actionItems` array.
{{< /hint >}}

## Examples of Defined Quests

###### Linear Quest

A linear Quest "Z World", with just only two step and with `CUSTOM` action types:

```json
{
  "name": "Z World",
  "description": "Zombies World",
  "imageUrl": "https://the-image-u-want-to-be-displayed-on-dcl-explorer.com",
  "definition": {
    "steps": [
      {
        "id": "STEP_1",
        "description": "First Step",
        "tasks": [
          {
            "id": "STEP_1_1",
            "description": "First Task of First Step",
            "actionItems": [
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "CUSTOM_EVENT_1"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "STEP_2",
        "description": "Second Step",
        "tasks": [
          {
            "id": "STEP_2_1",
            "description": "First Task of Second Step",
            "actionItems": [
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "CUSTOM_EVENT_2"
                }
              }
            ]
          }
        ]
      }
    ],
    "connections": [
      {
        "stepFrom": "STEP_1",
        "stepTo": "STEP_2"
      }
    ]
  }
}
```

###### Linear Quest 2

A linear Quest "Z World", with 3 steps and with `CUSTOM`, `LOCATION` ad `JUMP` action types:

```json
{
  "name": "Z World",
  "description": "Zombies World",
  "imageUrl": "https://the-image-u-want-to-be-displayed-on-dcl-explorer.com",
  "definition": {
    "steps": [
      {
        "id": "STEP_1",
        "description": "First Step",
        "tasks": [
          {
            "id": "STEP_1_1",
            "description": "First Task of First Step",
            "actionItems": [
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "CUSTOM_EVENT_1"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "STEP_2",
        "description": "Second Step",
        "tasks": [
          {
            "id": "STEP_2_1",
            "description": "First Task of Second Step",
            "actionItems": [
              {
                "type": "LOCATION",
                "parameters": {
                  "x": "100",
                  "y": "-101"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "STEP_3",
        "description": "Third Step",
        "tasks": [
          {
            "id": "STEP_3_1",
            "description": "First Task of Thitd Step",
            "actionItems": [
              {
                "type": "JUMP",
                "parameters": {
                  "x": "105",
                  "y": "-101"
                }
              }
            ]
          }
        ]
      }
    ],
    "connections": [
      {
        "stepFrom": "STEP_1",
        "stepTo": "STEP_2"
      },
      {
        "stepFrom": "STEP_2",
        "stepTo": "STEP_3"
      }
    ]
  }
}
```

###### Linear Quest 3

A linear Quest "Z World", similar to "Linear Quest 2" but this one **gives rewards to its players**. It uses `https://the-rewards-webhook-url.com/rewards` as the webhook URL, so this endpoint will be called when a user completes this Quest. The request to this server includes a JSON in the Request Body. The JSON has two placeholders that are replaced by the Quests Server with the actual values. The rewards include **only one** item called "Zombie Head", with the image `https://the-wearable-item-image.com`:

```json
{
  "name": "Z World",
  "description": "Zombies World",
  "imageUrl": "https://the-image-u-want-to-be-displayed-on-dcl-explorer.com",
  "definition": {
    "steps": [
      {
        "id": "STEP_1",
        "description": "First Step",
        "tasks": [
          {
            "id": "STEP_1_1",
            "description": "First Task of First Step",
            "actionItems": [
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "CUSTOM_EVENT_1"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "STEP_2",
        "description": "Second Step",
        "tasks": [
          {
            "id": "STEP_2_1",
            "description": "First Task of Second Step",
            "actionItems": [
              {
                "type": "LOCATION",
                "parameters": {
                  "x": "100",
                  "y": "-101"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "STEP_3",
        "description": "Third Step",
        "tasks": [
          {
            "id": "STEP_3_1",
            "description": "First Task of Third Step",
            "actionItems": [
              {
                "type": "JUMP",
                "parameters": {
                  "x": "105",
                  "y": "-101"
                }
              }
            ]
          }
        ]
      }
    ],
    "connections": [
      {
        "stepFrom": "STEP_1",
        "stepTo": "STEP_2"
      },
      {
        "stepFrom": "STEP_2",
        "stepTo": "STEP_3"
      }
    ]
  },
  "reward": {
    "hook": {
      "webhookUrl": "https://the-rewards-webhook-url.com/rewards",
      "requestBody": {
        "player": "{user_address}",
        "quest": "{quest_id}",
        "myIdentifier": "my-identifier-123-456"
      }
    },
    "items": [
      {
        "name": "Zombie Head",
        "imageLink": "https://the-wearable-item-image.com"
      }
    ]
  }
}
```

{{< hint info >}}
**💡 Tip**: To give more than one item as a reward, add more items to the `items` array. These images may be used to display a quest's rewards in-world.
{{< /hint >}}

###### Branching Quest

This Quest is \*more complex. A Branching Quest "Z World", with 4 steps:

- `STEP_1_1`: **One** of two possible **fist steps** of the Quest. It has two tasks: `STEP_1_1` and `STEP_1_2`. Both tasks have only one action item, and both action items are `CUSTOM` action items.

  - The first task has a `CUSTOM` action item with `CUSTOM_EVENT_1` as the `id` of the custom event that the player has to complete.
  - The second task has a `CUSTOM` action item with `SECOND_TASK_COLLECT_EVENT` as the `id` of the custom event that the player has to complete. This step has a connection to `STEP_2`.

- `STEP_1_2`: **One** of two possible **fist steps** of the Quest. It has two tasks: `STEP_1_2_1` and `STEP_1_2_2`.
  - The first task has a `LOCATION` action item with `100` as the `x` coordinate and `-101` as the `y` coordinate.
  - The second task has **two** `CUSTOM` action items with `SECOND_TASK_COLLECT_EVENT` as the `id` of the custom event that the player has to complete. As there are two identical action items, the action has to be repeated by the user. This step has a connection to `STEP_2`.

{{< hint info >}}
**📔 Note**:
`STEP_1_1` and `STEP_1_2` are two different steps, but they both lead to `STEP_2`. This means that the player must complete `STEP_1_1` **and** `STEP_1_2` to continue to `STEP_2` and the other next steps.
{{< /hint >}}

- `STEP_2`: It has one task: `STEP_2_1`. This task has two action items: `JUMP` and `LOCATION`. The `JUMP` action item has `105` as the `x` coordinate and `-101` as the `y` coordinate. The `LOCATION` action item has `103` as the `x` coordinate and `-101` as the `y` coordinate. This step has a connection to `STEP_3`.

- `STEP_3`: It has one task: `STEP_3_1`. This task has three action items: `CUSTOM`, `CUSTOM` and `CUSTOM`. The first two `CUSTOM` action items have `USERACTION_STEP_3` as the `id` of the custom event that the player has to complete. Once more, since the action items are identical, the user must repeat the same action. The third `CUSTOM` action item has `ANOTHER_USERACTION_STEP_3` as the `id` of the custom event that the player has to complete. This step has no connections, so it's considered the last step of the Quest. After finishing this step, the Quest is completed.

```json
{
  "name": "Z World",
  "description": "Zombies World (branching version)",
  "imageUrl": "https://the-image-u-want-to-be-displayed-on-dcl-explorer.com",
  "definition": {
    "steps": [
      {
        "id": "STEP_1_1",
        "description": "First Step 1",
        "tasks": [
          {
            "id": "STEP_1_1",
            "description": "First Task of First Step 1",
            "actionItems": [
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "CUSTOM_EVENT_1"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "STEP_1_2",
        "description": "First Step 2",
        "tasks": [
          {
            "id": "STEP_1_2_1",
            "description": "First Task of First Step 2",
            "actionItems": [
              {
                "type": "LOCATION",
                "parameters": {
                  "x": "100",
                  "y": "-101"
                }
              }
            ]
          },
          {
            "id": "STEP_1_2_2",
            "description": "Second Task of First Step 2",
            "actionItems": [
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "SECOND_TASK_COLLECT_EVENT"
                }
              },
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "SECOND_TASK_COLLECT_EVENT"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "STEP_2",
        "description": "Second Step",
        "tasks": [
          {
            "id": "STEP_2_1",
            "description": "First Task of Second Step",
            "actionItems": [
              {
                "type": "JUMP",
                "parameters": {
                  "x": "105",
                  "y": "-101"
                }
              },
              {
                "type": "LOCATION",
                "parameters": {
                  "x": "103",
                  "y": "-101"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "STEP_3",
        "description": "Third Step",
        "tasks": [
          {
            "id": "STEP_3",
            "description": "First Task of Third Step",
            "actionItems": [
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "USERACTION_STEP_3"
                }
              },
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "USERACTION_STEP_3"
                }
              },
              {
                "type": "CUSTOM",
                "parameters": {
                  "id": "ANOTHER_USERACTION_STEP_3"
                }
              }
            ]
          }
        ]
      }
    ],
    "connections": [
      {
        "stepFrom": "STEP_1_1",
        "stepTo": "STEP_2"
      },
      {
        "stepFrom": "STEP_1_2",
        "stepTo": "STEP_2"
      },
      {
        "stepFrom": "STEP_2",
        "stepTo": "STEP_3"
      }
    ]
  },
  "reward": {
    "hook": {
      "webhookUrl": "https://the-rewards-webhook-url.com/rewards",
      "requestBody": {
        "player": "{user_address}",
        "quest": "{quest_id}",
        "myIdentifier": "my-identifier-123-456"
      }
    },
    "items": [
      {
        "name": "Zombie Head",
        "imageLink": "https://the-wearable-item-image.com"
      }
    ]
  }
}
```
