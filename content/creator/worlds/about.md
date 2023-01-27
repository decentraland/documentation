---
title: "Worlds Overview"
slug: "/contributor/worlds/about"
weight: 1
---

In this document you will learn how to use Decentraland Worlds BETA, a new service that lets you deploy isolated scenes that you can access with the Decentraland Explorer and using your digital identity.  

The name **Worlds** was given to scenes that exist outside the Genesis City boundaries. Worlds can be used to do experiments, create new experiences, as scenes portfolio or even as a Scene Preview Service to test the content before uploading it to the Genesis City. Worlds scenes are attached to [Decentraland NAMEs](https://builder.decentraland.org/names) (a `NAME NFT` within the DCL ecosystem that can be assigned to your avatar or LAND and costs 100 MANA to create or can be purchased from a previous owner in the Marketplace) and the NAMEs are used to tell Decentraland Explorer which World to load.  

### WARNINGS: The Worlds Service is in BETA state

Consider that this product is in BETA state before making it a key part of your product road map.  

The BETA is open to anyone to use, to kick-off the product and be able to assess the scaling, a World scene must meet the following limitations: 
- Scenes have no parcel limitations since January 2023
- 100 MB is the maximum size for the scene deployment 
- Up to 100 users will be allowed to join a World scene concurrently  

### Publish a World 

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

Of course, the **name** specified there needs to be owned as a Decentraland NAME token by the wallet signing the deployment.

To publish a scene to a world via the Decentraland Editor:

1. Open VSCode in a Decentraland scene project.
2. Click on the Decentraland icon on the left sidebar.
3. Click on the three dot menu at the top right of the sidebar, next to the green reload arrow button, select **Publish Scene To Your World**
4. Approve the transaction
	- If you need to use Metamask on the browser, click **Open in Browser** to open this same window on a browser tab. Then approve the transaction on the Metamask browser extension.


To deploy a scene to a world via the CLI, you need to specify the target server in the deployment command-line and use the Worlds Content Server URL: 

```bash
dcl deploy --target-content https://worlds-content-server.decentraland.org`
```


Once you run the command, you will be prompted to sign the deployment with your wallet and a set of validations will be executed to allow or reject the scene: 
- The wallet signing the deployment must own the Decentraland NAME specified in the scene.json file 
- The scene has no parcel limitations (since January 2023)
- The total size of the scene must be less or equal to 100 MB

### Joining a World 

Once a scene is uploaded to the Worlds server you can access it by using the 
Decentraland Explorer with the following friendly URL `https://play.decentraland.org/world/NAME`, where `NAME` should be replaced by the Decentraland NAME to which the deployment was done to. You may use the NAME with or without the `.dcl.eth` suffix.

On the other hand, NAMEs also work as realms, so you can leverage the existing change realm mechanisms to access a world. One way would be by typing the `/changerealm NAME.dcl.eth` command in the chatbox and another possibility is by changing the query parameter in the Explorer URL: if your NAME is `my-name.dcl.eth` you can use the following URL to access the world: `https://play.decentraland.org/?realm=my-name.dcl.eth` 

### Migrating a World to the Genesis City  

If you are a LAND owner and you wish to deploy a World scene to the Genesis City, it is completely possible. You just need to re-deploy your scene to the decentralized Catalyst network, the targeted content server for Genesis City

Things to remember:
* remove the `worldConfiguration` section from `scene.json`
* the size limitation for Worlds (100 MB, an average of 25MB per parcel) is larger than that for LAND parcels (15MB a parcel), so make sure your scene is sized correctly for deployments to Genesis City!

### World defaults 

A couple of optional custom settings can be specified in the `scene.json` when deploying a world scene:

**skybox**: This property indicates how many seconds have passed (in Decentraland time) since the start of the day, assuming the full cycle lasts 24 hours. Divide the seconds value by 60 to obtain minutes, and by 60 again to obtain the hours since the start of the day. For example, if the seconds value is 36000, it corresponds to 10:00 am. If no value is set for this field, the world will follow the same day/night cycle as Genesis City.

**fixedAdapter**: indicates which Communication Service should by used by the scene. For the time being only the `offline:offline` value is allowed and when set, the scene will have no Communication Service at all and each user joining that world will always be alone. If not set, the Worlds content server will generate a proper value based on how it is configured.

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
