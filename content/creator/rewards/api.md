---
title: 'Server API'
url: /creator/rewards/api
weight: 5
---

This section explains how to interact with the Rewards service using the API and how to enhance the security of your dispensers.

Refer to the [API SPEC](https://decentraland.org/rewards/docs/api/) for complete details, including the expected inputs and outputs for each method.
- [Assigning Wearables or Emotes reward](#assigning-wearables-or-emotes-reward)
- [Securing the Rewards Dispenser](#securing-the-rewards-dispenser)
  - [Date Range Protection](#date-range-protection)
  - [Limit Assignments](#limit-assignments)
  - [Captcha Protection](#captcha-protection)
  - [Beneficiary Signature](#beneficiary-signature)
  - [Connected to Decentraland](#connected-to-decentraland)
  - [Position inside Decentraland](#position-inside-decentraland)

{{< hint warning >}}
⚠️ There is no way to prevent users from farming wearables/emotes. All security measures described in this section are meant to avoid automation, but you should assume that users are capable of manually switching between multiple accounts to get more than one of your rewards.
{{< /hint >}}

# Assigning Wearables or Emotes reward

Once your [campaign is configured]({{< ref "/content/creator/rewards/getting-started.md" >}}) you are ready to start minting wearables or emotes rewards for your users by using the Rewards Server API.

Make sure you have your dispenser key (a.k.a campaign key). Use the key to send the `fetch` request to the rewards API:

```ts
// User data is only required if your code is running on a Decentraland scene
import { getPlayer } from '@dcl/sdk/src/players'

export async function main() {
  const user = getPlayer()
  if (!user || user.userId) return

  const request = await fetch('https://rewards.decentraland.org/api/rewards', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      campaign_key: '[DISPENSER_KEY]',
      beneficiary: user.userId, // or beneficiary: "0x0f5d2fb29fb7d3cfee444a200298f468908cc942"
    }),
  })
  const response = await request.json()  
}
```

**JSON Response Example**: 
```json
{
  "ok": true,
  "data": [
    {
      "id": "00000000-0000-0000-0000-000000000000",
      "user": "0x0f5d2fb29fb7d3cfee444a200298f468908cc942",
      "campaign_id": "00000000-0000-0000-0000-000000000000",
      "campaign_key": "[DISPENSER_KEY]",
      "status": "assigned",
      "chain_id": 137,
      "airdrop_type": "CollectionV2IssueToken",
      "target": "0x7434a847c5e1ff250db456c55f99d1612e93d6a3",
      "value": "0",
      "group": null,
      "priority": 2144355453,
      "transaction_id": null,
      "transaction_hash": null,
      "token": "Polygon sunglasses",
      "image": "https://peer.decentraland.zone/lambdas/collections/contents/urn:decentraland:amoy:collections-v2:0x7434a847c5e1ff250db456c55f99d1612e93d6a3:0/thumbnail",
      "assigned_at": "2021-09-24T01:30:16.770Z",
      "created_at": "2021-09-24T01:25:14.534Z",
      "updated_at": "2021-09-24T01:25:14.534Z"
    }
  ]
}
```

This call to the API will assign (and eventually mint) a wearable or emote to the beneficiary user. The response includes useful information about the wearable/emote that is going to be minted, including the image, the name, and id.

You can follow the update of every reward using its id just by fetching `https://rewards.decentraland.org/api/rewards/:reward_id` where `:reward_id` is the id of the reward you want to check.

# Securing the Rewards Dispenser

The Rewards campaign dispenser includes several configuration options designed to help prevent rewards farming. While the service offers automated protections to deter individuals from mass-minting wearables, no system can be entirely immune to exploits. In this section, we'll review the various security measures available for your dispenser to enhance its protection.

<img src="/images/rewards/dispenser-config.png" alt="dispenser configuration" style="width:80%; margin: 0 auto;display: block;" width="2296" height="1012" />

## Date Range Protection

You can restrict your dispenser to deliver rewards only within a specific date range. This is particularly useful if you want to set up your scene ahead of an event but prevent rewards from being distributed before a certain time. This configuration doesn't require any code changes.

## Limit Assignments 

The code provided will successfully mint a wearable or emote to the user, but there are a few risks to consider:

- The dispenser will mint a wearable or emote to the user every time the API is called.
- It will mint a wearable or emote to any user who calls it, even if they have already claimed that item.

To mitigate these risks, you can limit the number of wearables or emotes a user can claim from each dispenser by enabling the Assign Only 1 Reward flag. When this flag is enabled, the dispenser will only mint one wearable or emote per user address, and this doesn't require any code changes.

{{< hint warning >}}
Please note that this assignment limit is specific to each dispenser. If you have multiple dispensers, a user will be able to claim one wearable or emote from each dispenser.
{{< /hint >}}

{{< hint info >}}
**💡 Tip**: It's also a good practice to prevent sending a request sending redundant requests to the server at all. See the example scene for tips on how to throttle requests and prevent re-sending in a same session.
{{< /hint >}} 

## Captcha Protection

If your users interact with the dispenser directly within your scene, your keys are exposed in code that can be accessed and replicated through the browser. To minimize the risk of automation and abuse, you can enable the *Captcha challenge* flag on your dispenser. This flag requires users to solve a captcha before a wearable or emote is assigned to them, adding an extra layer of security.  

When the Captcha flag is enabled, you first need to create a new captcha challenge using the `/api/captcha` endpoint from the rewards server. The response will provide all the necessary details to render the captcha image, including the image URL, dimensions, and expiration date, which indicates when the captcha will be invalidated. Be sure to save the captcha ID, as you will need it later.

```tsx
const request = await fetch(`https://rewards.decentraland.org/api/captcha`, { method: 'POST' })
const captcha = await request.json()
```
**JSON Response Example**: 
```json
{
  "ok": true,
  "data": {
    "width": 300,
    "height": 100,
    "id": "9e6b2d07-b47b-4204-ae87-9c4dea48f9b7",
    "expires_at": "2023-11-08T12:49:44.457Z",
    "image": "https://rewards2-assets-prd-05e0ac2.decentraland.org/catpcha/9e6b2d07-b47b-4204-ae87-9c4dea48f9b7.png"
  }
}
```

{{< hint info >}}
This is an example of what a captcha looks like:
<img src="/images/rewards/captcha.png" alt="Captcha" width="300" height="100" />
{{< /hint >}}

You then need to include the captcha id and value that resolves the captcha in the request body that assigns the reward.

```tsx {hl_lines=[13,14]}
import { signedFetch } from '@decentraland/SignedFetch'
import { getPlayer } from '@dcl/sdk/src/players'

export async function main() {
  const user = await getPlayer()
  if (!user || !user.userId) return
  const response = await signedFetch({
    url: 'https://rewards.decentraland.org/api/rewards',
    init: {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        campaign_key: '[DISPENSER_KEY]',
        beneficiary: user.userId,
        captcha_id: '[CAPTCHA_ID]', // "9e6b2d07-b47b-4204-ae87-9c4dea48f9b7"
        captcha_value: '[CAPTCHA_VALUE]', // "dbdcbf" or "DBDCBF"
      }),
    },
  })

  if (!response || !response.body) {
    throw new Error('Invalid response')
  }
  let json = await JSON.parse(response.body)
}
```

## Beneficiary Signature

If your users interact with the dispenser directly within your scene, consider enabling the **Beneficiary Signature** flag on your dispenser. This flag requires users to sign the request using the [@decentraland/SignedFetch]({{< ref "/contributor/runtime/modules/signed_fetch.md" >}}) module, ensuring that the user requesting the wearable or emote owns the associated Ethereum address.

For dispensers with this flag enabled, you'll need to make a slight modification to your code, as shown below:

```tsx {hl_lines=[1,5]}
import { signedFetch } from '@decentraland/SignedFetch'
import { getPlayer } from '@dcl/sdk/src/players'

export async function main() {
  const user = getPlayer()
  if (!user || user.userId) return
  const response = await signedFetch({
    url: 'https://rewards.decentraland.org/api/rewards',
    init: {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        campaign_key: '[DISPENSER_KEY]',
        beneficiary: user.userId,
      }),
    },
  })

  if (!response || !response.body) {
    throw new Error('Invalid response')
  }
  let json = await JSON.parse(response.body)
```

## Connected to Decentraland

Another effective way to reduce automation risks is by requiring users to be connected to Decentraland. This can be easily achieved by enabling the "Connected on Decentraland" flag on your dispenser.

When this flag is enabled, users must be connected to a Decentraland Catalyst Server to claim a reward. To perform this check, users need to send the server they are connected to, which can be accomplished using the @decentraland/EnvironmentAPI module. This ensures that only users actively participating in Decentraland can access the rewards, adding an extra layer of security against automated abuse.

{{< hint info >}}
**📔 Note**: Checks against the Catalyst server don’t provide real-time information; there’s a slight delay between when a user enters Decentraland and when their position is updated on the Catalyst server. While this delay is typically minimal, it can become significant in scenes with many users. To avoid triggering a "User not connected" error, it’s best not to place your dispensers too close to the user spawn point. This ensures that players spend some time in the scene before attempting to claim a reward, allowing the server to update their connection status.
{{< /hint >}}


```tsx {hl_lines=[1,5,14]}
import { getRealm } from '~system/Runtime'
import { getPlayer } from '@dcl/sdk/src/players'

export async function main() {
  const user = await getPlayer()
  const realm = await getRealm({})
  if (!user || !user.userId || !realm || !realm.baseUrl) return
  const response = await signedFetch({
    url: 'https://rewards.decentraland.org/api/rewards',
    init: {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        campaign_key: '[DISPENSER_KEY]',
        beneficiary: user.userId,
        catalyst: realm.baseUrl,
      }),
    },
  })

  if (!response || !response.body) {
    throw new Error('Invalid response')
  }
  let json = await JSON.parse(response.body)
}
```

{{< hint warning >}}
⚠️ This flag does not work on Worlds
{{< /hint >}}

## Position inside Decentraland

In addition to the "Connected on Decentraland" flag, you can further enhance security by requiring users to be within a specific location inside Decentraland. This can be easily achieved by enabling the "Position inside Decentraland" flag on your dispenser.

When this flag is enabled, you can use the same code as for the "Connected to Decentraland" flag to verify both the user's connection and their position within the virtual world.

{{< hint info >}}
**📔 Note**: Checks against the Catalyst server don’t provide real-time information; there’s a slight delay between when a user enters Decentraland and when their position is updated on the Catalyst server. While this delay is typically minimal, it can become significant in scenes with many users. To avoid triggering a "User not connected" error, it’s best not to place your dispensers too close to the user spawn point. This ensures that players spend some time in the scene before attempting to claim a reward, allowing the server to update their connection status.
{{< /hint >}}

{{< hint warning >}}
⚠️ This flag does not work on Worlds
{{< /hint >}}
