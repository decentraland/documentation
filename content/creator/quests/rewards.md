---
title: 'Quest Rewards'
url: /creator/quests/rewards
weight: 3
---

A Quest can have rewards for the players who complete it. When a Quest is created, the creator can set up a reward, which consists of a webhook and a list of items.

The webhook is a URL that is called when the Quest is completed. The list of items includes one or several items to give to the player when the Quest is completed.

The **[Quests System](/creator/quests/overview)** is in charge of sending the request to the given webhook URL when it detects that a player has completed a quest.

## API Requirements

The interface with rewards servers is very flexible, as long as you meet the API requirements for the webhook endpoint. These are:

- POST Request: Use the parameters of a POST request to send any additional information needed by your service to give the reward to the player, in addition to the placeholders we provide.
- JSON Response: If the response's `ok` field is `true`, the Quests service considers that the reward correctly reached the player. If the `ok` field is `false`, it will interpret that the reward didn't reach the player.

```typescript
{
  ok: boolean
}
```

## Placeholder values

You can use a set of placeholders in the `webhookUrl` field to include some dynamic information about the player or the quest as part of the URL. The Quests service currently supports these placeholders:

- `{quest_id}`: The id of the Quest
- `{user_address}`: The Ethereum address of the player

The **[Quests System](/creator/quests/overview)** replaces the placeholders with the actual values before sending the request to the webhook URL.

The example below uses both these placeholders to construct the URL:

```typescript
{
    ...,
    reward: {
        hook: {
            webhookUrl: "https://my-rewards-webhook.com/quests/{quest_id}/user/{user_address}",
        },
        ...
    }
}
```

## Request body

If you need to send extra information to your rewards server or a specific value to your webhook, you can optionally include a `requestBody` when you create the Quest. This `requestBody` will be sent as the body of the POST request to the webhook URL. The body can include the same set of placeholder values described in the previous section.

The example below includes additional information in the request body:

```typescript
{
    ...,
    reward: {
        hook: {
            webhookUrl: "https://my-rewards-webhook.com/quests/{quest_id}",
            requestBody: {
                "user": "{user_address}"
                "your_service_key": "your_service_value"
            }
        },
        ...
    }
}
```

Another Example:

```typescript
{
    ...,
    reward: {
        hook: {
            webhookUrl: "https://my-rewards-server.com/quests",
            requestBody: {
                "user": "{user_address}"
                "quest": "{quest_id}",
                "your_service_key": "your_service_value"
            }
        },
        ...
    }
}
```

See [defining a quest](/creator/quests/define) for more details on the quest definition JSON structure.
