
from main.models import Category, Documentation

import json
from urllib import urlopen

URL = "https://raw.githubusercontent.com/rgarcia/dochub/master/static/data/"

FILES = [
  dict(
    name="python",
    file="python.json",
  ),
  dict(
    name="css",
    file="css-mdn.json",
  ),
  dict(
    name="html",
    file="html-mdn.json",
  ),
  dict(
    name="javascript",
    file="js-mdn.json",
  ),
  dict(
    name="jquery",
    file="jquery.json",
  ),
]


def importing():
  for f in FILES:
    try:
      content = json.load(open(f['file']))
    except:
      content = json.load(urlopen(URL + f['file']))

    c, created = Category.objects.get_or_create(item=f['name'])
    for item in content:
      if not item['title']:
        continue

      print "processing %s" % item["title"]
      d, created = Documentation.objects.get_or_create(item=item['title'], category=c)
      d.category = c
      d.url = item['url']
      d.html = ""

      html = 'html'
      if 'sectionHTMLs' in item:
        html = 'sectionHTMLs'

      for html in item[html]:
        d.html += html

      d.save()

