---
title: Login
url: /contributor/social-service/login
weight: 3
---

The authentication process for the Social Service involves interacting with the [Matrix server](https://matrix.org/), used under the hood for the private chat subsystem. Users must log in to Matrix using their address, signing a fetch operation to obtain an authentication token. This token is then used to authorize interactions with the Social Service.

## HTTP Request

To acquire the authentication token, as [the Matrix documentation refers](https://spec.matrix.org/v1.3/client-server-api/#login), a POST request must be made to the following URL: `https://social.decentraland.org/_matrix/client/r0/login` as in the example below.

To login into Matrix, you need to create and sign a message with AuthChain.

### Request Body

```json
{
  "auth_chain": authChain,
  "identifier": {
    "type": "m.id.user",
    "user": address
  },
  "timestamp": timestamp.toString(),
  "type": "m.login.decentraland"
}
```

### Response Body

```json
{
  "user_id": "@0x123abC:decentraland.org",
  "social_user_id": "0x123abC",
  "access_token": "syt_SomETokEN",
  "device_id": "FRFREGRG",
  "home_server": "decentraland.org",
  "well_known": {
      "m.homeserver": {
          "base_url": "https://synapse.decentraland.org/"
      }
  }
}
```

The authentication token, present in the `access_token` field, is required for subsequent interactions with the Social Service.

## JS Code Example

```javascript
import fetch from 'cross-fetch'
import { AuthIdentity, Authenticator } from '@dcl/crypto'

export async function getMatrixToken(matrixUrl: string, address: string, identity: AuthIdentity): Promise<string> {
  const timestamp = Date.now()
  const authChain = Authenticator.signPayload(identity, timestamp.toString())

  try {
    const response = await fetch(`${matrixUrl}/_matrix/client/r0/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        auth_chain: authChain,
        identifier: {
          type: 'm.id.user',
          user: address
        },
        timestamp: timestamp.toString(),
        type: 'm.login.decentraland'
      })
    })

    if (response.ok) {
      const responseBody = await response.json()
      return responseBody.access_token
    } else {
      throw new Error(`Matrix server responded with a ${response.status} status code`)
    }
  } catch (error) {
    throw new MatrixLoginError(isErrorWithMessage(error) ? error.message : 'Unknown error')
  }
}
```

Code from [social-rpc-client-js](https://github.com/decentraland/social-rpc-client-js/blob/main/src/client.ts#L14)