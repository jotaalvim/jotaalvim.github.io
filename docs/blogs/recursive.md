2026-10-15
keywords: recursion, functional programming, infinity 
# Recursive Blog

I find the idea that a procedure can be applied to itself repeatedly astonishing. It fascinates me profoundly as it seems like magic how
recursion even works. Whether it's on functional programming or in fractals like the [Mandelbrot set](https://websim.com/@ticksclone/fractal-explorer-4)
there's an undeniable beauty in those patterns. The hard thing  with recursion is not applying a function to itself but rather when to stop apllying it. Even I don't know when to stop

<button id="loadBtn">Here's a good reference on the subject</button>


<iframe
  id="myIframe"
  width="100%"
  height="600px"
  style="border: none;">
</iframe>

<script>
  const btn = document.getElementById('loadBtn');
  const iframe = document.getElementById('myIframe');

  btn.addEventListener('click', () => {

    // Browsers block a URL already loaded by more than one ancestor frame so give each nesting level a different query string
    const depth = Number(new URLSearchParams(location.search).get('depth') || 0);

    iframe.src = location + '?depth=' + (depth + 1);

    btn.disabled = true;
  });
</script>
