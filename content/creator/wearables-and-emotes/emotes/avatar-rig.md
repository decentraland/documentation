---
date: 2022-09-01
title: Avatar rig
description: Basics about the avatar rig.
categories:
  - emotes
type: Document
aliases:
  - /emotes/avatar-rig
url: /creator/emotes/avatar-rig
weight: 3
---


202A rig is a virtual skeleton that allows a model to move. It consists of a hierarchy of individual bones, much like a real life skeleton, and it works under a parent/child relationship.  This document will cover some basic rigging concepts, such as bone position, bone orientation, deforming and non-deforming bones, the difference between IK and FK and their purposes. The structure of an avatar’s rig, custom attributes, and setup for animating can be found in [rig features]({{< ref "/content/creator/wearables-and-emotes/emotes/rig-features.md" >}}).

# The Basics

### Bone Position or Pivot Points

Even though a rig is not an exact replica of the human skeleton, it is good practice to follow the position of real life bones when placing digital ones. This is done in order to guarantee believable and fluid deformation. Bone position is important because it sets the pivot point (where the movement will start from). A misplaced bone will cause bad deformation of the mesh. The images below show the difference in bone position.

![head_pivot_rig_1.0.gif](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/head_pivot_rig_1.0.gif)

![head_pivot_rig_2.0.gif](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/head_pivot_rig_2.0.gif)

### Bone Orientation

The orientation of bones will define in which direction they’ll rotate, like positive X, negative Z, etc. They can be set up in many different ways as long as it’s consistent through the whole rig. For example, if the X axis is chosen for the bending forward motion of the spine, it makes sense that the same set up is used for the legs. The orientation is also important because it’ll affect mirroring behavior. That means that, usually, the right side orientation is the mirrored version of the left side’s and vice versa.

![Turn on the axes to show bone orientation.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/bone_axis.gif)

_Turn on the axes to show bone orientation._

![The axes are the directions in which the bone will rotate.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/bone_orientation.gif)

_The axes are the directions in which the bone will rotate._

### Deforming and Non-deforming Bones

Deforming bones are the ones that will deform the mesh, they are responsible for the way the model moves. That’s the base skeleton and it **should not be edited at all**. Changing it in any way can break the rig and the animation won’t work when exported. For this reason, this base rig was moved to its own layer (the last one at the bottom). These bones are the armature that’s exported with the mesh.

Non-deforming bones are the ones that won’t deform the mesh, but they are still necessary in a robust rig and are used for the setup for [IKs, FKs](#what’s-FK-and-IK-in-a-rig) and other custom properties. Examples for non-deforming bones are controls, IK and FK bones, foot setup bones. These shouldn’t be exported, they are only used for animation purposes.

![Deforming bones.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/deforming_bones.png)

_Deforming bones._

![Non-deforming bones.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/non_deforming_bones.png)

_Non-deforming bones._

> **Warning**: **Do not edit the base skeleton at all!**

![The base skeleton.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/deforming.png)

_The base skeleton._

### Controls

As a good practice, a rig shouldn’t be animated by manipulating the deforming bones because it might cause the rig to break. Instead, **animations should be done by manipulating controls.**

Controls are basically non-deforming bones, which means they will not affect the mesh, making them completely safe to be manipulated and animated. Their function is to control the base skeleton through constraints and drivers, without directly touching it. They usually have different shapes and colors as a visual cue for their functions and purposes, making it easier for the animator to tell bones apart. Some of them will also have more than just location, rotation, and scale transforms because it’s possible to add custom properties to them, such as an IK/FK switch.

It’s also important to notice that it’s not possible to use the controls setup in a software different from the one it was originally done in. Each software has its own logic and it’s not possible to export constraints.

![Controls and their different shapes and colors.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/controls.png)

_Controls and their different shapes and colors._

> **Warning**: **The rig has to be animated in the same software it was created in. It’s not possible to use a Blender setup in, for example, Maya and vice versa.**


### What’s FK and IK in a rig?

A rig can use two different setups that will influence how it moves: FK and IK.

### FK - Forward Kinematics

In the forward kinematics, or FK, the parent in the hierarchy moves all the child bones under it. Let’s take the arm as an example: when the shoulder rotates, the rest of the arm will rotate as well; when the arm rotates, the forearm will follow its behavior. When animating in FK, each bone has to be rotated individually. This setup gives a lot of control over the movement and is great for arc motions, which are essential for a fluid animation.

![Direction of movement in the hierarchy.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/FK.png)

_Direction of movement in the hierarchy._

![In FK, each bone has to be rotated individually.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/FK.gif)

_In FK, each bone has to be rotated individually._

### IK - Inverse Kinematics

In inverse kinematics, or IK, the child in the hierarchy can influence the movement of its parents. In this case, taking the arm as an example again, when the hand is moved around, the rest of the arm will follow the motion. It also means that no matter how the shoulder moves, the hand will maintain its position. In this setup, a pole vector/pole target will control in which direction the bones will bend. Legs are usually in IK and that’s essential for the feet to stick to ground level while animating.

![Direction of movement in hierarchy.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/IK.png)

_Direction of movement in hierarchy._

![In IK, the hand will move all the arm and also maintain it’s position. The pole target drives the direction in which the elbow bends.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/IK.gif)

_In IK, the hand will move all the arm and also maintain it’s position. The pole target drives the direction in which the elbow bends._
