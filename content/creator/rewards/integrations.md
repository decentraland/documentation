---
title: 'Rewards API Integrations'
url: /creator/rewards/integrations
weight: 6
---

This section explains how to integrate Rewards with your scene, server, or quests.

- [With your scene](#with-your-scene)
- [With Quest service](#with-quest-service)
- [With your server](#with-a-custom-server)

## With your scene

Rewards can be integrated directly into Decentraland scenes. This exposes all the logic in code that is accessible to the user, so it is not recommended for minting items with a rarity lower than [EPIC]({{< ref "/content/creator/wearables-and-emotes/manage-collections/creating-a-collection.md" >}}#rarity). Consider the possibility that users possessing adequate knowledge and time could potentially solve captchas, alter their IP addresses, and subsequently mint all the available items, ultimately selling them on the marketplace. The only real incentive to prevent this is having enough items to mint to ensure that everyone is getting a wearable/emote.

### Recommended dispenser flags

The following measures are recommended to reduce the risk of exploits in this scenario:

- [Limit assignation]({{< ref "/content/creator/rewards/api.md" >}}#limit-assignation)
- [Beneficiary Signature]({{< ref "/content/creator/rewards/api.md" >}}#beneficiary-signature)
- [Captcha]({{< ref "/content/creator/rewards/api.md" >}}#captcha)
- [Connected to Decentraland]({{< ref "/content/creator/rewards/api.md" >}}#connected-to-decentraland)
- [Position inside Decentraland]({{< ref "/content/creator/rewards/api.md" >}}#position-inside-decentraland) (if it applies to your use case)

### Example

```tsx
import { getUserData } from '@decentraland/Identity'
import { signedFetch } from '@decentraland/SignedFetch'
import { getCurrentRealm } from '@decentraland/EnvironmentAPI'

// 1. Get captcha challenge to show to the user
const captchaRequest = await fetch(
  `https://rewards.decentraland.org/api/captcha`
)
const captcha = await request.json()
console.log(captcha)

// Response:
//
// {
//   "ok": true,
//   "data": {
//     "width": 300,
//     "height": 100,
//     "id": "9e6b2d07-b47b-4204-ae87-9c4dea48f9b7",
//     "expires_at": "2023-11-08T12:49:44.457Z",
//     "image": "https://rewards2-assets-prd-05e0ac2.decentraland.org/catpcha/9e6b2d07-b47b-4204-ae87-9c4dea48f9b7.png"
//   }
// }

// 2. Get user data
const user = await getUserData()

// 3. Get current realm
const realm = await getCurrentRealm()

// 4. Send request to assign a wearable/emote
const assignRequest = await signedFetch(
  'https://rewards.decentraland.org/api/rewards',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      campaign_key: '[DISPENSER_KEY]', // dispenser key
      beneficiary: user.publicKey, // ethereum address
      catalyst: realm.domain, // catalyst domain
      captcha_id: captcha.data.id, // "9e6b2d07-b47b-4204-ae87-9c4dea48f9b7"
      captcha_value: '[CAPTCHA_VALUE]', // "123456"
    }),
  }
)

const reward = await assignRequest.json()
console.log(reward)

// Response:
//
// {
//   ok: true,
//   data: [
//     {
//       id: '00000000-0000-0000-0000-000000000000',
//       user: '0x0f5d2fb29fb7d3cfee444a200298f468908cc942',
//       campaign_id: '00000000-0000-0000-0000-000000000000',
//       campaign_key: "[DISPENSER_KEY]",
//       status: 'assigned',
//       chain_id: 137,
//       airdrop_type: 'CollectionV2IssueToken',
//       target: '0x7434a847c5e1ff250db456c55f99d1612e93d6a3',
//       value: '0',
//       group: null,
//       priority: 2144355453,
//       transaction_id: null,
//       transaction_hash: null,
//       token: 'Polygon sunglasses',
//       image:
//         'https://peer.decentraland.zone/lambdas/collections/contents/urn:decentraland:mumbai:collections-v2:0x7434a847c5e1ff250db456c55f99d1612e93d6a3:0/thumbnail',
//       assigned_at: '2021-09-24T01:30:16.770Z',
//       created_at: '2021-09-24T01:25:14.534Z',
//       updated_at: '2021-09-24T01:25:14.534Z',
//     }
//   ]
// }
```

## With Quest the service

You can easily integrate Rewards with the [Quests service]({{< ref "/content/creator/quests/overview.md" >}}), this is ideal if you want to reward users for completing a quest.

### Recommended dispenser flags

The following measures are recommended to reduce the risk of exploits in this scenario:

- [Limit assignation]({{< ref "/content/creator/rewards/api.md" >}}#limit-assignation) (if it applies to your use case)

Any other of the other flags will make your integration fail, avoid using them.

{{< hint warning >}}
⚠️ The dispenser key should be kept secret, so you should never expose it to the user at anytime.
{{< /hint >}}

### Example

To integrate your Quest with the Rewards service, you just need a dispenser key and to [configure a webhook]({{< ref "/content/creator/quests/rewards.md" >}}) to receive the rewards.

```js
{
    // ...
    "reward": {
        "hook": {
            "webhookUrl": "https://rewars.decentraland.org/api/rewards",
            "requestBody": {
                "campaign_key": "[DISPENSER_KEY]",
                "beneficiary": "{user_address}"
            }
        },
        // ...
    }
}
```

## With a custom server

You can integrate Rewards directly from your server, this is ideal for carrying out extra checks before minting items. Another benefit is that users never have contact with the code on your server, making it harder to find vulnerabilities.

### Recommended dispenser flags

The following measures are recommended to reduce the risk of exploits in this scenario:

- [Limit assignation]({{< ref "/content/creator/rewards/api.md" >}}#limit-assignation) (if it applies to your use case)

Any of the other flags will make your integration more complex or, depending on your use case, can make it fail, so we don't recommend using them, but you may consider taking advantage of them.

{{< hint warning >}}
⚠️ The dispenser key should be kept secret, so you should never expose it to the user at anytime.
{{< /hint >}}

### Example

```tsx
const request = await fetch('https://rewards.decentraland.org/api/rewards', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    campaign_key: '[DISPENSER_KEY]',
    beneficiary: '0x0f5d2fb29fb7d3cfee444a200298f468908cc942', // ethereum address
  }),
})

const response = await request.json()
console.log(response)

// Response:
//
// {
//   ok: true,
//   data: [
//     {
//       id: '00000000-0000-0000-0000-000000000000',
//       user: '0x0f5d2fb29fb7d3cfee444a200298f468908cc942',
//       campaign_id: '00000000-0000-0000-0000-000000000000',
//       campaign_key: "[DISPENSER_KEY]",
//       status: 'assigned',
//       chain_id: 137,
//       airdrop_type: 'CollectionV2IssueToken',
//       target: '0x7434a847c5e1ff250db456c55f99d1612e93d6a3',
//       value: '0',
//       group: null,
//       priority: 2144355453,
//       transaction_id: null,
//       transaction_hash: null,
//       token: 'Polygon sunglasses',
//       image:
//         'https://peer.decentraland.zone/lambdas/collections/contents/urn:decentraland:mumbai:collections-v2:0x7434a847c5e1ff250db456c55f99d1612e93d6a3:0/thumbnail',
//       assigned_at: '2021-09-24T01:30:16.770Z',
//       created_at: '2021-09-24T01:25:14.534Z',
//       updated_at: '2021-09-24T01:25:14.534Z',
//     }
//   ]
// }
```
