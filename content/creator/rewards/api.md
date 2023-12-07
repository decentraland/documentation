---
title: 'Rewards API'
url: /creator/rewards/api
weight: 5
---

This section explains how you can interact with the Rewards service using the API and add some extra security to your dispensers.

{{< hint warning >}}
⚠️ There is no way to prevent users from farming wearables/emotes. All security measures described in this section are meant to avoid automation, but you should assume that users are capable of manually switching between multiple accounts to get more than one of your rewards.
{{< /hint >}}

- [Assigning Wearables/Emotes](#assigning-wearables-emotes)
- [Date rage](#date-rage)
- [Limit assignation](#limit-assignation)
- [Beneficiary Signature](#beneficiary-signature)
- [Captcha](#captcha)
- [Connected to Decentraland](#connected-to-decentraland)
- [Position inside Decentraland](#position-inside-decentraland)

## Assigning Wearables/Emotes

Once you [configured your campaign]({{< ref "/content/creator/rewards/gatting-started.md" >}}) you are ready to start minting wearables/emotes for your users by using the API.

Make sure you have your dispenser key (a.k.a campaign key). Use this key to send a `fetch` request to the API:

```ts
// User data is only required if your code is running on a Decentraland scene
import { getUserData } from '@decentraland/Identity'
const user = await getUserData({})

const request = await fetch('https://rewards.decentraland.org/api/rewards', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    campaign_key: '[DISPENSER_KEY]',
    beneficiary: user.publicKey,
    // or
    // beneficiary: "0x0f5d2fb29fb7d3cfee444a200298f468908cc942"
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

This call to the API will assign (and eventually mint) a wearable/emote to the user. The response includes useful information about the wearable/emote that is going to be minted, including the image, the name, and id.

You can follow the update of every reward using its id just by fetching `https://rewards.decentraland.org/api/rewards/:reward_id` where `:reward_id` is the id of the reward you want to check.

## Date rage

You can limit your dispenser to delivery only on a specific date range. This is useful if you want to deploy your scene in advance of an event but prevent delivering rewards before a particular moment. This configuration **doesn't require any code change**.

## Limit assignation

The code above works, but there are some risks to keep in mind:

- It will mint a wearable/emote to the user every time it is called
- It will mint a wearable/emote to any user that calls it, even if they already have claimed that wearable.

To prevent this, you can limit the number of wearables/emotes a user can claim on each dispenser by enabling the **Assign only 1 reward** flag on your dispenser.

<img src="/images/rewards/flag-assignation.png" alt="Assignation limited flag" width="810" hegiht="146" />

With this flag enabled, the dispenser will only mint one wearable/emote per user address and **doesn't require any code change**.

{{< hint warning >}}
It is important to note that this assignation limit is per dispenser, so if you have multiple dispensers, the user will be able to claim one wearable/emote per dispenser.
{{< /hint >}}

{{< hint info >}}
**💡 Tip**: It's also a good practice to prevent sending a request sending redundant requests to the server at all. See the example scene for tips on how to throttle requests and prevent re-sending in a same session.
{{< /hint >}}

## Beneficiary Signature

If your users interact with the dispenser directly on your scene, you need to consider enabling the "Beneficiary signature" flag on your dispenser. This flag will require the user to sign the request using the `@decentraland/SignedFetch` module. This ensures that the beneficiary owns the ethereum address requesting the wearable/emote.

<img src="/images/rewards/flag-signature.png" alt="Beneficiary signature flag" width="824" hegiht="168" />

For dispensers with this flag enabled, you need to slightly modify the code, as shown below:

```tsx {hl_lines=[1,5]}
import { signedFetch } from '@decentraland/SignedFetch'
import { getUserData } from '@decentraland/Identity'

const user = await getUserData({})
const request = await signedFetch({
  url:'https://rewards.decentraland.org/api/rewards',
  init:{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      campaign_key: '[DISPENSER_KEY]',
      beneficiary: user.publicKey,
    }),
  }
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

## Captcha

If your users interact with the dispenser directly on your scene, it means that your keys are exposed in code that can be read and replicated directly on the browser. To reduce automation risks, you can enable the "Captcha" flag on your dispenser. This flag will require the users to solve a captcha before assign them a wearable/emote.

<img src="/images/rewards/flag-captcha.png" alt="Captcha flag" width="882" hegiht="118" />

When that flag is enabled, you need to first to create a new captcha challenge using `/api/captcha`. The response includes all the information you need to render the captcha image, including the image url and dimensions, also the expiration date, that is the moment when the captcha will be invalidated. Save your captcha id, you will need it later.

```tsx
const request = await fetch(`https://rewards.decentraland.org/api/captcha`)
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
```

{{< hint info >}}
This is an example of what a captcha looks like:

<img src="/images/rewards/captcha.png" alt="Captcha" width="300" hegiht="100" />
{{< /hint >}}

You then need to include the captcha id and value that resolves the captcha in the request body.

```tsx {hl_lines=[13,14]}
import { signedFetch } from '@decentraland/SignedFetch'
import { getUserData } from '@decentraland/Identity'

const user = await getUserData({})
const request = await signedFetch({
  url: 'https://rewards.decentraland.org/api/rewards',
  init: {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      campaign_key: '[DISPENSER_KEY]',
      beneficiary: user.publicKey,
      captcha_id: '[CAPTCHA_ID]', // "9e6b2d07-b47b-4204-ae87-9c4dea48f9b7"
      captcha_value: '[CAPTCHA_VALUE]', // "dbdcbf" or "DBDCBF"
    }),
  }
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

## Connected to Decentraland

{{< hint warning >}}
⚠️ This flag does not work on Worlds
{{< /hint >}}

Another way to reduce automation risks is to require the user to be connected to Decentraland. This is as easy as enabling the "Connected on Decentraland" flag on your dispenser.

<img src="/images/rewards/flag-connected.png" alt="Conneted to Decentraland" width="850" hegiht="180" />

With this flag enabled, users will need to be connected to a Decentraland Catalyst Server to be able to claim a wearable/emote. In order to perform this check, users need to send the server they are connected to, which can be done using the `@decentraland/EnvironmentAPI` module

{{< hint info >}}
**📔 Note**: Checks against the catalyst server don't provide real-time information. There is a delay between when the user enters Decentraland and when the position is updated on the catalyst server. This delay is usually low, but for scenes with a lot of users, it can be significant. To prevent a "User not connected" error, avoid positioning your dispensers near the user spawn point, so players spend at least a little time in the scene before the claim attempt.
{{< /hint >}}

<div id="connected-to-decentraland-code"></div>

```tsx {hl_lines=[1,5,14]}
import { getRealm } from "~system/Runtime"
import { getUserData } from '@decentraland/Identity'

const user = await getUserData({})
const realm = await getRealm({})
const request = await signedFetch({
  url: 'https://rewards.decentraland.org/api/rewards',
  init: {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      campaign_key: '[DISPENSER_KEY]',
      beneficiary: user.publicKey,
      catalyst: realm.domain,
    }),
  }
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

## Position inside Decentraland

{{< hint warning >}}
⚠️ This flag does not work on Worlds
{{< /hint >}}

Additionally to the "Connected on Decentraland" flag, you can also require the user to be inside a specific position inside Decentraland. This is as easy as enabling the "Position inside Decentraland" flag on your dispenser.

<img src="/images/rewards/flag-positions.png" alt="Position inside Decentraland" width="1512" hegiht="622" />

With this flag enabled, you just need to use the [same code](#connected-to-decentraland-code) as the "Connected to Decentraland" flag.

{{< hint info >}}
**📔 Note**: Checks against the catalyst server don't provide real-time information. There is a delay between when the user enters decentraland and when the position is updated on the catalyst server. This delay is usually low but for scenes with a lot of users, it can be significant. To prevent a "User not connected" error, avoid positioning your dispensers near the user spawn point, so players spend at least a little time in the scene before the claim attempt. Also list adjacent parcels to where the reward drop occurs.
{{< /hint >}}
