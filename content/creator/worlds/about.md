---
title: "Worlds Overview"
slug: "/contributor/worlds/about"
weight: 1
---

In this document you will learn how to use Decentraland Worlds BETA, a new service that lets you deploy isolated scenes that you can access with the Decentraland Explorer and using your digital identity.  

The name **Worlds** was given to scenes that exist outside the Genesis City boundaries. Worlds can be used to do experiments, create new experiences, as scenes portfolio or even as a Scene Preview Service to test the content before uploading it to the Genesis City. Worlds scenes are attached to [Decentraland NAMEs](https://builder.decentraland.org/names) (a 'NAME NFT’ within the DCL ecosystem that can be assigned to your avatar or LAND and costs 100 MANA to create or can be purchased from a previous owner in the Marketplace) and the NAMEs are used to tell Decentraland Explorer which World to load.  

### WARNINGS: The Worlds Service is in BETA state

Consider that this product is in BETA state before making it a key part of your product road map.  

The BETA is open to anyone to use, to kick-off the product and be able to assess the scaling, a World scene must meet the following limitations: 
- Scenes can be 4 parcels large of any shape 
- 100 MB is the maximum size for the scene deployment 
- Up to 100 users will be allowed to join a World scene concurrently  

### Publish a World 

The starting point for this product is having a scene that meets the size requirements mentioned above, if you wish to know more about how to create a scene, check out the [Decentraland SDK](https://docs.decentraland.org/creator/development-guide/sdk-101/) documentation.

If you are a Content Creator, you may be already familiar with how the [CLI]
(https://docs.decentraland.org/creator/development-guide/sdk-101/) works, 
the experience is quite similar, but with two small caveats... 

You need to specify under which NAME that deployment is to be made. In your
`scene.json` you need to add the following section:

```json
{
  "worldConfiguration" : {
    "name": "my-name.dcl.eth"
  }
}
```

Of course, the NAME specified there needs to be owned by the wallet signing the deployment.

And secondly, you need to specify the target server in the deployment command-line and use the Worlds Content Server URL: 

`dcl deploy --target-content https://worlds-content-server.decentraland.org`

Once you run the command, you will be prompted to sign the deployment with your wallet and a set of validations will be executed to allow or reject the scene: 
- The wallet signing the deployment must own the Decentraland NAME specified in the scene.json file 
- The scene can occupy a maximum of 4 parcels of any shape
- The total size of the scene must be less or equal to 100 MB

### Joining a World 

Once a scene is uploaded to the Worlds server you can access it by using the 
Decentraland Explorer with the following friendly URL `https://play.decentraland.org/world/NAME`, where `NAME` should be replaced by the Decentraland NAME to which the deployment was done to. You may use the NAME with or without the `.dcl.eth` suffix.

On the other hand, NAMEs also work as realms, so you can leverage the existing change realm mechanisms to access a world. One way would be by typing the `/changerealm NAME.dcl.eth` command in the chatbox and another possibility is by changing the query parameter in the Explorer URL: if your NAME is `my-name.dcl.eth` you can use the following URL to access the world: `https://play.decentraland.org/?realm=my-name.dcl.eth` 

### Migrating a World to the Genesis City  

If you are a LAND owner and you wish to deploy a World scene to the Genesis City, it is completely possible. You just need to re-deploy your scene to the decentralized Catalyst network, the targeted content server for Genesis City

Just remember that the size limitation for Worlds (100 MB, an average of 25MB per parcel) is larger than that for LAND parcels (15MB a parcel), so make sure your scene is sized correctly for deployments to Genesis City!
