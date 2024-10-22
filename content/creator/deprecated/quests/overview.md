---
title: 'Quests Overview'
url: /creator/quests/overview
weight: 1
---

**Quests** are a way to create a series of tasks for players to complete. Creators can take advantage of quests to generate exciting interactive content for their players.

## The Quests Service

The Quests Service is an important feature that encourages players to explore the world, unlock achievements and potentially receive rewards.

A Quest is a series of steps or tasks that a player has to complete. Each step or task has an acceptance criteria to consider it as done.

The creator of a Quest must define the steps and their order or the path to the end. A quest is finished when those steps are completed. A Creator can use the Quests Service to create and manage quests. The Quest Service tracks the progress of players as they complete steps, saving their progress between sessions.

### Current Scope & Limitations

- Quests can be **linear**, meaning that the player has to complete the steps in order. Quests can also be **branching**, meaning that the player can first complete one path and then continue with another one. A player must complete all branches before the quest is considered completed.

- Quests can be completed only once by a player.

- When a player starts a Quest, a Quest Instance is created for that specific Quest and player. This instance will store the progress of the player in that Quest.

- A player can have multiple Quest Instances at the same time, but only one instance of each Quest.

- When an action event is sent to the **Quests RPC Service**, this event is enqueued and then the **Quests System** process it. When the event is processed by the **Quests System**, all player's Quest Instances are grabbed from the **Quests Database** and the action event is applied to each of them. If the event makes the player do some progress on the Quest Instance, the event is stored and progress is made on the Quest Instance. A single action event could be valid for multiple Quest Instances being played by the user.

- Quest Creators must manage their own Quest HUD as part of the content of the scene (or portable experience). They can design their own, or use the default one provided as part of the [Quests Client SDK Library]({{< ref "/content/creator/deprecated/quests/client.md" >}}).

- If a Quest Creator wants to give rewards to players who complete the quest, the creator is responsible of setting up a rewards service and providing all the information needed, as described [here]({{< ref "/content/creator/deprecated/quests/rewards.md" >}}).

- Due to current limitations of the SDK and Decentraland itself, all Quests are single player experiences. This means that a Quest cannot be done by multiple players or by a "team" of players.

- As long as a player logs into Decentraland with their wallet, the Quest progress is saved and can be continued in the future. If a player logs into Decentraland as a guest, the Quest progress will be lost when the player logs out, since the temporal address created at the login time cannot be restored.

- Quests tooling for Decentraland Scenes is built targeting the **SDK version 7**. So if you are using an older version of the SDK, you won't be able to use the Quests tooling. You can still use the Quests Service to track progress, send events and receive updates in your scene but you will have to create your own tooling to do so.

### Service Architecture

<img src="/images/quests/quests-arch.png" alt="Quests Service" style="width: 100%;"/>

A brief description of the components in the picture:

- **Quests API**: It consists of two different servers. One is the **Quests REST API** which has a set of endpoints that allow the creators to create and modify Quests as well as check their Quest's stats, for a more comprehensive spec on this API, [please refer to this link](https://quests.decentraland.org/api/docs). The other one is the **Quests RPC Service** which is used by scenes and the explorer to send events and track player's progress.
- **Quests Database**: It's a PostgreSQL database to store Quests and player's progress.
- **Quests System**: It's a service to process the incoming player's events, validate and update the player's progress. It also sends notifications to scenes and the explorer through **Quest Channels** when a player makes progress on a Quest.
- **Events Queue**: It's where the **Quests RPC Service** sends the events to be processed by the Quests System.
- **Quest Channels**: The scenes and explorer subscribe to these channels to receive notifications when a player makes progress on a Quest.

You can find the **Quests Service** repository [here](https://github.com/decentraland/quests).
