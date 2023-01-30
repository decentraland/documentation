#!/usr/bin/env python3
import sys, re, pathlib

re_struct = re.compile(r"enum (.*) \{((?:\n.+)+)", re.MULTILINE)
re_message = re.compile(r"message (.*) \{((?:\n.+)+)", re.MULTILINE)
re_service = re.compile(r"service (.*) \{((?:\n.+)+)", re.MULTILINE)

def gen(protodef, tpl, re_any):
    matches_groups = [ (m.group(0), *m.groups()) for m in re_any.finditer(protodef) ]
    matches_text = [ tpl.format(*groups) for groups in matches_groups ]
    
    return "\n\n".join(matches_text)

tpl_file = """
---
bookCollapseSection: false
weight: 1
title: {title}
---

{services}

## Messages
{messages}

## Types
{types}
"""

tpl_proto = """
```proto
{0}
```
""".strip()

tpl_service = tpl_proto

tpl_message = """
###### `{1}` {{#{1}}}

```proto
{0}
```
""".strip()

tpl_struct = """
###### `{1}` {{#{1}}}

```proto
{0}
```
""".strip()

path = "/Users/salezica/work/dcl/protocol/proto/" + sys.argv[1]
protodef = open(path).read()

out = tpl_file.format(
    title    =  pathlib.Path(path).stem.title(),
    services = gen(protodef, tpl_service, re_service),
    messages = gen(protodef, tpl_message, re_message),
    types  = gen(protodef, tpl_struct, re_struct)
)

print(out)