---
date: 2021-05-31
title: Publishing Collections
aliases:
  - /wearables/publishing-wearables/
  - /decentraland/publishing-wearables/
description: A description of the publication and approval process for Decentraland wearables
categories:
  - Decentraland
type: Document
url: /creator/wearables/publishing-collections
weight: 3
---

For detailed instructions on how to submit your collections for approval before publication, see [how to create a collection]({{< ref "/content/creator/wearables-and-emotes/manage-collections/creating-a-collection.md" >}}). This document explains how the approval process works when publishing wearables and emotes, and what criteria is used by the Curation Committee when reviewing wearables. For detailed information on the Curation Committee, [start here]({{< ref "/content/creator/wearables-and-emotes/publishing/curation-committee.md" >}}).

## **The Publication Process**

1. After clicking "Publish" on your completed proposal and pay the fees of the items, the collection will be submitted to the Curation Committee for approval. Collections pending approval will be flagged as "Under Review".
2. Any collections pending approval from the Curation Committee may not be minted until the approval process is completed.
3. Each time you publish a new collection, a post is automatically created on the [Decentraland Forum](https://forum.decentraland.org/), providing a list and overview of each item in the collection. This Forum post gives the community and the Curation Committee a space to share feedback or request any changes that you need to make before your collection can be approved.
4. If there are changes you need to make, the Curation Committee will notify you in the Forum thread of your collection.
5. You can make any necessary modifications and submit your collection for approval again. It is possible for collections to undergo multiple reviews and rejections before receiving final approval.
6. Once your collection has final approval, you will be notified in the Forum. You will also see a green visual indicator in the Wearable Editor next to the approved collection.
7. With a successful approval, you can begin minting items in your collection!

## **Publication Fees**

There is a required fee for publishing items. This fee was originally [voted in place by the Decentraland DAO](https://governance.decentraland.org/proposal/?id=50092c00-c315-11eb-ac84-1705d1ae4a66) to deter users from publishing an excessive number of wearables in an attempt to "spam" the wearables market.

On Jun 24, 2022 [a proposal](https://governance.decentraland.org/proposal/?id=b8075360-e8e7-11ec-82d9-d917cdd158ac
) regarding publication fees has pegged them to a fixed amount of **150 USD per item, to be paid in Polygon MANA**.

**Update**: On Sep 02, 2023 [a proposal](https://governance.decentraland.org/proposal/?id=98d74360-3eae-11ee-88e6-1fe6cb69ee51) updated the publication fees to **100 USD per item, to be paid in Polygon MANA**.

{{< hint warning >}}
**📔 Note**: You can move MANA between Ethereum and Polygon using the [Account dApp](https://account.decentraland.org).
{{< /hint >}}

For example, if you publish a collection with two items and the price of MANA at the time is 1.25 USD, you will have to pay a fee of 160 MANA (100 USD for each item divided by the price of MANA in USD) regardless of the rarity (or how many NFTs can be minted) of those items.

These fees are transferred to the curators committee and the Decentraland DAO, where they are used to help fund the growth of the platform through grants and other initiatives voted on by the greater Decentraland community.

{{< hint warning >}}
**📔 Note**: Currently, due to the time and resources required to review each collection submitted, **the publication fee is non-refundable**. If your collection is rejected, you will not receive your MANA back. If your collection is not immediately approved, the Curation Committee will provide you with suggestions and feedback on how to improve it, but the final acceptance of your collection cannot be guaranteed.
{{< /hint >}}

## **Acceptance Criteria**

Following is an overview of the criteria used by the Curation Committee when determining a collection’s eligibility. Much of this criteria is based on Section 2 of Decentraland’s [Content Policy](https://decentraland.org/content/).

Specifically, wearables may not:

- Involve illegality, such as piracy, criminal activity, terrorism, or child pornography
- Infringe third party intellectual property rights
- Contain cruel or hateful imagery that could harm, harass, promote or condone violence against, or that is primarily intended to incite hatred of, animals, or individuals or groups based on race or ethnic origin, religion, nationality, disability, gender, age, veteran status, or sexual orientation/gender identity
- Contain content that is libelous, false, inaccurate, misleading, or invades another person's privacy
- Breach the Privacy Policy
- Contain any content that promotes or could be construed as primarily intending to evade the limitations described above

Please refer to the full Content Policy [here](https://decentraland.org/content/) for additional details and definitions. Any submissions that violate the above criteria will be rejected.

**In addition to the Content Policy, the committee may reject wearable submissions on the following technical conditions:**

> - It is important that wearables be "skin weighted" correctly so that the avatar animations can be rendered as expected. Wearables without correct skin weighting will be rejected.
> - Wearables must preserve avatar UV mapping to ensure that user-selected skin tones can be rendered as expected.
> - The dimensions of eyebrow, eye, and mouth textures should not exceed 256 by 256px, and the image must have transparent background.
> - In the case of hands category, the wearable cannot be an item attached to the hand (a sword, shield, etc). The category is meant by hand accesories like bracelets, watches, rings,etc. and in the case of replacing the hand completely it should follow a proper armature skinning for the hand bones. 
> - Wearables with a disproportionate number of triangles, textures and materials may be rejected because can cause poor performance and a bad experience for players. Creators should not exceeding the limitation [guidelines]({{< ref "/content/creator/wearables-and-emotes/wearables/creating-wearables.md" >}}) when creating wearables. 
> - Wearables may not contain duplicate items within a collection. (Each item within a collection must be unique.)
> - Wearables may not mimic or copy other wearables that have already been published.
> - For security reasons, any wearables that contain any kind of QR Code may be rejected.
> - Wearables that exceed the space restrictions.
> - Wearables with misleading categories may be rejected; for example, a hat that is categorized as a lower body item.
> - Wearables must follow the armature humanoid structure to ensure a good quality gameplay. In this sense, currently vehicles or pets are not allowed because these are not wearables by definition.
> - Emotes that exceed the time and space restrictions. For more info check the [emote guidelines]({{< ref "/content/creator/wearables-and-emotes/emotes/creating-emotes.md" >}})
> - Curators from the curators committee can submit collections but not approve their own. In this case, another curator from the committee would needs to review in order and approve or reject.

## **Attributing Collaborators [#](https://docs.decentraland.org/creator/wearables/wearables-editor-user-guide/#attributing-collaborators)**

If you collaborated with other artists when creating your items, you can add attributions within the Wearables Editor. This can only be done after publishing a collection.

First, navigate to the **[Builder](https://builder.decentraland.org/)** and select the **Collections** tab. Select the collection containing the items you want to add attributions to, click the **…** icon next to the **Mint Items** button, and select **Collaborators**.

To add collaborators, simply enter their Ethereum address, and click **Add**. You can add as many collaborators as you want. To remove a collaborator, simply click **Remove** next to the collaborator’s address.

<img src="/images/wearables-and-emotes/publishing-collections/add-collaborators.png" width="900" />

## **Selling Items**

After your items are published in a collection and approved by the Curation Committee, they can be sold to other users in the metaverse.

Items can be sold in **primary sales** and **secondary sales**.

- **Primary sales** are performed by the Decentraland Store’s smart contract. During a primary sale, the **item is minted automatically**, and it is sold for the price set by you in the Wearable Editor.
- **Secondary sales** are performed by the Decentraland Marketplace’s smart contract. These occur anytime a user sells an item in the Marketplace **after it has been minted** or **purchased in a primary sale**. Items can be sold for any price in a secondary sale.

To view items available to purchase in a primary and secondary sales, head to the **[Decentraland Marketplace!](https://market.decentraland.org/)**

## **Primary Sales**

Primary sales occur when one of your items is purchased for the first time. These sales are only performed by the Decentraland Store’s smart contract.

When a user makes a primary purchase of one of your items, the store **mints the item automatically**, transfers the item to the purchaser, and sends the MANA proceeds to the beneficiary address.

> Remember! You do not need to mint your items in order to sell them in primary sales!

To sell your items via primary sales, begin by navigating to the **[Builder](https://builder.decentraland.org/)** and follow the next steps:

To enable Primary Sales, go to the **Collections** tab, select the one you want to enable and toggle the **_On Sale_** button, after that click **Turn On** in the confirmation window that appears. **When this switch is enabled, your collection will be available to purchase within the Decentraland store.**

<img src="/images/wearables-and-emotes/publishing-collections/selling-items-toggle.png" width="600" />

If the switch is turned on, the Decentraland store will automatically mint one of your items whenever a user makes a primary purchase. This allows you to mint and sell all of your available items until the maximum supply is reached. If you want to save one or more of your items before listing them for sale, you need to manually mint an item to one of your own wallet addresses.

Any purchaser of one of your items is able to resell it at any time and at any price in Decentraland's [Marketplace](https://market.decentraland.org/).

**All Primary Sales in the Decentraland in-world store are subject to a 2.5% fee, which is transferred to the Decentraland DAO.**

If you sell an item through a primary sale, you will receive your MANA on Polygon. The proceeds of any items sold on Polygon will reside on the sidechain. If you want to transfer your MANA from the Polygon sidechain to the main Ethereum chain, you will have to pay a transaction fee. You can do so from the [Accounts](https://account.decentraland.org/) page. For more information on the Polygon sidechain, see [this blog post](https://decentraland.org/blog/announcements/polygon-mana/).

### **Disabling Primary Sales**

To unlist your items, untoggle the **On Sale** switch to turn it off. This will only apply to primary sales for your items.

## **Secondary Sales**

Items can be sold in secondary sales at any time, and for any price, in the Decentraland Marketplace only after:

- They have been **minted**
- They have been **purchased in a Primary Sale**

In other words, anybody who owns an NFT for a wearable can sell it in the Decentraland Marketplace. There are royalties for wearables sold in secondary sales in Decentraland. Royalties goes to the item beneficiary.

## **Minting Wearables**

Minting is the process of creating the actual non-fungible tokens (NFTs) based on the items you’ve uploaded to the Wearables Editor.

All wearables in Decentraland are minted on the Polygon sidechain. This allows users to mint and transfer items without paying any gas fees (so long as these transactions are conducted solely on the Polygon sidechain).

As with selling items in primary sales, you will not be able to mint any items within a collection until the review process is complete. If your collection is still under review, you will see the tag **"Under Review"** appended to your collection. After it has been reviewed and approved, the tag will change to **"Published"**, and you can begin minting your items manually.

### **How To Manually Mint Items**

To mint published items, open the collection containing the items you’d like to mint, and click **Mint Items**.

<img src="/images/wearables-and-emotes/publishing-collections/minting-items-1.png" width="600" />

You will be shown a modal window containing a list of the items available along with the supply available for each. Remember, the supply is the total number of items you can mint. For example, if your supply reads 0/10, then you have used 0 out of your total supply of 10.

<img src="/images/wearables-and-emotes/publishing-collections/minting-items-2.png" width="600" />

When minting, you must set the address that will receive the minted items and you must set the number of items you want to mint to that address. You cannot mint more items than are available in the supply available.

If you enter your own address, then the items that are minted will be transferred to your account.

You can “gift” items to anyone you like by entering their address instead of your own under Address.

Remember, these items are minted and transferred to the address entered for free. The price you set for items is only collected in primary sales.

{{< hint warning >}}⚠️ Note: You can currently only mint 50 items per transaction. {{< /hint >}}

Are there any fees associated with minting items? No, items are minted on the Matic sidechain, thus removing any fees traditionally associated with minting NFTs on the main Ethereum blockchain.

### **Adding Minters to the Collection**

To add minters, simply enter their Ethereum address, and click **Add**. You can add as many minters as you want. To remove a minter, simply click **Remove** next to the minter’s address.

<img src="/images/wearables-and-emotes/publishing-collections/add-minters.png" width="600" />
