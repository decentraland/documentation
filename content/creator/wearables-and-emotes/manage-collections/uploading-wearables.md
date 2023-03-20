---
date: 2023-01-07
title: Uploading Wearables
description: Guidelines to upload Wearables to the Editor
categories:
  - Decentraland
type: Document
aliases:
  - /wearables/creating-wearables/
  - /decentraland/creating-wearables/
url: /creator/wearables/creating-wearables
weight: 2
---

# **Uploading Wearables**

Once you export your wearable, you’ll have to upload it to the builder. This document will cover the process of uploading wearables.

# **Uploading Your File**

Remember that you need to create a collection before you can upload your file. If you don’t know how to do that, check [Creating a Collection](/creator/wearables-and-emotes/manage-collections/creating-a-collection.md). To upload your wearable, just drag and drop the file on the ***New Item*** window or browse your computer. It will automatically detect if the file is an emote or wearable. **Remember that the collection max file size is 2MB**.

[NewItem]({{< ref “/images/uploading-wearables/01_new_item.png”>}})

When you upload the file, you will be asked to select a body shape, enter a name and define the rarity and the category. You can also add the thumbnail for the wearable.

### **Body Shape**

To ensure that your wearables can be worn by the intended avatars, you need to upload separate GLB files for each body shape. If you have two separate versions of the wearable, one for male and one for female, you can add one of the representations during the upload process and then add the other later using the editor. If your wearable is meant to be unisex, make sure to upload a single GLB file that is designed to fit both male and female versions.

[BodyShape]({{< ref “/images/uploading-wearables/03_body_shape.png”>}})
[BodyShapeBoth]({{< ref “/images/uploading-wearables/09_new_item.png”>}})

### **Rarity**

Add the rarity here:

|          Rarity |     Number of Items |
| --- | --- |
| Unique | 1 |
| Mythic | 10 |
| Legendary | 100 |
| Epic | 1,000 |
| Rare | 5,000 |
| Uncommon | 10,000 |
| Common | 100,000 |

[Rarity]({{< ref “/images/uploading-wearables/04_rarity.png”>}})

### **Category**

Wearables are organized into different categories, depending on what part of an avatar they modify. Select the appropriate category for your item.

[Category]({{< ref “/images/uploading-wearables/05_category.png”>}})

### **Custom Thumbnails**

You can add your own custom thumbnail by clicking on the camera icon and browsing your computer. Thumbnails must be a `.png` file of 512x512 pixels with transparent background. Collections containing thumbnails without transparent backgrounds will not be accepted by the Curation Committee.

[Thumbnail]({{< ref “/images/uploading-wearables/06_thumbnail.png”>}})

{{< hint warning >}}
Having a good render of your wearable is crucial in making it more appealing to potential users in the marketplace. It's important to avoid adding any graphics other than the wearable itself, because this may cause the curation committee to reject it.

[ThumbnailName]({{< ref “/images/uploading-wearables/07_thumbnail.jpeg”>}})
{{< /hint >}}

### **Properties**

Below the thumbnail you're going to find the properties of your wearable, number of triangles of your model, number of materials and textures.

[Properties]({{< ref “/images/uploading-wearables/08_properties.png”>}})


## **Uploading Mouth, Eyes and Eyebrows**

The mouth, eyes and eyebrows category have a different behaviour in the editor because these are just .png files. To upload these just drag and drop the png file as a transparent image (256X256 pixels). Mouth is going to be automatically tinted by skin color, same for the eyebrows tinted by the hair color.

If you want the asset to be masked, so a part of the mouth or eyebrows is not affected by the tinting, upload a zip file with both the png and the mask files. Remeber that the mask file should have a suffix “_mask” in order to work.

[MouthWearable]({{< ref “/images/uploading-wearables/02_mouth_wearable.png”>}})


After that uploading your wearables you will end up with a screen like this, that shows the items in your collection.

[WearablesList]({{< ref “/images/uploading-wearables/11_list_wearables.png”>}})

## **Setting the Price**

You can set the price of your wearable by clicking on ***Set Price***. This can all be edited anytime, so don’t worry if you want to change it later on. Prices are set in MANA. Remember that when you mint wearables, they are minted directly on Matic/Polygon. When a user purchases your item, the transaction will be conducted in Matic/Polygon MANA. 

You could also ***Make it Free***, which means that the price will be set as 0 MANA and the beneficiary address will be null. Know that making it free (primary sale) does not prevent it from being sold at any price as a secondary sale.

