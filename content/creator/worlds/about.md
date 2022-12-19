---
title: "Worlds Overview"
slug: "/contributor/worlds/about"
weight: 1
---

In this document you will learn how to use Decentraland Worlds, a new service that lets you deploy isolated scenes that you can access with the Decentraland Explorer and with your digital identity.  

The name **Worlds** was given to scenes that exist outside the Genesis City boundaries. Worlds can be used to do experiments, create new experiences or as a Scenes Preview Service to test scenes before uploading them to the Genesis City. Worlds scenes are attached to [Decentraland NAMEs](https://builder.decentraland.org/names) and the NAMEs are used to tell Decentraland Explorer which world to load.  

### WARNINGS: The Worlds Service is in BETA state

Consider that this product is in BETA state before making it a key part of your product roadmap.  

The BETA is open to anyone to use, in order to kick-off the product and be able to assess the scaling, the following scene limitations were added: 
- Scenes can occupy 4 parcels of any shape 
- 100MB is the maximum size for the scene deployment 
- Up to 100 users will be allowed to join a World scene concurrently  

### Publish a scene 

If you are a content creator, you are already familiar with the [CLI](https://docs.decentraland.org/creator/development-guide/sdk-101/), the only difference to upload a World scene is that you need to specify the target server in the deployment command-line and use the Worlds Server URL: 

`dcl deploy --target-content https://worlds-content-server.decentraland.org` 


Once you run the command you will be prompted to sign the deployment with your wallet and a set of validations will be executed to allow or reject the scene: 
- The wallet signing the deployment must own a Decentraland NAME 
- The scene can occupy a maximum of 4 parcels
- The size of the scene must be less or equal to 100MB 

In case you have multiple NAMEs in your wallet, you can specify under which 
NAME that deployment is to be made. In your `scene.json` you need to add a 
section like this:

```json
{
  "worldConfiguration" : {
    "dclName": "my-name.dcl.eth"
  }
}
```

Of course, the NAME specified there needs to be owned by the wallet signing 
the deployment.

### Joining a World 

Once a scene is uploaded to the Worlds server you can access it by using the Decentraland explorer with the following friendly URL `https://play.decentraland.org/world/NAME`, where `NAME` should be replaced by the Decentraland NAME to which the deployment was done to. 

On the other hand, NAMEs also work as realms, so you can leverage the existing change realm mechanisms to access a world, one way would be using the query parameter in the explorer URL, if your name is `my-name.dcl.eth` you can use the following URL to access the world: `https://play.decentraland.org/?realm=my-name.dcl.eth`. Another possibility is to just enter Decentraland and then type the `/changerealm my-name.dcl.eth` command in the chat and this will teleport you to the world scene. 
