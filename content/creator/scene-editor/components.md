---
date: 2024-08-20
title: Components
description: Understand how an item's components work
categories:
  - scene-editor
type: Document
url: /creator/editor/components
weight: 7
---

Select an item by clicking on it on the canvas or the entity tree. You'll then see its components displayed on the properties panel, on the right of the screen. Different items have different components that each display specific settings.

<img src="/images/editor/components-in-editor.png" alt="Scene name" width="200"/>

Most non-interactive items have the following components:

- **Transform**: Sets the position, rotation, and scale of the item. If the item has a parent, these value are relative to the parent's.
- **GLTF**: What 3D model to load. It includes the local path to the file for this 3D model. It also includes some properties for configuring [colliders]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#colliders-on-3d-models" >}}) on the model.

## Add components

To add components to an item, click the **+** sign at the top of the properties tab and select the component from the list. See [Make any item smart]({{< ref "/content/creator/scene-editor/smart-items/make-any-item-smart.md" >}})

<img src="/images/editor/add-component.png" alt="Scene name" width="200"/>

You can delete any component from an item by clicking the three dots icon on its right, and selecting **Delete Component**.

## Available components

The following components can be added to any entity via the Scene Editor UI:

- **Mesh Renderer**: Gives the item a visible shape based on a primitive shape (cube, plane, cylinder, cone, or sphere).
- **Mesh Collider**: Gives the item an invisible collider geometry. This can block the player from walking through the item, and/or can make it clickable. See [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}).
- **Material**: Defines the color, texture, and other properties of an item that has a **Mesh Renderer** component. See [materials]({{< ref "/content/creator/sdk7/3d-essentials/materials.md" >}}).
  {{< hint warning >}}
  **📔 Note**: The item Must have a **Mesh Renderer** component. It doesn't affect items with a **GLTF** visible shape.
  {{< /hint >}}

- **Visibility**: Defines if an item is invisible.

- **Audio Source**: Plays a sound from a sound file at the location of the item. See [Sounds]({{< ref "/content/creator/sdk7/3d-essentials/sounds.md" >}}).
- **Text Shape**: Displays text in the 3D space. See [Text]({{< ref "/content/creator/sdk7/3d-essentials/text.md" >}}).
- **Pointer Events**: Marks an item as clickable, displaying a hover-hint.
  {{< hint warning >}}
  **📔 Note**: The **Pointer Events** component only provides feedback. To perform actions when an item is interacted with, see [Make any item smart]({{< ref "/content/creator/scene-editor/smart-items/make-any-item-smart.md" >}})
  {{< /hint >}}

- **Multiplayer**: Shares any changes that happen to the item so that all players in the scene see it too. It can be configured to only share changes on certain components. See [Serverless Multiplayer]({{< ref "/content/creator/sdk7/networking/serverless-multiplayer.md#mark-an-entity-as-synced" >}}) for more details.

## Smart items

[Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) can also include special components that control the item's interactivity. These are typically:

- **Actions**: Lists all the possible actions the item can carry out.
- **Triggers**: Determines when the actions from the Actions component are carried out.
- **States**: Keeps track of the item's current state. The state can be used for conditional logic, to only trigger certain actions if the item is on certain state.
- **Counter**: Keeps track of a counter. The counter can be used for conditional logic, to only trigger certain actions if the counter's value is equal/greater/lower than a given value.

See [Smart items advanced]({{< ref "/content/creator/scene-editor/smart-items/smart-items-advanced.md" >}}) for more details.

<!-- TODO:

## About components

All the attributes of an item are determined by its components. They define what an item is, where it is, how it sounds, how it behaves.

In the Scene Editor, you configure the initial state of the scene. Any visible change in your scene will imply a change in a component. As the player performs actions or as the scene's systems (link) carry out their updates, the initial values you set on the components will change.

For example, a moving platform may have an initial position of X, but if you were to read its Transform after a second of starting the scene, it will have different values.

Link to doc on components

You can also define custom components via code, but those currently can't be added via the Scene Editor UI

light theory and link to architecture docs
custom components not available
they define the initial state, systems or player's actions can then change their values
 -->
