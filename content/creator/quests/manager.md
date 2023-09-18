---
title: 'Quests Manager'
url: /creator/quests/manager
weight: 7
---

Use the Quests Manager to create, edit and handle your quests. You can access the Quests Manager through the [CLI]({{< ref "/content/creator/quests/cli.md" >}}).

## Opening the Quests Manager

To open up the Quests Manager, use the following command:

```bash
$ npx @dcl/sdk-commands quests -m
```

After you run this command, the [CLI]({{< ref "/content/creator/quests/cli.md" >}}) will print out the URL to open up the Quests Manager in your browser and it will open up the Quests Manager in your default browser (if you didn't set `--no-browser` or `-b` flags).

When you open up the Quests Manager, you will be asked to log in with your Ethereum wallet.

## Dashboard

On the Dashboard (the main page `/`), you will be able to see your drafts and published quests.

<img src="/images/quests/quests-manager-dashboard.png" alt="Quests Service" style="width: 100%;"/>

As you can see, it's displayed two lists with the **draft** and **published** Quests and their names, their descriptions, their images, their status, and the actions you can perform on each quest. You can go and edit and update the quest, activate it or deactivate it.

If it's the first time that you open the Quests Manager, you will see a message saying that you don't have any quests yet. You can create a new one by clicking on the "Create Quest" button on the right.

When you already have **published** Quests, you will see your *active* and *deactivated* Quests but these Quests, displayed on the **published** section, are the last version of the Quest. Because a Quest can have multiple versions, because when a Quest is updated and the changes are published, a new Quest (with a new ID) is created and the old one is deactivated. These two Quests will be relationed since one is previous version of the other one. A "**Previous versions**" section is available on the edit page of a Quest to see all the previous versions of the Quest. Also, you can view the content of the previous versions by clicking on each link within the "**Previous versions**" section.

When you already have draft Quests, a section for them, are after the published Quests section. Here you can see their names, their descriptions, their images, and the actions you can perform on each quest. You can delete them directly from the Dashboard, or you can edit and update them by clicking on the "Edit" button. You can also click on "Export" and a [Quest JSON]({{< ref "/content/creator/quests/define.md" >}}) will be copied to your clipboard. 

## Create a new Quest

When you start creating a new Quest, this Quest is considered as a draft and it won't be visible to the players until you publish it.

To create a new Quest, click on the "Create Quest" button on the right of the Dashboard.

A page (`/design/create`), will be opened with the [Quests Designer](https://github.com/decentraland/quests-designer) to start designing your Quest and its steps and tasks. 

You can create a new Step (or Node) by dragging the "New Step" button onto the canvas. Or you can create a new Step (or Node) by pulling an edge from a exisiting Step (or Node) and dropping it on the canvas.

Every edge is editable, you can remove it by clicking on the edge "line" and clicking on the *backspace* key. You can also edit the edge by clicking on the edge "line" and dragging the edge to another Step (or Node).

Every Step (or Node) is removable also by clicking the *backspace* too. 

Every Step (or Node) has a set of properties that you can edit. You can edit the name, the description, the tasks and the task's actions. You can also edit the place of the Step (or Node) within the Qust by dragging it around the canvas and changing its edges.

{{< hint info >}}
**💡 Remember**: Each step ID and task ID should be unique within the **whole** Quest.
{{< /hint >}}

You can start designing your Quest and its steps and tasks. If you want to save your work, you can save the design as a draft and a new Quest draft will be created, with its appropiate ID and you will be redirected to new Quest Draft's Edit page (`/quests/drafts/:draftId`). 

On this page, you will be able to edit the rest of the Quest properties like its name, its description, its image, and its rewards. Like the Quest Steps, you can save the work you do on this page as a draft and it will be saved on the Quest Draft.

When you are done with the Quest, you can publish it by clicking on the "Publish" button on the bottom of the page. A Pop-up will be opened asking you if you want to keep the Quest Draft and publish the Quest, delete the Quest Draft and publish the Quest or if you want to cancel the operation.

After you publish the Quest, you will be redirected to the Edit (published) Quest page (`/quests/:questId`). Here you can update your Quest and its properties. You can also activate or deactivate the Quest. By default, your Quest is active when you publish it so it'll be public and visible, and playable (if you scene contains the code to play it). However, you can change it to "deactivated" and it won't be visible and it cannot be started by the players.

## Edit a Draft Quest

When you already have a draft Quest, you can edit it by clicking on the "Edit" button on the Dashboard. You will be redirected to the Edit (draft) Quest page (`/quests/drafts/:draftId`). Here you can edit the Quest as many time as you want and save it as a draft until you consider the Quest is ready to be published. You can edit the Quest Steps, the Quest Tasks, the Quest Actions, the Quest name, the Quest description, the Quest image, and the Quest rewards.

"Publish" button won't be enabled until you the Quest is a *valid* Quest. A Quest is considered as *valid* when it meet the requirements defined [here]({{< ref "/content/creator/quests/define.md" >}}). Or when it meets:
- A name longer than 5 chars.
- A description longer than 5 chars.
- A valid image URL.
- A valid Quest definition: A JSON with valid Steps and a Connections section. 
- If it has rewards, it should have: valid webhook URL, and valid reward items.

## Edit and Updating a Published Quest

When you already have a published Quest, you can edit it by clicking on the "Edit" button on the Dashboard. You will be redirected to the Edit (published) Quest page (`/quests/:questId`). You can edit the Quest Steps, the Quest Tasks, the Quest Actions, the Quest name, the Quest description, the Quest image, and the Quest rewards. When you are ready to make the changes public, you can click on the "Publish Changes" button and a new Quest will be created with the changes and the previous one will be deactivated.

When you do this, the player won't be able to start playing your previos Quest version, but they will be able to continue playing the Quest if they already started it. The player will be able to continue playing the Quest until they finish it or until they abandon it. If they abandon it, they won't be able to continue playing it and they will have to start the new version of the Quest from the beginning.

From Scene developing P.O.V, you should make sure that you make code to handle the Quests versions. You may want to apply some logic when a user is playing the old version and when a user is playing the new version. You should also make sure that a user that is currently playing the old version, can't start the new version. You can easily do this by using some of the function provided by the [Quests Client]({{< ref "/content/creator/quests/client.md" >}}) to get the user's quest instances and check if the user is playing the old version or the new version.

On Edit (published) Quest page (`/quests/:questId`), you can see all the previous version that a Quest has. You will always see the last version of a Quest on the Dashboard page. However, when you enter to the edit page, you will be able to see all the previous version and you can enter to each one to see what was the content of the Quest. 


