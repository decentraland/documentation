---
title: "Create a new Entity in the Content Server"
slug: "/contributor/tutorials/how-to-create-an-entity"
---

### When is needed to create a new entity?
First, check if an existing entity can solve the needed use case to avoid over engineering a solution.
If none of the existing entity types defined in https://github.com/decentraland/common-schemas/blob/main/src/platform/entity.ts#L13 satisfies the requirements, then you may need to create a new entity type.

### First answer:
- Is the new entity an NFT Collection?
- How will the ownership be validated?
- Which will be the size of it?
- What is the amount entities that will be created?


### Steps

First create a ADR in https://github.com/decentraland/adr where you will define the schema and the date to start validating the new entity.

#### Repositories

##### @dcl/schemas
1. Create the new entity type in the enum: https://github.com/decentraland/common-schemas/blob/main/src/platform/entity.ts#L19
2. Create the folder and files in https://github.com/decentraland/common-schemas/tree/main/src/platform generating the type and JSON schema, for example: https://github.com/decentraland/common-schemas/blob/main/src/platform/profile/profile.ts#L20

##### @dcl/content-validator

Implement the validations defined in the ADR, taking into account the date of that ADR in https://github.com/decentraland/content-validator/blob/main/src/validations/timestamps.ts. For example: https://github.com/decentraland/content-validator/blob/main/src/validations/items/emotes.ts#L8

1. Add the code to check the ownership of the new entity type in https://github.com/decentraland/content-validator/tree/main/src/validations/access-checker
2. Implement the validationForType for the new type, for example: https://github.com/decentraland/content-validator/blob/main/src/validations/profile.ts#L112
3. Here you will need to define the max size per entity in https://github.com/decentraland/content-validator/blob/main/src/validations/ADR51.ts.

##### @dcl/urn-resolver
1. If the new entity corresponds to a Collection, then nothing has to be added.
2. If not, then create a new urn corresponding to the new entity and define it in  https://github.com/decentraland/urn-resolver adding a resolver in https://github.com/decentraland/urn-resolver/blob/main/src/resolvers.ts#L23

##### Catalyst: Content Server
1. No change in database needed.
2. Update all modified libraries detailed above.

##### Catalyst: Lambdas Server
1. Update all modified libraries detailed above.
2. Check if the profile sanitization needs to be updated (`/lambdas/profiles` endpoint)
3. Check if the erc collections endpoint needs to be updated (`/lambdas/collections` endpoint)
4. Create an endpoint to show that entity, for example `/lambdas/wearables-by-owner`
