---
date: 2025-02-14
title: Scene Admin
description: Scene administrators have special control over what happens in the scene in real time.
categories:
  - scene-editor
type: Document
url: /creator/editor/scene-admin
weight: 8
---

Grant certain players the special role of admin on your scene. When a scene admin visits your scene, they will see a special UI on the top-right corner that only they are able to see. Through this UI they can pass video URLs to play, send announcements, drop collectibles, or activate any smart item in the scene. These actions are seen by all players in the scene that are connected to the same island as the admin.

During a live event, an admin can spontaneously control what happens in the scene from inside Decentraland, without needing to pre-schedule actions or relying on a 3rd party service. Start playing the music when enough of a crowd gathered, drop confetti or make a spaceship appear when the time feels right.

## Setting up admins

Add the Scene Admin Smart Item

- deployer
- scene owners?
- allowlisted

Open the UI

Icon screenshot, expanded

## Video playing

Add Video Player smart item

Configure Scene Admin Smart Item to point to it

You can list as many video players as you want

Check **Link all screens by default** if you want all screens to show the same video.

Note: This will make your scene run a lot smoother. You should avoid trying to have more than one different video playing at the same time, as that hurts performance a lot. You can have up to dozens of screens playing at the same time without much effort, as long as they're linked and playing the same video.

UI inworld

Screenshot

- Select which screen

- Paste a URL
  Note: The videos need to have CORS, etc, link to video doc

Press **Share** for all players to see

- Stop/pause/etc

- Mute/ volume controls

## Announcements

In the Announcements tab, admins can write messages that get seen by all players in the scene. Messages sent like this are perceived as more legitimate than a message on the chat by someone claiming to be an admin.

Write a message and click **Share**. The message can be up to 150 characters long.

You can write a message

## Airdrops

- Create an airdop in the Rewards server (link)

- Add a Collectible dispenser Smart Item

- Configure it with your Campaign ID and Dispenser Key

- Reference it from the Scene Admin smart item, give it a name

- In world select the Airdrop tab, select the airdop from the dropdown and select **Release**. Players will then see the airdrop drone descend to the ground, where they can click on the item to claim it. They will have to complete a Captcha

TODO: Always captcha or only if configured in the campaign??

## Trigger smart items

Trigger any action from a smart item that is present in the scene.

- Add any smart item
- Configure the Scene Admin Smart Item to reference it. give it a custom name and select a default action
- In the scene, select the Smart Item Actions tab

Select from the list of smart items configured on the Scene Admin Smart item, select the action and trigger it

You can also show or hide any smart item in this list, even if it doesn't have an action configured for that
