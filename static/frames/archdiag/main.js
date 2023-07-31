
document.querySelectorAll(".box > .cover").forEach(el => {
  return // click-to-cover functionality is disabled. Leaving this here in case we change our minds.

  const expanded = { minWidth: '100%', minHeight: '100%' }
  const contracted = { minWidth: '0', minHeight: '0' }

  const durationStr = getComputedStyle(document.documentElement)
    .getPropertyValue('--animation-short')
    .slice(0, -1)

  const options = {
    duration: parseFloat(durationStr) * 1000,
    fill: 'both',
    easing: 'ease-out'
  }

  el.onclick = () => {
    let animation

    if (el.classList.contains('expanded')) {
      animation = el.animate([ expanded, contracted ], options)
      el.classList.remove('expanded')

    } else {
      animation = el.animate([ contracted, expanded ], options)
      el.classList.add('expanded')
    }

    el.classList.add('animating')
    animation.finished.then(() => el.classList.remove('animating'))
  }
})

function onBoxClick(id) {
  window.parent.postMessage(`${window.frameElement.id}:click:${id}`)
}
