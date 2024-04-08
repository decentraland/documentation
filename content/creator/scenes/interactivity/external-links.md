---
date: 2020-04-16
title: Outbound links
description: Link to other scenes or external sites
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/external-links/
url: /creator/development-guide/external-links
weight: 6
---

{{< hint warning >}}
**📔 Note**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/interactivity/external-links.md" >}}).
{{< /hint >}}

You can add links from your scene out to other content, either to other scenes or to external websites.

## Teleports

To teleport a player to another scene, call the following function, indicating the coordinates that you want players to teleport to.

```ts
teleportTo('-51,1')
```

Players are presented a confirmation screen before they are teleported, this screen displays information from the destination scene’s `scene.json file`, including the scene `name`, `description` and `navmapThumbnail`. See [scene metadata]({{< ref "/content/creator/scenes/projects/scene-metadata.md" >}}) for details on how to set this data.

You can also teleport players to the most crowded place in Genesis City by doing `teleportTo(‘crowd’)`, which is equivalent to typing `/goto crowd` in the chat. Similarly you can teleport players to a random location from the curated list that you reach with `/goto magic` by doing ``teleportTo(‘magic’)`.

Bare in mind that teleports take you to a scene in the indicated coordinates, but not necessarily to that same coordinates. This means that when travelling to a scene that has multiple parcels, players may not be landing on the same coordinates as specified, but rather into one of the spawn points designated by the creator of the scene.

To move a player to another set of coordinates inside the current scene, use the `movePlayerTo()` function instead. See [Move a Player]({{< ref "/content/creator/scenes/interactivity/move-player.md" >}}).

## External links

To add a link to an external website, use the `openExternalURL()` command.

```ts
const entity = new Entity()
entity.addComponent(new BoxShape())
const transform = new Transform({ position: new Vector3(4, 0, 4) })
entity.addComponent(transform)
entity.addComponent(
	new OnPointerDown(() => {
		openExternalURL('https://docs.decentraland.org')
	})
)
engine.addEntity(entity)
```

To prevent any abusive usage of this feature to spam players, it's only possible to call the `openExternalURL` from an explicit click or button event on an entity. It's not possible to call this function as a result of a timer, or a collision area, or a global click event.

When `openExternalURL` is called, players are prompted with a confirmation screen, where they are informed of where the link will take them, and where can accept of decline to visit the link.

The link is opened in a new tab, keeping the original tab in Decentraland.

If players tick the _trust this domain_ checkbox, they won't be prompted again during their session, as long as the link comes from the same scene and is to the same domain.
