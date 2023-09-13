---
title: 'Quest HUD - SDK UI'
url: /creator/quests/quest-ui
weight: 5
---

The [Quests Client library]({{< ref "/content/creator/sdk7/quests/client.md" >}}) provides a default UI (HUD). This displays the player's progress, listing the steps in the quest and their status.

This default UI is highly customizable, but you can also build your own UI, entirely from scratch.

## HUD Properties

This HUD is fully-customizable. Below are the full set of options that can be set up:

```typescript
type LabelProps = EntityPropTypes & UiLabelProps

export type QuestHudOptions = {
  autoRender?: boolean
  leftSidePanel?: UiTransformProps
  questBox?: {
    uiBackground?: UiBackgroundProps
    uiTransform?: UiTransformProps
  }
  questNameContainer?: {
    uiTransform?: UiTransformProps
    label?: LabelProps
  }
  stepsContainer?: {
    uiTransform: UiTransformProps
    labels?: {
      labelUiEntity?: UiTransformProps
      props?: LabelProps
    }
    showTasksButton?: {
      buttonUiEntity: UiTransformProps
      buttonProps?: UiButtonProps
    }
  }
  tasksBox?: {
    uiTransform?: UiTransformProps
    uiBackground?: UiBackgroundProps
    labels?: {
      labelUiEntity?: UiTransformProps
      props?: LabelProps
    }
  }
  nextSteps?: {
    nextTitleUiEntity?: UiTransformProps
    nextTitleProps?: LabelProps
    labels?: {
      labelUiEntity?: UiTransformProps
      props?: LabelProps
    }
  }
  questCompletionLabel?: {
    uiTransform?: UiTransformProps
    label?: LabelProps
  }
  showHideToggleButton?: UiButtonProps
  closeTasksBoxButton?: UiButtonProps
}
```

- `autoRender`: If `true`, the HUD is rendered automatically. If `false`, you will need to call the `render` function to render the HUD. By default, it's **not** rendered automatically.

- `leftSidePanel`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify the `UiEntity` containing the box that contains all the Quest progress and the "Hide/Show" toggle button. In web terms, this would be the div acting as a container for the box and button.

- `questBox`: An object that contains two fields:

  - `uiBackground`: The `UiBackgroundProps` type from `@dcl/sdk/react-ecs`. Use this to modify the background of the `UiEntity` containing the box with the Quest name and steps. In web terms, this would be the `div` acting as a container for the Quest name and steps.
  - `uiTransform`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify the `UiEntity` containing the box with the Quest name and steps. In web terms, this would be the `div` acting as a container for the Quest name and steps.

- `questNameContainer`: An object that contains two fields:

  - `uiTransform`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify the `UiEntity` containing the Quest name. In web terms, this would be the `div` acting as a container for the Quest name.
  - `label`: The `LabelProps` type defined in the snippet above. Use this to modify the `Label` with the Quest name. In web terms, this would be the `p` tag containing the Quest name.

- `stepsContainer`: An object that contains three fields:

  - `uiTransform`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify the `UiEntity` listing the steps and their `description`. In web terms, this would be the `div` acting as a container for the steps.
  - `labels`: An object that contains two fields:
    - `labelUiEntity`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify every `UiEntity` that contains the step's `description` and the "Show Tasks" button. In web terms, this would be the `div` acting as a container for the step's `description` and the "Show Tasks" button.
    - `props`: The `LabelProps` type defined in the snippet above. Use this to modify every `Label` containing the step's `description`. In web terms, this would be the `p` tag containing the step's `description`.
  - `showTasksButton`: An object that contains two fields:
    - `buttonUiEntity`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify every `UiEntity` containing the "Show Tasks" button. In web terms, this would be the `div` acting as a container for the "Show Tasks" button.
    - `buttonProps`: The `UiButtonProps` type from `@dcl/sdk/react-ecs`. Use this to modify all the "Show Tasks" `Button`s.

- `tasksBox`: An object that contains three fields:

  - `uiTransform`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify every `UiEntity` containing and listing each step tasks with their `description`. In web terms, this would be the `div` acting as a container for a step tasks.
  - `uiBackground`: The `UiBackgroundProps` type from `@dcl/sdk/react-ecs`. Use this to modify the background of every `UiEntity` listing each step tasks with their `description`. In web terms, this would be the `div` acting as a container for the tasks.
  - `labels`: An object that contains two fields:
    - `labelUiEntity`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify every `UiEntity` containing the task's `description`. In web terms, this would be the `div` acting as a container for the task's `description`.
    - `props`: The `LabelProps` type defined in the snippet above. Use this to modify every `Label` containing the task's `description`. In web terms, this would be the `p` tag containing the task's `description`.

- `nextSteps`: An object that contains three fields:

  - `nextTitleUiEntity`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify the `UiEntity` containing the "Next Steps" title. In web terms, this would be the `div` acting as a container for the "Next Steps" title.
  - `nextTitleProps`: The `LabelProps` type defined in the snippet above. Use this to modify the `Label` containing the "Next Steps" title. In web terms, this would be the `p` tag containing the "Next Steps" title.
  - `labels`: An object that contains two fields:
    - `labelUiEntity`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify every `UiEntity` containing the next step's `description`. In web terms, this would be the `div` acting as a container for the next step's `description`.
    - `props`: The `LabelProps` type defined in the snippet above. Use this to modify every `Label` containing the next step's `description`. In web terms, this would be the `p` tag containing the next step's `description`.

