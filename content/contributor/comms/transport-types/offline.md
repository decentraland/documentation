---
title: "Offline Transport"
sidebartitle: "Offline"
url: "/contributor/comms/transport-types/offline"
weight: 4
---
The Offline transport is a dummy implementation to signal that there is no comms server available in a realm. It's commonly used in testing and development environments.

The transport never emits incoming messages, and ignores all outgoing messages. If you want an offline variant with simulated behavior, see [Simulator]({{< relref "simulator" >}}) instead.

URIs have this look:

```
offline:<custom suffix>
```

What comes after the `offline:` prefix is unspeficied, and can be used by implementations (or left empty) as they see fit.