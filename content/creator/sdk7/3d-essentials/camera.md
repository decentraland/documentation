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

As a creator, you can have full control over the player's camera. By default, players are free to chose between a 1st or 3rd person camera mode while exploring your scene, but you can impose a different camera modality.

Virtual cameras can be static, they can rotate to always look at the player or some other entity, or they can be attached to the player or some other entity so that they're always accompanying.

{{< hint warning >}}
**📔 Note**: To switch between the default 1st and 3rd person cameras, see [Camera modifier areas]({{< ref "/content/creator/sdk7/interactivity/avatar-modifiers.md#camera-modifiers">}}).
{{< /hint >}}

## Using virtual cameras

To use a custom camera behavior in your scene, you need two things:

- Create a Virtual Camera: Create an entity in your scene and give it a `VirtualCamera`.
- Assign that virtual camera: Add a `MainCamera` component to the [reserved entity]({{< ref "/content/creator/sdk7/architecture/entities-components.md#reserved-entities" >}}) `engine.CameraEntity`, with a reference to the entity with the `VirtualCamera` component.

The camera will then be attached to the entity with the `VirtualCamera` component. If the entity moves or rotates, the camera moves with it.

```ts
function main() {
	const myCustomCamera = engine.addEntity()
	Transform.create(myCustomCamera, {
		position: Vector3.create(1, 2, 1),
	})
	VirtualCamera.create(myCustomCamera, {})

	const mainCamera = MainCamera.createOrReplace(engine.CameraEntity, {
		virtualCameraEntity: myCustomCamera,
	})
}
```

In this example, the camera will always be on a fixed position in the scene, as long as the player stays inside the scene bounds. As soon as the player steps outside the scene bounds, the default camera behavior will be restored.

Your scene can include as many entities with a `VirtualCamera`component as you want, and dynamically switch between multiple virtual cameras as the player moves, or as they perform certain actions. Only one virtual camera is active at any given time, this is assigned by the `MainCamera` component on `engine.CameraEntity`.

To revert back to default camera behavior, set the value to `undefined` on `MainCamera.virtualCameraEntity`. The player is then free to switch between 1st and 3rd person cameras. If you want the player to only use one of these two modes, you can use a [Camera modifier areas]({{< ref "/content/creator/sdk7/interactivity/avatar-modifiers.md#camera-modifiers">}}) to force one of the two.

{{< hint warning >}}
**📔 Note**: Camera modifier areas only have an effect on the player if no virtual cameras are active. If the scene is currently using a virtual camera and the player steps into a camera modifier area, nothing happens.

If a 3D model includes a `camera` node as part of its contents, this can't be used by the SDK. You must create all cameras as entities with the SDK.
{{< /hint >}}

```ts
function main() {
	// custom virtual camera
	const myCustomCamera = engine.addEntity()
	Transform.create(myCustomCamera, {
		position: Vector3.create(1, 2, 1),
	})
	VirtualCamera.create(myCustomCamera, {})

	const mainCamera = MainCamera.createOrReplace(engine.CameraEntity, {
		virtualCameraEntity: myCustomCamera,
	})

	// clickable cube
	const clickCube = engine.addEntity()
	Transform.create(clickCube, { position: Vector3.create(8, 0, 8) })
	MeshRenderer.setBox(clickCube)
	MeshCollider.setBox(clickCube)
	pointerEventsSystem.onPointerDown(
		{
			entity: clickCube,
			opts: { button: InputAction.IA_POINTER, hoverText: 'Reset camera' },
		},
		() => {
			// reset camera to default behavior
			const mainCamera = MainCamera.getMutable(engine.CameraEntity)
			mainCamera.virtualCameraEntity = undefined
		}
	)
}
```

## Camera Transitions

Whenever the scene switches between virtual cameras, or between the default camera behavior and virtual cameras, players see a transition. The position, rotation and any other parameters of the virtual camera change smoothly over a period time.

The transition settings on a virtual camera determine how you transition _into_ that camera, from any other camera in the scene, including the default. They don't affect how you transition _out_ of that camera.

```ts
VirtualCamera.create(myCustomCamera1, {
	defaultTransition: { transitionMode: VirtualCamera.Transition.Time(6) },
})
```

{{< hint info >}}
**💡 Tip**: To avoid having a transition, and switch instantly to a camera, set the transition time or speed to 0.
{{< /hint >}}

Depending on your use case, you may prefer to set the speed of the transition instead of the duration:

- **Fixed Time**: You set the duration of the transition, the camera will move as fast as it needs to complete the path in that period of time.
- **Fixed Speed**: You set how fast you want the virtual camera to move during the transition, the duration will depend on the distance. The value used for speed is interpreted as **meters per second**.

