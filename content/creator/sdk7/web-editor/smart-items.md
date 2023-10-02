---
date: 2023-09-19
title: Smart Items
description: Using smart items in your scene to add interactivity.
categories:
  - web-editor
type: Document
url: /creator/smart-items
weight: 2
---

Some of the items in the catalog of the Decentraland Editor are **Smart Items**. These can be interacted with, have configurable properties, or can trigger actions on other smart items. For example, you can find doors that can be opened and closed, platforms that move up and down, or buttons and levers that can activate other items when interacted with.

You can recognize these items because they have a lightning icon and a different colored background
<screenshot>

## Using items

To use a smart item, simply drag it into your scene like any other item. Then run a preview of your scene to interact with the item.

You can also configure smart items to behave in custom ways. Change what button triggers them, the hover-hint text, change what sounds they play when an action is called, the animations they play, etc.

You can also make the triggering of one smart item cause an action on another smart item. For example clicking on a button can open a door, or move a platform. Any smart item can interact with any other smart item.

Note that when selecting a smart item, you'll see several more configurable fields on the right panel than with other items. These fields are typically grouped in the components **Action**, **Trigger**, and sometimes **States**, depending on the item.

The **Action** component lists all of the possible actions the item can perform. The **Trigger** component controls when these actions are carried out.

For example, in a door smart item, the Action component includes "open" and "close" actions. The Trigger component of the same door includes an "on_click" trigger that references the "open" action.

The Trigger component of a smart item can call actions on that same item, or also on any other smart item in the scene. For example, a button smart item can hold a Trigger component that references the "open" action on a door.

Triggers can also happen conditionally. To build upon the prior example, the button smart item could include two triggers in its Trigger component: one that opens the door if it was closed, another that closes the door if it was open. For more details see [States and conditional logic](#states-and-conditional-logic).

## Actions

The **Action** component lists actions the the item is able to carry out. These can include:

- playing an animation
- playing a sound
- performing a tween (move, rotate or change scale gradually)
- changing state

The Action component lists possible actions, to perform one of these actions, it needs to be activated by a [trigger](#triggers).

## Triggers

The **Trigger** component lists triggers, that can activate actions on this or other smart items. The following types of triggers exist:

- When the player clicks on the item
- When the item changes state
- When the scene starts running

## States and conditional logic

You can use conditional logic on a trigger, so that a trigger only occurs if certain conditions are met. For example, clicking on a door only opens it if it wasn't already open.

The **States** component lists possible states that the smart item can be in. At any given time, the smart item is in one of these states. For example, a door can be _open_ or _closed_. This state can change as a result of triggers affecting it. The resulting state can then be checked in the conditional logic of another trigger.

To toggle between two or more actions, you can define two triggers, each with a condition. For example, doors are triggered

A single trigger can include multiple conditions. These conditions can either all be AND or OR. If conditions are AND, they all have to be true. If conditions are OR, it's only necessary for one of them to be true.

on_state_change trigger
For example, to make a button open a door, you could make the button directly call the door's play animation action, its play sound action, and its change state. A better practice is to make the button just call the door's change state action, and have the door use its own on_state_change to call the play_animation and play_sound actions.

### Counter

on_counter_change

## Trigger on spawn

The on_spawn trigger activates an action as soon as the smart item spawns in the scene. Instead of waiting for the player to interact with it, it performs its action right away.

This is useful for example to have a platform continually moving. Give it an on_spawn trigger to make it perform a tween, then also

## Making any item smart

Smart items are just regular items with an Action and/or Trigger component. You can add these components to any item in your scene. You can also import your own custom 3D models and add the same to those.

This allows for a huge amount of creative possibilities. Turn a candle into a lever that opens up a secret passage behind a book shelf, play mysterious sounds from inside a well, make diamonds into collectable items that shrink to 0 when clicked and increase a counter for each diamond collected. There are tons of imaginative ways to combine these mechanics!

Tip: When interacting with an item, most of the time you want to show some kind of feedback. If the model doesn't have any animations, consider at least playing a sound. On some items it might also look good if the item performs a slight tween in scale or position and returns to its original, as a form of feedback.

### About Playing Animations

The play animation action runs an animation on the 3D model of the smart item once. This animation needs to already exist as part of the 3D model file. The **Select Animation** dropdown reads the metadata of the 3D model and displays a list of all of the available animations in that 3D mode.

To learn more about animations, see [Animations]({{< ref "/content/creator/3d-modeling/animations.md" >}}).

### About Playing sounds

To play a sound...

Import file

Link to play sounds

### About tweens

a tween transitions from its original position / scale / rotation to an ending one

the ending position or rotation can either be relative or absolute

on finish

combine with state to follow a repeating path

### About click triggers

Need to have colliders
Click distance
Button
Hover text
