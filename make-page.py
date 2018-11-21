#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import json
import time
import os
import io

def isInside(menu, htmlfile):
  for entry in menu["content"]:
    if entry[u"type"] == u"page":
      if entry[u"url"] == htmlfile:
        return True
    elif entry[u"type"] == u"directory":
      if fullLink(entry, htmlfile):
        return True
  
  return False

def buildMainLink(menu, htmlfile):
  for entry in menu[u"content"]:
    if entry[u"type"] == u"page" and u"index" in entry:
      if entry[u"url"] == htmlfile:
        return u'<a class="navbar-brand active" href="' + entry[u"url"] + u'" title="' + entry[u"title"] + u'">' + entry[u"txt"] + u'</a>'
      else:
        return u'<a class="navbar-brand" href="' + entry[u"url"] + u'" title="' + entry[u"title"] + u'">' + entry[u"txt"] + u'</a>'
  return ""

def buildEntryDepth2(entry, htmlfile):
  if entry[u"type"] == u"page":
    active = " active" if htmlfile == entry[u"url"] else ""
    return '<a class="dropdown-item' + active + '" href="' + entry[u"url"] + '" title="' + entry[u"title"] + '">' + entry[u"txt"] + '</a>'
  elif entry[u"type"] == u"separator":
    return "<hr />"


def buildEntryDepth1(entry, htmlfile, idElem):
  if entry[u"type"] == u"page":
    active = " active" if htmlfile == entry[u"url"] else ""
    return '<li class="nav-item"><a class="nav-link' + active + '" href="' + entry[u"url"] + '" title="' + entry[u"title"] + '">' + entry[u"txt"] + '</a></li>'
  elif entry[u"type"] == u"directory":
    result = '<li class="nav-item dropdown">'
    active = " active" if isInside(entry, htmlfile) else ""
    result += '<a class="nav-link dropdown-toggle' + active + '" href="#" id="dropdown' + idElem + '" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">' + entry[u"txt"] + '</a>'
    result += '<div class="dropdown-menu" aria-labelledby="dropdown' + idElem + '">'
    for e in entry[u"content"]:
      result += buildEntryDepth2(e, htmlfile)
    result += '</div>'
    result += '</li>'
    return result

def buildLeftMenu(menu, htmlfile):
  result = u'<ul class="navbar-nav mr-auto">'
  for i, entry in enumerate(menu[u"content"]):
    if (not "index" in entry) and (not ("align" in entry and entry[u"align"] == "right")):
      result += buildEntryDepth1(entry, htmlfile, "0" + str(i))
  result += "</ul>"
  return result

def buildRightMenu(menu, htmlfile):
  result = '<ul class="navbar-nav float-right">'
  for i, entry in enumerate(menu[u"content"]):
    if (not "index" in entry) and ("align" in entry and entry[u"align"] == "right"):
      result += buildEntryDepth1(entry, htmlfile, "0" + str(i))
  result += "</ul>"
  return result

def buildMenu(menu, htmlfile):
  result = u'<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">'
  result += buildMainLink(menu, htmlfile)

  result += '<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>'
  
  result += '<div class="collapse navbar-collapse" id="navbarsExampleDefault">'
  
  result += buildLeftMenu(menu, htmlfile)
  
  result += buildRightMenu(menu, htmlfile)
  result += '</div></nav>'
  return result



def fullLink(menu, htmlfile):
  for entry in menu["content"]:
    if entry[u"type"] == u"page":
      if entry[u"url"] == htmlfile:
        return "index" in entry
    elif entry[u"type"] == u"directory":
      if fullLink(entry, htmlfile):
        return True
  
  return False



def buildFooter(menu, htmlfile):
  datetime = time.localtime(os.path.getmtime(htmlfile))
  mois = ["janvier", u"février", "mars", "avril", "mai", "juin", "juillet", u"août", "septembre", "octobre", "novembre", u"décembre"]
  datemodif = str(datetime[2]) + " " + mois[datetime[1]-1] + " " + str(datetime[0])
  if fullLink(menu, htmlfile):
    return u'<footer class="container"><p>&copy; Jean-Marie Favreau, <a href="http://vml-asso.org">VML</a> — dernière modification ' + datemodif + u'. Vous pouvez télécharger l\'ensemble des pages de ce site <a href="pdf/archive-cln.zip">au format pdf, compressées en zip</a>.</p></footer>'
  else:
    pdffile = htmlfile.replace(".html", ".pdf")
    return u'<footer class="container"><p>&copy; Jean-Marie Favreau, <a href="http://vml-asso.org">VML</a> — dernière modification ' + datemodif + u'. Vous pouvez télécharger cette page <a href="pdf/' + pdffile + u'">au format pdf</a>.</p></footer>'

if len(sys.argv) != 4:
  print "Erreur de paramètres"
  exit(1)


with open(sys.argv[2]) as f:
    menu = json.load(f)

pagefile = io.open(sys.argv[1], "r", encoding="utf-8")
page = pagefile.read()

page = page.replace("<cln-menu />", buildMenu(menu, sys.argv[1]))
page = page.replace("<cln-footer />", buildFooter(menu, sys.argv[1]))

outpage = io.open(sys.argv[3], "w", encoding="utf-8")
outpage.write(page)

