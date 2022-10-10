#! /bin/sh

python3 buildscripts/sources.py $(find chapters -name '*.md') -o sources/ &&\
python3 buildscripts/check.py sources-metadata.yaml -p sources/

