---
title: 'API Integrations'
url: /creator/rewards/integrations
weight: 6
---

After creating and configuring a campaign and ensuring it has sufficient stock to provide rewards, the next step is to connect the campaign to a rewards trigger. This trigger can be a Scene, a Quest, or an external server. This section explains how different integrations with Rewards can be done. 

- [Grant rewards from a scene](#grant-rewards-from-a-scene)
  - [Recommended dispenser flags](#recommended-dispenser-flags)
  - [Example](#example)
- [Grant rewards from a Decentraland Quests](#grant-rewards-from-a-decentraland-quests)
  - [Recommended dispenser flags](#recommended-dispenser-flags-1)
  - [Example](#example-1)
- [With a custom server](#with-a-custom-server)
  - [Recommended dispenser flags](#recommended-dispenser-flags-2)
  - [Example](#example-2)

## Grant rewards from a scene

Rewards can be integrated directly into Decentraland scenes, but this approach comes with some risks. Since the logic is embedded in scene code that users can access, it’s not recommended for minting items with a rarity lower than [EPIC]({{< ref "/content/creator/wearables-and-emotes/manage-collections/creating-a-collection.md" >}}#rarity).

Keep in mind that determined users with enough technical knowledge could potentially bypass security measures like captchas, change their IP addresses, and mint all available items, which they could then sell on the marketplace. The primary safeguard against this is ensuring a sufficient supply of items, so everyone has a fair chance to receive a reward.

### Recommended dispenser flags

The following dispenser configurations are recommended to reduce the risk of exploits in this scenario: 

- [Limit Assignments]({{< ref "/content/creator/rewards/api.md" >}}#limit-assignments)
- [Beneficiary Signature]({{< ref "/content/creator/rewards/api.md" >}}#beneficiary-signature)
- [Captcha Protection]({{< ref "/content/creator/rewards/api.md" >}}#captcha-protection)
- [Connected to Decentraland]({{< ref "/content/creator/rewards/api.md" >}}#connected-to-decentraland)
- [Position inside Decentraland]({{< ref "/content/creator/rewards/api.md" >}}#position-inside-decentraland) (if it applies to your use case)

### Example

```tsx
import { getPlayer } from '@dcl/sdk/src/players'
import { signedFetch } from '@decentraland/SignedFetch'
import { getRealm } from '~system/Runtime'

export function main() {
  // 1. Get captcha challenge to show to the user
  const request = await fetch(`https://rewards.decentraland.org/api/captcha`, {
    method: 'POST',
  })
  const captcha = await request.json()

  // 2. Display captcha for player to complete - See example in studios.decentraland.org/resources

  // 3. Get user data
  const user = getPlayer()

  // 4. Get current realm
  const realmInfo = await getRealm({})

  // 5. Send request to assign a wearable/emote
  const assignRequest = await signedFetch('https://rewards.decentraland.org/api/rewards', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      campaign_key: '[DISPENSER_KEY]', // dispenser key
      beneficiary: user.userId, // ethereum address
      catalyst: realmInfo.baseUrl, // catalyst domain
      captcha_id: captcha.data.id, // "9e6b2d07-b47b-4204-ae87-9c4dea48f9b7"
      captcha_value: '[CAPTCHA_VALUE]', // "123456"
    }),
  })

  const reward = await assignRequest.json()
```

## Grant rewards from a Decentraland Quests

You can easily integrate Rewards with the [Decentraland Quests]({{< ref "/content/creator/quests/overview.md" >}}), this is ideal if you want to reward users for completing a quest.

### Recommended dispenser flags

The following dispenser configurations are recommended to reduce the risk of exploits in this scenario:

- [Limit Assignments]({{< ref "/content/creator/rewards/api.md" >}}#limit-assignments) (if it applies to your use case)

Any other of the other flags will make your integration fail, avoid using them.

{{< hint warning >}}
⚠️ The dispenser key should be kept secret, so you should never expose it to the user at anytime.
{{< /hint >}}

### Example

To integrate your Quest with the Rewards service, you just need a dispenser key and to [configure a webhook]({{< ref "/content/creator/quests/rewards.md" >}}) to grant rewards.

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

You can integrate Rewards directly from your server, which is ideal for performing extra checks before minting items. An additional advantage is that, unlike scene code, your server code might not be public, making it more challenging for users to discover and exploit vulnerabilities.

### Recommended dispenser flags

The following dispenser configurations are recommended to reduce the risk of exploits in this scenario:

- [Limit Assignments]({{< ref "/content/creator/rewards/api.md" >}}#limit-assignments) (if it applies to your use case)

Enabling any of the other flags could complicate your integration or, depending on your use case, potentially cause it to fail. Therefore, it is not recommend using them unless there is a specific need. However, you may want to explore their potential benefits.

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
```
