---
date: 2018-01-15
title: Custom components
description: Create a custom component to handle specific data related to an entity
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/custom-components/
weight: 3
---

Data about an entity is stored in its [components]({{< ref "/content/creator/sdk7/architecture/entities-components.md" >}}). The Decentraland SDK provides a series of base components that manage different aspects about an entity, like its position, shape, material, etc. The engine knows how to interpret the information in these, and will change how the entity is rendered accordingly as soon as they change their values.

If your scene's logic requires storing information about an entity that isn't handled by the default components of the SDK, then you can create a custom type of component on your scene. You can then build [systems]({{< ref "/content/creator/sdk7/architecture/systems.md" >}}) that check for changes on these components and respond accordingly.


## About defining components

To define a new component, use `engine.defineComponent`. Each component needs the following:

- An **componentName**: A unique string identifier that the SDK uses internally to identify this component type. This can be any string, as long as it's unique.
- A **schema**: A class that defines the data structure held by the component.


```ts
export const WheelSpinComponent = engine.defineComponent(
	"wheelSpinComponent",
	{
		spinning: Schemas.Boolean,
		speed: Schemas.Float
	})
```

{{< hint info >}}
**💡 Tip**:  Define your scene's custom components in a separate `/components` folder inside `/src`, each in its own file. That way it's easier to reuse these in future projects.
{{< /hint >}}

Once you defined a custom component, you can create instances of this component, that reference entities in the scene. When you create an instance of a component, you provide values to each of the fields in the component's schema. The values must comply with the declared types of each field.

```ts
// Create entities
const wheel = engine.addEntity()
const wheel2 = engine.addEntity()

// Create instances of the component
WheelSpinComponent.create(wheel1, {
	spinning: true,
	speed: 10	
})

WheelSpinComponent.create(wheel2, {
	spinning: false,
	speed: 0	
})
```

Each entity that has the component added to it instances a new copy of the component, holding specific data for that entity.

Your custom component can also perform the other common functions that are available on other components:

```ts
// Fetch a read only instance of the component from an entity
const readOnlyInstance MyCustomComponent.get(myEntity)

// Fetch a mutable instance of the component from an entity
const readOnlyInstance MyCustomComponent.getMutable(myEntity)

// Delete an entity's instance of the component
const readOnlyInstance MyCustomComponent.deleteFrom(myEntity)

```


## About the componentName

Each component must have a unique componentName, that differentiates it internally. You won't need to use this internal identifier anywhere else in your code. A good practice is to use the same name you assign to the component, but starting with a lower case letter, but all that really matters is that this identifier is unique within the project.

When creating components that will be shared as part of a library, be mindful that the component names in your library must not overlap with any component names in the project where it's being used, or on other libraries that are also used by that project. To avoid the risk of any overlap, the recommended best practice is to include the name of the library as part of the `componentName` string, for example following this formula `${packageName}::${componentName}`.

If you build a`MyUtilities` library that includes a `MoveEntity` component, set that `componentName` of that component to `MyUtilities::moveEntity`.


## Components as flags

You may want to add a component that simply flags an entity to differentiate it from others, without using it to store any data. To do this, leave the schema as an empty object.

This is especially useful when using [querying components]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}). A simple flag component can be used tell entities apart from others, and avoid having the system iterate over more entities than needed.

```ts
export const IsEnemyFlag = engine.defineComponent("isEnemyFlag", {})
```

You can then create a system that iterates over all entities with this component.

```ts
export function handleEnemies() {
  for (const [entity] of engine.getEntitiesWith(IsEnemyFlag)) {
	// do something on each entity
  }
}

engine.addSystem(handleEnemies)
```

## Component Schemas

A schema describes the structure of the data inside a component. A component can store as many fields as you want, each one must be included in the schema's structure. The schema can include as many levels of nested items as you need.

Every field in the schema must include a type declaration. You can only use the special schema types provided by the SDK. For example, use the type `Schemas.Boolean` instead of type `boolean`. Write `Schemas.` and your IDE will display all the available options.

```ts
export const WheelSpinComponent = engine.defineComponent("wheelSpinComponent", {
	spinning: Schemas.Boolean,
	speed: Schemas.Float
})
```

The example above defines a component who's schema holds two values, a `spinning` boolean and a `speed` floating point number. 


You can chose to create the schema inline while defining the component, or for more legibility you can create it and then reference it.

```ts
// Option 1: Inline definition
export const WheelSpinComponent = engine.defineComponent("wheelSpinComponent", {
	spinning: Schemas.Boolean,
	speed: Schemas.Float
})

// Option 2: define schema and component separately

//// schema
const mySchema = {
	spinning: Schemas.Boolean,
	speed: Schemas.Float
}

//// component
export const WheelSpinComponent = engine.defineComponent("wheelSpinComponent", mySchema)
```

