import time

header = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>TEST emoticons</title>
    <!--[if lt IE 9]>
      <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <link href='http://fonts.googleapis.com/css?family=Varela+Round&v2' rel='stylesheet' type='text/css'>
    <link href="/screen.css" rel="stylesheet" type="text/css">
    <link href="/favicon.png" rel="shortcut icon">
  </head>
  <body>
    <header>
      <h1>TEST emoticons</h1>
      <p>
        A complete list of
        <strong>%(count)s</strong>
        <a href="https://forum.pleaseignore.com/topic/200-jabber-emote-packs-most-clients-updated-dec-19-2011/">TEST Alliance</a> emoticons.
        Click to copy.
      </p>
    </header>
    <div class="emoticons">
"""

item = """
      <a href="%(text)s" onclick=' prompt("Copy this:", "%(text)s"); return false;'>
        <img alt="%(text)s" src="%(img)s" style="height:18px" title="%(text)s">
        <div class="shortcut">%(text)s</div>
      </a>
"""

footer = """
    </div>
    <footer>
      <p>
        Last updated %(date)s.
      </p>
      <p>
        By <a href="https://coderanger.net/">Noah Kantrowitz</a> (with styling and layout by <a href="http://henrik.nyh.se">Henrik Nyh</a>).
      </p>
      <p>
        <a href="https://github.com/coderanger/testemote">View source on GitHub</a>.
      </p>
    </footer>
  </body>
</html>
"""
def main():
    theme = open('pack/theme')
    for line in theme:
        if line.strip() == '[default]':
            break
    emotes = {}
    for line in theme:
        line = [s.strip() for s in line.split()]
        emotes[line[1]] = line[0]
    out = open('index.html', 'w')
    out.write(header % {'count': len(emotes)})
    for text, img in sorted(emotes.iteritems()):
        out.write(item % {'text': text, 'img': '/pack/%s'%img})
    out.write(footer % {'date': time.strftime('%Y-%m-%d')})

if __name__ == '__main__':
    main()