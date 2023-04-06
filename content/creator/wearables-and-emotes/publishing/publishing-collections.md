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
# **Publishing Collections**
For detailed instructions on how to submit your wearable collection for approval before publication, see the [User Guide](https://docs.decentraland.org/decentraland/wearables-editor-user-guide/). This document explains how the approval process works when publishing wearables, and what criteria is used by the Curation Committee when reviewing wearables. For detailed information on the Curation Committee, [start here]({{< ref "/content/creator/wearables-and-emotes/publishing/curation-committee.md" >}}).

## **The publication process**

1. After clicking "Publish" on your completed proposal, it will be submitted to the Curation Committee for approval. Collections pending approval will be flagged as "Under Review".
2. Any collections pending approval from the Curation Committee may not be minted until the approval process is completed.
3. Each time you publish a new collection, a post is automatically created on the Decentraland Forum, providing a list and overview of each item in the collection. This Forum post gives the community and the Curation Committee a space to share feedback or request any changes that you need to make before your collection can be approved.
4. If there are changes you need to make, the Curation Committee will notify you in the Forum thread for your collection.
5. After any needed changes have been made, you can resubmit your collection for approval. (Collections may be reviewed and rejected multiple times before final approval.)
6. Once your collection has final approval, you will be notified in the Forum. You will also see a visual indicator in the Wearable Editor next to the approved collection.
7. With a successful approval, you can begin minting items in your collection!

## **Publication fees**

There is a required fee for publishing items. This fee was originally [voted in place by the Decentraland DAO](https://governance.decentraland.org/proposal/?id=50092c00-c315-11eb-ac84-1705d1ae4a66) to deter users from publishing an excessive number of wearables in an attempt to "spam" the wearables market.

The [most recent vote](https://governance.decentraland.org/proposal/?id=b8075360-e8e7-11ec-82d9-d917cdd158ac) regarding publication fees has pegged them to a fixed amount of 150 United States dollars per item, to be paid in **Polygon MANA**.

{{< hint warning >}}
**📔 Note**: You can move MANA between Ethereum and Polygon using the [Account dApp](https://account.decentraland.org).
{{< /hint >}}

For example, if you publish a collection with two items and the price of MANA at the time is 1.5 USD, you will have to pay a fee of 200 MANA (150 USD for each item divided by the price of MANA in USD) regardless of the rarity (or how many NFTs can be minted) of those items.

These fees are transferred to the curators committee and the Decentraland DAO, where they are used to help fund the growth of the platform through grants and other initiatives voted on by the greater Decentraland community.

{{< hint warning >}}
**📔 Note**: Currently, due to the time and resources required to review each collection submitted, **the 150 USD in MANA publication fee is non-refundable**. If your collection is rejected, you will not receive your MANA back. If your collection is not immediately approved, the Curation Committee will provide you with suggestions and feedback on how to improve it, but the final acceptance of your collection cannot be guaranteed.
{{< /hint >}}

# **Acceptance criteria**

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

>- It is important that wearables be "skin weighted" correctly so that the avatar animations can be rendered as expected. Wearables without correct skin weighting will be rejected.
>- Wearables must preserve avatar UV mapping to ensure that user-selected skin tones can be rendered as expected.
>- The dimensions of eyebrow, eye, and mouth textures should not exceed 256 by 256px, and these textures must include an alpha channel for transparency.
>- Wearables with a disproportionate number of triangles and textures may be rejected. Wearables with too many triangles and textures can result in poor performance and a bad experience for users, so creators should avoid exceeding the following guidelines when creating wearables. For more info check the limitations here: **/creating-wearables**
>- Wearables may not contain duplicate items within a collection. (Each item within a collection must be unique.)
>- Wearables may not mimic or copy other wearables that have already been published.
>- Wearables with misleading categories may be rejected; for example, a hat that is categorized as a lower body item.
>- Wearables must follow the armature humanoid structure to ensure a good quality gameplay. In this sense, currently vehicles or pets are not allowed because these are not wearables by definition.
>- Curators from the curators committee can submit collections but not approve their own. In this case, another curator from the committee would needs to review in order and approve or reject.

## **Attributing collaborators [#](https://docs.decentraland.org/creator/wearables/wearables-editor-user-guide/#attributing-collaborators)**

If you collaborated with other artists when creating your items, you can add attributions within the Wearables Editor. This can only be done after publishing a collection.

First, navigate to the **[Builder](https://builder.decentraland.org/)** and select the **Collections** tab. Select the collection containing the items you want to add attributions to, click the **…** icon next to the **Mint Items** button, and select **Collaborators**.

To add collaborators, simply enter their Ethereum address, and click **Add**. You can add as many collaborators as you want. To remove a collaborator, simply click **Remove** next to the collaborator’s address.

[AddCollaborator](/images/publishing-collections/add-collaborator.png)

# **Selling items [#](https://docs.decentraland.org/creator/wearables/wearables-editor-user-guide/#selling-items)**

After your items are published in a collection and approved by the Curation Committee, they can be sold to other users in the metaverse.

Items can be sold in **primary sales** and **secondary sales**.

- **Primary sales** are performed by the Decentraland Store’s smart contract. During a primary sale, the **item is minted automatically**, and it is sold for the price set by you in the Wearable Editor.
- **Secondary sales** are performed by the Decentraland Marketplace’s smart contract. These occur anytime a user sells an item in the Marketplace **after it has been minted** or **purchased in a primary sale**. Items can be sold for any price in a secondary sale.

To view items available to purchase in a primary and secondary sales, head to the **[Decentraland store!](https://play.decentraland.org/?position=-70%2C0)**

## **Primary sales [#](https://docs.decentraland.org/creator/wearables/wearables-editor-user-guide/#primary-sales)**

Primary sales occur when one of your items is purchased for the first time. These sales are only performed by the Decentraland Store’s smart contract.

When a user makes a primary purchase of one of your items, the store **mints the item automatically**, transfers the item to the purchaser, and sends the MANA proceeds to the beneficiary address.

> Remember! You do not need to mint your items in order to sell them in primary sales!

To sell your items via primary sales, begin by navigating to the **[Builder](https://builder.decentraland.org/)** and selecting the **Collections** tab.

### **Enable primary sales** [#](https://docs.decentraland.org/creator/wearables/wearables-editor-user-guide/#enable-primary-sales)

To enable Primary Sales, click the ***On Sale*** toggle and click **Turn On** in the confirmation window that appears. When this switch is enabled, your collection will be available to purchase within the Decentraland store.

[SellingItemsToggle](/images/publishing-collections/selling-items-toggle.png)

If the switch is turned on, the Decentraland store will automatically mint one of your items whenever a user makes a primary purchase. This allows you to mint and sell all of your available items until the maximum supply is reached. If you want to save one or more of your items before listing them for sale, you need to manually mint an item to one of your own wallet addresses.

Any purchaser of one of your items is able to resell it at any time and at any price in Decentraland's [Marketplace](https://market.decentraland.org/).

**All primary sales in the Decentraland in-world store are subject to a 2.5% fee, which is transferred to the Decentraland DAO.**

If you sell an item through a primary sale, you will receive your MANA on Polygon. The proceeds of any items sold on Polygon will reside on the sidechain. If you want to transfer your MANA from the Polygon sidechain to the main Ethereum chain, you will have to pay a transaction fee. You can do so from the [Accounts](https://account.decentraland.org/) page. For more information on the Polygon sidechain, see [this blog post](https://decentraland.org/blog/announcements/polygon-mana/).

### **Disabling primary sales** [#](https://docs.decentraland.org/creator/wearables/wearables-editor-user-guide/#disabling-primary-sales)**

To unlist your items, click the **On Sale** switch to toggle it off. This will only apply to primary sales for your items.

## **Secondary sales [#](https://docs.decentraland.org/creator/wearables/wearables-editor-user-guide/#secondary-sales)**

Items can be sold in secondary sales at any time, and for any price, in the Decentraland Marketplace only after:

- They have been **minted**
- They have been **purchased in a primary sale**

In other words, anybody who owns an NFT for a wearable can sell it in the Decentraland Marketplace. There are royalties for wearables sold in secondary sales in Decentraland. Royalties goes to the item beneficiary.

## **Minting wearables [#](https://docs.decentraland.org/creator/wearables/wearables-editor-user-guide/#minting-wearables)**

Minting is the process of creating the actual non-fungible tokens (NFTs) based on the items you’ve uploaded to the Wearables Editor.

As with selling items in primary sales, you will not be able to mint any items within a collection until the review process is complete. If your collection is still under review, you will see the tag **"Under Review"** appended to your collection. After it has been reviewed and approved, the tag will change to **"Published"**, and you can begin minting your items manually.

### **Adding Minters to the Collection**

To add minters, simply enter their Ethereum address, and click **Add**. You can add as many minters as you want. To remove a minter, simply click **Remove** next to the minter’s address.

[AddMinters](/images/publishing-collections/add-minters.png)