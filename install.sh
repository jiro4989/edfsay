#!/bin/bash

set -eux

readonly DIR_PREFIX=/usr/local
readonly BIN_NAME=edf
readonly PROJECT_NAME=edfsay

sudo install -m 0755 "bin/$BIN_NAME"* "$DIR_PREFIX/bin/"
sudo install -d -m 0755 "$DIR_PREFIX/etc/$PROJECT_NAME"
sudo install -m 0644 "etc/$PROJECT_NAME"/* "$DIR_PREFIX/etc/$PROJECT_NAME"
