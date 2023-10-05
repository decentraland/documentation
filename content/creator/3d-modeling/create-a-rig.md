---
date: 2023-10-3
title: Create a Rig
description: Learn How To Create a Rig for Characters in Decentraland.

categories:
  - 3d-modeling
type: Document
aliases:
  - /3d-modeling/create-a-rig/
url:
  - /creator/3d-modeling/create-a-rig
weight: 7
---

This document shows how to set up a basic rig in Blender. If you want to get more familiar with some rigging concepts, check out [The Rig: Basic Concepts](https://docs.decentraland.org/creator/emotes/avatar-rig/).

## **Adding the Armature**

First of all, you’ll need to import your 3D model into Blender or, if you did it in Blender already, just open your blend file. In object mode, press `Shift+A` and select **_Armature_** on the menu, like show below. Then, in **_Object Data Properties_**, under **_Viewport Display_**, toggle **_In Front_**, so you can see the bone through the mesh. Mesh and armature should be aligned, so make sure the model is well positioned in the center of the world before adding the bones. The origin of the armature should be at 0,0,0 (X,Y,Z).

<img src="/images/3d-models-and-animations/create-rig/01_add_armature.gif" width="900" />

_Adding an armature and showing it through the mesh._

## **Editing the Armature**

After adding the Armature object, select it and go to **_Edit Mode_**. Here is where you add the other bones by extruding the original one (press `E`), duplicating it (`Shift+D`) or simply adding a new one with `Shift+A`. The skeleton should follow the shape of the model, like a real skeleton. Bones can be scaled, grabbed and rotated and they have two parts: the head and the tail. The head is the pivot point, which means that rotations and scale will start from there. That also means that it’s where the mesh deformation will happen, so position the bones as centered in the mesh as possible.

<img src="/images/3d-models-and-animations/create-rig/02_bone_head_tail.png" width="400" />

_Bone structure._

<img src="/images/3d-models-and-animations/create-rig/03_bone_pivot_rotation.gif" width="400" />

_Bone rotating from its pivot point._

There’s no need to worry about creating bones for the right and left side for now. Focus on creating only one side first.

## **Renaming the Bones**

Something really important to keep in mind is renaming all your bones properly, according to [Blender’s naming convention](https://docs.blender.org/manual/en/latest/animation/armatures/bones/editing/naming.html). This will not only keep everything organized, but also make it possible to mirror poses and weight paint. You could just rename it as the body part it represents, like Spine_01 or your could be more specific and call it DEF_spine.001 (DEF stands for deforming bone, so you kow that this bone is from the deforming hierarchy).

## **Bone Orientation**

Before moving on, you should check your bone orientation. You can do that by going to **_Object Data Properties_** and under **_Viewport Display_**, toggle **_Axes_**. This will make the bones’s axes visible, so you can check if they are going to rotate in the proper direction.

The axes should be aligned with the direction in which you want the bones to rotate. If it feels a little off, select the bone and, in the **_Item Transform_** menu on the right of the viewport, adjust the **_Roll_** until the orientation feels right.

<img src="/images/3d-models-and-animations/create-rig/04_bone_roll.gif" width="400" />

_Fixing the bone roll._

<img src="/images/3d-models-and-animations/create-rig/05_toggle_axes.png" width="400" />

_Toggle Axes on so you can see the direction in which the bone will rotate._

Fixing the bone roll is especially important for fingers, so all the joints bend in the same proper direction. You don’t have to do it for all the bones in a finger though, just get one of them right. Then, select the ones you want to fix first and the one with the proper roll last, go to **_Armature > Bone Roll > Recalculate Roll > Active Bone_** and they will all have the same roll. Or you can just press `Shift+N` > **_Active Bone_**. This can be used in many situations where you have a long chain of bones, like a tentacle, a tail, a long pony tail or a mechanical arm.

<img src="/images/3d-models-and-animations/create-rig/06_bone_roll_fingers.gif" width="400" />

_Press `Shift+N` to recalculate the bone roll._

## **Mirroring the Rig**

You don’t have to create bones for both sides. Just do one side first and when you’ve fixed all the naming and bone orientation, select all the bones you want to mirror, click with the right mouse button and select **_Symmetrize_**. That way all the bones will be mirrored properly, with the right orientations.

<img src="/images/3d-models-and-animations/create-rig/07_symmetrize.gif" width="600" />

_Use the Symmetrize option to mirror your bones._

{{< hint info >}}
**⚠️ Attention!**
Symmetrize will only work if the bones are renamed properly. If it doesn’t mirror properly you might want to double check the bones’s names.
{{< /hint >}}

## **Skinning**

Skinning is the process of binding the mesh to the armature. To do so, in **_Object Mode_**, select the mesh, then the armature and press `CTRL+P` > **_Armature Deform > With Automatic Weights._** Then, go to **_Pose Mode_** and test different poses to test the mesh deformation. Most of the time it will need some adjustments, as seen below.

<img src="/images/3d-models-and-animations/create-rig/08_skinning.gif" width="600" />

_For the Skinning, make the mesh child of the armature by pressing `CTRL+P` and test it in Pose Mode._

If you feel like a bone has been misplaced or that the pivot point is not accurate, you can always go back to the armature’s **_Edit Mode_** and adjust it. This won’t affect the skinning at all and you can always use **_Symmetrize_** to mirror the changes.

To fix weird deformations, go to **_Object Mode_**, select the mesh and go to **_Weight Paint_**. In **_Object Data Properties_** you will find the **_Vertex Groups_**.

<img src="/images/3d-models-and-animations/create-rig/09_weight_paint.gif" width="900" />

_Edit a bone’s influence in Weight Paint._

Before you start editing, to have you weight paint automatically mirrored as you paint, toggle **_Mirror Vertex Groups_** and select **_X_** in **_Mirror_** under **_Symmetry_** (in Blender 3.4.0) To edit the influences, select the vertex group one you want and, in the **_Tool_** menu, under **_Blend_**, switch between **_Add_** and **_Subtract_** according to your needs. You can also change the size, weight and strength of the brush.

<img src="/images/3d-models-and-animations/create-rig/10_weight_paint_tools.png" width="600" />

_Change the Blend to add or remove influence. Make sure Symmetry is right._

<img src="/images/3d-models-and-animations/create-rig/11_weight_paint_tools_02.png" width="400" />

Use the **_Blur_** tool ont the left side of the screen to smooth the weight paint and make it more even.

<img src="/images/3d-models-and-animations/create-rig/12_blur_tool.gif" width="600" />

_Blur Tool._

## **Setting Up the IK**

IK is essential when you want something to stay in place. The best example of its use is on legs, but it can be adopted in a variety of situations, like in the examples below:

<img src="/images/3d-models-and-animations/create-rig/13_IK_example_mch_arm.gif" width="600" />

_IK use in a mechanical arm._

<img src="/images/3d-models-and-animations/create-rig/14_IK_example_buddha.gif" width="600" />

_IK use in cables._

Since it’ll change the hierarchy of bones, it’s best to keep it as a separate setup. So the first thing you need to do is duplicate the bone chain that will be affected by the IK. Let’s use the leg as an example. Select the bones, press `Shift+D` to duplicate them and move them to a different layer by pressing `M` and selecting a different slot for it.

Remeber to rename the duplicated bones, adding IK to the name so you know they are part of the IK setup. And since they shouldn’t deform the mesh, select all them and in **_Bone Property_**, press and hold `Alt` and uncheck **_Deform_**.

<img src="/images/3d-models-and-animations/create-rig/15_Duplicating_bones.gif" width="600" />

_Duplicate the bones and move them to a different layer._

<img src="/images/3d-models-and-animations/create-rig/16_uncheck_deform.png" width="400" />

_Select all the IK bones and, while holding `Alt`, uncheck Deform._

Next, you’ll need to create a bone that’ll drive the IK chain. Select the head of the foot bone and extrude it on Y. Then, press `Alt+P` to unparent it because the IK bone can’t be part of the chain and can’t be connected to other bones. You’ll need to make the foot a child of the IK, so select the foot bone first and the IK bone last and press `CTRL+P` > **_Keep Offset_**.

<img src="/images/3d-models-and-animations/create-rig/17_IK_bone.gif" width="600" />

_Creating an IK bone._

In **_Pose Mode_**, click on the shin bone, press `CTRL+Shift+C` and select **_Inverse Kinematics_**. It will look all messed up, but don’t worry, it will be fixed once you change a few settings. With the shin selected, got to the **_Bone Constraint Properties_** as shown below.

<img src="/images/3d-models-and-animations/create-rig/18_constraint_tab.png" width="400" />

_In Bone Constraint Properties you can edit the IK settings._

For the **_Target_**, select **_Armature_**. Once you do that, an option called **_Bone_** will appear under Target. For that, select the IK bone you created. In **_Chain Length_** you will set the number of bones that should be affected by the IK. Since we are doing a leg, we want it to affect the shin and the thigh, so set it to **_2_**.

## **Pole Target**

The Pole Target lets you control the direction in which the bones will bend. These are the steps to properly add a pole target (or pole vector) to the IK chain:

- In **_Edit Mode_**, duplicate the thigh bone and place it anywhere.
- Select the knee joint (or the tail of the thigh bone), press `Shift+S` > **_Cursor to Selected._**
- Selected the duplicated thigh bone, press `Shift+S` > **_Selection to Cursor_**.
- In **_Transform Orientation_**, change it to **_Normal_** and in **_Tansform Pivot Point_** change it to **_Active Element_**.
- Rotate the bone in X -90 (or 90, depending on the orientation you set) so it points forward and grab it in Y until it has a nice position in front of the leg. You can also scale it down a little bit.

<img src="/images/3d-models-and-animations/create-rig/19_creating_pole_target.gif" width="600" />

_Creating a Pole Target._

Back into **_Pose Mode_**, select the shin again and go to the **_Bone Constraint Properties_**. For **_Pole Target_** select **_Armature_** and for **_Bone_**, select the pole target one you just created. If you show the deform bones, you will see that the pole target rotated the IK a little.

<img src="/images/3d-models-and-animations/create-rig/20_pole_target_rotation.png" width="600" />

_IK chain and deform bones are not aligned anymore because of pole target._

<img src="/images/3d-models-and-animations/create-rig/21_pole_target_rotation_fix.png" width="600" />

_The rotation can be fixed by changing the Pole Angle._

That can be easily fixed by changing the **_Pole Angle_**. Usually -90° will do the trick, but you can always adjust it manually to make sure they are perfectly aligned.

Finally, make both the IK bone and the pole target chilld of the root bone by selecting them both, then the root, press `CTRL+P` > **_Keep Offset_**.

Move the thigh and shin to another layer since you won’t need them for animation, they are just part os the IK setup.

## **Binding Deform Bones to Non-Deforming Ones**

The IK chain is all set up, but it should drive the deform bones and right now that’s not happening, but you can use constraints to fix that. In **_Pose Mode_**, select a bone from the IK chain first and the respective deforming bone last, press `CTRL+Shift+C` and select **_Copy Transforms_**. Do that for all the bones, which in the example are thigh, shin, foot and toes. The deform bones will have a green color to them, which means that they have a constraint. If you click on **_Bone Constraint Properties_**, you can see which constraint is being used and what bone is driving it.

<img src="/images/3d-models-and-animations/create-rig/22_constraints.gif" width="600" />

_Green bones have constraints. You can check them in Bone Constraints Properties._

{{< hint info >}}

### 💡Hint!

You don’t have to set up the IK all over again for the other side. In _Edit Mode_, just delete all the bones from the side that doesn’t have the IK, then select all the deforming bones and IK chain that you want to mirror, right click with the mouse and select _Symmetrize_. It will not only mirror the bones, but also all the constraints!
{{< /hint >}}

<img src="/images/3d-models-and-animations/create-rig/23_symmetrize_constraints.gif" width="600" />

_Use the option Symmetrize to mirror constraints too!_

## **Non-deforming Skeleton and Controls**

It’s good practice not to animate directly the deforming bones since you could end up breaking the rig and adding constraints to the deforming armature will affect the hierarchy and bone behaviour when exported.

The solution to this is to create a non-deforming skeleton that will drive the deforming one through constraints, and that can be animated safely, without risking breaking anything. You can also customize their shape to make it easier to identify a bone’s function. They will be the controls for your rig.

The process for this is pretty much the same done for the IK setup. Duplicate all the bones (except the IK setup) with `Shift+D` and move them to a different layer by pressing `M` and picking another slot. Rename them all by adding **Control_** or **CTRL_** as a suffix so you know these are part of the controls hierarchy. Press `A` to select all them and in **_Bone Property_**, press and hold `Alt` and uncheck **_Deform_**.

Now you’ll have to add constraints to bind the two skeletons together. To make this process easier, you can change the bone shape by clicking on **_Object Data Properties_** and, under **_Viewport Display_**, change **_Display As_** from **_Octahedral_** to **_B-Bone_**. Then, press `CTRL+Alt+S` to scale the bones up a little bit so their are bigger than the original ones.

<img src="/images/3d-models-and-animations/create-rig/24_b-bone_scale.gif" width="600" />

_Change the bone shape and scale them up so it’s easier to differentiate between the two skeletons._

For the constraints, select a control bonefirst and the respective deforming bone last, press `CTRL+Shift+C` and select **_Copy Transforms_**. Do that for all the control bones.

You can separate the control bones into different groups and assign colors to them. Go to **_Pose Mode_** > **_Object Data Properties_** > **_Bone Groups_**. Click on the **_+_** icon to add a new group, rename it as you see fit and select a color for it. Then, select the bones you want to be part of that group and click on **_Assign_**. You can create as many groups as you like to keep everything organized. You can also move different bone groups to different layers.

<img src="/images/3d-models-and-animations/create-rig/25_bone_groups.png" width="600" />

_Bone groups will help you keep your rig organized and more intuitive._

An extra way to improve your rig is to customize the shape of the bones. To do that, go to **_Object Mode_**, press `Shift+A` to ad a mesh, like a circle, for example. To keep everything organized, create a collection for your shapes and move there the circle you just created. Go back to Pose Mode and, in **_Object Data Properties_** > **_Viewport Display_** check **_Shapes_**. Select the bone you want and then, in **_Bone Properties_**, click on **_Viewport Display_** > **_Custom Shape_**. In **_Custom object_**, select the circle in the outliner.

<img src="/images/3d-models-and-animations/create-rig/26_bone_shape.gif" width="600" />

_Customizing the bone shape._

If the shape feels off, you can always edit it in **_Edit Mode_**, as shown below. Make sure the shape has the same orientation os the bone.

<img src="/images/3d-models-and-animations/create-rig/27_bone_shape_edit.gif" width="600" />

_Edit the shape in Edit Mode._

Create different shapes for different controls according to their function to make your rig more intuitive.

And that’s it! With all this information you’re ready to do a basic rig!
