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

- **Transform**: Sets the position, rotation, and scale of the item. If the item is a child of another item on the [Entity Tree]({{< ref "/content/creator/scene-editor/scene-editor-essentials.md#the-entity-tree" >}}), these value are relative to those of the parent's.
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

{{< hint warning >}}
**📔 Note**: Other components exist on the SDK that are currently only usable via code. You can also create your own [Custom components]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}) via code, these won't have a UI representation, but can be added and edited via code.

See [Combine with code]({{< ref "/content/creator/scene-editor/smart-items/combine-with-code.md" >}}) for how to edit the code of your scene.
{{< /hint >}}

## Smart items

[Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) can also include special components that control the item's interactivity. These are typically:

- **Actions**: Lists all the possible actions the item can carry out.
- **Triggers**: Determines when the actions from the Actions component are carried out.
- **States**: Keeps track of the item's current state. The state can be used for conditional logic, to only trigger certain actions if the item is on certain state.
- **Counter**: Keeps track of a counter. The counter can be used for conditional logic, to only trigger certain actions if the counter's value is equal/greater/lower than a given value.

See [Smart items advanced]({{< ref "/content/creator/scene-editor/smart-items/smart-items-advanced.md" >}}) for more details.

## About components

All the traits of an item are determined by its components. They define what an item is, where it is, how it sounds, and how it behaves. For example, a **Transform** component stores the item's coordinates, rotation and scale. A **MeshRenderer** component gives the item a visible shape (like a cube or a sphere), and a **Material** component gives the item a color or texture.

The values on components can change over time. In the Scene Editor you configure the initial values for these components. But once your scene is running, the player's actions or the passage of time can change those values.

For example, a moving platform Smart Item has an initial position that you set via its **Transform** component, but after the actions of this item make it move, its **Transform** will hold different values.

See [Entities and components]({{< ref "/content/creator/sdk7/architecture/entities-components.md" >}}) for an in-depth look at this concept and how they're used by Decentraland scenes.

{{< hint info >}}
**💡 Tip**: An **Entity** can be thought of as just another word for an **Item**, they are a more code-level concept. Items must have at least a position and a visible shape, an Entity doesn't need to have either.
{{< /hint >}}
