---
title: 'Quests CLI'
url: /creator/quests/cli
weight: 5
---

Use the Quests CLI to create, list, activate and deactivate your Quests.

Before you can use the Quests CLI, ensure you have all the dependencies installed, and familiarize yourself with Decentraland's CLI. Read [Using the CLI]({{< ref "/content/creator/sdk7/getting-started/using-the-cli.md" >}}).

## Wallet signatures

Before going into detail about each command, you should know that each command will require your signature (Ethereum Signature). The CLI uses this to generate the [authchain]({{< ref "/content/contributor/auth/authchain.md" >}}) and interact with the [Quests Server]({{< ref "/content/creator/quests/overview.md" >}}). To do that, the CLI will open the "Linker dApp" in your browser and ask you to sign a message.

## Create a new quest

To create a new quest, you can use two different commands:

###### Create a new Quest via prompts

```bash
$ npx @dcl/sdk-commands quests --create
```

The above command runs through a series of prompts to create a new Quest. You will be asked to provide the following information:

- Quest name: type the name for your Quest. It should be longer than 5 chars.

```bash
$ ? How do you want to name your Quest? >
```

- Quest description: type a description for your Quest. It should be longer than 5 chars.

```bash
$ ? Give a description to your Quest >
```

- Quest image: insert an image URL to display your Quest on Explorer. It should be a valid URL.

```bash
$ ? Image URL to display your Quest >
```

- Quest definition: Paste the JSON definition. It should consist of a JSON with valid Steps and a Connections section. For a better experience, it should be minified/compacted.

```bash
$ ? Paste the Defintion (Steps & Connections) of your Quest >
```

{{< hint info >}}
**💡 Tip**: Find more information about the JSON's required structure [here]({{< ref "/content/creator/quests/define.md" >}}).
{{< /hint >}}

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

- Quest Reward Webhook URL: Insert the webhook URL to send notifications when a user completes your Quest. It should be a valid URL. The URL can include placeholders as defined in the examples [here]({{< ref "/content/creator/quests/define.md" >}}) or in the rewards documentation [here]({{< ref "/content/creator/quests/rewards.md" >}})

```bash
$ ? Insert the Webhook URL of your Rewards Server >
```

After this, the CLI will ask you if you want a request payload to be sent to your webhook when a player completes your Quest:

```bash
$ ? Do you want to send a request body to your webhook? > (y/N)
```

If you type: `n`, you will be asked to provide the reward items information (this is described below).

If you type: `y`, you will be asked to provide the following information:

- Quest Reward Webhook's request body: Insert a JSON to be sent as the payload to your webhook when a player completes your Quest. It should be a valid JSON. For a better experience, it should be minified/compacted.

{{< hint info >}}
**💡 Tip**: You can make use of the placeholders as are defined in the examples [here]({{< ref "/content/creator/quests/define.md" >}}) or in the rewards documentation [here]({{< ref "/content/creator/quests/rewards.md" >}}).
{{< /hint >}}

```bash
$ ? Insert the request body to send within POST request to your webhook >
```

After this, you will be asked to provide the reward items information:

First, how many items do you want to give to the user that completes the Quest. It should be a number, greater than 0:

```bash
$ ? How many items the user will receive? >
```

Then, for each item, you will be asked to provide the following information:

- Item name: type the name for your item. It should be 3 chars long or more.

```bash
$ ? What is the name of your {THE_ITEM_NUMBER} reward? ›
```

- Item Image: insert the image URL for your item. It should be a valid URL.

```bash
$ ? Provide an image link for your {THE_ITEM_NUMBER} reward >
```

Once you finish providing the information for each item, the creation will be done and the "Linker dApp" will be opened so that you can sign the action with your Wallet. After you sign the the action, and if all went well, you will see the ID of your new Quest in the SDK console.

###### Create a new Quest with a JSON file

To avoid all the prompts, create a full JSON file with all of the information needed to create a Quest. Find more information about the quest definition JSON structure [here]({{< ref "/content/creator/quests/define.md" >}}).

```bash
$ npx @dcl/sdk-commands quests --create-from-json <path_to_json_file>
```

If your JSON file doesn't have any errors, the Quest will be created and the "Linker dApp" will open to sign the action with your Wallet. After you sign the the action, and if all went well, you will see the ID of your new Quest in the console.

The `<path_to_json_file>` should be an absolute path to your JSON file. For example:

```bash
$ npx @dcl/sdk-commands quests --create-from-json /Users/username/Desktop/quest.json
```

## List your quests

To list your quests, use the following command:

```bash
$ npx @dcl/sdk-commands quests --list <your_eth_address>
```

Or

```bash
$ npx @dcl/sdk-commands quests -l <your_eth_address>
```

The command validates that the address is valid. If valid, the command opens the "Linker dApp" to sign the action with your Wallet. After you sign the the action, and if all went well, the command prints out all the Quests you created, each with their names and IDs.

## Deactivate a Quest

To stop players from starting your Quest, you can deactivate it. The Players who have already started the Quest, can keep playing it, as long as the Scene where the Quest takes place keeps having the logic to do so.

So to deactivate it, use the following command:

```bash
$ npx @dcl/sdk-commands quests --deactivate <quest_id>
```

The `<quest_id>` should be a valid UUID, that you can obtain from the `--list` command.

{{< hint info >}}
**📔 Note**:
You can only activate or deactivate a quest if you are signing with the same wallet that signed when creating the quest.
{{< /hint >}}

## Activate a Quest

To activate a Quest that was previously deactivated, use the following command:

```bash
$ npx @dcl/sdk-commands quests --activate <quest_id>
```
