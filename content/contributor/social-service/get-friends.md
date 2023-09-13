---
title: Get friendships
url: /contributor/social-service/get-friends
weight: 4
---

Details about using the Social Service API to retrieve friendships, requests, and mutual friends in the Decentraland platform. The API allows developers to interact with the Social Service to retrieve friendships-related information.

### REST API

To retrieve friendships, the Social Service exposes a [REST API](https://social-service-api-specs.pages.dev/):

- `GET /friendships/me` - Retrieve the current user's friendships. Requires the access token in the Authorization header.
- `GET /friendships/{other-address}/mutuals` - Retrieve mutual friends with another user. Requires the access token in the Authorization header.

### WebSocket RPC Server

The Social Service WebSocket API provides two message types for retrieving friendships and mutual friends. You need first to establish a WebSocket connection and then use those methods to stream user-related information.

- `GetFriends` - Retrieve a user's friends. Returns a stream of user responses.
- `GetMutualFriends` - Retrieve mutual friends with another user. Returns a stream of user responses.

Refer to the [friendships.proto file](https://github.com/decentraland/protocol/blob/main/proto/decentraland/social/friendships/friendships.proto#L7) for more details about these message types.

## JavaScript Code Examples

To interact with the Social Service WebSocket API using JavaScript, you can use the provided RPC client as explained before. But if you need to implement it yourself, below there are code examples demonstrating how to retrieve friends and mutual friends:

### Getting All Friends

```javascript
import { createRpcClient, createWebSocketsTransport } from '@dcl/rpc/dist/client';
import { FriendshipsServiceDefinition } from './protobuff-types/decentraland/social/friendships/friendships.gen';

const socialClientRpcUrl = 'wss://social.decentraland.org'; // Replace with the actual URL
const webSocketsTransport = createWebSocketsTransport(socialClientRpcUrl);
const service = loadService(FriendshipsServiceDefinition, webSocketsTransport);

const response = service.getFriends(Payload.create({ synapseToken }));
for await (const friends of response) {
  processErrors(friends);
  const userList = friends.users?.users ?? [];
  // Process the list of friends
}
```

### Getting Mutual Friends

```javascript
const response = service.getMutualFriends(
  MutualFriendsPayload.create({
    user: { address }, 
    authToken: { synapseToken }
  })
);
for await (const mutualFriend of response) {
  processErrors(mutualFriend);
  const mutualFriendList = mutualFriend.users?.users ?? [];
  // Process the list of mutual friends
}
```

For more code examples and details, visit the [social-rpc-client-js GitHub repository](https://github.com/decentraland/social-rpc-client-js)