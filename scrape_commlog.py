#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

QUOTE_PTN = r"「([^」]+)」"

def main():
    url_edf4 = "https://www50.atwiki.jp/edf_4/pages/309.html"
    url_edf5 = "https://www65.atwiki.jp/edf5/pages/121.html"
    scrape_communication_log_page(url_edf4, 4)
    scrape_communication_log_page(url_edf5, 5)

def scrape_communication_log_page(url, edf_version):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for d in soup.find_all("div", class_="plugin_include"):
        for pre in d.find_all("pre"):
            line = pre.text.replace("\n", "").replace("　", "")
            for m in re.findall(QUOTE_PTN, line):
                print("%d,%s" % (edf_version, m))

if __name__ == '__main__':
    main()
