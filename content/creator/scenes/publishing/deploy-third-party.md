---
date: 2018-01-01
title: Preview in Heroku
description: Upload a preview of your scene to a server and share it offchain.
aliases:
  - /deploy/deploy-to-now/
  - /development-guide/deploy-to-now/
  - /development-guide/deploy-third-party/
categories:
  - development-guide
type: Document
url: /creator/development-guide/deploy-third-party
---

{{< hint warning >}}
**📔 Note**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/publishing/deploy-third-party.md" >}}).
{{< /hint >}}

If you do not possess any parcels in Decentraland or a Decentraland [NAME](https://builder.decentraland.zone/names) to publish your scene to a [World]({{< ref "/content/creator/worlds/about.md" >}}), or if you are not yet prepared to [deploy]({{< ref "/content/creator/scenes/publishing/publishing.md#the-test-server" >}}) your scene to Decentraland, there is an alternative option available. You can upload a preview of your scene to run as an application on server.

Once uploaded, the only thing that others have to do to explore your scene is follow a link. They don’t need to install the CLI, Node, NPM, or any of the other tools that would be required to run the preview on their local machine.

Note that it's not necessary to own LAND to upload a scene preview to a Heroku server. The uploaded content isn't linked to the blockchain in any way. When running the preview, other adjacent parcels appear as empty.

Follow the steps below to upload your scenes to a Heroku server:

1. Make sure you have the latest Decentraland CLI version installed on your machine `npm i -g decentraland@latest`.

2. Create a [Heroku](https://dashboard.heroku.com/) account, if you don't already have one.

3. Install the Heroku CLI. Do this via `npm i -g heroku`, or see [their documentation](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) for alternatives.

4. Create a git repository for your project. Use any tool you prefer for this, like [GitHub desktop](https://desktop.github.com/). To use git from the command line:

   a) Create a new repository by running `git init` in the project folder at root level

   b) Do `git add .` and `git commit -m 'your commit text`

   c) Set the current branch to _main_ via `git branch -m master main`

   d) Make sure the `.gitignore` file contains the following:

   ```
   /node_modules
   npm-debug.log
   .DS_Store
   /*.env
   bin
   ```

   > Note: Make sure your Decentraland project uses the latest SDK version, do `npm i decentraland-ecs@latest`. Projects uploaded to Heroku or similar platformas and built with versions older than 6.10.0 will not be supported and will not be allowed to fech avatar data from content servers.

   > Note: If you're deploying a project that was created using `dcl init`, you would need to remove the line `"yarn": "please use npm"` from your `package.json` file otherwise you're going to get an error while deploying.

5. Use the Heroku CLI to log into your Heroku account with `heroku login`. This opens a browser window to provide your user and password.

6. Create a new Heroku application and give it a unique name. In the Heroku site do that via **New** > **Create new App**. Otherwise, in the Heroku CLI do it via `heroku create -a example-dcl-scene`

7. Link your Decentraland project to your Heroku application. On the project folder run `heroku git:remote -a example-dcl-scene` (using the name you created you heroku application with)

8. Edit `package.json` in your scene to change the `start` script to `CI=true dcl start -p ${PORT:=8000}`

9. Explicitly install the Decentraland CLI as a dependency of your project, running `npm i --save decentraland`

10. Deploy your scene preview with `git push heroku main`

11. To access the scene, copy the link shared by the Heroku deploy command. Then manually add the following parameters to the URL `?realm=localhost-stub&explorer-branch=main`.

    For example if the link shared by Heroku is `https://example-dcl-scene.herokuapp.com`, the link you should enter is `https://example-dcl-scene.herokuapp.com/?realm=localhost-stub&explorer-branch=main`.

    If your scene is not in coordinates `0,0`, you should also include these as part of the URL. For example: `https://example-dcl-scene.herokuapp.com/?realm=localhost-stub&explorer-branch=main&position=50,-10`

Every time you make changes to your scene, make sure you:

- Commit and push your changes to the git repo
- Push the new version to the Heroku app `git push heroku main`

You can read the console logs of the scene preview by running `heroku logs --tail`
