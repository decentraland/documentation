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
To publish [publish]({{< ref "/content/creator/deprecated/scenes/publishing/publishing.md" >}}) your scene bla bla bla
```

---

### Debugging pages values

To debug the current context of Hugo (the site renderer) you may use this snippet

{{- printf "%#v" . -}}

or

{{- printf "%#v" $ -}}

### Multi platform tabs

Tabs should be used to list content for different platforms as seen in [/content/creator/sdk7/getting-started/sdk-101.md](/content/creator/sdk7/getting-started/sdk-101.md)

```markdown
{{< tabs "open-terminal" >}}
{{< tab "Windows" >}} Right click on the Start button, then search for "_cmd_" and select the "Command Prompt". {{< /tab >}}
{{< tab "MacOS" >}} Open the Launchpad (Cmd+space) and look for "_Terminal_" {{< /tab >}}
{{< tab "Linux" >}} You already know how to do it {{< /tab >}}
{{< /tabs >}}
```

# Docker

For development with hot reload (recommended), you can use Docker Compose. This setup will automatically detect changes in your files and rebuild the site in real-time.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Steps to Run with Hot Reload

1. Make sure you have cloned the repository with submodules:
   ```bash
   git clone --recurse-submodules https://github.com/decentraland/documentation.git
   cd documentation
   ```

2. Clean up any existing Docker images and containers (if you had previous issues):
   ```bash
   docker compose down
   docker system prune -f
   ```

3. Start the development server with hot reload:
   ```bash
   # For Apple Silicon (M1/M2) Macs:
   DOCKER_DEFAULT_PLATFORM=linux/arm64 docker compose up hugo-docs

   # For Intel Macs or Linux:
   DOCKER_DEFAULT_PLATFORM=linux/amd64 docker compose up hugo-docs
   ```

4. Access the documentation at [http://localhost:1313](http://localhost:1313)

5. Any changes you make to the content, themes, or configuration files will automatically trigger a rebuild of the site.

## Additional Docker Commands

- To stop the development server:
  ```bash
  docker compose down
  ```

- To rebuild the site without serving (useful for production builds):
  ```bash
  # For Apple Silicon (M1/M2) Macs:
  DOCKER_DEFAULT_PLATFORM=linux/arm64 docker compose --profile build up hugo-build

  # For Intel Macs or Linux:
  DOCKER_DEFAULT_PLATFORM=linux/amd64 docker compose --profile build up hugo-build
  ```

- To rebuild the Docker image (if you make changes to the Dockerfile):
  ```bash
  docker compose build --no-cache
  ```

## Notes
- The development server runs with the `config-dev.toml` configuration
- Hot reload is enabled by default
- All your local files are mounted into the container, so changes are reflected immediately
- The server runs on port 1313 by default
- For Apple Silicon (M1/M2) Macs, make sure to use `linux/arm64` platform
- For Intel Macs or Linux, use `linux/amd64` platform
