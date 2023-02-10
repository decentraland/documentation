---
title: "Basic Components"
sidebartitle: "Basic Components"
url: "/contributor/runtime/components"
weight: 6
---

The World Explorer supports a list of basic components that share their definition with scenes, providing built-in support for positioning, animation, media, world state queries

There are five types of components:

1. [Object components](#object) add visual and physical properties to Entities.
2. [Game components](#game) can request actions and receive information from the game engine.
3. [Media components](#media) can display images and play sounds.
3. [Area components](#area) alter the behavior of Entities in specific zones.
4. [UI components](#ui) allow scenes to render floating interfaces.

Except for [`Transform`](#Transform), which is specified in detail below, the state of all components is serialized using protocol buffers. You can follow the link in each title to see the complete definition.


## Object Components {#object}

The most common components are those that attach visual and pyhisical properties to an Entity. They can be used to position, resize, paint and add collision to in-game objects.


---
###### `Transform` {#Transform}

Adds position, rotation and scale to an entity.

This component is, by a wide margin, the most commonly used and frequently updated during the lifespan of a scene. Because of this, `Transform` is not serialized using protocol buffers, and is instead packed into a custom structure.

`Transform` has a size of `44` bytes, with this exact layout:

```goat
.-----------------------.-------------------------------.-----------------------.-----------------.
|   x   |   y   |   z   |   x   |   y   |   z   |   w   |   x   |   y   |   z   | parent (uint32) |
'-----------------------'-------------------------------'-----------------------'-----------------'
╵  position (3x float)  ╵      rotation (4x float)      ╵   scale (3x float)    ╵          
```

This approach allows the runtime (especially in low-level code environments) to avoid intermediate serialization and deserialization steps. The memory where a `Transform` resides can be copied, shared and directly pointed to.

Coordinates can be fractionary, and thus use a 4-byte floating point number.

The `parent` field indicates that this Entity should be positioned relative to another one, identified by their ID. 

Since the null-value for `parent` is also the [`RootEntity`]({{< ref "/contributor/runtime/entities#RootEntity" >}}) ID (`0`), any `Transform` is relative to it by default.


---
###### `MeshRenderer` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/mesh_renderer.proto#L7)</small> {#MeshRenderer}

Provides basic rendering behavior for an Entity.

It can be set to render a plane, a sphere, a cube or cylinder.

Entities with a [`GltfContainer`](#GltfContainer) are rendered according to the referenced model, and ignore this component.


---
###### `MeshCollider` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/mesh_collider.proto#L15)</small> {#MeshCollider}

Provides basic collision behavior and mouse pointer detection for an Entity.

It can be set to behave like a plane, a sphere, a cube or cylinder.

Entities with a [`GltfContainer`](#GltfContainer) detect collisions according to meshes defined in the 3D model, and ignore this component.


---
###### `Material` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/material.proto#L19)</small> {#Material}

Sets the texture, lighting, color and transparency properties of an Entity that also has the [`MeshRenderer`](#MeshRenderer) component.

It's a complex structure, but all fields have default values that can be left as they are, in order to only change a subset of the properties.

Entities with a [`GltfContainer`](#GltfContainer) are rendered according to the referenced model, and ignore this component.


---
###### `GltfContainer` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/gltf_container.proto#L7)</small> {#GltfContainer}

Attaches a 3D model to this Entity, given the [file path]({{< ref "/contributor/content/entities#files" >}}) of a `.gltf` asset in the scene's manifest.

Since the model has its own meshes and materials, this component overrides any behavior from [`MeshRenderer`](#MeshRenderer), [`MeshCollider`](#MeshCollider) and [`Material`](#Material).


---
###### `Billboard` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/billboard.proto#L17)</small> {#Billboard}

Makes an Entity automatically reorient its `Transform` to face the camera. As the name indicates, it's used to display in-game billboards and frequently combined with [`TextShape`](#TextShape).

It affects all directions by default, but can be set to only rotate in one axis.


---
###### `Animator` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/animator.proto#L7)</small> {#Animator}

Defines one or more animations that can be applied simultaneously to an entity.

Scenes can set the component state to customize, play and transition between animations, as well as read it to check which animations are available or currently being played.


---
###### `AvatarAttach` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/avatar_attach.proto#L16)</small> {#AvatarAttach}

Indicates that an Entity's position must follow a particular anchor point in an avatar's body.

It can affect any avatar, not only the player's, by setting a user ID.


---
###### `TextShape` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/text_shape.proto#L11)</small> {#TextShape}

Renders text on an Entity's position, given by its `Transform`.

It's highly configurable, supporting parameters like size, margin, padding, color, shadow and more.


---
###### `Visibility` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/visibility_component.proto#L7)</small> {#Visibility}

Sets whether an Entity is visible (the default) or invisible.

Invisible objects still exist, and will exhibit behavior from any other attached components.


---
###### `AvatarShape` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/avatar_shape.proto#L8)</small> {#AvatarShape}

Contains information about the player's avatar, including their body shape, colors, wearables and transitory state.

This component is attached to entities in the [avatar scene]({{< relref "execution#avatarScene" >}}).


## Game Components {#game}

Some basic components can be used by the scene and the runtime to exchange information. They leverage the [ECS synchronization mechanism]({{< relref "modules/engine_api#synchronization" >}}) to guarantee consistency and ordering for any state changes or events.


---
###### `CameraMode` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/camera_mode.proto#L8)</small> {#CameraMode}

Can be used to determine whether the player has a first-person o third-person view.


---
###### `PointerLock` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/pointer_lock.proto#L7)</small> {#PointerLock}

Can be used to determine whether the mouse pointer is automatically following the camera's point of focus (locked), or can move freely on the screen (unlocked).

It's attached to the [`CameraEntity`]({{< ref "/contributor/runtime/entities#CameraEntity" >}}), and its state can be read (but not written) from the scene.


---
###### `PointerEvents` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/pointer_events.proto#L17)</small> {#PointerEvents}

Shows visual feedback when the pointer clicks or hovers over an Entity.


---
###### `PointerEventsResult` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/pointer_events_result.proto#L13)</small> {#PointerEventsResult}

Contains information about recent input from the player, including keys and pointer actions.

It's attached to the `RootEntity`, and updated by the runtime with any new events on every frame.


---
###### `Raycast` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/raycast.proto#L15)</small> {#Raycast}

Can be attached to an Entity to request a raycast from the game engine. The `RaycastResult` component will later be attached to the same entity.

The origin, direction and maximum length of the ray can be configured.

---
###### `RaycastResult` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/raycast_result.proto#L9)</small> {#RaycastResult}

Attached by the runtime to Entities that have a [`Raycast`](#Raycast) component pending results.

It contains information about the original ray and identifies any Entities that were hit.


## Media Components {#media}

Scenes can attach special components to display images, show video or play sounds. 

---
###### `AudioSource` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/audio_source.proto#L7)</small> {#AudioSource}

Plays an audio clip bundled with the scene, given the [file's path in its manifest]({{< ref "/contributor/content/entities#files" >}}).

The sound originates from the associated entity's position. Its pitch, volume and looping behavior can be set, and the state of the audio player can be read.

{{< info >}}
In preparation for future upgrades, the field in `AudioSource` is called `audio_clip_url`, but in the current protocol version it's actually the manifest-defined path.
{{< /info >}}


---
###### `AudioStream` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/audio_stream.proto#L7)</small> {#AudioStream}

Similar to [AudioSource](#AudioSource), but the audio is streamed in real time from an external URL.

Despite being attached to a particular entity, the sound is not affected by its position. Its volume can be set, and the state of the audio player can be read.


---
###### `NftShape` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/nft_shape.proto#L36)</small> {#NftShape}

Displays an NFT associated to an image or video asset.

It renders a 2D canvas with a configurable decorative frame.


## Area Components

These components allow scenes to modify the default behavior of Entities within specified bounds.

---
###### `AvatarModifierArea` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/avatar_modifier_area.proto#L15)</small> {#AvatarModifierArea}


Changes the behavior of avatars within a space centered around an Entity.

It's defined with a 3D size vector, and can affect whether avatars are visible or clickable. Specific avatars can be excluded from this effect given their user's ID.


---
###### `CameraModeArea` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/camera_mode_area.proto#L11)</small> {#CameraModeArea}

Changes the camera mode (1st-person or 3rd-person) within a space centered around an Entity.

It's defined with a 3D size vector and a desired camera mode.


## UI Components {#ui}

The following components are used to create graphical interfaces that hover on top of the game world.

They are usually attached to sets of Entities that have hierarchical [`UiTransform`](#UiTransform) components, related to one another via the `parent` attribute.

For example, a floating options window could be an Entity with a [`UiTransform`](#UiTransform) and a [`UiBackground`](#UiBackground) component, plus a Entity with a child [`UiTransform`](#UiTransform) and a [`UiDropdown`](#UiDropdown).


---
###### `UiTransform` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/ui_transform.proto#L77)</small> {#UiTransform}

Describes the size, positioning, margin and padding of a UI component.

It's based on the flexbox model and highly customizable.


---
###### `UiBackground` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/ui_background.proto#L11)</small> {#UiBackground}

Describes a color or texture to use as background in a UI Entity.


---
###### `UiDropdown` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/ui_dropdown.proto#L11)</small> {#UiDropdown}

Defines a list of mutually exclusive options to be displayed in a dropdown widget.


---
###### `UiDropdownResult` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/ui_dropdown_result.proto#L9)</small> {#UiDropdownResult}

Contains the selected value from a [`UiDropdown`](#UiDropdown), set by the runtime and read by the scene.


---
###### `UiInput` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/ui_input.proto#L11)</small> {#UiInput}

Defines a text input widget, with some margin for customization.


---
###### `UiInputResult` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/ui_input_result.proto#L9)</small> {#UiInputResult}

Contains the text value of a [`UiInput`](#UiInput), set by the runtime and read by the scene.


---
###### `UiText` <small>[↗ source](https://github.com/decentraland/protocol/blob/ccb88d679f20c0e22840c324879d7b2535f6c9a6/proto/decentraland/sdk/components/ui_text.proto#L11)</small> {#UiText}

Defines a simple text view, with some margin for customization.


---