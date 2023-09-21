---
date: 2018-02-26
title: Scenes
description: Learn how to set up a scene and configure its metadata.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/scene-metadata/
weight: 1
---

A scene is a Decentraland project that is spatially delimited, and is mapped to one or several LAND parcels. If a scene is deployed to the Decentraland map, players can experience it by visiting the scene's coordinates.

See [Files in a scene]({{< ref "/content/creator/sdk7/projects/scene-files.md" >}}) for a list of what files are used in a scene project.

## Metadata

All scenes have a `scene.json` file where you can set metadata for the scene. Some fields in this file are predefined with information that's necessary to load your scene. You're also free to add any fields that you wish.

## Scene parcels

When [deploying]({{< ref "/content/creator/sdk7/publishing/publishing.md" >}}) a scene, the `scene.json` file must include information about what parcels will be occupied by this scene in the Decentraland map. The CLI reads this information from off this field and deploys to those parcels directly.

```json
 "scene": {
    "parcels": [
      "54,-14"
    ],
    "base": "54,-14"
  }
```

The default scene has its coordinates set to _0,0_, this information is not necessary to change while developing a scene offline, unless you need to occupy multiple parcels. You will need to change this before deploying, to coordinates where you do have deploy permissions.

The `base` field defines which parcel to consider the base parcel. If your scene has a single parcel, the base should be that parcel. If your scene has multiple parcels, the base should be the bottom-left (South-West) parcel. All entity positions will be measured in reference to the South-West corner of this parcel.

To display multiple parcels in the scene preview, list as many parcels as you intend to use. They don't need to be the exact parcels you'll deploy to, but they should all be adjacent and arranged in the same way in relation to each other.

```json
 "scene": {
    "parcels": [
      "54,-14",  "55,-14"
    ],
    "base": "54,-14"
  }
```

### Set parcels via the command line

You can set the parcels in your scene by running the `npx update-parcels` command in your scene folder. This is especially useful for large scenes, as you don't need to list every parcel involved.

**Single parcel**

Pass a single argument with the scene coords. This coordinate is also set as the base parcel.

`npx update-parcels <parcel>`

For example:

`npx update-parcels 15,-26`

**Multiple parcels**

Pass two arguments: the South-West and the North-East parcels. The South-West parcel is also set as the base parcel.

`npx update-parcels <parcel> <parcel>`

{{< hint info >}}
**💡 Tip**: The South-West parcel is always the one with the lowest numbers on both the _X_ and _Y_ coordinates.
{{< /hint >}}

For example:

`npx update-parcels 15,-26 17,-24`

This command generates a 3x3 scene, with its base parcel in `15,-26`.

**Customize Base Parcel**

Pass three arguments: the South-West and the North-East parcels, and the parcel to use as a base parcel.

`npx update-parcels <parcel> <parcel> <parcel>`

{{< hint warning >}}
**📔 Note**: The base parcel must be one of the parcels in the scene.
{{< /hint >}}

**Non-square scenes**

The above commands all generate rectangular-shaped scenes. Decentraland scenes can have L shapes or other configurations. You can generate a larger square with `npx update-parcels` and then manually remove excess parcels from the `scene.json` file.

{{< hint warning >}}
**📔 Note**: The base parcel must be one of the parcels in the scene.
{{< /hint >}}

## Scene title, description, and image

It's very important to give your scene a title, a description and a thumbnail image to attract players to your scene and so they know what to expect.

Players will see these displayed on a modal when they select the parcels of your scene on the map. They will also see these in a confirmation screen when being [teleported]({{< ref "/content/creator/sdk7/interactivity/external-links.md" >}}) there by another scene. Setting up compelling data here can significantly help drive traffic to your scene.

When players navigate the world and enter your scene, they are able to read the scene title from under the minimap.

<img src="/images/media/scene-name.png" alt="Scene name" width="200"/>

```json
  "display": {
    "title": "My Cool Scene",
	"description": "You won't believe how cool this scene is",
	"navmapThumbnail": "images/scene-thumbnail.png",
    "favicon": "favicon_asset"
   }
```

The thumbnail should be a _.png_ or _.jpg_ image of a recommended size of _228x160_ pixels. The minimum supported size is _196x143_ pixels. The image may be stretched if the width-to-height proportions don't match _228x160_.

The image on `navmapThumbnail` should be a path to an image file in the project folder. It can also be a URL link to an image hosted elsewhere.

{{< hint warning >}}
**📔 Note**: If you host an image elsewhere, make sure this is in a site that has permissive CORS policies for displaying content on other sites.
{{< /hint >}}

## Contact information

In case you want other developers to be able to reach out to you, you can add contact information into the `scene.json` file.

