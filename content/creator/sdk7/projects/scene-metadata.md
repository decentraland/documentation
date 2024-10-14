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

A scene is a Decentraland project that is spatially delimited, and is mapped to one or several LAND parcels. If a scene is deployed to the Decentraland Genesis City map, players can experience it by visiting the scene's coordinates. If a scene is deployed to a [World]({{< ref "/content/creator/worlds/about.md" >}}), players can visit it via URL.

See [Files in a scene]({{< ref "/content/creator/sdk7/projects/scene-files.md" >}}) for a list of what files are used in a scene project.

## Metadata

To edit a scene's metadata from a UI, open Visual Editor, and click the **pencil icon**.

<img src="/images/editor/pencil-icon.png" alt="Scene name" width="124"/>

This opens up the scene menu, where you can configure multiple properties.

<img src="/images/editor/metadata-ui.png" alt="Scene name" width="300"/>

Alternatively, you can directly edit the `scene.json` file, where all of these values are stored.

{{< hint warning >}}
**📔 Note**: Do not add custom fields to the `scene.json` file that are not mentioned in this page, as it could cause issues loading your scene.
{{< /hint >}}

## Scene title, description, and image

It's very important to give your scene a title, a description and a thumbnail image to attract players to your scene and so they know what to expect.

Players will see these displayed on a modal when they select the parcels of your scene on the map. They will also see these in a confirmation screen when being [teleported]({{< ref "/content/creator/sdk7/interactivity/external-links.md" >}}) there by another scene. Setting up compelling data here can significantly help drive traffic to your scene.

When players navigate the world and enter your scene, they are able to read the scene title from under the minimap.

<img src="/images/media/scene-name.png" alt="Scene name" width="200"/>

Add this data via the scene menu in the Decentraland Editor.

The thumbnail should be a _.png_ image of a recommended size of _228x160_ pixels. The minimum supported size is _196x143_ pixels. The image may be stretched if the width-to-height proportions don't match _228x160_.

The image on `navmapThumbnail` should be a path to an image file in the project folder. It can also be a URL link to an image hosted elsewhere.

{{< hint warning >}}
**📔 Note**: If you host an image elsewhere, make sure this is in a site that has permissive CORS policies for displaying content on other sites.
{{< /hint >}}

In case you want other developers to be able to reach out to you, you can also add contact information to your scene.

## Categories

You can add categories to your scene to help players and users explore Decentraland better. These are used in the [Decentraland Places dApp](https://places.decentraland.org) to categorize each place and make it easier for users to find what they're interested in.

**Categories** need to be chosen from a pre-defined list of options:

- 🎨 Art
- 🕹️ Game
- 🃏 Casino
- 👥 Social
- 🎶 Music
- 👠 Fashion
- 🪙 Crypto
- 📚 Education
- 🛍️ Shop
- 🏢 Business
- 🏅 Sports

A scene can belong to more than one category, it can have a maximum of 3 listed categories.

<!-- **Tags** are an open-ended list. You can write any word you want into the list. -->

In the `scene.json` categories are listed in the `tags` array.

<!-- If a string matches any of the predefined categories, it's treated as a category, if it doesn't it's treated as a tag. -->

These are the predefined categories:

- `art`
- `game`
- `casino`
- `social`
- `music`
- `fashion`
- `crypto`
- `education`
- `shop`
- `business`
- `sports`

For example, an Scene could be tagged as `game` and `casino` by adding the following to the `scene.json`

```json
  "tags": [
    "game",
    "casino",
  ],
```

After that, the scene is listed on the Places dApp under the `game` and `casino` categories.

## Age Rating

The **Age Rating** field is used to classify the content of your scene based on its appropriateness for different age groups. It helps in filtering content for players. The following options are available:

- **🟢 `T` for Teens (13+)**: This is the minimum age requirement as specified in Decentraland's [Terms of Use](https://decentraland.org/terms/#8-children). Opt for this category if your scene is limited to moderate violence, suggestive or horror-themed content, simulated gambling, and mild language.
- **🟡 `A` for Adults (18+)**: Choose this category if your scene features any of the following: intense offensive language, graphic violence, explicit sexual content and/or nudity, real money gambling, or substances like alcohol, tobacco, and drugs.

When editing the Age Rating via the `scene.json`, rating is a **single-letter code**, write either **T** for teens, or **A** for adults.

<img src="/images/media/content-moderation-flag-icon.png" style="margin: 1rem; display: block;width: 200px;"/>

```json
 "scene": {
    "rating": "T"
  }
```

### Restricted Content

There is a third category for scenes: 🔴 `R` for Restricted. This rating is manually applied by Content Moderators to scenes that violate Decentraland's [Content Policy](https://decentraland.org/content). Violations may include, but are not limited to:

- Suspicious content or spam
- Abusive or hateful content
- Sexual or degrading content
- Child abuse
- Harassment or bullying
- Promotion of terrorism/violence
- IP/Copyright infringement

Scenes with this rating won't load and no one will be able to interact with them. If your scene falls into this category, you should review and update it to comply with the [Content Policy](https://decentraland.org/content).

{{< hint warning >}}
**📔 Note**: Incorrectly categorizing your scene may result in player reports and subsequent moderation actions. For more details, refer to [Age Rating and Scene Reporting]({{< ref "/content/player/general/in-world-features/age-rating.md" >}}).
{{< /hint >}}

## Feature Toggles

There are certain features that can be disabled in specific scenes so that players can't use these abusively. Configure these on the **Settings** tab of the scene settings.

<img src="/images/editor/scene-restrictions.png" alt="Scene name" width="300"/>

Currently, only the following feature is handled like this:

- **Voice Chat**: Refers to players using their microphones to have conversations over voice chat with other nearby players.

- **Disable Portable Experiences**: This setting will set the behavior for any portable experience of a player while standing inside the your scene. This includes not only [portable experiences]({{< ref "/content/creator/sdk7/projects/portable-experiences.md" >}}) but also [smart wearables]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}). With this setting, you can chose to either keep them all enabled (default), disable them, or hide their UI. This is useful for scenes where portable experiences might give an unfair advantage to some players, for example using a jetpack in a parkour challenge. It's also recommended to prevent these in scenes where blockchain transactions take place, and where a malicious portable experience could potentially impersonate the scene´s UI.

