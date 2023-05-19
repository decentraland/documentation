---
date: 2020-04-16
title: Outbound links
description: Link to other scenes or external sites
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/external-links/
weight: 6
---

You can add links from your scene out to other content, either to other scenes or to external websites.

## Teleports

To teleport a player to another scene, call the following function, indicating the coordinates that you want players to teleport to.

```ts
import { teleportTo } from "~system/RestrictedActions"

const gridSize: number = 16

teleportTo({
  worldPosition: Vector3.create(-51 * gridSize, 0 , 1 * gridSize)
})
```

Players are presented a confirmation screen before they are teleported, this screen displays information from the destination scene’s `scene.json file`, including the scene `name`, `description` and `navmapThumbnail`. See [scene metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}) for details on how to set this data.

You can also teleport players to the most crowded place in Genesis City by doing `teleportTo(‘crowd’)`, which is equivalent to typing `/goto crowd` in the chat. Similarly you can teleport players to a random location from the curated list that you reach with `/goto magic` by doing ``teleportTo(‘magic’)`.

Bare in mind that teleports take you to a scene in the indicated coordinates, but not necessarily to that same coordinates. This means that when travelling to a scene that has multiple parcels, players may not be landing on the same coordinates as specified, but rather into one of the spawn points designated by the creator of the scene.

To move a player to another set of coordinates inside the current scene, use the `movePlayerTo()` function instead. See [Move a Player]({{< ref "/content/creator/sdk7/interactivity/move-player.md" >}}).

## External links

To add a link to an external website, use the `openExternalUrl()` command.

```ts
import {openExternalUrl} from "~system/RestrictedActions"

openExternalUrl({url: "google.com"})
```

To prevent any abusive usage of this feature to spam players, it's only possible to call the `openExternalUrl` from an explicit click or button event on an entity. It's not possible to call this function as a result of a timer, or a collision area, or a global click event. See [Button events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md" >}}) for details on how to do this.

When `openExternalUrl` is called, players are prompted with a confirmation screen, where they are informed of where the link will take them, and where can accept of decline to visit the link.

The link is opened in a new tab, keeping the original tab in Decentraland.

If players tick the _trust this domain_ checkbox, they won't be prompted again during their session, as long as the link comes from the same scene and is to the same domain.
