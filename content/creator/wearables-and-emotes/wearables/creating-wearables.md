---
date: 2021-05-31
title: Creating wearables
description: Tips and guidelines for creating Decentraland wearables
categories:
  - Decentraland
type: Document
aliases:
  - /wearables/creating-wearables/
  - /decentraland/creating-wearables/
url: /creator/wearables/creating-wearables
weight: 2
---

# **How To Create Wearables**

## **Intro**

This guide introduces the basics of creating custom 3D models for Decentraland wearables. It explains how the Decentraland avatar system works, and it illustrates how to properly model your own wearables.

*Note: this guide assumes that you already have some basic to intermediate knowledge of 3D modeling. If you’re new to 3D modeling, [start here](https://docs.decentraland.org/creator/3d-modeling/3d-models/).*


## **The Decentraland Avatar System [#](https://docs.decentraland.org/creator/wearables/creating-wearables/#the-decentraland-avatar-system)**

The Decentraland “avatar system” is the broad collection of different body components and subcomponents that can be decorated with custom wearables. These components are:

- Body shape
- Head
    - Head shape
    - Eyebrows
    - Eyes
    - Mouth
- Upper body
- Lower body
- Feet
- Accessories

### **Body Shape**

The basic form of an avatar. Wearables can be assigned to one, or both, body shapes. Currently, there are two body shapes: A or B.

[Creating]({{< ref “/images/wearables/1_creating_wearables.png”>}})

[Creating]({{< ref “/images/deploy.svg”>}})

### **Head** **[#](https://docs.decentraland.org/creator/wearables/creating-wearables/#head)**

The head includes several different meshes:

**Head Shape:** This is the base mesh of the head on which all other head features can be attach.

**Eyebrow Mesh:** The Eyebrow mesh works as a transparency mask. It is used to create different eyebrow styles.

**Eye Mesh:** The Eye mesh works as a transparency mask, and is used to create different eye styles.

**Mouth Mesh:** The mouth mesh works as a transparency mask, and is used to create different mouth styles.

### Upper Body **[#](https://docs.decentraland.org/creator/wearables/creating-wearables/#upper-body)**

The upper body, or torso, of an avatar includes the arms and hands. All upper body wearables are applied to the entire torso.

### Lower Body **[#](https://docs.decentraland.org/creator/wearables/creating-wearables/#lower-body)**

The lower body includes the pelvis, legs, and ankles of an avatar.

### Feet **[#](https://docs.decentraland.org/creator/wearables/creating-wearables/#feet)**

Boots, shoes, sandals, etc. are applied to this slot.

## **Wearable Categories [#](https://docs.decentraland.org/creator/wearables/creating-wearables/#wearable-categories)**

Each wearable has a specific category that determines which body part in the avatar system (e.g. head, upper body, etc.) the wearable will be applied to. Certain wearables will impact whether or not other wearables are rendered, depending on the specific category. Some wearables will entirely replace others with sometimes unexpected and surprising results. See the list below for details.

The different categories are:

- **Body Shape:** Replaces the entire avatar’s body.
- **Skin:** Replaces the entire avatar (head, upper body, lower body and feet except accessories)
- **Head:**
    - **Mouth**
    - **Eyes**
    - **Eyebrows**
    - **Facial Hair:** facial hair won’t replace or override any other wearables.
    - **Hair:** Replaces an avatar’s hair.
- **Upper Body**
- **Lower Body**
- **Feet**

There are also accessories that can be applied to different areas of an avatar. Some of these accessories can impact other wearables. The accessories are:

- **Mask**
- **Eyewear**
- **Earring**
- **Tiara**
- **Top Head:** This is rendered on the top of an avatar’s hard. For example, an angel’s halo.
- **Hat:** Replaces the avatar’s hat. For hats that leave some hair exposed, it must be attached to the hair in the mesh to prevent the avatar from going bald whenever they put on their hat.
- **Helmet:** Overrides the avatar’s entire head, replacing both hair and facial_hair.

## **Building 3D models for wearables [#](https://docs.decentraland.org/creator/wearables/creating-wearables/#building-3d-models-for-wearables)**

Let’s start to create some wearables!

### Tris, materials and texture limitations

To ensure that Decentraland runs smoothly for all users, it is important to create wearable models without using too many triangles. The goal is to keep models as simple as possible so that they can easily be rendered, without sacrificing too much detail.

The same goes for textures. It’s critical that we use as few textures as possible.

There are limits for the number of triangles and textures that can be used for each wearable or accessory:

- No more than 1.5K triangles per wearable slot: upper body, lower body, feet and hair.
- No more than 500 triangles per these accessories slots: mask, eyewear, earring, tiara, top_head and facial hair.
- No more than 1k triangles per these accessories slots: hat, helmet.
- No more than 2 textures (at a resolution of 512x512px or lower) per wearable. All textures must be square.
- No more than 2 materials (without counting the AvatarSkin_MAT)
- In the case of skin wearable, the amount of tris allowed are 5k and 5 textures.

{{< hint warning >}} **Wearable Tris Combiner:**

*If the wearable hide other wearables the creator is allowed to combine the tris per slot. For example: if you want to do a jumpsuit you could create it using the upper body category hiding lower body; in that case you could have 1.5K*2= 3K triangles.*

In the case of the helmet, if you hide all the wearables from the head (head, earrings, eyewear, tiara, hat, facial_hair, hair and top_head you can reach the 4k tris and 2 materials and 2 textures) 
{{< /hint >}}

### **Maps**

Decentraland supports 3 types of maps to texture your **Avatars/Wearables** Which are:

1. **Base Color**: This is the main texture with the colors and details of your model.
2. **Emission**: This map is for the parts that are glowing in your model. The emission map goes in a separated material specifically for emission.
3. **Alpha**: This map is to handle transparency. It uses the opacity channel of the texture.

Since Image textures in blender have a Color and Alpha output you can use the color texture and the opacity texture in the same material.

### **Don’t allowed maps**

Because Decentraland reference client uses of a Toon shader for the avatar materials, some maps are **not necessary** like:

- **Normal maps:** Normal maps are maps used to simulate height on a surface.
- **Roughness maps:** Roughness is used to determine which part of the surface will receive more or less roughness based on the amount of darkness on the map**.**

To use these maps in Decentraland the workaround is to bake them in one texture. You can find more info about baking textures here: [https://docs.blender.org/manual/en/latest/render/cycles/baking.html](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)

### Normals

Decentraland engine render only one side normals. (That means that a plane only will be visible from one side, the other side won’t be rendered) So, to ensure that your 3D is absolutely correct with the normals we can check that in two different ways.

The first one is to toggle the “Backface culling” on the Material properties settings, this is a good practice for spot inverted normals, like in this image:



The second way to check if the normals are right is by toggling “Face orientation” on the viewport overlay options. It will turn your model blue, but don’t worry. The blue faces are the correct ones and the red ones are the ones that needs to be corrected, you can find this option here:

