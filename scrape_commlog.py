#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

def main():
    url = "https://www65.atwiki.jp/edf5/pages/121.html#id_a39e1875"
    quote_ptn = r"「([^」]+)」"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for d in soup.find_all("div", class_="plugin_include"):
        for pre in d.find_all("pre"):
            line = pre.text.replace("\n", "").replace("　", "")
            for m in re.findall(quote_ptn, line):
                print("," + m)

if __name__ == '__main__':
    main()