On the `scene.json` file, these toggles are managed under `featureToggles`. The corresponding features are enabled by default, unless specified as _disabled_ in the `scene.json` file.

```json
"featureToggles": {
    "voiceChat": "disabled",
    "portableExperiences": "enabled" | "disabled" | "hideUi"
},
```

If a `featureToggles` property doesn't exist in your `scene.json` file, create it at root level in the json tree.

## Spawn location

The **Spawn Settings** in the **Settings** tab define where players spawn when they access your scene directly, either by directly typing in the coordinates into the browser or teleporting.

<img src="/images/editor/spawn-point-ui.png" alt="Scene name" width="200"/>

Your scene might have objects that can block players from moving if they happen to spawn right over them, like trees or stairs, or your scene might have an elevated terrain. It would be a bad experience for players if they spawned over something that doesn't let them move. That's why you have the option to set multiple spawn positions in ad-hoc locations.

The position is comprised of coordinates inside the scene. These numbers refer to a position within the parcel, similar to what you'd use in the scene's code in a Transform component to [position an entity]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md" >}}).

{{< hint warning >}}
**📔 Note**: All spawn points must be within the parcels that make up the scene. You can't spawn a player outside the space of these parcels.
{{< /hint >}}

Check the **Random Offset** box to randomly offset the spawning players around the spawn point, with a maximum value. This prevents all players from appearing overlapping each other when they spawn, which looks especially bad in crowded scenes. The **Max Offset** value is the maximum possible distance from the original spawn point, in both the X or Z axis.

Set the **Camera Target** to set the direction in which players start looking when they jump into your scene. This allows you to have better control over their first impression, and can be useful when wanting to help steer them towards a specific direction. By default this points at `{x: 8, y:1, z:8}`, which translates to the center of the scene for single-parcel scenes, or the center of the bottom-left parcel for larger scenes.

Click **Add Spawn Point** to list as many spawn points as you want. Players will randomly appear in one of those.

### Spawn points in JSON

Spawn points can also be configured via the `scene.json` file, on the `spawnPoints` field.

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

A single scene can have multiple spawn points. This is especially useful in large scenes. To have many spawn points, simply list them as an array.

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

#### Spawn regions

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

#### Rotation

You can also specify the rotation of players when they spawn, so that they're facing in a specific direction.

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

{{< hint warning >}}
**📔 Note**: Permissions are only relevant in [portable experiences]({{< ref "/content/creator/sdk7/projects/portable-experiences.md" >}}) and [smart wearables]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}). Normal scenes (both in parcels or in Worlds) are not affected by these permissions, and are free to use the corresponding functionality.
{{< /hint >}}

The corresponding features are blocked from being used by the scene, unless the permission is requested in the `scene.json` file.

```json
"requiredPermissions": [
    "ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE",
		"OPEN_EXTERNAL_LINK",
  ],
```

Currently, the following permissions are managed on smart wearables and portable experiences:

- `ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE`: Refers to [moving a Player]({{< ref "/content/creator/sdk7/interactivity/move-player.md" >}})
- `ALLOW_TO_TRIGGER_AVATAR_EMOTE`: Refers to [Playing emotes on the player avatar]({{< ref "/content/creator/sdk7/interactivity/trigger-emotes.md" >}})
- `USE_WEB3_API`: Refers to interacting with the player's browser wallets, to make transactions or sign messages.
- `USE_FETCH`: Refers to sending http requests to 3rd party servers, using `fetch` or `signedFetch`
- `USE_WEBSOCKET`: Refers to opening websocket connections with 3rd party servers
- `OPEN_EXTERNAL_LINK`: Refers to prompting the player to open links to external sites

If a `requiredPermissions` property doesn't exist in your `scene.json` file, create it at root level in the json tree.

## Scene parcels

When [deploying]({{< ref "/content/creator/sdk7/publishing/publishing.md" >}}) a scene, the content is uploaded to the coordinates assigned in the scene configuration. A scene can include a single parcel, or a list of up to dozens of them.

Edit this on the second tab of the scene menu in the Editor.

<img src="/images/editor/scene-parcels-3x3.png" alt="Scene name" width="300"/>

Use the dropdowns and click **Apply Layout** to change the dimensions of your scene. You can also click each individual parcel to toggle it off from your layout.

<img src="/images/editor/scene-parcels-toggled.png" alt="Scene name" width="300"/>

The default scene has its coordinates set to _0,0_, this information is not necessary to change while developing a scene offline, unless you need to occupy multiple parcels. You will need to change this before deploying, to coordinates where you do have deploy permissions.

You can also change the scene coordinates on the `scene.json` file:

```json
 "scene": {
    "parcels": [
      "54,-14"
    ],
    "base": "54,-14"
  }
```

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

{{< hint warning >}}
**📔 Note**: The largest scene size you can set is of 45 x 45 parcels.
{{< /hint >}}

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
