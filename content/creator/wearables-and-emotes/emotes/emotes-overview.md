---
date: 2023-01-07
title: Emotes Overview
description: An overview of emotes NFTs for Decentraland
categories:
  - emotes
type: Document
aliases:
  - /emotes/emotes/
  - /creator/emotes/emotes/
url: /creator/emotes/emotes-overview
weight: 1
---

<iframe id="emote-preview" style="width:100%;border:0;height:60vh;"></iframe>

<script>
  const profile = Math.ceil(Math.random() * 120)
  const emotes = ['clap', 'dab', 'dance', 'fashion', 'fashion-2', 'fashion-3','fashion-4', 'love', 'money', 'fist-pump', 'head-explode']
function emote() {
  return emotes[Math.floor(Math.random() * emotes.length)]
}
document.getElementById("emote-preview").src = "https://wearable-preview.decentraland.org/?profile=default"+profile+"&emote="+emote()+"&transparentBackground&loop=true"

  function changeProfile() {
document.getElementById("emote-preview").contentWindow.postMessage({
  type: 'update',
  payload: { options: {
    profile: `default${Math.ceil(Math.random() * 120)}`
  } }
},'*')
return false
  }

  function changeEmote() {
document.getElementById("emote-preview").contentWindow.postMessage({
  type: 'update',
  payload: { options: {
    emote: emote()
  } }
},'*')
return false
  }
</script>

<a onclick="changeProfile()" style="cursor: pointer">Change avatar ↺</a> - <a onclick="changeEmote()" style="cursor: pointer">Change emote ↺</a>


Emotes are animation sequences for avatars’ skeleton bones, which are defined in a transport file, usually in `.glb`, or `.gltf` formats.

There are a selection of free default Emotes that are available to any user, but Decentraland also supports the creation and use of custom Emotes that are represented by non-fungible tokens ( NFTs). This allows a finite amount of different Emotes to be created, or minted, on the blockchain, similar to **[Wearables](https://docs.decentraland.org/creator/wearables/wearables-overview/)**.

By default, Decentraland Emotes are minted on the Polygon/Matic sidechain so users can mint, buy, sell, or transfer items without having to pay gas fees (the DAO covers these costs as voted on in **[this Proposal](https://governance.decentraland.org/proposal/?id=548aa0c0-d51a-11ec-b521-2f98ffa6ccb0)**).

Emotes are organized into different categories depending on what a Creator thinks best describes what an Emote does. The available categories are:

- Dance
- Stunt
- Greetings
- Fun
- Poses
- Reactions
- Horror
- Miscellaneous