---
title: "About"
slug: "/contributor/worlds/about"
weight: 1
---

In this document you will learn how to use Decentraland Worlds, a new content server that lets you deploy isolated scenes which are accessible by the Decentraland explorer. 

The name **Worlds** was given to scenes that exists outside of the Genesis City boundaries. Worlds can be used to do experiments or as a Scenes Preview Service to tests experiences before uploading them to the Genesis City. Worlds are attached to [Decentraland NAMEs](https://builder.decentraland.org/names) and the NAMEs can be used as realms.  

### WARNINGS: The Worlds server is in ALPHA version

- Do not build product road map on top of this service
- In order scale this service and making it globally available some cost or limitations may be needed in the future to support the infrastructure 
- There can be bugs or downtime, the goal is to detect issues and fixe them as soon as possible 
- The future User Experience may change based on the feedback 


### Publish a scene 

If you are a content creator, you are already familiar with the CLI, the only difference to upload a Worlds is that you need to specify the target server and use the Worlds server URL. 

`dcl deploy --target-content https://worlds-content-server.decentraland.org` 

The only validation that is going to be made when uploading content to the Worlds Server is that you own a Decentraland NAME as that NAME is going to be the key to access the scene. 


### Joining a World 

Once a scene is uploaded to the Worlds server you can access it by using the Decentraland explorer and adding the NAME as the value for the realm query parameter in the URL, for example, if your name is `my-name.dcl.eth` you can use the following URL:  `https://play.decentraland.org/?realm=my-name.dcl.eth`. Another possibility is to just enter Decentraland and type the `/changerealm my-name.dcl.eth` command in the chat and this will teleport your scene. 


### Limitations: 

- Even if you withhold more than one name, only one deployment per account is supported at this time.
- The upload size limit is the same as a deployment to a Catalyst (200MB) 
- Once uploaded, it cannot be destroyed but you may override it with a new deployment