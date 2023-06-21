---
date: 2020-08-04
title: Move a player
description: Change a player's position inside the scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/move-player/
weight: 2
---

To change the player's position in the scene, use the `movePlayerTo()` function. This function takes an object with two properties:

- `newRelativePosition`: Where to move the player, expressed as a Vector3.
- `cameraTarget`: (optional) What direction to make the player face, expressed as a Vector3 that represents the coordinates of a point in space to stare at. If no value is provided, the player will maintain the same rotation as before moving.

```ts
import { movePlayerTo } from '~system/RestrictedActions'

// create entity
const myEntity = engine.addEntity()
MeshRenderer.setBox(myEntity)
MeshCollider.setBox(myEntity)

Transform.create(myEntity, {
  position: { x: 4, y: 1, z: 4 },
})

// give entity behavior
pointerEventsSystem.onPointerDown(
  {
    entity: myEntity,
    opts: { button: InputAction.IA_POINTER, hoverText: 'Click' },
  },
  function () {
    // respawn player
    movePlayerTo({
      newRelativePosition: Vector3.create(1, 0, 1),
      cameraTarget: Vector3.create(8, 1, 8),
    })
  }
)
```

The player's movement occurs instantly, without any confirmation screens or camera transitions.

{{< hint warning >}}
**📔 Note**: Players can only be moved if they already are standing inside the scene's bounds, and can only be moved to locations that are inside the limits of the scene's bounds. You can't use `movePlayerTo()` to transport a player to another scene. To move a player to another scene, see [Teleports]({{< ref "/content/creator/sdk7/interactivity/external-links.md#teleports">}}).
{{< /hint >}}

You must first add the `ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE` permission to the `scene.json` file before you can use this feature. If not yet present, create a `requiredPermissions` property at root level in the JSON file to assign it this permission.

```json
"requiredPermissions": [
    "ALLOW_TO_MOVE_PLAYER_INSIDE_SCENE"
  ],
```

See [Required permissions]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#required-permissions">}}) for more details.

{{< hint warning >}}
**📔 Note**: To prevent abusive behavior that might damage a player's experience, the ability to move a player is handled as a permission. Currently, this permission has no effect in how the player experiences the scene. In the future, players who walk into a scene with this permission in the `scene.json` file will be requested to grant the scene the ability to move them.
{{< /hint >}}
