---
title: "Defining a Quest"
url: /creator/quests/define
weight: 2
---

To start getting knowledge of how to define a Quest, let's take a look at the Quest schema as a Typescript type:
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

Let's start with the basics field:

- `name`: This is simple as its field's name. It's just the name of the Quest and the name that will be used on Decentraland to display it.
- `description`: A short description of the Quest to give the user an idea of what the Quest is about.
- `imageUrl`: The URL of the image that will be used to display the Quest on Decentraland.

Now, let's take a look at the `definition` field. This field is the most important one as it defines the steps and the order of the Quest.

- `steps`: This is an array of steps. Each step has an `id`, a `description` and an array of `tasks`. 
    - `id`: must be a unique identifier of the step. 
    - `description`: a short description of the step.
    - `tasks`: This is an array of tasks that the user has to complete to consider the step as done. Each task has an `id`, a `description` and an array of `actionItems`. 
        - `id` must be a unique identifier of the task. 
        - `description` is a short description of the task.
        - `actionItems`: This is an array of action items that the user has to complete to consider the task as done. Each action item has a `type` and a `parameters` field. 
            - `type`: This is the type of the action item. We currently support a set of `type`s. You can find the supported types [here](#action-items).
            - `parameters`: This is an object with the parameters needed to complete the action item. The parameters are different depending on the type of the action item. We currently support a set of `parameters` for each type. You can find the supported parameters [here](#action-items).
- `connections`: This is an array of connections. Each connection has a `stepFrom` and a `stepTo` field. The connections define the order of the steps. The steps that don't have a "from" defined within this array will be considered as the starting steps of the Quest. The steps that don't have a "to" defined within this array will be considered as the ending steps of the Quest. It's worth to mention that one step can take the users to more than one step.
    - `stepFrom`: it is the `id` of the step where the connection starts. 
    - `stepTo`: it is the `id` of the step where the connection ends.

Finally, let's take a look at the `reward` field. This field defines the reward that the user will receive when the Quest is completed. It's not mandatory for a Quest to give a reward to the user.

- `hook`: This is an object with two fields: `webhookUrl` and `requestBody`. 
    - `webhookUrl`: it is the URL of the webhook that will be called when the Quest is completed. 
    - `requestBody`: it is an object with the parameters that will be sent to the webhook. The webhook will be called with a POST request with the `requestBody` as the body of the request. The `requestBody` is optional.
- `items`: This is an array of items. The items are the rewards that the Quest will give to each user when they complete the Quest. Each item has a `name` and an `imageLink` field. 
    - `name`: is the name of the item. 
    - `imageLink`: is the URL of the image that will be used to display the item on Decentraland.

You can find more information about the Quest's reward [here](/creator/quests/rewards).

## Action Items

The action items are the tasks that the user has to complete to consider a task as done. We currently support a set of `type`s and `parameters` for each type.

- **Location**: This action item is used to check if the user is at a specific location. This action can be detected by the Quest Client library's system helpers. The `parameters` are the coordinates of the location. The `parameters` are:
    - `x`: The x coordinate of the location.
    - `y`: The y coordinate of the location.
```typescript
    {
        type: "LOCATION",
        parameters: { "x": string, "y": string }
    }
```

- **Jump**: This action item is used to check if the user has jumped. This action can be detected by the Quest Client library's system helpers. The `parameters` are the coordinates of the location where the user has to jump. The `parameters` are:
    - `x`: The x coordinate of the location.
    - `y`: The y coordinate of the location.
```typescript
    {
        type: "JUMP",
        parameters: { "x": string, "y": string }
    }
```

- **Emote**: This action item is used to check if the user has played an emote. This action can be detected by the Quest Client library's system helpers. The `parameters` are the coordinates of the location where the user has to play the emote and the `emote_id` of the emote that the user has to play. The `parameters` are:
    - `x`: The x coordinate of the location.
    - `y`: The y coordinate of the location.
    - `emote_id`: The `emote_id` of the emote that the user has to play.
```typescript
    {
        type: "EMOTE",
        parameters: { "x": string, "y": string, "emote_id": string }
    }
```

- **NPC interaction**: This action item is used to check if the user has interacted with an NPC. The `parameters` are the `npc_id` of the NPC that the user has to interact with. The `parameters` are:
    - `npc_id`: The `npc_id` of the NPC that the user has to interact with.
```typescript
    {
        type: "NPC_INTERACTION",
        parameters: { "npc_id": string }
    }
```

- **Custom**: This action item is used to check if the user has completed a custom action. This action is a "third-party" action so the Quest Creator is responsible to send the event to the Quest Service when it ocurrs. The `parameters` are the `id` of the custom action that the user has to complete. The `parameters` are:
    - `id`: The `id` of the custom action that the user has to complete.
```typescript
    {
        type: "CUSTOM",
        parameters: { "id": string }
    }
```

## Example of a Defined Quest
```typescript
```