- `questCompletionLabel`: An object that contains two fields:

  - `uiTransform`: The `UiTransformProps` type from `@dcl/sdk/react-ecs`. Use this to modify the `UiEntity` containing the Quest completion label. In web terms, this would be the `div` acting as a container for the Quest completion label.
  - `label`: The `LabelProps` type defined in the snippet above. Use this to modify the `Label` containing the text that lets the users know they have completed the Quest. In web terms, this would be the `p` tag containing the text noticing the completion of the Quest.

- `showHideToggleButton`: The `UiButtonProps` type from `@dcl/sdk/react-ecs`. Use this to modify the "Hide" and "Show Quest Progress" toggle `Button`. In web terms, this would be the `button` tag.

- `closeTasksBoxButton`: The `UiButtonProps` type from `@dcl/sdk/react-ecs`. Use this to modify the "Close" `Button` that appears when the user clicks on the "Show Tasks" `Button`. In web terms, this would be the `button` tag.

## Methods of the QuestHUD object

Once you created a Quest HUD with `createQuestHUD()`, you're returned a `QuestHUD` object. This object has the following methods:

```typescript
type QuestHUD = {
  upsert: (instance: QuestInstance) => void
  getHUDComponent: () => () => ReactEcs.JSX.Element
  render: () => void
  updateOptions: (opts: QuestHudOptions) => void
  getHUDComponentWithUpdatedOptions: (
    newOpts: QuestHudOptions
  ) => () => ReactEcs.JSX.Element
}
```

- `upsert`: Update the Quest HUD with the player's progress, you may want to call it when the users starts the Quest and when they make some progress. Also when the player loads into the scene with the quest already partially completed. This function receives a `QuestInstance` object. It creates an entity with this data to be used by a ReactECS UI component. This component is rendered in the scene UI, displaying the Quest progress.

- `getHUDComponent`: Get the ReactECS UI component that renders a ready-to-use Quest HUD. This is useful when you already have a UI to render, since `ReactEcsRenderer.setUiRenderer` overrides everything that previously exists.

- `render`: Render the Quest HUD. You may want to call this function when you have the `autoRender` option set to `false` and you want to render the Quest HUD manually.

<!--(TODO: check if recalling it when entity updates is needed.)  -->

To use it, import the `createQuestHUD` function from `@dcl/quests-client/dist/hud`. For example:

```typescript
// index.ts

//...
import { executeTask } from '@dcl/sdk/ecs'
import { createQuestsClient, QuestInstance } from '@dcl/quests-client'
import { createQuestHUD } from '@dcl/quests-client/dist/hud'

const questHud = createQuestHUD()

const MY_QUEST_ID = 'quest-id-1234-5678-9012'

executeTask(async () => {
  const serviceUrl = 'wss://quests-rpc.decentraland.zone'

  try {
    const questsClient = await createQuestsClient(serviceUrl, MY_QUEST_ID)
    console.log('Quests Client is ready to use!')

    client.onStarted((quest: QuestInstance) => {
      // react to the start of your Quest
      questHud.upsert(quest)
    })

    client.onUpdate((quest: QuestInstance) => {
      // update your state here to react to the quest updates
      questHud.upsert(quest)
    })
  } catch (e) {
    console.error('Error on connecting to Quests Service')
  }
})
```

The above code creates a default Quest HUD object, with no customization. You can find the defaults in the code [here](https://github.com/decentraland/quests-client/blob/main/src/hud.tsx), or render the HUD to see how it looks.

When the quest is stated or it receives any player progress update, the `questHud.upsert` function is called to update this UI. This function receives a `QuestInstance` object. It creates an SDK entity with this data to be used by a ReactECS UI component. This component is rendered in the scene UI, displaying the Quest progress, including which steps and tasks are completed or not.

### Customizing the Quest HUD

```typescript
// index.ts

//....
const questHud = createQuestHUD({
  autoRender: true,
  leftSidePanel: {
    position: { top: '8%' },
  },
  questBox: {
    uiBackground: {
      color: Color4.fromHexString('ff2d5382'),
    },
  },
})

//....
//....
```

The above code creates a customized Quest HUD. This HUD is rendered automatically, so it's updated whenever the player starts the Quest or makes progress or the `upsert` function is called.

This Quest HUD is configured to be rendered `8%` far from the top of the screen. This works well in Worlds, where there is no minimap. The default is `28%` places the quest HUD below the height of the minimap, ideal for quests inside Genesis Plaza.

This example also sets the Quest box background color to `#ff2d5382`. This is the primary color of Decentraland (a light red), with almost 50% of opacity.

You are free to use the SDK to create your own custom UI to display quest progress based on this same information. See [Onscreen UI]({{< ref "/content/creator/sdk7/2d-ui/onscreen-ui.md" >}}) for guidance about how to do this.
