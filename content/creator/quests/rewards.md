---
title: "Rewards"
url: /creator/quests/rewards
weight: 3
---

A Quest can have a rewards for the users who complete it. When a Quest is created, the creator could set a reward which consists of a webhook and a set of items.
The webhook is a URL that will be called when the Quest is completed. The items are a set of items (it could be only one item) that will be given to the user when the Quest is completed.

The **[Quests System](/creator/quests/overview)** is in charge of sending the request to the given webhook URL when it detects that a user has completed a quest.

## How flexible is this?
It's super flexible as long as you meet the API requirements for the webhook endpoint which are:

- POST Request: it's a POST request so that you can send additional information needed by your service to give the reward to the user, apart from the placeholders we provide.
- JSON Response: if the `ok` field is set to `true`, it should indicate that the reward was given to the user. If the `ok` field is set to `false`, it should indicate that the reward was not given to the user.
```typescript
{
    ok: boolean
}
```

You can also set a `requestBody` when you create the Quest. This `requestBody` will be sent as the body of the POST request to the webhook URL.

You are able to receive Quest or User information on your endpoint. You can use a set of placeholders in the `webhookUrl` and `requestBody` fields to receive this information. We currently support these placeholders:
- `{quest_id}`: the id of the Quest
- `{user_address}`: the Ethereum address of the user

So an example of this could be:
```typescript
{
    ...,
    reward: { 
        hook: { 
            webhookUrl: "https://my-rewards-webhook.com/quests/{quest_id}", 
            requestBody: { 
                "user": "{user_address}"
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
                "quest": "{quest_id}"
            }
        },
        ...
    }
}
```

As we defined [here](/creator/quests/define), the `requestBody` is optional. If you don't need to send any information to your webhook, you can just omit it. So an example of this could be:
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

The **[Quests System](/creator/quests/overview)** will replace the placeholders with the actual values before sending the request to the webhook URL.