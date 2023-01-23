---
title: Scenes
url: /contributor/content/entity-types/scenes
weight: 1
---

Scenes are the [entities]({{< relref "../entities" >}}) that produce behavior in different parts of Decentraland. They can span multiple land parcels, and players walking through them in a World Explorer will execute special code provided by the scene.

You can find a complete real-life example in [this scene's manifest](https://peer.decentraland.org/content/contents/bafkreidihplrc5cxarjkji2enmzhicpjoa2vrlqyyffnholmxb3o2xft3u) on the Foundation's content server.

## Pointers {#pointers}

Scenes have one or more associated [pointers]({{< relref "../pointers" >}}) in the form of parcel coordinate strings, such as `"0,0"`. Every parcel running the scene will be listed in the [`pointers` array]({{< relref "../entities#properties" >}}) of the entity manifest, and all those pointers will be resolved by the content server to that scene.

In other words, you can choose the x/y coordinates of a parcel and locate the scene it's running by querying the content server for the `"<x>,<y>"` pointer. This is the way World Explorers decide whether to enable a scene's behavior as the player navigates the world.

A typical `pointers` array looks like this:

```json
{
  "pointers": [
    "-113,-134",
    "-113,-133",
    "-113,-132",
  ],
  // ... other entity properties
}
```

This data is also available in the `metadata.scene.parcels` field detailed below, in case you want to save only the scene-specific object in the manifest.

## Metadata Fields

There are several special properties for [entities]({{< relref "../entities" >}}) of type `scene` located in the `metadata` top-level field.

| Field | Value |
| ----- | --- |
| `owner` | Information about the scene's maintainer.
| `main` | The [internal filename]({{< relref "../entities#files" >}}) to this scene's main JavaScript file.
| `tags` | An array of string labels descriptive of this scene.
| `display` | Information about the scene for Explorers to show players (see below).
| `scene` | The parcels this scene is active on, and its central location (see below).
| `contact` | Name and email address to reach the scene's creators or maintainers (see below).
| `spawnPoints` | Locations and camera angles for players jumping into this scene (see below).
| `requiredPermissions` | Recommended permissions for Explorers to ask from players (see below).
| `featureToggles` | Settings for feature flags

{{< info >}}
Remember that entities and their metadata are allowed to have custom fields. You may find some properties out there that are not listed here.
{{< /info >}}

### Display

In `metadata.display`, you'll find properties that are useful to inform players about the scene before they enter it.

| Field | Value |
| ----- | --- |
| `title` | The display name of this scene.
| `description` | An extended description of this scene.
| `favicon` | _Deprecated_ The [internal filename]({{< relref "../entities#files" >}}) to an icon, displayed when this scene is active.
| `navmapThumbnail` | The [internal filename]({{< relref "../entities#files" >}}) to this scene's thumbnail for the world map.

An example:

```json
{
  "title": "my_cool_scene",
  "favicon": "favicon.png",
  "navmapThumbnail": "thumbnail.png"
}
```

### Scene

The `metadata.scene` property is an object describing the position of this scene in the world map.

| Field | Value |
| ----- | --- |
| `parcels` | An array of parcel pointers that run this scene.
| `base` | The parcel pointer for the origin point of this scene.

In practice, it looks like this:

```json
{
  "parcels": [
    "17,-112", 
    "17,-113"
  ],
  "base": "17,-112"
}
```

The `base` field is always included in the `parcels` array.

### Contact

The `metadata.contact` object contains the contact information of the scene's owner or maintainer.

| Field | Value |
| ----- | --- |
| `name` | A name for this contact.
| `email` | (Optional) An email address to reach out to.

In JSON:

```json
{
  "name": "cool_scene_maker",
  "email": "hello@decentraland.org"
}
```

While the `name` field is filled in every scene, you'll find that in actual practice the `email` field is often an empty string. This is a privacy choice made the scene's creator.

### Spawn Points

The `metadata.spawnPoints` field defines an array of points and camera directions determining where players entering the scene should appear, and where they should be initially looking. There must be at least one defined spawn point.

Each item in the array has a number of properties:

| Field | Value |
| ----- | --- |
| `name` | A label to identify this spawn point.
| `position` | The starting position in an `{ x, y, z }` object with float coordinates.
| `cameraTarget` | The starting camera direction in an `{ x, y, z }` object with float coordinates.
| `default` | Whether this spawn point is used unless otherwise specified.

For example:

```json
[
  {
    "name": "spawn1",
    "position": { "x": 10.02, "y": 5.27, "z": 15.23  },
    "cameraTarget": { "x": 10.02, "y": 6.27, "z": 31.23 },
    "default": true
  }
]
```

### Required Permissions {#permissions}

In `metadata.requiredPermissions` you'll find an array of well-known strings declaring which permissions should be asked from the player before the World Explorer allows certain actions. This is incumbent on the Explorer, on other clients built for different purposes may choose to ignore this.

This is the current set of supported permissions:

| Permission | Purpose |
| ----- | --- |
| `USE_FETCH` | Let the scene perform external HTTP requests.
| `USE_WEBSOCKET` | Let the scene use the Websocket API to establish external connections.
| `OPEN_EXTERNAL_LINK` | Let the scene open a URL (in a browser tab or web view).
| `USE_WEB3_API` | Let the scene communicate with a wallet.
| `ALLOW_TO_TRIGGER_AVATAR_EMOTE` | Let the scene to animate the player's avatar with an emote.
| `ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE` | Let the scene to change the player's position.

### Feature Toggles

The `metadata.featureToggles` field lets a scene indicate whether certain features of the World Explorer should be enabled or disabled.

The field contains an object of the form `{ [featureName]: 'enabled' | 'disabled' }`, like this one:

```json
{
  "voiceChat": "enabled"
}
```

Currently, `voiceChat` is the only commonly supported feature flag.