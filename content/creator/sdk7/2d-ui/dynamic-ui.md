---
date: 2022-10-20
title: Dynamic UIs
description: Learn how to make UIs dynamic, responding to changes in data.
categories:
  - development-guide
type: Document
url: /creator/development-guide/dynamic-ui/
weight: 2
---


You can include dynamic elements in the UI, that are updated on every tick based on changing variables.

To do this, simply set the value in one of the components in a uiEntity to a variable. As the variable changes value, the UI will adapt accordingly.



```ts
  let counter = 0
  
  export const uiComponent = () => (
	<UiEntity
	  uiTransform={{
		width: 700,
		height: 400,
		margin: { top: '35px', left: '500px' }
	  }}
	  uiBackground={{ backgroundColor: Color4.create(0.5, 0.8, 0.1, 0.6) }}
	>
	  <UiEntity
		uiTransform={{
		  width: '100%',
		  height: '20%',
		  justifyContent: YGJustify.YGJ_CENTER,
		  alignItems: YGAlign.YGA_CENTER,
		  display: YGDisplay.YGD_FLEX
		}}
	  >
		<UiEntity
		  uiText={{ value: 'SDK 7', fontSize: 80 }}
		  uiBackground={{ backgroundColor: Color4.fromHexString('#fbf0f0') }}
		/>
	  </UiEntity>
	  <UiEntity
		uiTransform={{
		  width: '100%',
		  height: '20%',
		  justifyContent: YGJustify.YGJ_CENTER,
		  alignItems: YGAlign.YGA_CENTER,
		  display: YGDisplay.YGD_FLEX
		}}
	  >
		<UiEntity
		  uiText={{ value: `Counter: ${counter}`, fontSize: 60 }}
		  uiBackground={{ backgroundColor: Color4.fromHexString('#fbf0f0') }}
		/>
	  </UiEntity>
	  <UiEntity
		uiTransform={{
		  width: '100%',
		  height: '100px',
		  justifyContent: YGJustify.YGJ_CENTER,
		  alignItems: YGAlign.YGA_CENTER,
		  display: YGDisplay.YGD_FLEX
		}}
	  >
		<UiEntity
		  uiText={{ value: `Player: ${getPlayerPosition()}`, fontSize: 40 }}
		  uiBackground={{ backgroundColor: Color4.fromHexString('#fbf0f0') }}
		/>
	  </UiEntity>
	</UiEntity>
  )
  
 
  
  renderUi(uiComponent)
  
  // Cube factory
  function createCube(x: number, y: number, z: number, spawner = true): Entity {
	const meshEntity = engine.addEntity()
	Transform.create(meshEntity, { position: { x, y, z } })
	MeshRenderer.create(meshEntity, { box: { uvs: [] } })
	MeshCollider.create(meshEntity, { box: {} })
	if (spawner) {
	  PointerHoverFeedback.create(meshEntity, {
		pointerEvents: [
		  {
			eventType: PointerEventType.PET_DOWN,
			eventInfo: {
			  button: InputAction.IA_PRIMARY,
			  hoverText: 'Press E to spawn',
			  maxDistance: 100,
			  showFeedback: true
			}
		  }
		]
	  })
	}
	return meshEntity
  }

  createCube(8, 1, 8)
  
  
  function UpdateCounterSystem() {
	const clickedCubes = engine.getEntitiesWith(PointerEvents)
	for (const [entity] of clickedCubes) {
	  if (wasEntityClicked(entity, InputAction.IA_PRIMARY)) {
		counter++
	  }
	}
  }
  

  engine.addSystem(UpdateCounterSystem)

   function getPlayerPosition() {
	const playerPosition = Transform.getOrNull(engine.PlayerEntity)
	if (!playerPosition) return ''
	const { x, y, z } = playerPosition.position
	return `{x: ${x.toFixed(2)}, y: ${y.toFixed(2)}, z: ${z.toFixed(2)} }`
  }
  
  
```