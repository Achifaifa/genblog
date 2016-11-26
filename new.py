#! /usr/bin/env python

import os, sys
import markdown

entryname=sys.argv[1]
exec("from %s import *"%entryname)

# Get header and footer from files, modify entry title
with open("./header.html","r") as f:
  header=f.read().replace("$title$", entry_title)
with open("./footer.html","r") as f:
  footer=f.read()

# Create new folder for the entry
try: 
  os.mkdir(entryname)

  # If folder (that is, entry) exists, create new entry in blog index
  with open("./index.html","r") as f:
    index=f.read()
  index=index.replace("<!--newentry-->","<!--newentry-->\n<li> <a href='%s'>%s</a> (%s)<br/> "%(entryname, entry_title, entry_date))
  with open("./index.html","w+") as f:
    f.write(index)
except:
  if raw_input("folder exists. overwrite? [y/n]")!="y": 
    exit()

# Compose entry
entry=markdown.markdown(entry_text.decode("UTF-8"), extensions=['fenced_code']).replace("<pre>","<pre style='margin:50;'>")
entry=header+entry+footer

# Write entry to file
with open("./%s/index.html"%entryname,"w+") as f:
  f.write(entry)