---
date: 2018-01-01
title: FAQ
aliases:
  - /docs/faq
  - /faq
  - /docs/frequently-asked-questions
  - /decentraland/faq
description: Frequently Asked Questions
categories:
  - Decentraland
type: Document
url: /player/general/faq
weight: 2
---

Download Decentraland [here](https://decentraland.org/download).

{{< details class="faq-details" anchor="true" title="What equipment or software do I need to play in Decentraland?" >}}

A PC or Mac. See [hardware requirements]({{< ref "/player/general/hardware-requirements.md" >}})

- **Can I play on a mobile device?<br/>**

  For the moment we don’t support mobile devices. But please stay tuned!

- **Can I log in from multiple computers?<br/>**

  Yes, you can run Decentraland from multiple computers.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I login with my email or social media account?" >}}

Yes! You can easily login with your email address or social media account.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Do I need a wallet to play in Decentraland?" >}}

If you don't already have your own [digital wallet]({{< ref "/content/player/blockchain-integration/get-a-wallet.md" >}}), you don't need to get one if you don't want to. When you sign-in to Decentraland for the first time—creating your account—a digital wallet will be created for you behind the scenes, it's as simple as that!

This digital wallet is part of your Decentraland account and is used to store any digital assets you acquire, such as free Wearables you might claim in-world or a fun Emote you purchase in the Marketplace.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="I lost my digital wallet! What happens with my account?" >}}

If you lose access to your wallet you will lose your Avatar, name, any of the wearables or NFT items stored within. Please remember to always keep your wallet recovery pass phrases in a safe and secure location.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="What is MANA?" >}}

[MANA](https://etherscan.io/token/decentraland) is Decentraland’s fungible, ERC20 cryptocurrency token. MANA is burned, or spent, in exchange for LAND parcels. For a current summary of critical stats like total and circulating supply, please visit our [MANA Token Information](https://governance.decentraland.org/transparency/) transparency dashboard.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Will I be able to buy things other than LAND with MANA?" >}}

Yes! In addition to burning MANA in exchange for LAND, users will be able to trade MANA with other users in exchange for goods and services hosted within Decentraland.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Some players have fancy wearables. How can I get them?" >}}

The Avatar editor provides a big selection of wearables and accessories – all for free. You can also buy exclusive wearables in the <a href="https://decentraland.org/marketplace/">Decentraland Marketplace</a> or earn them by participating in different events.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="What do the collectibles colors mean?" >}}

<img src="/images/media/faqs-rarities-2.png" style="margin: 2rem auto; display: block;width: 90%;" />

Each collectible is assigned a rarity category, represented by a different name and color and denoting supply of collectible.

Their maximum issuance is:

- Common: 100000
- Uncommon: 10000
- Rare: 5000
- Epic: 1000
- Legendary: 100
- Exotic: 50
- Mythic: 10
- Unique: 1

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I claim my Avatar name later?" >}}

Yes. Visit the <a href="https://decentraland.org/builder/names">Names</a> page in the Builder to claim it. All you need is an installed digital wallet and at least 100 MANA to burn. Another alternative is to buy a name in the <a target="_blank" href="https://decentraland.org/marketplace/">Decentraland Marketplace</a>.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How can I block or report a player?" >}}

Blocking other users is not currently possible on the latest version of the Decentraland client, but this functionality will be added back soon.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How can I report a scene?" >}}

Locate the Flag Scene button (Beneath the mini map). Select a category that you believe the scene belongs to. Identify the issues present in the scene and submit the report.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="What are useful chat commands in Decentraland?" >}}

Chat commands are used to trigger actions, such as teleporting or reloading, by entering specific text into the chat box in-world. To use one, just open the chat box, type the command, and hit enter.

* **Teleporting around Genesis City**
- ```/goto x,y```  (x,y are the coordinates of a scene)
* **Visiting Worlds**
- ```/goto World’sName```
* **Reloading a Scene**
- ```/reload```
* **Open Debug Mode (shows FPS and other metrics)**
- ```/debug```
* **Discover More Chat Commands**
- ```/help```

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How can I teleport around Decentraland and into Worlds?" >}}

To travel around Decentraland’s Genesis City quickly, you can teleport with chat commands in the chat box or via the map in the upper left corner. To visit someone’s World, all you’ll need is a chat command.

**Chat Commands:**

* **Teleporting around Genesis City**:
- ```/goto x,y``` (x,y are the coordinates of a scene)
* **Visiting Worlds:**
- ```/goto World’sName```

**Genesis City Map:**
Open the in-world map in the upper left. To teleport to a specific parcel, click on it, then select ‘Jump In’. If you’re not sure where on the map the parcel you want to visit is, you can search for it by name in the map’s search bar.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="What is LAND?" >}}

LAND is a non-fungible digital asset maintained in an Ethereum smart contract. LAND is divided into parcels that are referenced using unique x,y cartesian coordinates. Each LAND token includes a record of its coordinates, its owner, and a reference to a content description file or <a href="https://github.com/decentraland/proposals/blob/master/dsp/0020.mediawiki">parcel manifest</a> that describes and encodes the content the owner wishes to serve on his or her land.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How large is a tile of LAND?" >}}

Land parcels are 16m x 16m, or 52ft x 52ft. Height is restricted based on [these limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}).

{{</ details >}}

{{< details class="faq-details" anchor="true" title="What is an Estate?" >}}

Like LAND, an estate is a non-fungible digital asset. An estate is an association of two or more directly adjacent parcels of LAND. These parcels must be directly adjacent and cannot be separated by a road, plaza or any other parcel. By connecting parcels to form Estates, you can more easily manage your larger LAND holdings. Estates are especially useful when building larger scenes that span more than one parcel.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How can I buy LAND or Estates in Decentraland?" >}}

