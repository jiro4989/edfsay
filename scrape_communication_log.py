#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re, time

QUOTE_PTN = r"「([^」]+)」"

def main():
    url_edf3 = "https://www21.atwiki.jp/edf_3/pages/%d.html"
    for i in [50, 51, 53, 54, 55]:
        url = url_edf3 % i
        scrape_communication_log_page_for_EDF3(url, "EDF3")
        time.sleep(1)

    url_edf4 = "https://www50.atwiki.jp/edf_4/pages/309.html"
    url_edf5 = "https://www65.atwiki.jp/edf5/pages/121.html"
    scrape_communication_log_page(url_edf4, "EDF4")
    scrape_communication_log_page(url_edf5, "EDF5")

def scrape_communication_log_page(url, edf_version):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for d in soup.find_all("div", class_="plugin_include"):
        for pre in d.find_all("pre"):
            line = pre.text.replace("\n", "").replace("　", "")
            for m in re.findall(QUOTE_PTN, line):
                print("%s,%s" % (edf_version, m))

def scrape_communication_log_page_for_EDF3(url, edf_version):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for d in soup.find_all("div", id="wikibody"):
        for pre in d.find_all("pre"):
            line = pre.text.replace("\n", "").replace("　", "")
            for m in re.findall(QUOTE_PTN, line):
                print("%s,%s" % (edf_version, m))

if __name__ == '__main__':
    main()
