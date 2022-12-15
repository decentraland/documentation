---
title: "Pointers"
sidebartitle: "Pointers"
url: "/contributor/content/pointers"
weight: 4
---

Pointers are unique strings that reference an active [[entity]], usually taking the form of a [[Decentraland URN]]. Content servers can resolve these pointers to locate the referenced entity.

Remember that both [[entities]] and their [[files]] are immutable in the Decentraland content system, and their identifiers change when replacement versions are uploaded. Pointers, on the other hand, are stable references that persist across replacements.

This is achieved by automatically redirecting the pointer to a new entity when the owner uploads a replacement.

As you may gather, the most common use of pointers is obtaining the ID for the active version (i.e. latest replacement) of an entity, in order to download it.

## Entity Pointers

Pointers referencing entities are [[Decentraland URNs]] that include the entity ID, such as this one:

```
urn:decentraland:entity:bafkreid44xhavttoz4nznidmyj3rjnrgdza7v6l7kd46xajleor5lmsxfm
```

### Optional components

Entity URNs can include a `baseUrl` to suggest a content server to use, making the URN easily translatable into an HTTP address. For example:

```
urn:decentraland:entity:<id>?baseUrl=https://contentserver.com/files/
```

This tells an application that the entity can be downloaded from `https://contentserver.com/files/<id>`, though other content servers can also be used.


## Land Pointers

_Pending answer to some questions_

## Other types

_Pending answer to some questions_

## Content Server Hints

_Pending answer to some questions_
