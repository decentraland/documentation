---
title: 'Quests CLI'
url: /creator/quests/cli
weight: 5
---

To use the Quests CLI, make sure you have read and followed: [Using the CLI]({{< ref "/content/creator/sdk7/getting-started/using-the-cli.md" >}}).

Once you have all the dependencies installed, you can use the Quests CLI to create, list, activate and deactivate your Quests.

Before talking about each command, you need to know that each command will require your signature (Ethereum Signature) so that the CLI can generate the [authchain]({{< ref "/content/contributor/auth/authchain.md" >}}) and interact with the [Quests Server]({{< ref "/content/creator/quests/overview.md" >}}). To do that, the CLI will open the "Linker dApp" in your browser and ask you to sign a message.

## Create a new quest

To create a new quest, you can use two different commands: 

###### Create a new Quest by prompts

```bash
$ npx @dcl/sdk-commands quests --create
```

Above command will start giving you prompts to create a new Quest. You will be asked to provide the following information:

- Quest name: type the name for your Quets. It should be more than 5 chars.

```bash
$ ? How do you want to name your Quest? >
```

- Quest description: type the description for your Quest. It should be more than 5 chars.

```bash
$ ? Give a description to your Quest > 
```

- Quest image: insert an image URL to display your Quest on Explorer. It should be a valid URL.

```bash
$ ? Image URL to display your Quest >
```

- Quest definition: Paste the JSON definition. It should be a valid Steps and Connections JSON, and for better experience, it should be minified/compacted. You can find more information about this [here]({{< ref "/content/creator/quests/define.md" >}}).

```bash
$ ? Paste the Defintion (Steps & Connections) of your Quest >
```

An example of this: 
```JSON
{"steps":[{"id":"Step-1","description":"","tasks":[{"id":"Step-1_0","description":"","actionItems":[{"type":"CUSTOM","parameters":{"id":"CUSTOM_1"}}]}]},{"id":"Step-2","description":"","tasks":[{"id":"Step-2_0","description":"","actionItems":[{"type":"CUSTOM","parameters":{"id":"CUSTOM_2"}}]}]},{"id":"Step-3","description":"","tasks":[{"id":"Step-3_0","description":"","actionItems":[{"type":"CUSTOM","parameters":{"id":"CUSTOM_3"}}]}]}],"connections":[{"stepFrom":"Step-1","stepTo":"Step-3"},{"stepFrom":"Step-2","stepTo":"Step-3"}]}
```

```bash
$ ? Paste the Defintion (Steps & Connections) of your Quest > {"steps":[{"id":"Step-1","description":"","tasks":[{"id":"Step-1_0","description":"","actionItems":[{"type":"CUSTOM","parameters":{"id":"CUSTOM_1"}}]}]},{"id":"Step-2","description":"","tasks":[{"id":"Step-2_0","description":"","actionItems":[{"type":"CUSTOM","parameters":{"id":"CUSTOM_2"}}]}]},{"id":"Step-3","description":"","tasks":[{"id":"Step-3_0","description":"","actionItems":[{"type":"CUSTOM","parameters":{"id":"CUSTOM_3"}}]}]}],"connections":[{"stepFrom":"Step-1","stepTo":"Step-3"},{"stepFrom":"Step-2","stepTo":"Step-3"}]}
```

After this, the CLI will ask you if you want to give rewards to the players:

```bash
$ ? Do you want to give rewards to the players? > (y/N)
```

If you type: `n`, the creation will be done and the "Linker dApp" will be opened so that you can sign the action with your Wallet. 

If you type: `y`, you will be asked to provide the following information:

- Quest Reward Webhook URL: Insert the webhook URL to notify you when a user completes your Quest. It should be a valid URL. You can make use of the placeholders as are defined in the examples [here]({{< ref "/content/creator/quests/define.md" >}}) or in the rewards documentation [here]({{< ref "/content/creator/quests/rewards.md" >}})

```bash
$ ? Insert the Webhook URL of your Rewards Server > 
```

After this, the CLI will ask you if you want a request payload to be sent to your webhook when a player completes your Quest:

```bash
$ ? Do you want to send a request body to your webhook? > (y/N)
```
If you type: `n`, you will be asked to provide the reward items information (it's described below).

If you type: `y`, you will be asked to provide the following information:

- Quest Reward Webhook's request body: Insert a JSON to be sent as the payload to your webhook when a player completes your Quest. It should be a valid JSON, and for better experience, it should be minified/compacted. You can make use of the placeholders as are defined in the examples [here]({{< ref "/content/creator/quests/define.md" >}}) or in the rewards documentation [here]({{< ref "/content/creator/quests/rewards.md" >}})

```bash
$ ? Insert the request body to send within POST request to your webhook >
```

After this, you will be asked to provide the reward items information:

First, how many items do you want to give to the user that completes the Quest, it should be a valid number, greater than 0:

```bash
$ ? How many items the user will receive? >
```

Then, for each item, you will be asked to provide the following information:

- Item name: type the name for your item. It should be 3 chars or more.

```bash
$ ? What is the name of your {THE_ITEM_NUMBER} reward? ›
```

- Item Image: insert the image URL for your item. It should be a valid URL.

```bash
$ ? Provide an image link for your {THE_ITEM_NUMBER} reward >
```

Once you finish providing the information for each item, the creation will be done and the "Linker dApp" will be opened so that you can sign the action with your Wallet. After you sign the the action, and if all went well, you will see the ID of your new Quest in the SDK console.

###### Create a new Quest with a JSON file

If you want to avoid all the prompts, you can create a JSON file with the information needed to create a Quest. You can find more information about this [here]({{< ref "/content/creator/quests/define.md" >}}).

```bash
$ npx @dcl/sdk-commands quests --create-from-json <path_to_json_file>
```

The command tells you if you have any error in your Quest file. If you don't have any error, the Quest will be created and the "Linker dApp" will be opened so that you can sign the action with your Wallet. After you sign the the action, and if all went well, you will see the ID of your new Quest in the SDK console.

The `<path_to_json_file>` should be an absolute path to your JSON file. For example:

```bash
$ npx @dcl/sdk-commands quests --create-from-json /Users/username/Desktop/quest.json
```

## List your quests

To list your quests, you can use the following command:

```bash
$ npx @dcl/sdk-commands quests --list <your_eth_address>
```

Or 

```bash
$ npx @dcl/sdk-commands quests -l <your_eth_address>
```

The command will validate that you're providing a valid address. If it's not valid, an error will be thrown. If it's valid, the command will open up the "Linker dApp" to make you sign the action with your Wallet. After you sign the the action, and if all went well, the command will print out all the Quests you have with their names and IDs.

## Deactivate a Quest

If you want user to stop playing your Quest, you can deactivate it so that nobody can start the Quest. The Players who have started the Quest, can keep playing it if the Scene or World where the Quest is played, keep the logic to do so.

Of course, you can only deactivate the Quest if you are the Creator.

So to deactivate it, you can use the following command:

```bash
$ npx @dcl/sdk-commands quests --deactivate <quest_id>
```

The `<quest_id>` should be a valid UUID, you can get it from the `--list` command

## Activate a Quest

If you want to activate a Quest that was previously deactivated. You can use the following command:

```bash
$ npx @dcl/sdk-commands quests --activate <quest_id>
```

Of course, you can only activate the Quest if you are the Creator.