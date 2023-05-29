---
title: "Signed Login Transport"
sidebartitle: "Signed Login"
url: "/contributor/comms/transport-types/signed-login"
weight: 3
---

The Signed Login transport can be used by servers that want to customize the way they assign clients to islands, replacing or wrapping Archipelago in their architecture.

Instead of connecting directly to a real-time backend, Signed Login makes a [signed fetch]({{< ref "/contributor/auth/signed_fetch" >}}) to obtain the connection string. This intermediate step allows servers to employ whatever assignment strategy they want.

Signed Login URIs have this shape:

```
signed-login:https://comms.example.com/auth&param=value
```

The portion after the `signed-login:` prefix can be any valid URL.


## Usage

A Signed Login request is constructed using the [signed fetch]({{< ref "/contributor/auth/signed_fetch" >}}) mechanism.

The response, if successful, will have status `200` and a JSON body with _at least_ the following fields:


| Field | Type | Value
| ----- | --- | --- |
| `fixedAdapter` | `string` | The assigned transport URI (e.g. `livekit:` or `ws-room:`)


For example:

```
{ 
  fixedAdapter: "ws-room:wss://comms.example.com/rooms/17"
}
```

In case of failure, the response can have any appropriate status code and a JSON body with _at least_ the following fields:

| Field | Type | Value
| ----- | --- | --- |
| `message` | `string` | (Optional) an explanation or error code for the failure.

Responses with additional fields in the JSON body are valid, and the contents of the error `message` left unspecified. Implementations can use this flexibility to integrate `signed-login:` into their applications as they see fit.
