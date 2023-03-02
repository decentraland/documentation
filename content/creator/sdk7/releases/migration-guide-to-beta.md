---
title: "Migration guide 7.1"
url: "/creator/sdk7/releases/migration-guide-to-beta"
weight: 3
---


Between the _Alpha_ version 7.0.5 and the _Beta_ version 7.1.0 of the `@dcl/sdk` framework there have been multiple breaking changes. A scene written using 7.0.5 will need some minor adjustments when migrated to 7.1.0 Below are the changes that need to be considered:


- Component ids are now a string, instead of a number. Also when defining a component, the order of parameters has been reversed. Now the ID goes first, then the schema.
	```ts
	// OLD
	export const PainterComponent = engine.defineComponent(
	{
		myField: Schemas.Number
	},
	1234
	)

	// NEW
	export const PainterComponent = engine.defineComponent(
	'PainterComponent',
	{
		myField: Schemas.Number
	}
	)
	```
- UI alignment properties have changed types, they’re no longer enums, instead special string types.
	{{< hint info >}}
	**💡 Tip**:  In Visual Studio Code, on each property press _Ctrl + Space bar_ to see a dropdown of suggestions with the allowed values.
	{{< /hint >}}
- The `PointerHoverFeedback` component was renamed to `PointerEvents`
- The `Billboard` component has changed properties. It now only has one `BillboardMode` property, that takes an enum that sets several different modes.
- `getRealmData()` is deprecated. Use `getRealm()` instead.
- `isPreview()` is deprecated. `getRealm()` now returns an additional `preview` boolean property to use instead.
- `getParcel()` is deprecated. Use `getSceneInfo()`  instead.
- The `albedoColor` in a PBR `Material` component changed from type `Color3` to type `Color4`, to support transparent colors.
- In `package.json`, the `scripts` section must be changed to the following: 
	```json
	"scripts": {
			"start": "sdk-commands start",
			"build": "sdk-commands build",
			"upgrade-sdk": "npm install --save-dev @dcl/sdk@latest",
			"upgrade-sdk:next": "npm install --save-dev @dcl/sdk@next"
		},
	```
- Loading of texture images from external sources requires adding domain to an allowlist on the scene’s scene.json file. <SNIPPET>
- When running a preview of an SDK7 scene via the command line, use `npm run start` and `npm run build`. Don't use `dcl start` or `dcl build`. The Decentraland Editor is encouraged as the defacto way to run scene previews.
- The orientation of Textures is now flipped on plane and cube primitives. This results in a more intuitive result, as the default orientation of a plane now exhibits an image facing the right way. It is also consistent with how video textures are oriented.
- Fixed bug with rotating platforms, they now move players that are standing on them.



## New features

Additionally, the following new features are now available:

- VideoTexture is now implemented for playing streamed videos
- New Schema types `Schemas.Vector3` and `Schemas.Quaternion`. These are useful for defining custom components that store these common data types.
- New `Entity` type has been added, it helps with type checking for operations that expect or return an entity
- New `onMouseDown` and `onMouseUp` properties for UI pointer events
- New `Dropdown` UI element
- New `Input` UI element
- New `Label` UI element
- New `texture` and `textureType` properties in `uiBackground` let you set images on a UI element.
- New `textureSlices` property lets you perform 9-Slice stretching of UI textures, to preserve proportions on the corners and margins.
- Basic materials on the `Material` component have a new `diffuseColor` property to apply a plain color to a shade-less material.
- The `PointerLock` component allows you to know if the player currently has the cursor locked
