---
title: Authentication Chain
url: /contributor/auth/authchain
weight: 2
---

Many actions in the Decentraland protocol either require or benefit from authorization with a signature from the user's Ethereum account. For example:

1. Upload a new version of any [Entity]({{< ref "/contributor/content/entities" >}}) they own (such as their profile).
2. Authenticate themselves to 3rd-party services.
3. Authorize delegates to act on their behalf.

To perform these actions, users and delegates must sign payloads describing their intent and produce an _authentication chain_.

## Introduction

Authentication chains encapsulate a series of verification steps, with each step depending on the succcessful verification of the previous one. All steps must be deemed valid by the verifier for any restricted action to take place.

Every chain begins by identifying the user, and ends with a signed payload representing the requested action. The smallest chain thus contains two elements, which indicate:

```md
1. The authority is the Ethereum account <user-address>
2. The payload is <payload>, authorized by <user-signature>
```

This basic chain can be evaluated by verifying that the signature's public key corresponds to the address. In this case, it's equivalent to a plain signature.

When users authorize delegates to act on their behalf, intermediate steps appear in the chain. For example, a chain with a single delegation would indicate:

```md
1. The authority is the Ethereum account <user-address>
2. The delegate is <delegate-address>, authorized by <user-signature> until <date>
3. The payload is <payload>, authorized by <delegate-signature>
```

Chains are longer when delegates authorize their own delegates. In other words, authorization is transitive.

{{< info >}}
You can think of authentication chains as analogous to the TLS certificate chains used in HTTPS. with the user as the equivalent of the root authority.
{{< /info >}}

This single-delegate chain is the most common form of authorization used in Decentraland, since users authorize a key for their World Explorer to avoid having to sign every individual action with their Ethereum account.

### Constructing a Chain {#constructing}

Each step in the authentication chain contains three pieces of information: a `type`, a `payload` and a corresponding `signature`.