{{< hint info >}}
**💡 Tip**:  When creating an instance of a component, the VS Studio autocomplete options will suggest what fields you can add to the component by pressing _Ctrl + Space_.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**:  All values in a custom component are optional when instancing a component. There is no mechanism to define default values for these fields when instancing the component, but you can define systems that execute default behaviors if no values are present for a given field.
{{< /hint >}}

### Default Schema types

The following basic types are available for using within the fields of a schema: 

- `Schemas.Boolean`
- `Schemas.Byte`
- `Schemas.Double`
- `Schemas.Float`
- `Schemas.Int`
- `Schemas.Int64`
- `Schemas.Number`
- `Schemas.Short`
- `Schemas.String`
- `Schemas.Entity`

The following complex types also exist. They each include a series of nested properties with numerical values.

- `Schemas.Vector3`
- `Schemas.Quaternion`
- `Schemas.Color3`
- `Schemas.Color4`

{{< hint info >}}
**💡 Tip**:  See [Geometry types]({{< ref "/content/creator/sdk7/3d-essentials/special-types.md" >}}) and [Color types]({{< ref "/content/creator/sdk7/3d-essentials/color-types.md" >}}) for more details on how these types of data are useful.
{{< /hint >}}

For example, you can use these schema types in a component like this to track the gradual movement of an entity. This component stores an initial and a final position as Vector3 values, as well as a speed and fraction of the completed path as float numbers. See [Move entities]({{< ref "/content/creator/sdk7/3d-essentials/move-entities.md#move-between-two-points" >}}) for the full implementation of this example.

```ts
const MoveTransportData = {
  start: Schemas.Vector3,
  end: Schemas.Vector3,
  fraction: Schemas.Float,
  speed: Schemas.Float,
}

export const LerpTransformComponent = engine.defineComponent("lerpTransformComponent", MoveTransportData)
```



### Array types

To set the type of a field as an array, use `Schemas.Array()`. Pass the type of the elements in the array as a property.

```ts
const MySchema = {
	numberList: Schemas.Array(Schemas.Int),
  }
```

### Custom schema types


To set the type of a field to be an object, use `Schemas.Map()`. Pass the contents of this object as a property. This nested object is essentially a schema itself, nested within the parent schema.


```ts
const MySchema = {
	simpleField: Schemas.Boolean,
	myComplexField: Schemas.Map({
		nestedField1: Schemas.Boolean,
		nestedField2: Schemas.Boolean			
	})}
}
```

Alternatively, to keep things more readable and reusable, you could achieve the same by defining the nested schema separately, then referencing it when defining the parent schema.

```ts
const MyNestedSchema = Schemas.Map({
		nestedField1: Schemas.Boolean,
		nestedField2: Schemas.Boolean			
	})

const MySchema = {
	simpleField: Schemas.Boolean,
	myComplexField: MyNestedSchema
}
```



### Enums types

You can set the type of a field in a schema to be an enum. Enums make it easy to select between a finite number of options, providing human-readable values for each.

To set the type of a field to an enum, you must first define the enum. Then you can refer to it using `Schemas.Enum`, passing the enum to reference between `<>`, as well as the type as a parameter (usually all enums are `Schemas.Int`).

```ts
// Define an enum
enum CurveType {
  LINEAR,
  EASEIN,
  EASEOUT
}

// Define a schema that uses this enum in a field
const MyCurveSchema = {
  curve:  Schemas.Enum<CurveType>(Schemas.Int),
}

```

## Building systems to use a component

With your component defined and added to entities in your scene, you can create systems to perform logic, making use of this data stored on the component.

```ts
// define component
export const WheelSpinComponent = engine.defineComponent("wheelSpinComponent", {
	spinning: Schemas.Boolean,
	speed: Schemas.Float
})

// Create entities
const wheel = engine.addEntity()
const wheel2 = engine.addEntity()

// Create instances of the component
WheelSpinComponent.create(wheel1, {
	spinning: true,
	speed: 10	
})

WheelSpinComponent.create(wheel2, {
	spinning: false,
	speed: 0	
})

// Define a system to iterate over these entities
export function spinSystem(dt: number) {
	// iterate over all entiities with a WheelSpinComponent
  for (const [entity, wheelSpin] of engine.getEntitiesWith(WheelSpinComponent)) {

	// only do something if spinning == true
	if(wheelSpin.spinning){

		// fetch a mutable Transform component 
		const transform = Transform.getMutable(entity)

		// update the rotation value accordingly
		transform.rotation = Quaternion.multiply(transform.rotation, Quaternion.fromAngleAxis(dt * wheelSpin.speed, Vector3.Up()))
	}
  }
}

// Add system to engine
engine.addSystem(spinSystem)
```

The example above defines a system that iterates over all entities that include the custom `wheelSpinComponent`, and rotates them slightly on every tick of the game loop. The amount of this rotation is proportional to the `speed` value stored on each entity's instance of the component. The example makes use of [component queries]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}) to obtain only the relevant entities.