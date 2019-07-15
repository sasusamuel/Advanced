from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
   <p>I like python</p>
  </body>
</htlm>
"""

soup = beautifulSoup(html_doc, 'html.parser')
