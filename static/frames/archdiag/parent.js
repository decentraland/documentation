// Parent initialization script for the architectural diagram iFrame.
// Requires a pre-existing iFrame element, and should be included with a <script> tag like this one:
//
// <script 
//   src="/frames/archdiag/init.js" 
//   data-iframe-id="<id the iframe element>">
// </script>

(function() {
  // Locate the frame referenced in this <script>:
  const iframe = document.getElementById(document.currentScript.dataset.iframeId)
  
  // Observe layout changes and automatically resize iframe to fit its own content:
  iframe.onload = () => {
    const onResize = () => {
      iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px'
    }

    new ResizeObserver(onResize).observe(iframe)
  }

  // Receive click messages from the diagram's iframe, and navigate:
  window.addEventListener('message', event => {
    const msg = event.data

    // Our messages are strings, so verify that first:
    if (typeof msg !== 'string') return

    // In particular, they contain colon-separated segments, like so:
    //   "<id>:<event>:<...extra segments>"

    // All messages are clicks at this point, so let's KISS :)
    const prefix = `${iframe.id}:click:`
    if (!msg.startsWith(prefix)) return

    // Handle the thing:
    const targetId = msg.slice(prefix.length)

    window.location.hash = targetId // for linking
    document.getElementById(targetId).scrollIntoView() // to actually move
  })
})()
