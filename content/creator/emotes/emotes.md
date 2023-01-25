---
date: 2022-09-01
title: Emotes overview
description: Basics about the process of creating emotes for Decentraland avatars.
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

Emotes are animation sequences for avatars’ skeleton bones, which are defined in a transport file, usually in `.glb`, or `.gltf` formats.

There are a selection of free default Emotes that are available to any user, but Decentraland also supports the creation and use of custom Emotes that are represented by non-fungible tokens ( NFTs). This allows a finite amount of different Emotes to be created, or minted, on the blockchain, similar to [Wearables]({{< ref "/content/creator/wearables/wearables-overview.md" >}}).

By default, Decentraland Emotes are minted on the Polygon/Matic sidechain so users can mint, buy, sell, or transfer items without having to pay gas fees (the DAO covers these costs as voted on in [this Proposal](https://governance.decentraland.org/proposal/?id=548aa0c0-d51a-11ec-b521-2f98ffa6ccb0)).

Emotes are organized into different categories depending on what a Creator thinks best describes what an Emote does. The available categories are:

- Dance
- Stunt
- Greetings
- Fun
- Poses
- Reactions
- Horror
- Miscellaneous

## Collections & Items

As with Wearables, Emotes exist as individual **items** that can be grouped into **collections that can consist of only Wearables, only Emotes, or a combination of both.**

### Collections

**Collections** exist to help creators organize and manage their items before publication.

For example, let’s say you create an Emote that ‘shoots’ and one that makes an avatar play dead. These two Emotes could be added to a new collection called ‘Western Duel’. After publishing your collection, you can then mint copies of each Emote to share, trade, or sell.

### Items

Each different type of Emote, or **item,** can be minted to create multiple NFTs of the particular Emote in question. The amount of NFTs you can mint for an Emote will depend on the rarity you select for it (the rarer the item, the fewer NFTs you can mint).
**Items** are referred to as the “representations” of an Emote. To be specific, a representation is the actual .glb file that contains the animation sequence for the Emote.

# Creating Emotes

## The Armature

[The Rig - Basic Concepts]({{< ref "/content/creator/emotes/avatar-rig.md" >}})

[Rig Features ]({{< ref "/content/creator/emotes/rig-features.md" >}})

## Animation Guidelines

[Creating and Exporting Emotes]({{< ref "/content/creator/emotes/creating-and-exporting-emotes.md" >}})

# Publishing Emotes

This document explains how the approval process works when publishing Emotes and what criteria is used by the Curation Committee when reviewing them. For detailed information on the Curation Committee, read [here]({{< ref "/content/creator/wearables/curation-committee.md" >}}).

### The Publication Process

**Summary**

1. Upload your Emote file to the Builder, define the metadata, and hit Publish.
2. After clicking ‘Publish’ on your Collection detail page, it will be submitted to the Curation Committee for approval. Collections pending approval will be flagged as “Under Review”.
3. Any collections pending approval from the Curation Committee cannot be minted until the approval process is completed.
4. Each time you publish a new collection, a post is automatically created on the [Decentraland Forum](https://forum.decentraland.org), providing a list and overview of each item in the collection. This Forum post gives the community and the Curation Committee a space to share feedback or request any changes you need to make before your collection can be approved.
5. If there are changes you need to make, the Curation Committee will notify you in the Forum thread for your collection.
6. After any needed changes have been made, you can resubmit your collection for approval. (Collections may be reviewed and rejected multiple times before final approval with no extra cost.)
7. Once your collection has final approval, you will be notified in the Forum. You will also see a visual indicator in the Editor next to the approved collection.
8. With a successful approval, you can begin minting items in your collection!

See [Editor Guide](#Editor-User-Guide) below for a detailed guide of the entire publication process

### Publication fees

A fee is required for publishing items. This fee was originally [voted in place by the Decentraland DAO](https://governance.decentraland.org/proposal/?id=50092c00-c315-11eb-ac84-1705d1ae4a66) to deter users from publishing an excessive number of Wearables in an attempt to ‘spam’ the Wearables market.

The [most recent vote](https://governance.decentraland.org/proposal/?id=b8075360-e8e7-11ec-82d9-d917cdd158ac) regarding publication fees has pegged them to a fixed amount of 150 United States dollars per item, to be paid in MANA.

For example, if you publish a collection with two items and the price of MANA at the time is 1.5 USD, you will have to pay a fee of 200 MANA (150 USD for each item divided by the price of MANA in USD) regardless of your item’s rarity (how many NFTs can be minted).

These fees are transferred to the Curator Committee and the Decentraland DAO, where they are used to help fund the growth of the Decentraland through grants and other initiatives voted on by the greater Decentraland community.

{{< hint warning >}}
**📔 Note:**    
Currently, due to the time and resources required to review each collection submitted, the 150 USD in MANA publication fee is non-refundable. If your collection is rejected, you will not receive your MANA back. If your collection is not immediately approved, the Curation Committee will provide you with suggestions and feedback on how to improve it, but the final acceptance of your collection cannot be guaranteed.
{{< /hint >}}


### Acceptance Criteria


Following is an overview of the criteria used by the Curation Committee when determining a collection’s eligibility. Much of this criteria is based on Section 2 of Decentraland’s [Content Policy](https://decentraland.org/content/).

Specifically, Emotes may not:

- Involve illegality, such as piracy, criminal activity, terrorism, or child pornography
- Infringe on third party intellectual property rights
- Contain cruel or hateful moves that could harm, harass, promote or condone violence against anyone, or that is primarily intended to incite hatred of animals or of individuals or groups based on race or ethnic origin, religion, nationality, disability, gender, age, veteran status, or sexual orientation/gender identity
- Contain content that is libelous, false, inaccurate, misleading, or invades another person’s privacy
- Breach Decentraland’s [Privacy Policy](https://decentraland.org/content/)
- Contain any content that promotes or could be construed as primarily intending to evade the limitations described above

Please refer to the full Content Policy [here](https://decentraland.org/content/) for additional details and definitions. Any submissions that violate the above criteria will be rejected.

**In addition to the Content Policy, the committee may reject submissions on the following technical conditions:**

- Emotes may not contain duplicate items within a collection. (Each item within a collection must be unique.)
- Emotes may not mimic or copy other Emotes that have already been published.
- Curators from the Curator Committee can submit collections but not approve their own. In this case, another curator from the committee would need to review in order and approve or reject.
- Emotes must not move below the floor line and must not float or jump excessively high to keep gameplay sanity.
- Max file size is 1MB
- Animations can’t be longer than 10 seconds or 300 frames
- Files can only have one animation
- Files should be exported in .glb
- Framerate is 30FPS

See [Creating and Exporting Emotes]({{< ref "/content/creator/emotes/creating-and-exporting-emotes.md" >}}) for complete specifications and guidelines.

# Editor User Guide

The Editor is a tool within Decentraland’s [Builder](https://builder.decentraland.org/) that allows you to upload, add metadata, and publish your custom Emotes or Wearables.

{{< hint warning >}}
**📔 Note**:  these Docs don’t explain how to animate an Avatar to create an Emote, they explain how to use the Editor to upload and publish your Wearables or Emotes. To create an Emote we recommend using [Blender](https://www.blender.org/).
{{< /hint >}}

### Uploading Emotes

If you haven’t uploaded any items yet, click **New Item** or **New Collection** to get started. If you’ve already uploaded Wearables or Emotes, you can either edit them by clicking on the item or collection and then clicking **Edit**, or you can upload new Emotes by clicking the **+** icon next to the **Open Editor** button.

### Creating a Collection

When creating a collection, first enter the name you would like to give your collection **(beware of IP rights and misspellings)** and click **Create**. After creating your collection, you can begin adding items.

**The name of your collection cannot be changed after publication!**


![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/Untitled.png)

You can add as many items as you want until you publish your collection. **Always remember, you cannot add, remove, or change the rarity of items in published collections.**

### Adding Items to a Collection

To add an item to your new collection, select the collection, click **Add Item**, and drop/select your  files.

![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images//emotes/Untitled%201.png)

Also, you can first create your items as Single items and then add them to a collection from the Collections Tab.

![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images//emotes/Untitled%202.png)

### Uploading an Item

When uploading an item you can either browse your computer to find the file you want, or you can click and drag your file right into the Editor.

![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images//emotes/Untitled%203.png)

After uploading your file, you will be prompted to enter some descriptive information:

![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images//emotes/Untitled%204.png)

**Name:** 
The name you would like to give your Emote.

The name of your collection cannot be changed after publication!


**Rarity:**
The rarity of your Wearable determines the total number of NFTs that may be minted based on your item. The rarities and the maximum number of NFTs that you may mint for each are:

**Play Mode:**
How the Emote will reproduce: it can be simple or loop.

**Categories:**
You can choose up to 3 categories to your Emote. Be as accurate as possible so that buyers can find what they’re looking for.

- Dance
- Stunt
- Greetings
- Fun
- Poses
- Reactions
- Horror
- Miscellaneous

When you’re finished entering your descriptive metadata, click **Next**.

**Edit the thumbnail** by choosing the frame of the animation that best represents the Emote. This is what buyers will see in the marketplace when they find your Emote. Then click **Next**.

![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images//emotes/Untitled%205.png)

**Set the price** of your Emote and the beneficiary that will get the profit from primary sales. It could be your own wallet address or someone else’s. Click **Save**.

![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images//emotes/Untitled%206.png)

After you set all the parameters of your Emote, you can see how it will look in the Editor. You can also combine it with a Wearable to see how the combination of both assets look in the Decentraland Avatar.

![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images//emotes/Untitled%207.png)

You need to make sure that your Emote is not traspassing the established boundaries. To check this in the Editor, you can turn on the cylinder view, and see if the avatar is not going over, or throught the red cylinder. The avatar must not traspass the floor either. 

![](/images/emotes/emotes-preview.png)

If everything is looking good, you are ready to **publish your Collection.**

### Publishing Items

After you’ve added all of the relevant metadata to the Emotes and Wearables in your collection, and you’ve set the price and beneficiary address (or made your items free!) you can begin the publication process.

First, navigate to the [Builder](https://builder.decentraland.org/) and select the **Collections>Emotes** tab. Select the collection you’d like to publish and click **Publish**.

You might have to authorize the MANA contract to operate MANA on your behalf. By granting this authorization, you are permitting the MANA smart contract to withdraw MANA from your balance to pay the publication fee and to deposit MANA into your account from future sales of your items. In this scenario, you will have to sign a message from your wallet, but there is no gas fee.

When you are ready, click **Publish** and sign the message when prompted by your wallet.

![Untitled](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images//emotes/Untitled%208.png)

{{< hint danger >}}
**❗Warning**  

**You will not be able to add or remove items in your collection after beginning the publication process.** You will be able to see your items within the Decentraland Marketplace, but you won’t be able to buy, sell, or transfer them until they have been approved by the Curator Committee.

{{< /hint >}}


### Selling Items

After your items are published in a collection and approved by the Curator Committee, they can be sold to other users in Decentraland.

Items can be sold in the **Store** **(primary sales)** and in **Listings (secondary sales)**.

- **Primary sales** are performed by the Decentraland Store’s smart contract. During a primary sale, the **item is minted automatically**, and is sold for the price set by you in the Wearable Editor.
- **Secondary sales** are performed by the Decentraland Marketplace’s smart contract. These occur anytime a user sells an item in the Marketplace **after it has been minted** or **purchased in a primary sale**. Items can be sold for any price in a secondary sale.