Don’t forget to set the beneficiary address, which is the one that will receive the MANA from your sales. You can use any Ethereum address you like. To automatically fill in the address you are logged in with, click ***I’m the Beneficiary.***

[SetPrice]({{< ref “/images/uploading-wearables/12_set_price.png”>}})

Save the price and you will be back to the list of wearables in your collection. When you click on the item, you will get its general info. Click on the button ***Preview*** to see it on the editor.

[ClickItem]({{< ref “/images/uploading-wearables/13_click_item.png”>}})

# **The Editor**

Once you click on ***Preview***, you will have the editor open. You can edit all the info of your wearable, as well as add new ones, such as description, tags and overrides. This also where you add other body shape representation to your wearable.

[Editor]({{< ref “/images/uploading-wearables/14_editor.png”>}})

## **Description**

This is a brief statement describing your item that will be displayed in the marketplace.

## **Overrides**

Overrides determine what other wearable categories your item will either replace, or hide. For example, if a hat has hair attached to the model, you might want to hide the category ***Hair***. Or if you are submitting a deep sea diver helmet you may want hide all the head accessories that are not going to be visible such as earrings, eyewear, tiara, etc. You can add multiple categories to each override; just select them on the dropdown menu.

- **Replaces**: any items within the categories added to this override will be unequipped from a users’ avatar when they equip your item. A user would have to re-equip any “replaced” items after unequipping your item. This does not delete items, it only unequips them.
- **Hides**: any items within the categories added to this override will only be hidden (they won’t be rendered) when a user equips your item. When a user unequips your item, the hidden items will be rendered again automatically.

For a detailed description of each category, and how items within each category interact or replace one another, see **[Creating Wearables](https://docs.decentraland.org/creator/wearables-and-emotes/wearables/creating-wearables/)**.

## **Tags**

Tags are simply descriptive words that users can use when searching or filtering for items. These are relevant to competitions or events!

## **Adding Another Representation**

If your wearable has a different representation for male and female you will need to upload another file. So far, you only have one uploaded. In the example, it was the female version of the Krampus Sweater. To add the other representation, click on the three dots (*…*) at the top right, next to ***Properties*** and select ***Add male/female*** representation. In the example below, we needed the male version.

[Variation]({{< ref “/images/uploading-wearables/15_add_variation.png”>}})

Once you click on it, you will get the Add Male/Female Representation window, so drag and drop the other representation file to upload it. Once uploaded, another window will show up the wearable and if everything is ok, just click on Save.

[AddRepresentation]({{< ref “/images/uploading-wearables/16_add_male_representation_01.png”>}})

[AddMaleRepresentation]({{< ref “/images/uploading-wearables/17_add_male_representation_02.png”>}})


## **Preview**

To preview your wearable, hover your mouse over the wearable icon on the top left and click on the eye symbol.

[PreviewWearable]({{< ref “/images/uploading-wearables/18_preview_wearables_03.gif”>}})

By clicking on the icon at the lower left you will be able to edit the avatar. This is pretty useful if you have a male and female version of your wearable, so make sure to check how both versions look like in editor, testing different emotes to identify if there are any skinning issues and mixing other wearables to see how it matches with different clothes. When you’re done editing your wearable, click on Save.

[EditAvatar]({{< ref “/images/uploading-wearables/19_edit_avatar_wearable_03.gif”>}})

## **Testing in World**

Even after testing the wearable in the editor, it’s important to check how it’s actually going to look like and behave in Decentraland. To test it in world, go to the Collections tab, select the desired collection and it will show all the items you have in it. Click on the three dots (***…***)next to the item you want to test and select ***See in world***.

[TestInWorld]({{< ref “/images/uploading-wearables/20_test_in_world_01.png”>}})

Once you select ***See in world***, a new tab will open on your browser and you will get this message.

[Goerli]({{< ref “/images/uploading-wearables/21_goerli.png”>}})

Click on Switch to Goerli and a popup from your wallet will show up asking to switch the network. Simply click on Switch Network and the new tab will automatically refresh. To test your wearable, go in the backpack and select it.

[WearableWorld]({{< ref “/images/uploading-wearables/22_wearable_world.gif”>}})

## **Before Publishing**

Make sure to set the price properly, add a nice description and double check if all the information and settings are right. If you’ve filled all the information necessary you will see ***Done*** as the status of your item.









