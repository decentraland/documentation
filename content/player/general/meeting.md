---
date: 2023-16-23
title: Meeting with friends
description: Understand the basic concepts to meet with your friends in world
categories:
  - Decentraland
type: Document
url: /player/general/meet-with-friends
weight: 6
---

Being a decentralized platform involves having different servers hosted by different community members and to be able to meet with your friends or colleagues in-world, you all need to be in the same place. This can represent a challenge until you understand what being at the same place means.

There are two aspects to take into consideration when we talk about a place in Decentraland, the first one is the Realm or Server and the second one is the Position.

The platform currently has 11 servers, each denoted by friendly names such as Hela, Baldr, or Loki, and represents a realm, a distinct virtual environment. There is one default realm called MAIN where users are initially placed upon logging in. However, users have the flexibility to switch to other realms at any time. The primary objective of the MAIN realm is to gather the majority of users into the same connection level, facilitating and promoting social connections within the platform and making it easier to meet your friends. Finding or changing the realm is an easy process and can be done in various ways. Once you are in-world, you can access your profile at the top right corner of the screen. In the window that opens, you can find the option to switch realms at the top left corner, where you can view the current realm you are in.: 


![realm](/images/media/realm.png)

If you click on the realm name, a new pop up window will be opened showing the complete list of available realms and the quantity of users in each of them and, by clicking on the **WARP IN** link you can easily jump between realms.

![realms-list](/images/media/realms-list.png)

Another way to jump to a different realm is to use one of the available chatbox commands, the commands are a common handy tool that every platform user should learn about. To change realm using a command you need to open the chat as if you were about to send a message to the nearby players and write the following message that starts with a forward slash `/changerealm [realm-name]`, replacing `[realm-name]` for the actual `name` of the realm that you want to go (there are different handy commands that you can explore using the `/help` command on the chatbox), for example `/changerealm loki` will take you to the Loki realm:  

![change-realm](/images/media/change-realm.png)

Now that you are in the realm where you want to meet your mates, the second aspect to be at the same place is the **position** or location coordinates which are determined by two numbers representing the **x** and **y** axis of the Genesis City map. When you enter Genesis City you land at the `0,0` coordinates that are at the center of the world and this is where the Genesis Plaza is located, usually a crowded place as it is where most users land. The range of possible coordinates goes from `-150` to `150` for both axes and as a result, you get 90 thousand possibilities to choose from.     

Now the questions are: How to pick a location? And how to get there?

On the Map at the top left coroner of the screen, there is a section where you have your current location coordinates and the Map view it’s also a portal to the rest of Genesis City. Open the full map by click on it and jump in any Genesis City location just by selecting the point on the map, you can go crazy and pick a random spot or, you can also open the Places page that has the city points of interest list and pick a cool location from there. To see the existing points of interest, click on your profile picture again, then select the `Discover` section and open the `Places` tab.

![map](/images/media/map.png)

There is another chabtox command that you can use to move around different locations on the Genesis City, open the chat and write `/goto [x,y]` and replace `[x,y]` with the two coordinates that you want to go, for example writing `/goto 100,-50` will take you to that location.

At this point you should be at the meeting place, realm & location, so it's time to share this with your friends, send them a message *"let's meet in Loki at 100,-33"* or they can also search for you on their friends list and click on the red arrow button that will take them exactly where you are. Finally, if you are using the web browser client, there is another less convenient possibility, to share your current URL as it will contains your current locations details and take there anyone who opens it.

{{< hint warning >}}
**📔 Note**: There is another layer of users grouping at Decentraland that may prevent you from seeing someone that is at the same place that you are. Users are grouped in communication islands and the islands have a maximum allowed size of 100 users per island. When there are more than 100 users on the same place, more than one island will also exist. If you and your friend are at the same place but in different islands, you won't be able to see or talk to each other. To workaround this you can try to force the island by just copy/pasting your friend's full URL ([more info](https://adr.decentraland.org/adr/ADR-70)).

{{< /hint >}}



**The TL;DR version**:
To meet with someone you need to be in the same realm and position. Use the Map view to move around or the realm selection window to change where you are. You can also use the `/changerealm [realm-name]` and `/goto [x,y]` commands te get to where you want.
