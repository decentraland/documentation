# Docs web
[https://docs.decentraland.org/](https://docs.decentraland.org/)

# Set up local environment

1. [Install Hugo locally](https://gohugo.io/getting-started/installing/)
2. Clone this repository (including the submodules)
   ```
   git clone --recurse-submodules https://github.com/decentraland/documentation.git
   ```
3. Run `hugo serve` to preview changes locally and follow the instructions in the terminal to open a browser

# Links syntax

`[Link to page]({{< ref "/content/subsection/page.md" >}})`

More info: https://gohugo.io/content-management/cross-references/

```markdown
To publish [publish]({{< ref "/content/creator/scenes/publishing/publishing.md" >}}) your scene bla bla bla
```

---

### Debugging pages values

To debug the current context of Hugo (the site renderer) you may use this snippet

  {{- printf "%#v" . -}}

  or

  {{- printf "%#v" $ -}}


### Multi platform tabs

Tabs should be used to list content for different platforms as seen in [/content/creator/scenes/getting-started/sdk-101.md](/content/creator/scenes/getting-started/sdk-101.md)

```markdown
{{< tabs "open-terminal" >}}
{{< tab "Windows" >}} Right click on the Start button, then search for "_cmd_" and select the "Command Prompt". {{< /tab >}}
{{< tab "MacOS" >}} Open the Launchpad (Cmd+space) and look for "_Terminal_" {{< /tab >}}
{{< tab "Linux" >}} You already know how to do it {{< /tab >}}
{{< /tabs >}}
```
