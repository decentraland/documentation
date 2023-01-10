---
date: 2022-09-20
title: Data mutability
description: Learn how to handle ead-only and mutable data from components
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/mutable-data/
weight: 2
---

When referencing data from a [component]({{< ref "/content/creator/sdk7/architecture/entities-components.md" >}}), you can either fetch the mutable or the read-only (immutable) version. 

You should always deal with the read-only versions of data when possible. This practice can bring a very significant improvement in the performance of your scene, when compared to always dealing with mutable versions of that same data.

The `.get()` function in a component returns a read-only (immutable) version of the component. You can only read its values, but can't change any of the properties on it.

The `.getMutable()` function returns a version of the component that allows you to change its values. Use mutable versions only when you plan to make changes to a component, otherwise, always use `get()`.

```ts
// fetch a read-only (immutable) version
const immutableTransform = Transform.get(myEntity)

// the following does NOT work:
// 	immutableTransform.position.y = 2

const mutableTransform = Transform.getMutable(myEntity)

// the following line DOES change the entity's position
mutableTransform.position.y = 2
```

A good practice is to iterate over read-only components to check values, and then only fetch the mutable version of an individual component when a change is required.


```ts
// hard-coded maximum height
const MAX_HEIGHT = 10

// Define the system
function HeightLimitSystem(dt: number) {
	// iterate over all entities that have a Transform component
  for (const [entity] of engine.getEntitiesWith(Transform)) {

	// get read-only values
	const currentHeight = Transform.get(entity).position.y

	// compare values
	if(currentHeight > MAX_HEIGHT){

		// fetch mutable version to make a change
		const mutableTransform = Transform.getMutable(entity)

		// change transform
		mutableTransform.position.y = MAX_HEIGHT
	}
  }
}

// Add system to engine
engine.addSystem(HeightLimitSystem)
```

In the example above, a system checks the read-only values of an entity's `Transform` component. On every tick it checks to see if the position's _y_ is higher than a hard-coded maximum height. If the height on the transform happens to be above this limit, then and only then we fetch the mutable version of the Transform. This may seem like extra work for the scene, but in a scene where we're checking values on every tick of the game loop, and only making changes occasionally, it results in huge performance gains.

This practice follows the principles of [data oriented programming]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}). It's also gradually being adopted as an industry standard practice in the gaming, because of how much of an improvement it makes.


{{< hint warning >}}
**📔 Note**   In older versions of the SDK (6.x or older), components were always treated as mutable. That pattern may be a bit more straight forward to learn, but was a lot less efficient to run.
{{< /hint >}}

