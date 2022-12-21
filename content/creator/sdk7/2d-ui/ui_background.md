

---
date: 2022-10-28
title: UI Background
description: Set a background color on a UI entity.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/ui-background/
weight: 4
---

## uiBackground

A `uiBackground` colors an entity's area. It uses the size and position defined by the entity's `uiTransform`.

The following fields can be configured:

- `backgroundColor`: The color to use on the entity, as a [Color4]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md">}}) value.

> Tip: Make an entity semi-transparent by setting the 4th value of the `Color4` to less than 1.


```ts
ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: 700,
      height: 400
    }}
    uiBackground={{ 
		backgroundColor: Color4.create(0.5, 0.8, 0.1, 0.6) 
	}}
  >
))
```