Below are examples for both these transition modes:

```ts
// fixed duration
VirtualCamera.create(myCustomCamera1, {
	defaultTransition: { transitionMode: VirtualCamera.Transition.Time(6) },
})

// fixed speed
VirtualCamera.create(myCustomCamera1, {
	defaultTransition: { transitionMode: VirtualCamera.Transition.Speed(3) },
})
```

Below is a full example with two virtual cameras, and transitions between them:

```ts
function main() {
	// custom virtual camera 1
	const myCustomCamera1 = engine.addEntity()
	Transform.create(myCustomCamera1, {
		position: Vector3.create(1, 2, 1),
	})
	VirtualCamera.create(myCustomCamera1, {
		defaultTransition: { transitionMode: VirtualCamera.Transition.Time(1) },
	})

	// custom virtual camera 2
	const myCustomCamera2 = engine.addEntity()
	Transform.create(myCustomCamera2, {
		position: Vector3.create(1, 2, 1),
	})
	VirtualCamera.create(myCustomCamera2, {
		defaultTransition: { transitionMode: VirtualCamera.Transition.Time(3) },
	})

	const mainCamera = MainCamera.createOrReplace(engine.CameraEntity, {
		virtualCameraEntity: myCustomCamera,
	})

	// clickable cube
	const clickCube = engine.addEntity()
	Transform.create(clickCube, { position: Vector3.create(8, 0, 8) })
	MeshRenderer.setBox(clickCube)
	MeshCollider.setBox(clickCube)
	pointerEventsSystem.onPointerDown(
		{
			entity: clickCube,
			opts: { button: InputAction.IA_POINTER, hoverText: 'Reset camera' },
		},
		() => {
			// reset camera to default behavior
			const mainCamera = MainCamera.getMutable(engine.CameraEntity)
			mainCamera.virtualCameraEntity =
				mainCamera.virtualCameraEntity == myCustomCamera1
					? myCustomCamera2
					: myCustomCamera1
		}
	)
}
```

Transitions always move in a straight line, without considering any obstacles in the path. You could instead create a transition manually by using another virtual camera as an intermediary, that way you'd have full control over its movements. This intermediary virtual camera could perform a [Tween]({{< ref "/content/creator/sdk7/3d-essentials/move-entities.md#move-between-two-points" >}}) from the position of the first camera to the position of the second camera, or follow a more custom path that avoids obstacles or takes a cinematic detour.

## Camera following

You can configure a virtual camera so that it always faces the direction of the player, or some specific entity in the scene. The camera's position will remain static, but its rotation will change to always keep this entity centered.

This can be achieved with the `lookAtEntity` property in the `VirtualCamera` component. To follow the player, use the [reserved entity]({{< ref "/content/creator/sdk7/architecture/entities-components.md#reserved-entities" >}}) `engine.PlayerEntity`.

```ts
const myCustomCamera1 = engine.addEntity()
Transform.create(myCustomCamera1, {
	position: Vector3.create(1, 2, 1),
})
VirtualCamera.create(myCustomCamera1, {
	lookAtEntity: engine.PlayerEntity,
})
```

If an entity is being followed by the camera, this will only change the rotation, not the position of the camera.

As the camera rotates, the Transform of the entity with the `VirtualCamera` component does not change. However, you can read the camera's rotation from the Transform on `engine.CameraEntity`. The rotation and position of this entity will be absolute, it won't be conditioned by that of the entity with the `VirtualCamera` component. The rotation of this transform is affected as by the `lookAtEntity` behavior.

{{< hint warning >}}
**📔 Note**: If you configure the virtual camera with a `lookAtEntity` that references the same entity that holds the virtual camera, or the `engine.MainCamera` entity, the resulting behavior will be the same as not assigning any entity at all.
{{< /hint >}}

## Attach to the player

Another use of the virtual camera is to follow the player from a custom distance or angle, by attaching a virtual camera to the player entity. Note that the player can't change the camera's rotation freely, so in this case the camera's rotation will be fixed to that of the virtual camera. This could be useful for example for race games, where the player is expected to always look forward.

```ts
function main() {
	const myCustomCamera = engine.addEntity()
	Transform.create(myCustomCamera, {
		position: Vector3.create(0, 1, 5),
		parent: engine.PlayerEntity,
	})
	VirtualCamera.create(myCustomCamera, {
		defaultTransition: { transitionMode: VirtualCamera.Transition.Time(2) },
	})

	const mainCamera = MainCamera.createOrReplace(engine.CameraEntity, {
		virtualCameraEntity: myCustomCamera,
	})
}
```