| Field       | Value                                                                 |
| ----------- | --------------------------------------------------------------------- |
| `type`      | The name of a type ([see below](#types)).                             |
| `payload`   | A type-dependent string.                                              |
| `signature` | The hex-encoded Ethereum signature of `payload`, beginning with `0x`. |

{{< info >}}
Since the most common serialization of an authentication chain is a JSON array, the examples below are presented in that form. See [Transmitting a Chain](#transmitting) for more details.
{{< /info >}}

### First Step: Identification

The first step, which identifies the original authority (i.e the user), must meet these conditions:

1. The `type` is [`SIGNER`](#SIGNER)
2. The `payload` is the encoded Ethereum account.
3. The `signature` is empty.

For example:

```json
// First step in any authentication chain:
{
  "type": "SIGNER",
  "payload": "0xdB055877e6c13b6A6B25aBcAA29B393777dD0a73",
  "signature": ""
}
```

The second step must carry a `signature` from this account for its `payload`.

### Intermediate Steps: Delegation

When delegates are acting on the user's behalf, an item is added to the middle of the chain for each of them. The conditions for these steps are:

1. The type is [`ECDSA_EPHEMERAL`](#ECDSA_EPHEMERAL)
2. The `payload` is a specially crafted text (see below).

The `payload` is designed to be easy to read and easy to parse, since both humans (when using their wallet UI) and programs (when crafting and validating) must work with it. It contains exactly 3 lines of case-sensitive plain text:

```md
<purpose>
Ephemeral address: <delegate-address>
Expiration: <date>
```

For example, this is a typical payload used by World Explorers during login, when they generate their temporary delegate key for the user to approve:

```
Decentraland Login
Ephemeral address: 0xBB9aDF0183b1742196A4Aa55622D5838f4f483a7
Expiration: 2023-02-25T13:00:19.730Z
```

Note that:

1. The `Ephemeral address` doesn't need to be an actual Ethereum account with funds in the blockchain. The field may only represent a temporary public key.

2. The `Expiration` is a serialized datetime in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) form. It doesn't need to be UTC.

3. The delegate key must be periodically renewed with a fresh signature from the user, due to this expiration date.

{{< info >}}
It's standard practice (and highly recommended) to generate a new key for every renewal (thus the name `ECDSA_EPHEMERAL`).
{{< /info >}}

An example delegation step (values abbreviated for clarity):

```json
{
  "type": "ECDSA_EPHEMERAL",
  "payload": "Decentraland Login\nEphemeral address: 0xBBa7...\nExpiration: 2021-01-25T...",
  "signature": "0x1370a4120a7cb0d2f6e4a5..."
}
```

The next step, whether it's another delegation or the final authorization, carries a signature from this delegate's key.

### Last Step: Authorization

After the `SIGNER` has been specified and all `ECDSA_EPHEMERAL` delegate keys were validated by verifying the chain of intermediate signatures, the final step is the actual action that needs to be authorized.

The `payload` is dependent on the `type` of the step. For example, if a user is uploading a new profile (or any entity they own) to a content server, the last element will have this form:

```json
{
  // The type indicates that `payload` is an entity ID (details in the Content section):
  "type": "ECDSA_SIGNED_ENTITY",

  // The payload is the raw ID string:
  "payload": "bafkreicfbg7ybpuoslkcf6x2vfnvzl5vwgqtb2pnheqiut2i4sgpblicqi",

  // The signature is produced by the account in the previous step (user or delegate):
  "signature": "0x7e71dbbab..."
}
```

If this last signature is also valid, the action can proceed.

### Transmitting a Chain {#transmitting}

As mentioned above, the most common serialization of an authentication chain is a JSON array. This is the recommended approach.

However, the protocol does not impose this. Developers are allowed to use an alternative serialization strategy if it's more convenient for a particular use-case, such as YAML, CSV files, optimized binary formats or simple strings with delimited fields.

An example of alternative serialization from within the protocol itself can be found in the [`SignedFetch`]({{< ref "/contributor/runtime/modules/signed_fetch" >}}) module, which uses a sequence of HTTP headers instead of a JSON array.

### Choosing an Expiration Date

When selecting the valid duration for a delegate key, there's a tradeoff: shorter expirations increase security, but longer expirations improve user experience (since delegates have to be renewed with human interaction at a lower frequency).

There is no universal strategy to decide what the valid time window should be. The Foundation's World Explorer, for reference, requests authorization for its delegate key for one month.

{{< info >}}
Ephemeral keys should never hold funds or possess the ability to transfer digital assets. It's much safer for end-users if the leak of an ephemeral key cannot result in financial losses.
{{< /info >}}

## Formalization

What follows is a more formal and precise definition of the processes involved. Follow these instructions to successfully handle authentication chains.

### Creation

Clients crafting an authentication chain for the user follow these steps:

1. Add the identification step:

   1. Set the `type` to `SIGNER`.
   2. Set the `payload` to the user's Ethereum address.
   3. Set the `signature` to an empty string.

2. Add delegations steps:

   1. Generate or use an existing delegate private key (may require interaction).
   2. Calculate the delegate Etherum address derived from the corresponding public key.
   3. Set the `type` to `ECDSA_EPHEMERAL`.
   4. Set the `expiration` to a date in the future.
   5. Choose a `purpose` for this key.
   6. Set the `payload` to this exact form:
      ```md
      <purpose>
      Ephemeral address: <delegate-address>
      Expiration: <date>
      ```
   7. Set the `signature` field to the `payload` signature from the previous key (user or delegate).
   8. Repeat for all successive delegates.

3. Add the action authorization step:

   1. Set the `type` to a valid value ([see below](#types))
   2. Set the `payload` to the type-specific value (such as the entity ID).
   3. Set the `signature` field to the `payload` signature from the previous key (user or delegate).

4. Send the authentication chain to the verifier.

### Verification

Content servers and 3rd-party services implementing verification follow these steps:

1. Verify identification:

   1. Verify the `type` is `SIGNER`.
   2. Verify the `payload` is the Ethereum address of the user.
   3. Verify the `signature` is an empty string.

2. Verify delegates:

   1. Verify the `type` is `ECDSA_EPHEMERAL`.
   2. Verify the `payload` is in this form and extract the fields:
      ```md
      <purpose>
      Ephemeral address: <delegate-address>
      Expiration: <date>
      ```
   3. Verify the `date` is still in the future.
   4. Verify the `purpose` is supported by your service.
   5. Verify the `signature` is valid for the given `payload` and the previous public key.
   6. Repeat for all successive delegates.

3. Verify action authorization:

   1. Verify the `type` is a valid value ([see below](#types)).
   2. Verify the `payload` is valid for this `type`.
   3. Verify the `signature` is valid for the given `payload` and the previous public key.

4. Accept the authentication chain.

### Standard Action Types and Purposes {#types}

The `type` and `payload` values for identification and delegation are standard and must be verified as laid out above, but clients and services can agree on any action `type`, and its `payload` structure, as well as set a `purpose` for their delegate keys that they consider valid.

The protocol defines three standard types, and one standard purpose:

##### Type `SIGNER` {#SIGNER}

**Must** be the initial `type` in the chain, where `payload` is the user's Ethereum address and `signature` is an empty string.

##### Type `ECDSA_EPHEMERAL` {#ECDSA_EPHEMERAL}

**Must** be the `type` for intermediate steps in the chain, where `payload` is in the form described above.

##### Type `ECDSA_SIGNED_ENTITY` {#ECDSA_SIGNED_ENTITY}

The final `type` in the chain for authorizing entity deployments, where `payload` is the ID of an entity owned by the user.

##### Purpose `Decentraland Login` {#DecentralandLogin}

The usual `purpose` for World Explorers, signed both when logging into the world and when renewing their delegate key.
