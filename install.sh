#!/bin/bash

set -eux

readonly DIR_PREFIX=/usr/local
readonly BIN_NAME=edf
readonly PROJECT_NAME=edfsay

install -m 0755 "bin/$BIN_NAME"* "$DIR_PREFIX/bin/"
install -d -m 0755 "$DIR_PREFIX/etc/$PROJECT_NAME"
install -m 0644 "etc/$PROJECT_NAME"/* "$DIR_PREFIX/etc/$PROJECT_NAME"
