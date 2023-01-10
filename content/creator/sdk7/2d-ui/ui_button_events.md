
---
date: 2022-10-28
title: UI Button events
description: Handle button events on UI entities.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/ui-button-events/
weight: 3
---

The current alpha version of SDK7 does not yet support making UI elements clickable. This feature will be available soon.

<!-- 
Make a UI entity clickable by giving it an `onClick` component. The `onClick` component references a function that runs every time the UI entity is clicked.


{{< hint warning >}}
**📔 Note**   To click on a UI component, players must first unlock the cursor from the view control. They do this by pressing the _right mouse button_ and keeping it pressed, or by hitting `Esc`.
{{< /hint >}}

The following example shows how to create a clickable UI entity. 

```ts
ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity 
		uiTransform = {{ width: 100, height: 100 }} 
		uiBackground={{ backgroundColor: Color4.Green() }}
		onClick = { ()=>{ console.log("Clicked on the UI")} } 
	/>
))
```

You can also write the function that is executed by the click outside the UI definition, and reference it by name. This helps keep the UI code more readable, and is also useful if multiple clickable UI entities need to call the same function. 

```ts
function handleClick() {
	// Do something onClick
	console.log("Clicked on the UI")
}
ReactEcsRenderer.setUiRenderer(() => (
	<UiEntity 
		uiTransform = {{ width: 100 }} 
		onClick = {{handleClick}} 
	/>
))
``` -->




<!--

TODO: children of an entity with OnClick aren't clickable too, right?

TODO: is there an euqivalent to isPointerBlocker?

{{< hint info >}}
**💡 Tip**:  If you want to add text over a button, keep in mind that the text needs to have the `isPointerBlocker` property set to `false`, otherwise players might be clicking the text instead of the button.
{{< /hint >}}
 -->


