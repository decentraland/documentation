---
title: "Content API with Python"
bookhidden: true
url: "/contributor/content/practice/python"
---

This practice shows how to write a simple program that downloads and analyzes some content using the [snapshots]({{< relref "snapshots" >}}) provided by content servers.

{{< info >}}
You can find the [full script](https://github.com/decentraland/documentation/blob/main/content/contributor/content/practice/snapshots_mini.py) in GitHub, along with a [more advanced example](https://github.com/decentraland/documentation/blob/main/content/contributor/content/practice/snapshots.py).
{{< /info >}}

We'll be using the Decentraland Foundation's server at `peer.decentraland.org`, and Python 3 as our language of choice. 

This is what we'll do:

1. Query the status of the content server.
2. Select and download a [snapshot]({{< relref "snapshots" >}}) with a list of entities.
3. Print the type and ID of all referenced entities.

Let's begin our script with some preparations. We'll use standard library modules only, but in real code you'll probably want a more comfortable HTTP client (like the [requests](https://github.com/psf/requests) library).

```py
# Make an HTTP GET request, return a file-like HTTP response.
def fetch(path):
    url = f"https://peer.decentraland.org/{path}"
    headers = { "User-Agent": "urllib" } # important on some servers (if empty, 403 Forbidden)

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)

    return response
```

Our simple helper makes an HTTP `GET` request, and returns the file-like response object. Nothing fancy. Let's use it to hit the `/about` endpoint and check the server's status:

```py
# Check the server status:
about = json.load(fetch('about'))

if not about['healthy']:
    print("Server not healthy!")
    sys.exit(1)
```

If we get past this point, the server is up and running (we got a `200` response) and reports being operational. We can request the current set of snapshots (which comes in JSON array format):

```py
# Get the list of snapshots:
all_snapshots = json.load(fetch('content/snapshots'))
```

Snapshot files (especially for the longer time ranges) can be very large. For a quick experiment, let's grab the smallest in the list by `numberOfEntities`:

```py
# Take the smallest snapshot, in terms of included entities:
snapshot = min(all_snapshots, key=lambda s: s['numberOfEntities'])
```

To download the content, we need the `hash` field of `snapshot`. We get the file URL by appending it to the content root:

```py
# Request the file from the content API:
response = fetch('content/contents/' + snapshot['hash'])
```

The file we selected is small enough to buffer in memory, but let's pretend we don't know that and stream it. The first line is the snapshot header, and every line after that contains a JSON object.

Let's check the header, always a good idea:

```py
# Verify the snapshot header:
header = response.readline().decode('utf-8').strip()

if header != '### Decentraland json snapshot':
    print("Invalid snapshot header: " + header)
    sys.exit(1)
```

Now we can process all entities in the snapshot, reading the response line by line. For our humble purposes, _process_ means printing the entity type and ID:

```py
# Read and decode all items, one JSON per line:
for line in response:
    item = json.loads(line)
    print(item['entityType'], item['entityId'])
```

This loop will start streaming, parsing and printing lines like these until it's done with the snapshot:

```
profile bafkreic36qmzyprs6whkpuxbeiif4no6kvdrr2tfpichbx2fzfz5py6eyv
scene bafkreibr5xfujqrp5q3o4s73vm2yljlcp7cucqgugssnarsuclxv4emlmy
profile bafkreid7khr5wnkialba44rsslffi633rh3lvctad5oa5vjoe6wa7s4c5a
wearable bafkreihlqcb7jgubomyidikpwpqhgzbagltk5m4rgbjdvzydxmoka7bg4i
```

Cheers! We've used the snapshot system to explore some of the available content in Decentraland.

Remember you can find the [full script](https://github.com/decentraland/documentation/blob/main/content/contributor/content/practice/snapshots_mini.py) in GitHub, along with a [more advanced example](https://github.com/decentraland/documentation/blob/main/content/contributor/content/practice/snapshots.py).

