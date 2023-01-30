---
bookCollapseSection: false
weight: 5
title: Permissions
---

The permissions RPC interface allows scenes to check whether or not certain [[scene permissions]] were granted by the user.

With this interface, scenes can avoid attempting to use functionality only to see it fail, or implement graceful fallbacks where needed.

```proto
service PermissionsService {
  rpc HasPermission(HasPermissionRequest)          returns (PermissionResponse) {}
  rpc HasManyPermissions(HasManyPermissionRequest) returns (HasManyPermissionResponse) {}
}
```

You can find the complete definition in the [[proto file]].

## Messages

- [`HasPermissionRequest`](#HasPermissionRequest)
- [`PermissionResponse`](#PermissionResponse)
- [`HasManyPermissionRequest`](#HasManyPermissionRequest)
- [`HasManyPermissionResponse`](#HasManyPermissionResponse)

###### `HasPermissionRequest` {#HasPermissionRequest}

Check whether the scene was granted a [`PermissionItem`](#PermissionItem).

```proto
message HasPermissionRequest {
  PermissionItem permission = 1;
}
```

###### `PermissionResponse` {#PermissionResponse}

Answers a `HasPermissionRequest` indicating whether the specified [`PermissionItem`](#PermissionItem) was granted.

```proto
message PermissionResponse {
  bool has_permission = 1;
}
```

###### `HasManyPermissionRequest` {#HasManyPermissionRequest}

Check whether the scene was granted a many [`PermissionItem`](#PermissionItem) in a single call.

```proto
message HasManyPermissionRequest {
  repeated PermissionItem permissions = 1;
}
```

###### `HasManyPermissionResponse` {#HasManyPermissionResponse}

Answers a `HasManyPermissionRequest` indicating whether each of the specified [`PermissionItem`](#PermissionItem) was granted.

```proto
message HasManyPermissionResponse {
  repeated bool has_many_permission = 1;
}
```

## Types

- [`PermissionItem`](#PermissionItem)

###### `PermissionItem` {#PermissionItem}

An `enum` identifying the different [[scene permissions]] by a numeric code.

```proto
enum PermissionItem {
  PI_ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE = 0;
  PI_ALLOW_TO_TRIGGER_AVATAR_EMOTE = 1;
  PI_USE_WEB3_API = 2;
  PI_USE_WEBSOCKET = 3;
  PI_USE_FETCH = 4;
}
```