```json
  "contact": {
    "name": "author-name",
    "email": "name@mail.com"
  },
```

## Spawn location

The `spawnPoints` field defines where players spawn when they access your scene directly, either by directly typing in the coordinates into the browser or teleporting.

Your scene might have objects that can block players from moving if they happen to spawn right over them, like trees or stairs, or your scene might have an elevated terrain. It would be a bad experience for players if they spawned over something that doesn't let them move. That's why you have the option to set multiple spawn positions in ad-hoc locations.

```json
  "spawnPoints": [
    {
      "name": "spawn1",
      "position": {
        "x": 5,
        "y": 1,
        "z": 4
      }
    }
  ],
```

The position is comprised of coordinates inside the scene. These numbers refer to a position within the parcel, similar to what you'd use in the scene's code in a Transform component to [position an entity]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md" >}}).

{{< hint warning >}}
**📔 Note**: All spawn points must be within the parcels that make up the scene. You can't spawn a player outside the space of these parcels.
{{< /hint >}}

### Multiple spawn points

A single scene can have multiple spawn points. This is especially useful in large scenes, to prevent players from spawning too far away from the coordinates where they originally intended to load. To have many spawn points, simply list them as an array.

```json
  "spawnPoints": [
    {
      "name": "spawn1",
      "position": {
        "x": 5,
        "y": 1,
        "z": 4
      }
	},
	{
      "name": "spawn2",
      "position": {
        "x": 3,
        "y": 1,
        "z": 1
      }
    }
  ],
```

When there are multiple spawn points, the one that's closest to the coordinates indicated by the player is picked.

If a coordinate is marked as `default`, it will always be used, regardless of if it's the closest. If multiple spawn points are marked as `default`, the closest one of these is picked.

```json
  "spawnPoints": [
    {
      "name": "spawn1",
      "default": true,
      "position": {
        "x": 5,
        "y": 1,
        "z": 4
      }
	},
	{
      "name": "not-used",
      "position": {
        "x": 3,
        "y": 1,
        "z": 1
      }
    }
  ],
```

### Spawn regions

You can set a whole region in the scene to act as a spawn point. By specifying an array of two numbers on any of the dimensions of the position, players will appear in a random location within this range of numbers. This helps prevent the overlapping of entering players.

```json
  "spawnPoints": [
    {
      "name": "region",
      "position": {
        "x": [1,5],
        "y": [1,1],
        "z": [2,4]
      }
    }
  ],
```

In the example above, players may appear anywhere in the square who's corners are on _1,1,2_ and _5,1,4_.

A scene can also have multiple spawn regions, just like it can have multiple spawn points.

```json
  "spawnPoints": [
    {
      "name": "region1",
      "position": {
        "x": [1,5],
        "y": [1,1],
        "z": [2,4]
      }
    },
      {
      "name": "region2",
      "position": {
        "x": [1,5],
        "y": [1,1],
        "z": [6,8]
      }
    }
  ],
```

### Rotation

You can also specify the rotation of players when they spawn, so that they're facing in a specific direction. This allows you to have better control over their first impression, and can be useful when wanting to help steer them towards a specific direction.

Simply add a `cameraTarget` field to the spawn point data. The value of `cameraTarget` should reference a location in space, with _x_, _y_ and _z_ coordinates relative to the scene, just like the `position` field.

```json
  "spawnPoints": [
    {
      "name": "spawn1",
      "position": {
        "x": 5,
        "y": 1,
        "z": 4
      },
      "cameraTarget": {
        "x": 10,
        "y": 1,
        "z": 4
      }
    }
  ],
```

This example spawns a player on _5, 1, 4_ looking East at _10, 1, 4_. If the spawn position is a range, then the player's rotation will always match the indicated target. If there are multiple spawn points, each can have its own separate target.

## Required Permissions

The `requiredPermissions` property manages various controlled features that could be used in an abusive way and damage a player's experience.

The corresponding features are blocked from being used by the scene, unless the permission is requested in the `scene.json` file.

```json
"requiredPermissions": [
    "ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE"
  ],
```

Currently, the following permissions are managed on all content:

