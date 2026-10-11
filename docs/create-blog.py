import collections
import glob
import html
import os
import re
import urllib.parse

import markdown

BLOGS_DIR = 'blogs'
SITE_TITLE = 'João Alvim'
# og:image is read by crawlers off-site, so it has to be absolute
SITE_URL = 'https://jotaalvim.github.io'


def head(prefix, title, extra='', container='content'):
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{html.escape(title)}</title>
    <meta charset="utf-8">
    <!-- ensures proper rendering for mobile -->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="{prefix}style.css">
{extra}  </head>

  <body>

  <nav class="navbar navbar-default">
      <div class="container">
          <div class="navbar-header">
              <a class="navbar-brand" href="{prefix}index.html">
                  <div class="d-flex align-items-center">
                      <img src="{prefix}img/perfil-logo.jpg" alt="João Alvim">
                      <span class="ml-auto">{SITE_TITLE}</span>
                  </div>
              </a>
          </div>
          <ul class="nav navbar-nav navbar-right">
              <li><a href="{prefix}blog.html">Blog</a></li>
              <li><a href="{prefix}vitae.html">Curriculum Vitæ</a></li>
              <li><a href="{prefix}contact.html">Contact</a></li>
          </ul>
      </div>
  </nav>


    <div class="container {container}">
"""


FOOT = """
    <br>
    <br>
    </div>
  </body>
</html>
"""

# Clicking a keyword filters the list in place, without a page load. The links
# are real URLs (blog.html?q=haskell) so they can be shared and linked to from
# the posts; the filtering itself is this script's job.
FILTER_JS = """
    <script>
    (function () {
      var posts = Array.prototype.slice.call(document.querySelectorAll('#posts .post'));
      var keywords = Array.prototype.slice.call(document.querySelectorAll('.keyword-list .kw'));
      var empty = document.getElementById('no-results');
      var selected = '';

      function apply(kw) {
        selected = kw;
        var shown = 0;
        posts.forEach(function (post) {
          var list = post.getAttribute('data-keywords').split('|');
          var match = !kw || list.indexOf(kw) !== -1;
          post.hidden = !match;
          if (match) { shown++; }
        });
        keywords.forEach(function (link) {
          var mine = link.getAttribute('data-kw') || '';
          link.classList.toggle('active', mine === kw);
        });
        empty.hidden = shown !== 0;
      }

      keywords.forEach(function (link) {
        link.addEventListener('click', function (e) {
          if (e.metaKey || e.ctrlKey || e.shiftKey) { return; }  // let it open in a tab
          e.preventDefault();
          var kw = link.getAttribute('data-kw') || '';
          if (kw && kw === selected) { kw = ''; }  // clicking the active one clears it
          if (history.replaceState) {
            history.replaceState(null, '',
              kw ? '?q=' + encodeURIComponent(kw) : location.pathname);
          }
          apply(kw);
        });
      });

      // ?q=haskell - set by the keyword links on each post, and by a shared URL
      var q = (location.search.match(/[?&]q=([^&]*)/) || [])[1];
      apply(q ? decodeURIComponent(q.replace(/\\+/g, ' ')) : '');
    })();
    </script>
"""


def parse_post(path):
    """A post is: a date line, an optional `keywords:` line, a `# Title`, then the body."""
    with open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')

    def skip_blanks():
        while lines and not lines[0].strip():
            lines.pop(0)

    date = lines.pop(0).strip() if lines else ''
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date):
        print(f'  warning: {path} does not start with a YYYY-MM-DD date (got {date!r})')

    skip_blanks()
    keywords = []
    if lines and lines[0].lower().startswith('keywords:'):
        raw = lines.pop(0).split(':', 1)[1]
        keywords = [k.strip() for k in raw.split(',') if k.strip()]
    else:
        print(f'  warning: {path} has no `keywords:` line')

    skip_blanks()
    title = lines.pop(0).lstrip('#').strip() if lines else ''

    body = markdown.markdown('\n'.join(lines))
    # posts write images as /img/foo.png, which only resolves once the site is
    # served with docs/ as its root; relative paths work locally too
    body = body.replace('src="/img/', 'src="../img/')
    return {
        'date': date,
        'title': title,
        'keywords': keywords,
        'body': body,
        'url': f"{BLOGS_DIR}/{os.path.basename(path)[:-3]}.html",
    }


def keyword_url(prefix, keyword):
    return f"{prefix}blog.html?q={urllib.parse.quote_plus(keyword)}"


def render_post(post):
    description = f"{post['title']} - {post['date']}"
    meta = f"""    <meta name="keywords" content="{html.escape(', '.join(post['keywords']))}">
    <meta name="description" content="{html.escape(description)}">
    <meta property="og:title" content="{html.escape(post['title'])}">
    <meta property="og:description" content="{html.escape(description)}">
    <meta property="og:image" content="{SITE_URL}/img/rubiks2.png">
"""
    tags = ''.join(
        f'<a class="tag" href="{keyword_url("../", k)}">{html.escape(k)}</a>'
        for k in post['keywords']
    )
    header = f"""
      <h1>{html.escape(post['title'])}</h1>
      <p class="post-meta">
        <span class="date">{post['date']}</span>
        {tags}
      </p>
"""
    page_title = f"{post['title']} — {SITE_TITLE}" if post['title'] else SITE_TITLE
    return head('../', page_title, meta) + header + post['body'] + FOOT


def render_index(posts):
    rows = []
    for post in posts:
        keys = html.escape('|'.join(post['keywords']))
        rows.append(f"""          <a class="post" href="{post['url']}" data-keywords="{keys}">
            <span class="post-date">{post['date']}</span>
            <span class="post-title">{html.escape(post['title'])}</span>
          </a>
""")

    counts = collections.Counter(k for post in posts for k in post['keywords'])
    # most used first, alphabetical within the same count
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    links = [f"""          <a class="kw kw-all" href="blog.html" data-kw="">all posts<span class="count">{len(posts)}</span></a>
"""]
    links += [
        f"""          <a class="kw" href="{keyword_url('', k)}" data-kw="{html.escape(k)}">{html.escape(k)}<span class="count">{n}</span></a>
"""
        for k, n in ordered
    ]

    body = f"""
      <div class="blog-layout">

        <div id="posts">
{''.join(rows)}          <p id="no-results" class="no-results" hidden>No posts with that keyword.</p>
        </div>

        <aside class="keyword-list">
          <h2>keywords</h2>
{''.join(links)}        </aside>

      </div>
{FILTER_JS}"""
    return head('', f'Blog — {SITE_TITLE}', container='content content-wide') + body + FOOT


def main():
    paths = sorted(glob.glob(os.path.join(BLOGS_DIR, '*.md')))
    print(f'{len(paths)} posts found')

    posts = []
    for path in paths:
        print(path)
        post = parse_post(path)
        with open(post['url'], 'w', encoding='utf-8') as f:
            f.write(render_post(post))
        posts.append(post)

    posts.sort(key=lambda p: p['date'], reverse=True)
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(render_index(posts))
    print('blog.html written')


if __name__ == '__main__':
    main()
