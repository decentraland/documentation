---
title: Javascript Client
url: /contributor/social-service/js-client
weight: 2
---

This documentation is extracted from [social-rpc-client-js](https://github.com/decentraland/social-rpc-client-js#using-the-client)

### Basic setup and usage

To use the client, install the package in your NPM project:

```bash
npm install -S @dcl/social-rpc-client
```

Import the client creator function from the installed package:

```typescript
import { createSocialClient } from "@dcl/social-client";
```

Create a new client instance by providing the client with:
1. A URL to the Social Service's REST API
2. A URL to the Social Service's Websocket endpoint
3. The user's address (the same as the one used to sign the identity)
4. An identity, signed with the user's wallet.

```typescript
import { createSocialClient } from "@dcl/social-client";
import { Wallet } from 'ethers'

// Generate a random wallet for testing purposes or use the user's one in production environments.
const wallet = Wallet.createRandom()
const identity = await createIdentity(wallet, expiration)

const socialClient = await createSocialClient(
  "https://social.decentraland.org",
  "wss://social-service.decentraland.org",
  wallet.address,
  identity
);
```

The `createSocialClient` will connect perform the required operations to connect to the Social Service and will return the connected client.


Use the client to interact with the Social Service:

```typescript
import { createSocialClient } from "@dcl/social-client";

const socialClient = await createSocialClient(
  "https://social.decentraland.org",
  "wss://social-service.decentraland.org",
  wallet.address,
  identity
);

const friends = socialClient.getFriends()
for await (const friend of friends) {
  console.log(friend)
}
```

The client exposes the methods available through the [social protobuff](https://github.com/decentraland/protocol/blob/main/public/social.proto) and a disconnect method which disconnects the client from the Social Service.


### Generating an identity

To authenticate users with the Social Service, you'll need to generate an identity for them. To do so, the `@dcl/crypto` library provides the `Authenticator.initializeAuthChain` method. Use it to generate an identity for your users:

```typescript
  import { Wallet } from 'ethers'
  import { Authenticator } from '@dcl/crypto'
  // Generate a random wallet for testing purposes or use the user's one in production environments.
  const userWallet = Wallet.createRandom()

  // Generate an identity for the user.
  const address = await userWallet.getAddress()
  const ephemeralWallet = Wallet.createRandom()
  const payload = {
    address: ephemeralWallet.address,
    privateKey: ephemeralWallet.privateKey,
    publicKey: ephemeralWallet.publicKey
  }
  const identity = await Authenticator.initializeAuthChain(address, payload, expiration, (message: string) => signer.signMessage(message))
```