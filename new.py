#! /usr/bin/env python

import os, sys

entryname=sys.argv[1]
exec("from %s import *"%entryname)

with open("./header.html","r") as f:
  header=f.read().replace("$title$", entry_title)

with open("./footer.html","r") as f:
  footer=f.read()

try: os.mkdir(entryname)
except:
  if raw_input("folder exists. overwrite? [y/n]")!="y": 
    exit()
    
with open("./%s/index.html"%entryname,"w+") as f:
  f.write(header+entry_text+footer)