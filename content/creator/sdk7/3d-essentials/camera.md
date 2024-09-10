---
date: 2024-09-09
title: Camera
description: Learn how to control the player's camera
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/camera/
weight: 5
---

<!--
By default, players can chose between a 1st or 3rd person camera mode while exploring your scene.

You can also assign virtual cameras in your scene, and have full control over how they behave. You can assign any entity to be a virtual camera, and then move that entity with the same movement that you can move any other entity in the scene, applying tweens (link) for smooth movement, etc

Tip : camera modifier

## Camera assignment

To assign a virtual camera:

- Create a virtual camera: Add a `VirtualCamera` component to any entity.
- Determine which camera to use: Add a `MainCamera` component on `engine.CameraEntity`, with a reference to the entity with the `VirtualCamera` component

The entity with the `VirtualCamera` component will be that will behave as an anchor to the camera. If the entity moves, the camera moves with it.

Only one camera may be in use at a time.

```ts
function main() {
	const myCustomCamera = engine.addEntity()
	Transform.create(myCustomCamera, {
		position: Vector3.create(8, 1, 8),
	})
	MeshRenderer.setBox(myCustomCamera)
	VirtualCamera.create(myCustomCamera, {
		defaultTransition: { transitionMode: { $case: 'time', time: 0 } },
	})

	const mainCamera = MainCamera.createOrReplace(engine.CameraEntity, {
		virtualCameraEntity: myCustomCamera,
	})
}
```

Note: camera needs to be inside scene bounds

Assigning MainCamera.virtualCameraEntity as 0 frees the MainCamera to use the default camera behavior. The player is then free to switch between 1st and 3rd person cameras.

Note: if there's a camera modifier area (link) it won't change the camera. Virtual cameras are given priority, camera modifier areas only work when there is no virtual camera

## Camera Transitions

you can define the behavior for whenever the virtual camera changes. It can be an instant change of camera, or be a transition from one position to the other.

The transition settings on a virtual camera determine how you transition _into_ that camera, from any other camera in the scene, including the default. They don't affect how you transition _out_ of that camera.

Depending on your use case, you can choose to control:

- Time: How long you want the transition to last, the camera will move as fast as it needs to do it in that period of time
- Speed: How fast you want the transition to move, the time will depend on the distance

```ts
defaultTransition: {
        transitionMode: VirtualCamera.Transition.Speed(15),
        fromEntity: cameraEntity1,
        toEntity: cameraEntity2
      },
```

```ts
   defaultTransition: {
        transitionMode: VirtualCamera.Transition.Time(6),
        fromEntity: cameraEntity1,
        toEntity: cameraEntity2
      },
```

## Camera following

You can configure a camera so that it always rotates to look directly at something, this could be the player, or some other entity in the scene.

Use the `lookAt` property

snippet with player

snippet with entity

This rotation is done engine-side, so will be smooth even if the player has bad performance on the scene.

It will only change the rotation, not the position

Assigning VirtualCamera.lookAt as same entity or as engine.MainCamera is the same as not assigning any -->
