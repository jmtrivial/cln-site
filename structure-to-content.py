#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys
import json
import time
import os
import io
from bs4 import BeautifulSoup


def build_contents(structure):
    result = []
    for entry in structure:
        if entry[u"type"] == u"page":
            result.append(entry)
        elif entry[u"type"] == u"directory":
            result += build_contents(entry[u"content"])
    return result


with open(sys.argv[1]) as f:
    structure = json.load(f)

entrees = build_contents(structure["content"])



for entree in entrees:
    html = open(entree["url"], "r")
    soup = BeautifulSoup(html, 'html.parser')
    entree["content"] = soup.get_text()
    entree["summary"] = " ".join([el.get_text() for el in soup.find_all("p", { "class": "lead"})])

json_object = json.dumps(entrees, indent=4)
with open(sys.argv[2], "w") as outfile:
    outfile.write(json_object)
