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

- `steps`: An array of steps. Each step has an `id`, a `description` and an array of `tasks`.
  - `id`: A unique identifier of the step.
  - `description`: A short description of the step.
  - `tasks`: An array of tasks that the player has to complete to consider the step as done. Each task has an `id`, a `description` and an array of `actionItems`.
    - `id` A unique identifier of the task.
    - `description` A short description of the task.
    - `actionItems`: An array of action items that the player has to complete to consider the task as done. Each action item has a `type` and a `parameters` field.
      - `type`: The type of the action item. Find the supported types [here](#action-items).
      - `parameters`: An object with the parameters needed to complete the action item. The parameters are depend on the type of the action item. Find the supported parameters [here](#action-items).
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

## Rewards section

Finally, let's take a look at the `reward` section. This section defines the reward that players will receive after completing the quest. It's not mandatory for a Quest to give a reward to the player, this section is optional.

- `hook`: An object with two fields: `webhookUrl` and `requestBody`.
  - `webhookUrl`: The URL of the webhook that is called when the Quest is completed.
  - `requestBody`: An optional object with parameters that are sent to the webhook. The webhook is called via a POST request with the `requestBody` as the body of the request.
- `items`: An array of items. Each items is a reward that the Quest gives to each player after completing the Quest. Each item has a `name` and an `imageLink` field.
  - `name`: The name of the item.
  - `imageLink`: The URL of the image that is used to display the item on Decentraland.

Read more about the Quest's rewards [here](/creator/quests/rewards).

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

## Example of a Defined Quest

```typescript

```
