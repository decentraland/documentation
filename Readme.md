Docs web
https://docs.decentraland.org/

Set up local environment
Install Hugo locally
Clone this repository (including the submodules)
git clone --recurse-submodules https://github.com/decentraland/documentation.git
Run hugo serve to preview changes locally and follow the instructions in the terminal to open a browser
Links syntax
[Link to page]({{< ref "/content/subsection/page.md" >}})

More info: https://gohugo.io/content-management/cross-references/

To publish [publish]({{< ref "/content/creator/scenes/publishing/publishing.md" >}}) your scene bla bla bla
Debugging pages values
To debug the current context of Hugo (the site renderer) you may use this snippet

{{- printf "%#v" . -}}

or

{{- printf "%#v" $ -}}

Multi platform tabs
Tabs should be used to list content for different platforms as seen in /content/creator/scenes/getting-started/sdk-101.md

{{< tabs "open-terminal" >}}
{{< tab "Windows" >}} Right click on the Start button, then search for "_cmd_" and select the "Command Prompt". {{< /tab >}}
{{< tab "MacOS" >}} Open the Launchpad (Cmd+space) and look for "_Terminal_" {{< /tab >}}
{{< tab "Linux" >}} You already know how to do it {{< /tab >}}
{{< /tabs >}}
