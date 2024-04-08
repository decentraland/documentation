---
date: 2018-02-26
title: Scenes
description: Learn how to add metadata to a scene.
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/scene-metadata/
url: /creator/development-guide/scene-metadata
weight: 1
---

{{< hint danger >}}
**❗Warning**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}).
{{< /hint >}}

All scenes have a `scene.json` file where you can set metadata for the scene. Some fields in this file are predefined with information that's necessary for the Decentraland client.

You're also free to add any fields that you wish. In the future, custom fields can then be checked by alternative clients, or other scripts embedded in interactive inventory items.

## Scene parcels

When [deploying]({{< ref "/content/creator/scenes/publishing/publishing.md" >}}) a scene, the `scene.json` file must include information about what parcels will be occupied by this scene in the Decentraland map. The CLI reads this information from off this field and deploys to those parcels directly.

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

You can set the parcels in your scene by running the `dcl coords` command in your scene folder. This is especially useful for large scenes, as you don't need to list every parcel involved.

**Single parcel**

Pass a single argument with the scene coords. This coordinate is also set as the base parcel.

`dcl coords <parcel>`

For example:

`dcl coords 15,-26`

**Multiple parcels**

Pass two arguments: the South-West and the North-East parcels. The South-West parcel is also set as the base parcel.

`dcl coords <parcel> <parcel>`

{{< hint info >}}
**💡 Tip**: The South-West parcel is always the one with the lowest numbers on both the _X_ and _Y_ coordinates.
{{< /hint >}}

For example:

`dcl coords 15,-26 17,-24`

This command generates a 3x3 scene, with its base parcel in `15,-26`.

**Customize Base Parcel**

Pass three arguments: the South-West and the North-East parcels, and the parcel to use as a base parcel.

`dcl coords <parcel> <parcel> <parcel>`

{{< hint warning >}}
**📔 Note**: The base parcel must be one of the parcels in the scene.
{{< /hint >}}

**Non-square scenes**

The above commands all generate rectangular-shaped scenes. Decentraland scenes can have L shapes or other configurations. You can generate a larger square with `dcl coords` and then manually remove excess parcels from the `scene.json` file.

{{< hint warning >}}
**📔 Note**: The base parcel must be one of the parcels in the scene.
{{< /hint >}}

## Scene title, description, and image

Give your scene a title, a description and a thumbnail image to attract players to your scene and so they know what to expect.

Players will see these when they select the parcels of your scene on the map, they will also see these in a confirmation screen when being [teleported]({{< ref "/content/creator/scenes/interactivity/external-links.md" >}}) there by another scene.

<!-- screenshot -->

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
      "default": true,
      "position": {
        "x": 5,
        "y": 1,
        "z": 4
      }
    }
  ],
```

The position is comprised of coordinates inside the scene. These numbers refer to a position within the parcel, similar to what you'd use in the scene's code in a Transform component to [position an entity]({{< ref "/content/creator/scenes/3d-essentials/entity-positioning.md" >}}).

{{< hint info >}}
**💡 Tip**: Define a [range](#spawn-regions) for the **x** and **z** locations to prevent users spawning all together in the same spot.
{{< /hint >}}

If your scene does not define any spawn points, users might appear at any random location within the base parcel. In the past, the reference client always spawned users in the **0,0** position. Make sure you update your scene.json if this is not the behavior you expect.

{{< hint warning >}}
**📔 Note**: All spawn points must be within the parcels that make up the scene. You can't spawn a player outside the space of these parcels.
{{< /hint >}}

### Multiple spawn points

A single scene can have multiple spawn points. This is useful to limit the overlapping of players if they all visit a scene at the same time. To have many spawn points, simply list them as an array.

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
      "name": "spawn2",
      "default": true,
      "position": {
        "x": 3,
        "y": 1,
        "z": 1
      }
    }
  ],
```

Spawn points marked as `default` are given preference. When there are multiple spawn points marked as `default`, one of them will be picked randomly from the list.

{{< hint warning >}}
**📔 Note**: In future releases, when a player tries to spawn into a scene and the default spawn points are occupied by other players, the player will be sent to another of the listed locations. This will open the door to allowing players to teleport to a spawn point based on the spawn point's name, as described in the `scene.json`.
{{< /hint >}}

### Spawn regions {#spawn-regions}

You can set a whole region in the scene to act as a spawn point. By specifying an array of two numbers on any of the dimensions of the position, players will appear in a random location within this range of numbers. This helps prevent the overlapping of entering players.

```json
  "spawnPoints": [
    {
      "name": "spawn1",
      "default": true,
      "position": {
        "x": [1,5],
        "y": [1,1],
        "z": [2,4]
      }
    }
  ],
```

In the example above, players may appear anywhere in the square who's corners are on _1,1,2_ and _5,1,4_.

### Rotation

You can also specify the rotation of players when they spawn, so that they're facing in a specific direction. This allows you to have better control over their first impression, and can be useful when wanting to help steer them towards a specific direction.

