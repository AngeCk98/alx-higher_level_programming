#!/bin/bash
# A script that takes URL and displays allowed HTTP methods
curl -sI "$1" | grep -i Allow | cut -d ' ' -f 2-
