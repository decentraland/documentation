---
title: "Worlds Overview"
slug: "/contributor/worlds/about"
weight: 1
---

Welcome to Decentraland Worlds! Here, you will discover everything about this service that empowers you to deploy self-contained scenes. These scenes are easily accessible through the Decentraland Explorer, providing you with a platform to experiment, unleash your creativity and explore new horizons.

The term **Worlds** refers to scenes located beyond the boundaries of Genesis City. These Worlds serve various purposes, such as conducting experiments, creating new experiences, building a portfolio of scenes, or even serving as a Scene Preview Service for testing content before uploading it to Genesis City. Worlds scenes are associated with [Decentraland NAMEs](https://builder.decentraland.org/names), which are NAME NFTs within the DCL ecosystem. Acquiring a NAME requires 100 MANA and can be assigned to your avatar or LAND. Alternatively, you can purchase a NAME from a previous owner in the [Marketplace](https://market.decentraland.org/). These NAMEs are then utilized by the Decentraland Explorer to load the designated World.

Worlds serve as a gateway for aspiring content creators, providing an accessible entry point to the platform and the freedom to experiment with scene creation. These isolated experiences come with certain limitations to ensure scalable growth:  

- Scene Deployment Size: The maximum size allowed for scene deployment is 100 MB.
- Concurrent User Limit: Each World scene can accommodate up to 100 users simultaneously 

## Publish a World 

Users have various options to publish content on their World: 

* [Builder dApp](https://builder.decentraland.org/scenes): web app and no coding skills needed 
* Decentraland Editor: IDE for developing Decentraland scenes
* CLI: Advanced users can leverage the CLI for efficient content publishing.

## Using the Builder dApp (no-code)

The Builder is the go-to option for non-developers. Scenes can be created from scratch using the Scene Builder by dragging and dropping items into the scene. Smart Items can also be used for player interaction once the scene is deployed. 

Creators can also use Templates, edit them, and then deploy them to their World. More templates from the Foundation will be uploaded over time. 
Another way is to use a scene from the Scene Pool. Anyone can get a scene from the pool, download it, and then Import it  in the Builder to edit it, or deploy it to a World as it is. 

## Using the SDK and Editor

The starting point for this product is having a scene that meets the size requirements mentioned above. If you wish to know more about how to create a scene, check out the [Decentraland SDK]({{< ref "/content/creator/scenes/getting-started/sdk-101.md" >}}) documentation.

If you are a Content Creator, you may be already familiar with how the [publishing of a scene]({{< ref "/content/creator/scenes/publishing/publishing.md" >}}) works, the experience is quite similar, but with a small caveat: 

You need to specify under what **name** your deployment is to be made. Add the following section in your
`scene.json`:

```json
{
  "worldConfiguration" : {
    "name": "my-name.dcl.eth"
  }
}
```

Of course, the **name** specified there needs to be owned as a Decentraland NAME token by the wallet signing the deployment (or by any wallet that has been given permission explicitly via Access Control Lists (ACL), as explained further down).

Keep the following in mind:
- The wallet signing the deployment must own the Decentraland NAME specified in the `scene.json` file 
- The total size of the scene must be less or equal to 100 MB
- The scene has no parcel limitations (since January 2023)

Some of the Worlds deployed to the Foundation's Worlds Content Server may be eligible for being listed in Decentraland Places. See [eligibility criteria]({{< ref "/content/creator/places/faq.md#worlds" >}}) for more details. 

If you wish to opt-out from your Worlds being indexed in Places, you can add the following section in your `scene.json`:

```json
{
  "worldConfiguration": {
    "name": "my-name.dcl.eth",
    "placesConfig": {
      "optOut": true
    }
  }
}
```

### Publish via the Decentraland Editor:

1. Open VSCode in a Decentraland scene project.
2. Click on the Decentraland icon on the left sidebar.
3. Click on the three dot menu at the top right of the sidebar, next to the green reload arrow button, select **Publish Scene To Your World**
4. Approve the transaction
	- If you need to use Metamask on the browser, click **Open in Browser** to open this same window on a browser tab. Then approve the transaction on the Metamask browser extension.

### Publish via the CLI

To deploy a scene to a world via the CLI, you need to specify the target server in the deployment command-line and use the Worlds Content Server URL.

For SDK6 scenes, use the following command:

```bash
dcl deploy --target-content https://worlds-content-server.decentraland.org
```

For SDK7 scenes, use the following command:

```bash
npm run deploy -- --target-content https://worlds-content-server.decentraland.org
```


Once you run the command, you will be prompted to sign the deployment with your wallet and a set of validations will be executed to allow or reject the scene.

## Joining a World 

Once a scene is uploaded to the Worlds server you can access it by using the 
Decentraland Explorer with the following friendly URL `https://play.decentraland.org/world/NAME`, where `NAME` should be replaced by the Decentraland NAME to which the deployment was done to. You may use the NAME with or without the `.dcl.eth` suffix.

On the other hand, NAMEs also work as realms, so you can leverage the existing change realm mechanisms to access a world. One way would be by typing the `/changerealm NAME.dcl.eth` command in the chatbox and another possibility is by changing the query parameter in the Explorer URL: if your NAME is `my-name.dcl.eth` you can use the following URL to access the world: `https://play.decentraland.org/?realm=my-name.dcl.eth` 

## Migrating a World to the Genesis City  

If you are a LAND owner and you wish to deploy a World scene to the Genesis City, it is completely possible. You just need to re-deploy your scene to the decentralized Catalyst network, the targeted content server for Genesis City

Things to remember:
* remove the `worldConfiguration` section from `scene.json`
* the size limitation for Worlds (100 MB total size) is different from that for LAND parcels (15MB per parcel), so make sure your scene is sized correctly for deployments to Genesis City!

## World defaults 

A couple of optional custom settings can be specified in the `scene.json` when deploying a world scene:

**skybox**: This property indicates how many seconds have passed (in Decentraland time) since the start of the day, assuming the full cycle lasts 24 hours. Divide the seconds value by 60 to obtain minutes, and by 60 again to obtain the hours since the start of the day. For example, if the seconds value is 36000, it corresponds to 10:00 am. If no value is set for this field, the world will follow the same day/night cycle as Genesis City.

**fixedAdapter**: indicates which Communication Service should be used by the scene. For the time being only the `offline:offline` value is allowed and when set, the scene will have no Communication Service at all and each user joining that world will always be alone. If not set, the Worlds content server will generate a proper value based on how it is configured.

**Example:**
```json
{
  "worldConfiguration" : {
    "name": "my-name.dcl.eth",
    "skybox": 36000,
    "fixedAdapter": "offline:offline"
  }
}
```

## Access Control Lists (ACL)

When a team (more than one person) are contributing to the development of a scene, it may be beneficial to have each contributor have the ability to publish the scene under a single NAME. As stated above, the NAME owner is the only one allowed to run such deployment.

So the concept of Access Control List (or ACL for short) was introduced. The idea is that the owner of the NAME can grant other wallets permission to publish a scene under his NAME. This way the whole team (or a group of selected members) can be added to the world ACL and those will be able to publish the scene.

This ACL is stored in the World Content Server where the world is deployed. It is not stored on the blockchain. This makes it much more flexible, giving more granular control. For e.g. if you want to deploy a scene under the same NAME in two different World Content Server hosting providers, then you can have different sets of permissions in each server. And also, there is no transaction fees involved in maintaining the ACL (granting or revoking permissions).

A new command has been added to Decentraland CLI that allows to show the current ACL stored in the Worlds Content Server for a given NAME, and it also allows granting access to more wallets or revoking access to wallets that are already in the ACL. 

![world-acl help screen](/images/worlds/world-acl-help.png)

In order to grant permission for publishing a scene to another wallet you have to:

* Make sure to have the latest version of Decentraland CLI (v3.16.2 or later).
* Make sure you own the NAME for which you want to manage the ACL.
* Use command `dcl world-acl NAME.dcl.eth grant 0x1 0x2 ... 0xn` where those `0xn` are a list of addresses separated by spaces.

By default, `world-acl` will act on `worlds-content-server.decentraland.org`. If you are using a different hosting provider, make sure to add `--target-content https://your-hosting.com` to each of the subcommands (`show`, `grant` and `revoke`).
