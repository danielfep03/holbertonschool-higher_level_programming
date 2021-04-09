#!/bin/bash
# Displays the size of the body of the response
curl -I "$1" | grep -i "content-length:" | cut -d " " -f 2