Simply add a `cameraTarget` field to the spawn point data. The value of `cameraTarget` should reference a location in space, with _x_, _y_ and _z_ coordinates relative to the scene, just like the `position` field.

```json
  "spawnPoints": [
    {
      "name": "spawn1",
      "default": true,
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

## Age Rating

The `rating` field is used to classify the content of your scene based on its appropriateness for different age groups. It helps in filtering content for players. The rating is a **single-letter code** that you should add to your `scene.json` file. Here are the available options:

- **🟢 `T` for Teens (13+)**: This is the minimum age requirement as specified in Decentraland's [Terms of Use](https://decentraland.org/terms/#8-children). Opt for this category if your scene is limited to moderate violence, suggestive or horror-themed content, simulated gambling, and mild language.
- **🟡 `A` for Adults (18+)**: Choose this category if your scene features any of the following: intense offensive language, graphic violence, explicit sexual content and/or nudity, real money gambling, or substances like alcohol, tobacco, and drugs.

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

## Required Permissions

The `requiredPermissions` property manages various controlled features that could be used in an abusive way and damage a player's experience.

The corresponding features are blocked from being used by the scene, unless the permission is requested in the `scene.json` file.

```json
"requiredPermissions": [
    "ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE"
  ],
```

Currently, the following permissions are managed on all content:

- `ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE`: Refers to [moving a Player]({{< ref "/content/creator/scenes/interactivity/move-player.md" >}})
- `ALLOW_TO_TRIGGER_AVATAR_EMOTE`: Refers to [Playing emotes on the player avatar]({{< ref "/content/creator/scenes/interactivity/trigger-emotes.md" >}})

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

The corresponding features are enabled by default, unless specified as _dissabled_ in the `scene.json` file.

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

## Worlds Configuration

When you are planning to upload yor scene to a Decentraland [World]({{< ref "/content/creator/worlds/about.md" >}}) instead of Genesis City, you must specify the NAME that you are going to target. On the other hand, if your world meets the requirements to be listed on [Places](https://places.decentraland.org/) (owning a LAND or having an active LAND rental contract), and you prefer not to list your scene, you can also configure it accordingly.

```
{
  "worldConfiguration" : {
    "name": "my-name.dcl.eth",
    "placesConfig": {
      "optOut": true
    }
  }
}
```

{{< hint warning >}}
**📔 Note**: Attempting to upload a scene with the `worldConfiguration`` section to a Catalyst will result in the deployment being rejected.
{{< /hint >}}

## Fetch metadata from scene code

You may need a scene's code to access the fields from the metadata, like the parcels that the scene is deployed to, or the spawn point positions. This is especially useful for scenes that are meant to be replicated, or for code that is meant to be reused in other scenes. It's also very useful for smart items, where the smart item's code might for example need to know where the scene limits are.

To access this data, first import the `ParcelIdentity` library to your scene:

```ts
import { getParcel } from '@decentraland/ParcelIdentity'
```

Then you can call the `getParcel()` function from this library, which returns a json object that includes much of the contents of the scene.json file.

The example bleow shows the path to obtain several of the more common fields you might need from this function's response:

```ts
import { getParcel } from '@decentraland/ParcelIdentity'

executeTask(async () => {
	const parcel = await getParcel()

	// parcels
	log('parcels: ', parcel.land.sceneJsonData.scene.parcels)
	log('base parcel: ', parcel.land.sceneJsonData.scene.base)

	// spawn points
	log('spawnpoints: ', parcel.land.sceneJsonData.spawnPoints)

	// general scene data
	log('title: ', parcel.land.sceneJsonData.display?.title)
	log('author: ', parcel.land.sceneJsonData.contact?.name)
	log('email: ', parcel.land.sceneJsonData.contact?.email)

	// other info
	log('tags: ', parcel.land.sceneJsonData.tags)
})
```

{{< hint warning >}}
**📔 Note**: `getParcel()` needs to be run as an [async function]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}), since the response may delay a fraction of a second or more in returning data.
{{< /hint >}}

## Tags

You can add tags to your scene to help players and users explore Decentraland better. These tags are used in the [Decentraland Places dApp](https://places.decentraland.org) to categorize each place and make it easier for users to find what they're intreseted in.

You can only use a preselected list of tags and a maximum of 3 tags per scene.

The tags you can use are:

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
    "casino"
  ],
```

After that, the scene will be listed on the Places dApp under the `game` and `casino` categories.

Here is how the tag names look on the Places dApp:

```json
{
	"art": "🎨 Art",
	"game": "🕹️ Game",
	"casino": "🃏 Casino",
	"social": "👥 Social",
	"music": "🎶 Music",
	"fashion": "👠 Fashion",
	"crypto": "🪙 Crypto",
	"education": "📚 Education",
	"shop": "🛍️ Shop",
	"business": "🏢 Business",
	"sports": "🏅 Sports"
}
```