You can visit the <a href="https://decentraland.org/marketplace/">Decentraland Marketplace</a> to browse through all of the available LANDs or Estates of LAND that are currently for sale.
On December 15th, 2017, we held our first LAND auction, called the Terraform Event, to distribute the first parcels of LAND to the community. The auction concluded in January 2018 and LAND tokens have been distributed to participants.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="What does ‘owning’ virtual LAND mean and how does it work?" >}}

LAND within Decentraland is represented by non-fungible LAND tokens (meaning that each is unique and cannot be replicated) that track ownership on the Ethereum blockchain. Owning LAND within Decentraland is akin to owning any other unique, crypto asset like <a href="https://www.cryptokitties.co/">CryptoKitties</a> or <a target="_blank" href="https://www.larvalabs.com/cryptopunks">CryptoPunks</a>, however you will be able to use your LAND within Decentraland to build three dimensional spaces and applications. LAND is built on our <a target="_blank" href="https://github.com/decentraland/erc721">ERC721</a> standard, making it a digital asset that can be traded with other users, like other digital assets.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Why is LAND scarce?" >}}

Like CryptoKitties and CryptoPunks, LAND is a non-fungible digital asset. To ensure that the value of LAND parcels remains stable, the amount of land in Decentraland corresponds to the fixed, total amount of MANA.

Without LAND scarcity, many parcels would likely be left abandoned, negatively impacting the quality of content in Decentraland and the user experience.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Creating an Event" >}}

- **How do I post an event to the Event page?**
Check out a quick breakdown [here](https://www.youtube.com/watch?v=jMNk_W1yqjU)
 
    And yes, you can edit your event after publishing!

- **How does the event review process work?**

    Review times depend on day/time of event submission, but won’t take longer than a few hours. Events are reviewed by the team at the Decentraland Foundation. Make sure to add your email or Discord username so you can be contacted if there is something wrong with the event submission.

- **My event wasn’t published, why not?**

    Your event may not have passed review because you did not fill in all the required information. Make sure you complete every field in the form when submitting an event.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Does Decentraland run on top of its own blockchain?" >}}

Decentraland uses the Ethereum blockchain to store and verify information about LAND ownership and LAND content. It does not run on its own independent blockchain. Content within Decentraland is hosted and served to users via a network of community-owned content servers.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Who validates transactions?" >}}

The Ethereum LAND smart contract registers any changes to the state of a parcel of LAND, such as a change in the contents of the LAND or a transfer of ownership. These changes are recorded and verified by the Ethereum blockchain.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How is content distributed?" >}}

The visual, audio and three dimensional content of Decentraland will be stored in a network of content servers. Anyone can submit a server to join this network, but it must be voted on by the community. This is handled by a <a href="https://decentraland.org/dao/">Decentralized Autonomous Organization (DAO)</a>. When you visit Decentraland, the content needed to render your location will be pulled from the content servers. Each LAND token, stored on the Ethereum blockchain, is associated with an x,y location within the world and links to the content for that location.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="What tools should I use to start building in Decentraland?" >}}

The Creator Hub is the recommended tool for creators of all knowledge levels. It's a desktop application that lets you create:

- Wearables & Smart Wearables
- Emotes
- Scenes

Download the Creator Hub [here](https://decentraland.org/download/creator-hub).

Learn more about [creating in Decentraland]({{< ref "/content/creator/_index.md" >}})

{{</ details >}}

<!--
## How do I avoid being “boxed-in” by surrounding parcels?

Decentraland’s client design has a number of solutions to this problem, although not all will necessarily be implemented. These solutions may include a ghost mode allowing players to clip through unrestricted parcels, unrestricted teleportation, functionality in plazas that exposes quality content, and design incentives that enable users to create content that doesn’t visually box-in adjacent parcels.
-->

{{< details class="faq-details" anchor="true" title="Will I be able to control who can see content on my parcels?" >}}

Yes. You will be able to control how certain content on your parcel is served to other users within the Decentraland platform. For example, you could make 3D models, images, video, or sound content only visible to a player in Decentraland after they have submitted a payment or fulfilled some other requirement.

However, remember that by uploading content to the content servers you are essentially making it publicly available since the content servers are a distributed file system. While we intend to make it possible to limit how that content is served to players through a Decentraland client, the content itself will always remain discoverable on the content servers.

You will be able to control who you can see and interact with (and who can see and interact with you) within Decentraland. For example, imagine that you have a house on your parcel and you only want to invite certain friends into your house. You will be able to specify which players you can see (and which players can see you) within your house, but you won’t necessarily be able to prevent anyone from seeing your house or its contents since the assets required to render your house reside on the content server.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I monetize my content?" >}}

Yes. You are free to decide whether you will charge other players to access your content and how you will implement said charge. Decentraland is in no way involved in the monetization of your content and does not guarantee any return, profit or income. The success of the platform depends entirely on the efforts of the users. Your fate, your success, and eventually your journey, depends on you, your efforts, your imagination.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="I need support! Where can I contact you?" >}}

In case of any questions or issues, please reach out to us at <hello@decentraland.org> or visit <a href="https://decentraland.org/help/">Support</a>.
You can also join our <a href="https://dcl.gg/discord">Discord</a> and visit our #help channel to ask whatever questions you have. We’ll answer as soon as possible. Our friendly community members can help too. While you’re there why not check out some of the other channels to learn more about Decentraland?

{{</ details >}}
