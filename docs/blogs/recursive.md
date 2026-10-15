2026-10-15
keywords: recursion, functional programming, infinity 
# Recursive Blog

I find the idea that a procedure can be applied to itself repeatedly astonishing. It fascinates me profoundly as it seems like magic how
recursion even works. Whether it's on functional programming or in fractals like the [Mandelbrot set](https://websim.com/@ticksclone/fractal-explorer-4)
there's an undeniable beauty in those patterns. The hard thing  with recursion is not applying a function to itself but rather when to stop applying it. Even I don't know when to stop

<button id="loadBtn">Here's a good reference on the subject</button>

<div id="frameBox" class="recursion" hidden>
<iframe id="myIframe" title="This page, one level deeper" scrolling="no"></iframe>
</div>

<style>
  /* each level is drawn smaller than the one around it, so the nesting shows at a glance */
  .recursion {
    margin-top: 14px;
    overflow: hidden;
    border-radius: 6px;
    /* a shadow, not a border: a border would eat into the height set from the script */
    box-shadow: 0 0 0 1px #ccc, 0 6px 18px rgba(0, 0, 0, .15);
  }

  /* laid out wider than the box, then scaled down to fit it */
  .recursion iframe {
    display: block;
    border: 0;
    width: calc(100% / var(--scale));
    transform: scale(var(--scale));
    transform-origin: 0 0;
  }
</style>

<script>
  const SCALE = 0.7;
  const btn = document.getElementById('loadBtn');
  const box = document.getElementById('frameBox');
  const iframe = document.getElementById('myIframe');
  box.style.setProperty('--scale', SCALE);

  // every level runs this same script, so each page stretches the frame it sits in
  // to its full height and there is nothing to scroll inside a frame
  if (window.frameElement) {
    new ResizeObserver(() => {
      window.frameElement.style.height = document.documentElement.offsetHeight + 'px';
    }).observe(document.documentElement);
    // shown whole, so any scroll offset would only hide the top of the page
    addEventListener('scroll', () => scrollTo(0, 0));
  }

  // transform doesn't change layout, so the box is shrunk to the scaled height by hand
  new ResizeObserver(() => {
    box.style.height = iframe.offsetHeight * SCALE + 'px';
  }).observe(iframe);

  btn.addEventListener('click', () => {

    // Browsers block a URL already loaded by more than one ancestor frame so give each nesting level a different query string
    const depth = Number(new URLSearchParams(location.search).get('depth') || 0);
    const url = new URL(location.href);
    url.searchParams.set('depth', depth + 1);

    // bring the new level into view by scrolling the outermost page only:
    // map the box's position up through each scaled frame. Waits a moment so
    // the frames have grown first, or the page is still too short to scroll that far
    iframe.addEventListener('load', () => setTimeout(() => {
      let y = box.getBoundingClientRect().top;
      for (let w = window; w.frameElement; w = w.parent) {
        y = w.frameElement.getBoundingClientRect().top + y * SCALE;
      }
      top.scrollBy({ top: y - 10, behavior: 'smooth' });
    }, 250), { once: true });

    iframe.src = url;
    box.hidden = false;
    btn.disabled = true;
  });
</script>
