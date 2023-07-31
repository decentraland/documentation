---
bookCollapseSection: false
weight: 1
title: Players
draft: true # Documenting this module was postponed
---

The `Players` module allows [scenes]({{< ref "/contributor/content/entity-types/scenes" >}}) to look for players in their environment and get information about their identity and [profiles]({{< ref "/contributor/content/entity-types/profiles" >}}).

```ts
const Players = require("~system/Players")
```

It contains the following methods and types:

* [`function getPlayersInScene`](#getPlayersInScene)
* [`function getConnectedPlayers`](#getPlayersInScene)
* [`function getPlayerData`](#getPlayerData)
* [`interface Player`](#Player)
* [`interface UserData`](#UserData)


## Methods

There's two methods in this module to discover players in the scene, and one to obtain their profiles.

###### `getPlayersInScene` {#getPlayersInScene}

Returns a [`Player`](#Player) array, each with a `userId` that can be used in [getPlayerData](#getPlayerData).

```ts
interface Request {}

interface Response {
  players: Player[]
}

function getPlayersInScene(Request): Promise<Response>
```

###### `getConnectedPlayers` {#getConnectedPlayers}

```ts
interface Request {}

interface Response {
  players: Player[]
}

function getConnectedPlayers(Request): Promise<Response>
```

###### `getPlayerData` {#getPlayerData}

Returns the [`UserData`](#UserData) for a user, if known for the given `userId`.

```ts
interface Request {
  // The user identifier, (for non-guests, their Ethereum address).
  userId: string
}

interface Response {
  // The profile information for this user, if available.
  data?: UserData
}

function getPlayerData(Request): Promise<Response>
```

## Types

There's only two types in this module: [`Player`](#Player) and [`UserData`](#UserData).

###### `Player` {#Player}

Holds a reference to a `userId`.

```ts
interface Player {
  // The user identifier, (for non-guests, their Ethereum address).
  userId: string
}
```

###### `UserData` {#UserData}

Holds (possibly partial) information about a user, their identity and avatar. 

World Explorers obtain this information through the [content system]({{< ref "/contributor/content/overview" >}}).

The [profile entity definition]({{< ref "/contributor/content/entity-types/profiles" >}}) details all of these fields and more. While the structure and keys of `UserData` are slightly different, the meaning of each field is the same.

```ts
export interface UserData {
  // The user identifier (i.e. their Ethereum address).
  userId: string

  // A name to call them in the UI.
  displayName: string

  // The Ethereum public key they sign with.
  publicKey?: string

  // Whether they have web3 functionality enabled.
  hasConnectedWeb3: boolean

  // The sequential version of this information, incremented on each user update.
  version: number;

  // Information about their avatar, if available.
  avatar?: {
    // Pointers to the assets required to render this avatar.
    bodyShape: string
    wearables: string[]

    // Hex-encoded RGB/RGBA color tints for different body parts.
    skinColor: string
    hairColor: string
    eyeColor: string

    // File identifiers for the "photos" of this avatar.
    snapshots?: {
      face256: string
      body: string
    }
  }
}
```
