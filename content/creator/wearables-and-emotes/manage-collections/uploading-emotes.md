---
date: 2023-01-07
title: Uploading Emotes
description: Guidelines to upload Emotes to the Editor
categories:
  - Decentraland
type: Document
aliases:
url: /creator/wearables-and-emotes/manage-collections/uploading-emotes
weight: 3
---

Once you export your emote, you’ll have to upload it to the builder. This document will cover the process of uploading emotes.

## **Uploading Your File**

Remember that you need to create a collection before you can upload your file. If you don’t know how to do that, check [Creating a Collection](/creator/wearables-and-emotes/manage-collections/creating-a-collection.md). To upload your emote, just drag and drop the file on the **_New Item_** window or browse your computer. It will automatically detect if the file has any animation, identifying it as an emote.

<img src="/images/wearables-and-emotes/uploading-emotes/01_new_item.png" width="400" />

_Drag and drop your animation file to upload it._

You will be asked to enter a name for your emote, define its rarity, the category and the play mode. Below the thumbnail is shown the number of animation clips in your file, the length of the animation in seconds, the length in frames and the frame rate.

<img src="/images/wearables-and-emotes/uploading-emotes/upload_emote.png" width="400" />

## **Uploading Emotes Using a .zip File**

If the emote has sound (_mp3_ or _ogg_) it must be zipped with the `.glb`. After that, just drag and drop the `.zip` to the builder. Also, it is possible to add a `.json` file along with the other assets in the same `.zip` to add name, description, rarity, category, play mode and/or tags. These are the definitions for each:

- `name`: Name of the Emote
- `description`: Description of your Emote (no more than 64 characters in total, counting spaces)
- `category`: Category of the Emote ("dance", "stunt", "greetings", "fun", "poses", "reactions", "horror", "miscellaneous")
- `rarity`: Rarity of the Item ("unique", "mythic", "legendary", "epic", "rare", "exotic", "uncommon", "common")
- `play_mode`: Simple or Loop Animation ("simple", "loop")
- `tags`: Tags for easy finding in the marketplace.

To add those definitions to the emote just create a text file, naming it **emote.json** and add the following lines as the example:

```
{
  "name": "Tennis Shot",
  "description": "Show me you can do tennis",
  "category": "fun",
  "rarity":"epic",
  "play_mode": "simple",
  "tags":["tennis", "emote", "shot"]

}

```

This way the builder is going to take all the .json information and it automatically to the emote.

**Rarity**

Check the rarity chart in [here](/creator/wearables-and-emotes/manage-collections/creating-a-collection.md#rarity).

## **Category**

Choose the category that best describe your emote.

- Dance
- Stunt
- Greetings
- Fun
- Poses
- Reactions
- Horror
- Miscellaneous

## **Play Mode**

There are currently two play modes:

- **_Play Once_**: means that your emote will only play once. After that the avatar will return to _Idle_ position.
- **_Loop_**: the emote will keep playing in loop until the user input another action.

## **Custom Thumbnails**

For emotes, you don’t have to upload any images since the editor already has a built in tool to create a thumbnail. Just select the frame that best represents the action.

{{< hint warning >}}
People should be able to identify what the animation is about through the thumbnail. If a front shot isn’t good enough, try rotating the model, zoom in or out, pan up or down, pick any frame from your clip. It’s really important that you select the best shot!
{{< /hint >}}

<img src="/images/wearables-and-emotes/uploading-emotes/Edit_thumbnail.gif" width="600" />

_Rotate, zoom in or out, pan up and down. Use the tools to get the best shot of your animation!_


## The Editor

Once you set the thumbnail, you will have the editor open. This is where you can check if the animation is playing well since a 3D avatar will be performing it.

<img src="/images/wearables-and-emotes/uploading-emotes/boundaries.png" width="900" />
_The editor._

By clicking on the icon at the lower left you will be able to edit the avatar. Click on the cilinder icon on the lower right to check if you animation is staying within the boundaries of height and space.

<img src="/images/wearables-and-emotes/uploading-emotes/edit_avatar.gif" width="900" />

<img src="/images/wearables-and-emotes/uploading-emotes/edit_avatar.gif" width="900" />

_Cylinder icon shows the boundaries for the animation._

You can also edit the emote’s name, thumbnail, category, rarity and play mode, as well as add a description of the animation and add tags to it. Click on **_Save_** when you are done.

- **Description:** This is a brief statement describing your item that will be displayed in the marketplace.
- **Utility** Describe the in-world utility of the Wearable or Emote.
- **Tags:** Tags are simply descriptive words that users can use when searching or filtering for items. These are relevant to competitions or events!

<img src="/images/wearables-and-emotes/uploading-emotes/08_description.png" width="900" />

# Testing in World

Even after testing the animation in the editor, it’s important to check how it’s actually going to look like and behave in Decentraland. To test it in world, go to the Collections tab, select the desired collection and it will show all the items you have in it. Click on See in Decentraland.

<img src="/images/wearables-and-emotes/uploading-emotes/09_test_in_world.png" width="900" />

You will be asked to choose if you want to test it in an Empty Parcel or in Genesis Plaza. Selecting Empty Parcels will teleport you to a place without too much content, which will load faster. Selecting Genesis Plaza will take you to the main plaza.

<img src="/images/wearables-and-emotes/uploading-wearables/23_see_in_world.png" width="600"/>

After choosing, a new tab will be open in your browser with a message informing you that you are about to use a custom Catalyst. Click on TRUST PEER-TESTING.DECENTRALAND.ORG to continue.

<img src="/images/wearables-and-emotes/uploading-emotes/13_emote_preview.png" width="900"/>

After that, you will get a pop-up asking to open the Decentraland Explorer. Once the explorer is running, click on Jump Into Decentraland. 

<img src="/images/wearables-and-emotes/uploading-emotes/14_emote_gif.gif" width="900" />

Once in world, press I to open the backpack and, in the emotes tab, select the emote to test.

<img src="/images/wearables-and-emotes/uploading-emotes/14_emote_gif.gif" width="900" />


## **Before Publishing**

Make sure to add a nice description and verify if all the information and settings are right. Double check the thumbnail too. If you’ve filled all the information necessary you will see Ready to Submit as the status of your item. Now your emote is ready to be published!

<img src="/images/wearables-and-emotes/uploading-emotes/12_item_ready.png" width="900" />

_The Done status means that your file is ready be published!_
