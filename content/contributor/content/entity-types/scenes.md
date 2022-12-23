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
| `communications` | The protocol used for real-time communication between players (see below).
| `policy` | Recommended limitations for Explorers to enforce on players (see below).
| `spawnPoints` | Locations and camera angles for players jumping into this scene (see below).
| `requiredPermissions` | Recommended permissions for Explorers to ask from players (see below).

### Display

In `metadata.display`, you'll find properties that are useful to inform players about the scene before they enter it.

| Field | Value |
| ----- | --- |
| `title` | The display name of this scene.
| `description` | An extended description of this scene.
| `favicon` | The [internal filename]({{< relref "../entities#files" >}}) to an icon, displayed when this scene is active.
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
  "email": "csmaker@gmail.com"
}
```

While the `name` field is filled in every scene, you'll find that in actual practice the `email` field is often an empty string. This is a privacy choice made the scene's creator.

### Policy

{{< wip >}}

### Communications

{{< wip >}}

### Spawn Points

{{< wip >}}    

### Required Permissions

{{< wip >}}

