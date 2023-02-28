---
bookCollapseSection: false
weight: 5
title: SignedFetch
---


The `SignedFetch` module provides an implementation of the `fetch` interface that automatically includes additional verification headers. Servers can use these to check the authenticity of the operation.

The procedures for signing and verifying this request are detailed in the [authentication chain]({{< ref "/contributor/auth/authchain" >}}) page.

Using `SignedFetch` from a scene requires the [`USE_FETCH`]({{< ref "/contributor/content/entity-types/scenes#permissions" >}}) permission.

## Automatic Headers

The added headers contain the information the server needs to validate the request signature. In practice, this means the signed fields that are not represented in the HTTP request itself, plus the authentication chain public keys.

* `X-Identity-Timestamp`: the `timestamp` field included in the signed payload.
* `X-Identity-Metadata`: the `metadata` field included in the signed payload.
* `X-Identity-AuthChain-<index>`: the [JSON-serialized authentication step]({{< ref "/contributor/auth/authchain#constructing" >}}) `<index>`, starting from `0`.

From the scene's point of view, this is all transparently handled by the runtime, which can request use of the Explorer's delegate key.


## Authorization and Verification

To authorize the request, construct the following payload and sign it as described in the [authentication chain]({{< ref "/contributor/auth/authchain" >}}) specification. On the server side, verify as specified as well.

```ts
const payloadFields = [
  // The HTTP method, such as "GET" or "POST":
  method,
  
  // The request pathname (URL without domain, query or hash)
  path, 

  // A client-chosen timestamp for this request, which the server can examine:
  timestamp,

  // Additional data that can be included for verification or security:
  metadata
]

const payload = payloadFields.join(":").toLowerCase()
```

## Methods

###### `signedFetch` {#signedFetch}

Make an HTTP request as you would with ([`fetch`]({{< relref "../globals#http" >}})), automatically adding the verification headers.

```ts
interface Request {
  // The request target URL:
  url: string

  // Optional, self-explanatory parameters for the request:
  init?: {
    method?: string
    body?: string
    headers: { [key: string]: string }
  }
}

interface Response {
  // Whether the HTTP request was performed successfully (codes other than 2xx are not failures)
  ok: boolean

  // The self-explanatory details of the response:
  status: number
  statusText: string
  headers: { [key: string]: string }
  body: string
}

function signedFetch(Request): Promise<Response>
```
