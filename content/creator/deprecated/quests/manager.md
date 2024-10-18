---
title: 'Quests Manager'
url: /creator/quests/manager
weight: 7
---

Use the Quests Manager to create, edit and handle your quests. You can access the Quests Manager through the [CLI]({{< ref "/content/creator/deprecated/quests/cli.md" >}}).

## Opening the Quests Manager

To open the Quests Manager, use the following command:

```bash
$ npx @dcl/sdk-commands quests -m
```

After you run this command, the [CLI]({{< ref "/content/creator/deprecated/quests/cli.md" >}}) opens the Quests Manager in your default browser (unless you set `--no-browser` or `-b` flags), and prints out the URL if you prefer to open it manually.

When you open up the Quests Manager, you will be asked to log in with your Ethereum wallet.

## Dashboard

On the Dashboard (the main page `/`), you can see your drafts and published quests.

<img src="/images/quests/quests-manager-dashboard.png" alt="Quests Service" style="width: 100%;"/>

It displays two lists of quests: **draft** and **published**, including descriptions, images, status, and actions you can perform on each. You can edit and update a quest, activate it or deactivate it.

The first time that you open the Quests Manager, you will see a message saying that you don't have any quests yet. Create a new one by clicking "Create Quest", on the right.

If you have **published** Quests, you will see your _active_ and _deactivated_ Quests displayed on the **published** section. These quests are the latest versions of each.

If you have draft Quests, you can see them in a section after the published Quests. Here you can see their names, their descriptions, their images, and the actions you can perform on each. You can delete them directly from the Dashboard, or you can edit and update them by clicking on the "Edit" button. You can also click on "Export" to copy the [Quest JSON]({{< ref "/content/creator/deprecated/quests/define.md" >}}) to your clipboard.

## Quest versions

When a Quest is updated and the changes are published, a new Quest (with a new ID) is created and the old one is deactivated.

You always see the latest version of a quest on the Dashboard page. Open the "**Previous versions**" section on the edit page of a Quest to see all its previous versions. Each version includes a link to view its content.

## Create a new Quest

When creating a new Quest, this Quest is saved as a draft and won't be visible to players until you publish it.

To create a new Quest, click on the "Create Quest" button, on the right of the Dashboard.

A page (`/design/create`), opens with the [Quests Designer](https://github.com/decentraland/quests-designer) to start designing your Quest.

Create a new step (a Node) by dragging the "New Step" button onto the canvas. You can also create a new step by pulling an edge from a existing step and dropping it on the canvas. Any step can be removed by clicking the _backspace_.

Every connection is editable, you can remove it by clicking on the connection and hitting the _backspace_ key. You can also edit the connection by clicking on it and dragging it to another step.

Each step has a set of properties. You can edit the name, description, tasks and the task's actions. You can also edit the place of the step within the quest by dragging it around the canvas and changing its connections.

{{< hint info >}}
**💡 Remember**: Each step ID and task ID must be unique within the **whole** quest.
{{< /hint >}}

When you save your work, a new quest draft is created, with its corresponding ID. You will be redirected to the edit page of this new quest draft (`/quests/drafts/:draftId`).

On this page, you can edit the quest's global properties: name, description, image, and rewards. Like when editing the quest steps, you can save the work on this page as a draft.

When you are done with the Quest, you can publish it by clicking on the "Publish" button on the bottom of the page. A Pop-up opens, asking if you want to either keep the Quest Draft and publish the Quest, or delete the Quest Draft and publish the Quest, or cancel the operation.

{{< hint warning >}}
**📔 Note**: Keep in mind that a published quest is stored separate from the draft, with its own unique ID.
{{< /hint >}}

After you publish the Quest, you are redirected to the Edit (published) quest page (`/quests/:questId`). Here you can update your Quest and its properties. You can also activate or deactivate it. By default, a Quest is public and visible. It's already playable, as long as a published scene contains code that references it. You can change the quest's state to "deactivated" so it won't be visible and can't be played.

## Edit a draft quest

Once you have a draft quest, you can edit it by clicking the "Edit" button on the Dashboard. You are redirected to the Edit (draft) quest page (`/quests/drafts/:draftId`). Here you can edit the quest and save it as a draft until you consider it's ready to be published. You can edit the steps, the tasks, the actions, the Quest name, the Quest description, the image, and the rewards.

The "Publish" isn't enabled until the Quest is _valid_. A Quest is considered _valid_ when it meets the requirements defined [here]({{< ref "/content/creator/deprecated/quests/define.md" >}}). In summary, it has:

- A name longer than 5 chars.
- A description longer than 5 chars.
- A valid image URL.
- All steps and connections are valid, with all required fields completed and all IDs being unique.
- If it includes rewards, it should have: valid webhook URL, and valid reward items.

## Edit a published quest

Once you have a published quest, you can edit it by clicking on the "Edit" button on the dashboard. You are redirected to the edit (published) quest page (`/quests/:questId`). You can edit the steps, the tasks, the actions, the quest name, the quest description, the image, and the rewards. When you are ready to make the changes public, click on the "Publish Changes" button and a new quest is created with a new ID. the previous quest deactivated.

Players aren't able to start playing the previous inactive quest version, but they are able to continue playing it if they had already started, as long as your scene supports that. They can continue playing inactive quests until they either finish it or abandon it. If they abandon an inactive quest, they won't be able to resume, they will have to start the new version of the quest from the beginning.

If you want to allow players on older versions of the quest to finish it, you should ensure your scene's code handles all quests versions that might currently be in use. You should also make sure that a user that is currently playing through an old version can't also start the new version, as they could end up with duplicate rewards. You can easily do this by using the functions provided in the [Quests Client]({{< ref "/content/creator/deprecated/quests/client.md" >}}) to get the user's quest instances for the old versions of the quest, and check for any progress.
