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

Portable experiences are essentially scenes that are not constrained to parcels of land. Players can carry these with them anywhere they go in Decentraland, adding a new layer of content over the world. Smart Wearables are examples of portable experiences.
Portable Experiences are scenes deployed to a World (tied to a NAME) and can be loaded by another scene using the SDK7.

## Getting started

To create a new portable experience (only SDK7 is supported)

### Using CLI
1. Open a command line in a new folder and run

`npx sdk-commands init --project px-template`

### Using Editor
Make sure you've [installed the Decentraland editor]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md" >}}), then:

1. Open a Visual Studio Code window on an _empty folder_.
2. Select the Decentraland tab on Visual Studio's left margin sidebar
3. Click **Create Project**
4. The editor will prompt you about what kind of project to create. Select **Portable Experience**.


This command creates the basic files and structure for a new portable experience scene. This folder is very similar to that of a Decentraland scene, but you will notice the following differences:

- `scene.json` is a lot shorter, it doesn’t include properties that are irrelevant to a wearable, like parcels or spawn points

## The Preview

Running a preview of a portable experience is just like running that of a scene, simply run `npm run start`. You’ll notice that all the visible around you are the default empty parcels. In this preview mode, you are not restricted to any set of parcels, you can add 3D models or sounds anywhere in the world.


## Publish

To publish your portable experience you need to own a [Decentraland NAME](https://builder.decentraland.org/names)

You need to specify under what **name** your deployment is to be made.


Add the following section in your
`scene.json`:

```json
{
  "worldConfiguration" : {
    "name": "my-name.dcl.eth"
  }
}
```

{{< hint warning >}}
**📔 Note**:  Be carefull, this will override the scene of the world, if you have already deployed one.
{{< /hint >}}

## Lifetime of a portable experience in a scene

You can spawn a portable experience from your scene.
You just need yo have the DCL name where the Portable experience was deployed.
```
import { spawn } from '~system/portableexperiences'

executeTask(async () => {
  const { pid } = await spawn({ ens: 'boedo.dcl.eth'})
})
```

You may want to know if a player is using a portable experience, since this may enable players to have abilities that could be considered cheating in a competitive game. For example, in a platform game, a player that wears a jetpack has a very unfair advantage over others.

```
import { spawn, getPortableExperiencesLoaded, kill } from '~system/PortableExperiences'

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

## Restricted actions

To prevent abuse, certain features aren't permitted on portable experiences by default, and require adding a permission flag.
Or if you own a scene and want to manage how portable experiences are going to work on your scene.

See [Required permissions]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#required-permissions">}}) for more details.


## Tips
- When positioning an entity, note that positions are global, relative to the 0,0 coordinates of Genesis Plaza.
- To react to nearby players:
  - use `getConnectedPlayers()` to know what players are already there, and `onPlayerConnectedObservable` / `onPlayerDisconnectedObservable` to track other players coming and going.
  - Be mindful that the loading of the portable experience, surrounding scenes and other players may occur in different orders depending on the situation. If the player enters Decentraland with the smart wearable already on, it’s likely that your portable experience will load before other players do. On the other hand, tf the player first loads into a scene and then puts on the wearable, it’s likely that other players will already be loaded by the time the portable experience starts running.
  - Wait till the player is connected to an island inside their realm. Fetch the realm data and check for the ‘room’ field. If the ‘room’ field is null, the player is not yet connected to an island and other players won’t be loaded yet. You can periodically check this every 1 second till the ‘room’ field is present, and only initialize your logic then.
- To interact with surrounding scenes:
  - You can’t directly send any instructions to nearby scenes or other portable experiences, the `messageBus` is currently sandboxed for each portable experience/scene.
  - You can use an intermediate server to send information between the portable experience and a scene.
  - If you do a raycast, you can detect hits against the colliders of entities from the surrounding scenes. This can tell you the exact hit location, normal direction, and even the entity name and mesh name of the 3D model.
- Kill a portable experience: Run the `kill()` method to self-terminate a portable experience.
