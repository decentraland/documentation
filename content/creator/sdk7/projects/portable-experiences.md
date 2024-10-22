---
date: 2022-07-19
title: Portable experiences
description: Portable experiences
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/portable-experiences/
weight: 4
---

Portable experiences are essentially scenes that are not constrained to parcels of land. Players can carry these with them anywhere they go in Decentraland, adding a new layer of content over their experience.
Portable Experiences can be tied to a NAME and can be loaded by another scene using the SDK.

{{< hint warning >}}
**📔 Note**: Portable experiences can only be created using SDK 7. Also, only scenes built with SDK 7 are capable of loading a portable experience.

The **Creator Hub** doesn't currently support creating Portable Experience projects. Use the **VS Studio Code** extension instead.
{{< /hint >}}

Smart Wearables are a kind of portable experience that is associated to a wearable, and activated based on if the player is using that wearable. This document doesn't cover those, see [smart wearables]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}) for more details.

## Getting started

### Using the VS Code Extension

Make sure you've [installed the Decentraland VS Code Extension]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md#vs-code-extension" >}}), then:

1. Open a Visual Studio Code window on an _empty folder_.
2. Select the Decentraland tab on Visual Studio's left margin sidebar
3. Click **Create Project**
4. The Decentraland extension will prompt you about what kind of project to create. Select **Portable Experience**.

This command creates the basic files and structure for a new portable experience scene. This folder is very similar to that of a Decentraland scene, but you will notice the following differences:

- `scene.json` is a lot shorter, it doesn’t include properties that are irrelevant to a portable experience, like parcels or spawn points.

### Using the CLI

1. Open a command line in a new folder and run

`npx sdk-commands init --project px-template`

## Preview

Running a preview of a portable experience is just like running that of a scene, simply click the **Run Scene** button on the Decentraland tab, or run `npm run start` in the command line.

You’ll notice that rather than seeing an empty grid, you are surrounded by the default empty parcels content. In a portable experience, you are not restricted to any set of parcels, you can add 3D models or sounds anywhere in the world. Since the portable experience is meant to be experienced anywhere in Decentraland, you're most likely going to focus on entities attached to the player or UI, but you can also place entities freely in the world.

## Publish

To publish your portable experience, you need to own a [Decentraland NAME](https://builder.decentraland.org/names).

To specify under what **name** to make your deployment, add the following section in your `scene.json`:

```json
{
	"worldConfiguration": {
		"name": "my-name.dcl.eth"
	}
}
```

{{< hint warning >}}
**📔 Note**: Each NAME references a single portable experience or world. If your name already pointed to a world, deploying a portable experience will override that content.
{{< /hint >}}

Make sure you're either using the Ethereum account that owns this name, or an account that has been given permissions to deploy to this name.

### Using the VS Code Extension

Open the Decentraland tab and click the three-dots icon at the top, and select **Publish scene to your world**.

### Using the CLI

Run:

```
npm run deploy --target-content https://worlds-content-server.decentraland.org
```

## Lifecycle of a portable experience in a scene

Portable expereinces need to be activated by a scene, either in Genesis City or a world.

1. The player visits the scene that activates the portable experience. The scene can spawn the portable experience right away or use custom logic to do it after the player does an action.
2. The player is prompted about the portable experience, including details about the requested permissions. The portable experience is only activated if the player gives conscent.
3. The player will now carry the portable experience with them wherever they go for the rest of the session, including teleporting or jumping to worlds. If the player reloads the browser window, it will be gone.

To spawn a portable experience from your scene, use the `spawn()` function. To terminate a portable experience, use `kill()`. In both cases, you just need yo know the DCL name where the Portable experience was deployed.

```ts
import {spawn} from "~system/PortableExperiences"

// spawn
executeTask(async () => {
  const { pid } = await spawn({ ens: 'boedo.dcl.eth'})
})

// kill
executeTask(async () => {
  await kill({'boedo.dcl.eth'})
})
```

## Restricting portable experiences

You might be worried about preventing the use of portable experiences in your scene, since these could give players abilities that could be considered cheating in a competitive game. For example, in a platform game, a player that wears a jetpack has a very unfair advantage over others.

The simplest approach is to add a flag to block all portable experiences entirely on your scene at any time, or prevent their UIs from showing. See [feature toggles]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#feature-toggles" >}}). This also applies to portable experiences linked to smart wearables.

Another approach is to query to view a player's portable experiences, and take action accordingly.

```ts
import {
	spawn,
	getPortableExperiencesLoaded,
	kill,
} from '~system/PortableExperiences'

executeTask(async () => {
	const { loaded } = await getPortableExperiencesLoaded({})

	for (const portableExperience of loaded) {
		const { ens, name, pid } = portableExperience
		if (name === 'some-name.dcl.eth') {
			await kill({ pid })
		}
	}
})
```

In the example above, the scene is using `kill()` to terminate portable experiences if they match a certain name. You could keep track of a denylist of non-allowed portable experience names, and chose to only terminate those. You could also chose to terminate all of them.

An alternative to terminating portable experiences is to change the behavior of your scene when they are present. For example, the player might be able to keep their portable experience, but not be allowed to start a match, or to claim any rewards as long as they have any enabled.

## Restricted actions in portable experiences

To prevent abuse, certain features aren't permitted on portable experiences by default, and require adding a permission flag.

See [Required permissions]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#required-permissions">}}) for more details.

{{< hint warning >}}
**📔 Note**: Players are notified about the required flags by the portable experience. Avoid adding permissions you don't need, since it can make players distrust your portable experience and reject it.
{{< /hint >}}

## Limitations

Portable experiences only run for the player that activates it. Other players don't see the effects. For example, if the portable experience renders a pet that follows the player, other players around won't see this pet. However, other players will see avatars perform animations that run as part of the portable experience, even [custom avatar animations]({{< ref "/content/creator/sdk7/interactivity/trigger-emotes.md#custom-animations">}}) uploaded as part of the portable experience's files.

## Tips

- When positioning an entity, note that positions are global, relative to the 0,0 coordinates of Genesis Plaza.
- To react to nearby players:
  - See [Fetch all players]({{< ref "/content/creator/sdk7/interactivity/user-data.md#fetch-all-players" >}}) to know how to obtain data from other players in the surroundings.
  - Be mindful that the loading of the portable experience, surrounding scenes and other players may occur in different orders depending on the situation. If the player enters Decentraland with the portable experience already on, it’s likely that your portable experience will load before other players do. On the other hand, tf the player first loads into a scene and then activates the portable experience, it’s likely that other players will already be loaded by the time the portable experience starts running.
  - For multiplayer experiences, wait till the player is connected to an island inside their realm. Run `getRealm()` and check for the ‘room’ field. If the ‘room’ field is null, the player is not yet connected to an island and other players won’t be loaded yet. You can periodically check this every 1 second till the ‘room’ field is present, and only initialize your logic then.
- To interact with surrounding scenes:
  - You can’t directly send any instructions to nearby scenes or other portable experiences, the `messageBus` is sandboxed for each portable experience/scene.
  - You can use an intermediate server to send information between the portable experience and a scene.
  - If you do a raycast, you can detect hits against the colliders of entities from the surrounding scenes. This can tell you the exact hit location, normal direction, and even the entity name and mesh name of the 3D model. This only works when hitting entities on scenes written with SDK7.
- Kill a portable experience: Run the `kill()` method to self-terminate a portable experience.
