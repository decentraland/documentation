---
date: 2024-03-08
title: Kinds of Projects
description: The available kinds of projects you can create in Decentraland.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/kinds-of-projects/
weight: 1
---

There are different types of content that you can make for Decentraland.

<img src="/images/content-types.png" width="600" />

## Scenes

Decentraland scenes can either be hosted in Parcels in Genesis City or in Worlds.

### Published to LAND

Scenes that are published to Parcels can be found at specific coordinates inside Decentraland's open world.

These scenes are linked ot LAND ore Estate tokens. Each parcel takes up 16x16 meters. Multiple adjacent parcels can be used up by a single scene, these can be arranged into any shape, as long as the borders touch.

LAND tokens can be bought in the [Marketplace](https://decentraland.org/marketplace/lands). There's a limited supply of them, covering the map of Genesis City.

Scenes published to LAND are easier to discover, as players may run into them while visiting nearby content or exploring.

Scenes published to LAND can use up to 15 MB of space per each parcel in the scene. The more parcels, the more room available. This is to prevent overloading the player's CPU, since players may be experiencing many nearby scenes at the same time. See [size limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}).

### Published to Worlds

Scenes published to a World must be accessed via a link.

These scenes are linked to NAME tokens. NAME tokens can be bought in the [Marketplace](https://decentraland.org/marketplace/names/claim). You can claim any name you want as long as it's not claimed yet.

Scenes published to a World can use up to 100 MB, and have as many parcels of land as you wish. The same [size limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}) per parcel apply as in scenes published to LAND parcels, but you can add more parcels to your scene without any cost.

See [Worlds]({{< ref "/content/creator/worlds/about.md" >}}) for more info.

Worlds offer a few options to customize the scene sky box, which aren't available in Genesis City (where a same sky is shared by all surrounding scenes). See [World defaults]({{< ref "/content/creator/worlds/about.md#world-defaults" >}})

## Global Scenes

Global scenes can transform the already existing landscape of Decentraland, adding layers of interactivity and gameplay. These are scenes that are not constrained to only run on certain parcels of LAND or certain Worlds. Players carry them with them wherever they go.

### Portable Experience

A portable experience is linked to a NAME token. NAME tokens can be bought in the [Marketplace](https://decentraland.org/marketplace/names/claim). You can claim any name you want as long as it's not claimed yet.

{{< hint warning >}}
**📔 Note**: If a NAME token is assigned to a World, it can't also be used for a Portable Experience. Prior content will be overwritten.
{{< /hint >}}

Portable experiences can be activated as part of the interactive code of a scene (either in LAND or a World).

Players are prompted asking if they want to run this portable experience, and if they do they'll carry it with them wherever they go for the rest of their session. [Learn more]({{< ref "/content/creator/sdk7/projects/portable-experiences.md" >}}).

### Smart Wearables

Smart wearables are linked to Wearable tokens. These are sold as NFTs and purchased in the [Marketplace](https://decentraland.org/marketplace/browse?section=wearables&vendor=decentraland&page=1&sortBy=newest&status=on_sale).

Smart Wearables are activated whenever the player puts on the associated wearable item. They are turned off if the player takes off the item, or they can also turn off the global scene manually via the UI.

- Learn everything about [Creating wearables]({{< ref "/content/creator/wearables-and-emotes/wearables/creating-wearables.md" >}}).

- Learn about [smart wearables]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}})
