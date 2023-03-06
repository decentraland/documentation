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

https://github.dev/decentraland/documentation/blob/testing-new-order-wearables/static/images/wearables/1_creating_wearables.png


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

[Head]({{< ref “/images/media/blender-export-settings-animations.png”>}})

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