---
title: "Overview"
url: /creator/quests/overview
weight: 1
---

**Quests** are a way to create a series of tasks for players to complete. Creators can take advantage of quests to generate to produce exciting, interactive content for their users. 

## Quests Service

The Quests Service is an important feature that facilitates users to explore the world, unlock achievements and potentially receive rewards. 

A Quest is a series of steps or tasks that a user has to complete. Each step or task has an acceptance criteria to consider it as done. 

A Quest creator has to define the steps and the order or the path to the end, so the quest is finished when those steps are completed. A Creator can use the Quests Service to create and manage quests as well as tracking the progress of the users on their quests and between users' sessions.

###### Current Scope & Limitations

- Quest can be **linear**, meaning that the user has to complete the steps in order. Quest can also be **branching**, meaning that the user can first complete one path and then continue with another one.

- Quest can be played only once time by a player.

- Quests can be created by creators with enough voting power. The voting power required is 100 or more.

- Quest Creators have to create their own Quest HUD or use the default one provided by Decentraland in [Quests Client SDK Library](/creator/quests/client).

- If a Quest Creator wants to give rewards to players, the creator is responsible of setting up a rewards service and provide all the information needed as it's mentioned [here](/creator/quests/rewards).

- Due to current limitations of SDK and Decentraland theirself, all Quests are single player. This means that a Quest cannot be done by multiple user or by a "team" of players. 

- As long as a player logs into Decentraland with their wallet, the Quest progress will be saved and can be continued in the future. Otherwise, if a player logs into Decentraland as a guest, the Quest progress will be lost when the player logs out since the address created at the login time cannot be restored.

- Quests tooling for Decentraland Scenes is targeting the **SDK version 7**. So if you are using an older version of the SDK, you won't be able to use the Quests tooling. You can still use the Quests Service to track progress, send events and receive updates in your scene but you will have to create your own tooling to do so.

###### Service's Architecture

<img src="/images/quests/quests-arch.png" alt="Quests Service" style="width: 100%;"/>

A brief description of the components in the picture:

- **Quests API**: It consists of two different servers. One is the **Quests REST API** which has a set of endpoints that allow the creators to create and modify Quests as well as check their Quests' stats. The other one is the **Quests RPC Service** which is used by scenes and explorer to send events and track users' progress. 
- **Quests Database**: It's a PostgreSQL database to store Quests and user's progress.
- **Quests System**: It's a service to process the incoming users' events, validate and update the user's progress. It also sends notifications to scenes and explorer through **Quest Channels** when a user make progress on a Quest.
- **Events Queue**: It's where the **Quests RPC Service** sends the events to be processed by the Quests System.
- **Quest Channels**: The scenes and explorer subscribe to these channels to receive notifications when a user makes progress on a Quest.

You can find the **Quests Service** repository [here](https://github.com/decentraland/quests)