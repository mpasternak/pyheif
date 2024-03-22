#!/bin/bash

. /opt/homebrew/bin/virtualenvwrapper.sh

mkvirtualenv py310 -p python3.10
workon py310
make all

mkvirtualenv py311 -p python3.11
workon py311
make all

mkvirtualenv py312 -p python3.12
workon py312
make all
