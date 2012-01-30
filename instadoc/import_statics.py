
from main.models import Category, Documentation

import json
from urllib import urlopen

URL = "https://github.com/rgarcia/instacss/raw/master/static/data/"

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
    content = json.load(urlopen(URL + f['file']))

    c, created = Category.objects.get_or_create(item=f['name'])
    for item in content:
      print "processing %s" % item["title"]
      d, created = Documentation.objects.get_or_create(item=item['title'], category=c)
      d.category = c
      d.url = item['url']
      d.html = ""
      for html in item['sectionHTMLs']:
        d.html += html

      d.save()