- `ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE`: Refers to [moving a Player]({{< ref "/content/creator/sdk7/interactivity/move-player.md" >}})
- `ALLOW_TO_TRIGGER_AVATAR_EMOTE`: Refers to [Playing emotes on the player avatar]({{< ref "/content/creator/sdk7/interactivity/trigger-emotes.md" >}})
- `ALLOW_MEDIA_HOSTNAMES`: Refers to fetching resources (including images, video streams, and audio streams) from external sources rather than being limited to the files stored in the scene folder. You must also list the allowlisted high-level domains you will be fetching resources from.
  `json
"requiredPermissions": [
	"ALLOW_MEDIA_HOSTNAMES"
],
"allowedMediaHostnames": [
	"somehost.com",
	"otherhost.xyz"
]
`
  {{< hint warning >}}
  **📔 Note**: The `allowedMediaHostnames` lists only the high-level domains from where your assets are being requested. If there are any chained requests, these don't need to be explicitly listed. For example, if a video streaming service forwards content from a network of alternative servers, you only need to list the original URL you'll be explicitly calling from your code, not those other servers.
  {{< /hint >}}

Portable experiences and smart wearables are also affected by the following permissions:

- `USE_WEB3_API`: Refers to interacting with the player's browser wallets, to make transactions or sign messages.
- `USE_FETCH`: Refers to sending http requests to 3rd party servers, using `fetch` or `signedFetch`
- `USE_WEBSOCKET`: Refers to opening websocket connections with 3rd party servers
- `OPEN_EXTERNAL_LINK`: Refers to prompting the player to open links to external sites

If a `requiredPermissions` property doesn't exist in your `scene.json` file, create it at root level in the json tree.

{{< hint warning >}}
**📔 Note**: In future releases, when a player enters a scene that has items listed in the `requiredPermissions` property, the scene will prompt the player to grant these permissions. The player will be able to decline these permissions for that scene.
{{< /hint >}}

## Feature Toggles

There are certain features that can be disabled in specific scenes so that players can't use these abusively. The `featureToggles` property manages these permissions.

The corresponding features are enabled by default, unless specified as _disabled_ in the `scene.json` file.

```json
"featureToggles": {
    "voiceChat": "disabled",
    "portableExperiences": "enabled" | "disabled" | "hideUi"
},
```

Currently, only the following feature is handled like this:

- `voiceChat`: Refers to players using their microphones to have conversations over voice chat with other nearby players.

-`portableExperiences`: This setting will set the behavior for any portable experience of a player while standing inside the your scene. This includes not only [portable experiences]({{< ref "/content/creator/sdk7/projects/portable-experiences.md" >}}) but also [smart wearables]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}). With this setting, you can chose to either keep them all enabled (default), disable them, or hide their UI. This is useful for scenes where portable experiences might give an unfair advantage to some players, for example using a jetpack in a parkour challenge. It's also recommended to prevent these in scenes where blockchain transactions take place, and where a malicious portable experience could potentially impersonate the scene´s UI.

If a `featureToggles` property doesn't exist in your `scene.json` file, create it at root level in the json tree.

## Fetch metadata from scene code

[Scene API Reference](https://js-sdk-toolchain.pages.dev/modules/js_runtime_apis.__system_Scene_)

You may need a scene's code to access the fields from the scene metadata, like the parcels that the scene is deployed to, or the spawn point positions. This is especially useful for scenes that are meant to be replicated, or for code that is meant to be reused in other scenes. It's also very useful for libraries, where the library might for example need to know where the scene limits are.

To access this data, first import the `getSceneInformation` function:

```ts
import { getSceneInformation } from '~system/Runtime'
```

Then you can call the `getSceneInformation()` function, which returns a json object that includes much of the contents of the scene.json file.
The example below shows the path to obtain several of the more common fields you might need from this function's response:

```ts
import { getSceneInformation } from '~system/Runtime'

executeTask(async () => {
  const sceneInfo = await getSceneInformation({})

  if (!sceneInfo) return
    console.log("SCENE INFO: ", sceneInfo)
  }

})
```

{{< hint warning >}}
**📔 Note**: `getSceneInformation()` needs to be run as an [async function]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}), since the response may delay a fraction of a second or more in returning data.
Do not use the deprecated `getSceneInfo()` function.
{{< /hint >}}

The object returned by `getSceneInformation()` includes the following:

- `baseUrl`: The base URL where the scene's content is hosted
- `content`: An array with all the files of the scene, including their hash, that can be used together with the baseUrl to retrieve them.
- `metadataJson`: The full contents of the scene's scene.json, as a string. You must parse this to obtain specific values.
- `urn`: The unique urn for the scene as a whole.

The example below parses the contents from `metadataJson` to obtain values from properties in the scene.json file

```ts
import { getSceneInformation } from '~system/Runtime'

executeTask(async () => {
  const sceneInfo = await getSceneInformation({})

  if (!sceneInfo) return

  const sceneJson = JSON.parse(sceneInfo.metadataJson)
  const spawnPoints = sceneJson.spawnPoints
  const parcels = sceneJson.scene.parcels
  console.log({ parcels, spawnPoints })

})
```
