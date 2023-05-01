---
bookCollapseSection: false
weight: 5
title: SignedFetch
---


The `SignedFetch` module provides an implementation of the `fetch` interface that is transparently compliant with the [signed fetch]({{< relref "../../auth/signed_fetch" >}}) protocol, which defines how to attach signed [authentication chains]({{< relref "../../auth/authchain" >}}) to outgoing requests.

The procedures for signing and verifying this request are detailed in the [authentication chain]({{< ref "/contributor/auth/authchain" >}}) page. !! link to section

Using `SignedFetch` from a scene requires the [`USE_FETCH`]({{< ref "/contributor/content/entity-types/scenes#permissions" >}}) permission.

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
