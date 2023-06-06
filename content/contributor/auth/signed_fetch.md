---
title: Signed Fetch
url: /contributor/auth/signed-fetch
weight: 2
---

When protocol clients what to make authenticated HTTPs requests, they can leverage the standard _signed fetch_ mechanism.

A signed fetch is request that includes an [authentication chain]({{< relref "authchain" >}}), represented through headers. Servers with Decentraland-compatible APIs can validate identities before, for example, [allowing requests from scenes]({{< relref "../runtime/modules/signed_fetch" >}}) or creating [adapters]({{< relref "../comms/overview" >}}).

## Headers

The information the server needs to validate the authentication chain is relayed in 3+ headers:

* `X-Identity-Timestamp`: the `timestamp` field included in the signed payload (see below).
* `X-Identity-Metadata`: the `metadata` field included in the signed payload (see below).
* `X-Identity-AuthChain-<index>`: the [JSON-serialized authentication step]({{< ref "/contributor/auth/authchain#constructing" >}}) `<index>`, starting from `0`.

The transmitted chain is validated by the server [as specified]({{< relref "authchain" >}}).

## Body

The request body is unspecified. Services have full flexibility to use any protocols or formats they like.

## Payload

The authentication chain [payload]({{< relref "authchain#constructing" >}}) for a signed fetch is a **lower-case, colon-separated** string that includes some of the request elements:

```
<method>:<path>:<timestamp>:<metadata>
```

The `method` and `path` fields must match those of the request, and `timestamp` is the same as in the `X-Identity-Timestamp` header.

The last field, `metadata`, can have arbitrary content.

For example:

```
get:/some/path:1682790056:{"some":"custom json"}
```