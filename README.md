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
