---
date: 2021-05-31
title: Wearables Overview
aliases:
  - /wearables/wearables-overview/
  - /decentraland/wearables-overview/
description: An overview of wearables NFTs for Decentraland
categories:
  - Decentraland
type: Document
url: /creator/wearables/wearables-overview
weight: 1
---

<iframe id="emote-preview" style="width:100%;border:0;height:60vh;"></iframe>

<script>
  const profile = Math.ceil(Math.random() * 120)
document.getElementById("emote-preview").src = "https://wearable-preview.decentraland.org/?profile=default"+profile+"&transparentBackground&loop=true"

  function changeProfile() {
document.getElementById("emote-preview").contentWindow.postMessage({
  type: 'update',
  payload: { options: {
    profile: `default${Math.ceil(Math.random() * 120)}`
  } }
},'*')
return false
  }
</script>

<a onclick="changeProfile()" style="cursor: pointer">Refresh wearables ↺</a>

# **Wearables Overview**

<img src="/images/wearables-overview/00_wearables_overview.png" alt="WearablesOverview" width="400"/>

## **What are wearables?**

Wearables are the various items of clothing, accessories, and body features that can be used to customize the appearance of a Decentraland avatar. There is a selection of default wearables that are freely available to all avatars, but Decentraland also supports the creation and use of custom wearables that are represented by non-fungible tokens (or NFTs). This allows a finite amount of different wearables to be created, or minted, on the blockchain, similar to the LAND.

There’s a growing range of available wearables including cyberpunk themed sneakers, fashionable jackets, fun top hats, and more! All of these stylistic choices give users an exciting and meaningful way to invest in, and express, their own unique personalities. By allowing wearables to be minted, and then sold, as NFTs, Decentraland provides content creators with a fun way to monetize their creative work.

By default, Decentraland Wearables are minted on the Polygon/Matic side-chain so users can mint, buy, sell, or transfer items without having to pay gas fees.

**Wearables are organized into different categories, depending on what part of an avatar they modify:**

- Body shape (the shape of the entire avatar)
- Hair
- Facial hair
- Head
- Upper body
- Lower body
- Feet
- Skin

**Wearables can also include accessories that are applied to different parts of an avatar’s body:**

- Mask
- Hat
- Helmet
- Eyewear
- Earring
- Tiara
- Top-head (wearable that goes above the head)

For a detailed description of each category, and how items within each category interact or replace one another, see **[Creating Wearables]({{< ref "/content/creator/wearables-and-emotes/wearables/creating-wearables.md" >}})**.

The following shared folder contains example wearables, base models, textures and other resources you can use:

- **[Wearables Reference Models](https://drive.google.com/drive/u/1/folders/12hOVgZsLriBuutoqGkIYEByJF8bA-rAU)**