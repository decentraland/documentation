---
title: "Simulator Transport"
sidebartitle: "Simulator"
url: "/contributor/comms/transport-types/simulator"
weight: 4
---

The Simulator transport is a completely arbitrary implementation, with no specified behavior other than the transport interface. 

It can emit incoming messages and handle outgoing messages as desired, without semantic requirements. The implementation can choose to never emit messages and ignore all method calls, but the [Offline transport]({{< relref "offline" >}}) is better suited for that.

Simulator URIs look like this:

```
simulator:<custom suffix>
```

What comes after the `simulator:` prefix is unspeficied, and can be used by implementations (or left empty) as they see fit.