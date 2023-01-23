
---
bookCollapseSection: false
weight: 1
title: Players
---

```proto
service PlayersService {
    rpc GetPlayerData(GetPlayerDataRequest) returns (PlayersGetUserDataResponse) {}
    rpc GetPlayersInScene(GetPlayersInSceneRequest) returns (PlayerListResponse) {}
    rpc GetConnectedPlayers(GetConnectedPlayersRequest)  returns (PlayerListResponse) {}
}
```

## Messages
###### `Player` {#Player}

```proto
message Player {
    string user_id = 1;
}
```

###### `PlayersGetUserDataResponse` {#PlayersGetUserDataResponse}

```proto
message PlayersGetUserDataResponse {
    optional decentraland.common.sdk.UserData data = 1;
}
```

###### `PlayerListResponse` {#PlayerListResponse}

```proto
message PlayerListResponse {
    repeated Player players = 1;
}
```

###### `GetPlayerDataRequest` {#GetPlayerDataRequest}

```proto
message GetPlayerDataRequest {
    string user_id = 1;
}
```

## Types


