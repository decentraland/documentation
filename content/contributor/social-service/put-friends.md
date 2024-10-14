---
title: Act on events and users
url: /contributor/social-service/put-friends
weight: 5
---

Interact with the Social Service API to perform actions related to events and users. These actions include creating new friend requests, accepting or rejecting incoming requests, and deleting friendships. The Social Service allows users to manage their relationships and interactions within the platform.

## Friendships and Actions

Friendships within the Social Service are bidirectional relationships between users. Actions can be taken to update these friendships, such as sending friend requests, accepting or rejecting requests, canceling requests, and removing friendships. Each of these actions has specific implications for the relationship between users.


## Implementing Friendship Updates

To perform these friendship-related actions, the `UpdateFriendshipEvent` message needs to be utilized. This message allows for the execution of various actions related to friendships, such as requesting, accepting, rejecting, canceling, and removing.

The exact payload structure and required parameters for each action are specified in the `UpdateFriendshipEvent` message.

**Example Usage**

Here's an example of how you might use the `UpdateFriendshipEvent` to send a friend request:

```proto
message UpdateFriendshipEvent {
  string userAddress = 1;
  string targetUserAddress = 2;
  FriendshipAction action = 3;
}
```

In this example, `userAddress` represents the sender's address, `targetUserAddress` represents the recipient's address, and `action` denotes the type of action to be performed (requesting, accepting, rejecting, canceling, or removing).

### Sending Friend Requests

Any user can send a friend request to another user. However, to establish a friendship, the recipient user must accept the request.

```javascript
requestFriendship: async (address: string, message?: string) => {
  const response = await service.updateFriendshipEvent({
    event: { request: { user: { address }, message } },
    authToken: { synapseToken }
  })
  processErrors(response)
  return response.event
}
```

### Accepting or Rejecting Requests

When a user receives a friend request, they have the option to accept or reject it. Accepting a request establishes a mutual friendship between the users. Rejecting a request denies the establishment of a friendship.

```javascript
acceptFriendshipRequest: async (address: string) => {
  const response = await service.updateFriendshipEvent(
    UpdateFriendshipPayload.create({
      event: { accept: { user: { address } } },
      authToken: { synapseToken }
    })
  )
  processErrors(response)
  return response.event
}
```

```javascript
rejectFriendshipRequest: async (address: string) => {
  const response = await service.updateFriendshipEvent(
    UpdateFriendshipPayload.create({
      authToken: { synapseToken },
      event: { reject: { user: { address } } }
    })
  )
  processErrors(response)
  return response.event
}
```

### Canceling Friend Requests

If a user decides to retract a sent friend request before it's accepted, they can cancel the request. This prevents the recipient from seeing or responding to the request.

```javascript
cancelFriendshipRequest: async (address: string) => {
  const response = await service.updateFriendshipEvent(
    UpdateFriendshipPayload.create({
      event: { cancel: { user: { address } } },
      authToken: { synapseToken }
    })
  )
  processErrors(response)
  return response.event
}
```

### Removing Friendships

Either user in a mutual friendship has the option to remove the friendship. When a friendship is removed, it is deleted from the records of both users, ending the mutual relationship.

```javascript
removeFriend: async (address: string) => {
  const response = await service.updateFriendshipEvent(
    UpdateFriendshipPayload.create({
      authToken: { synapseToken },
      event: { delete: { user: { address } } }
    })
  )
  processErrors(response)
  return response.event
}
```


