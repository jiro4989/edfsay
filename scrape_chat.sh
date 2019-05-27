#!/bin/bash

set -eu

curl -s https://www65.atwiki.jp/edf5/pages/148.html \
  | grep "atwiki_tr_even atwiki_tr" \
  | sed -E 's@.*td.style."">([^<]+)<.*@\1@g' \
  | sed -E 's@.*-->([^<]+)</span.*@\1@g' \
  > chat.txt
