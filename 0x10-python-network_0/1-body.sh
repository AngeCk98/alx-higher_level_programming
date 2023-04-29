#!/bin/bash
# A script that takes and sends GET to URL and displays body of response
curl -sb -X GET -L "$1"
