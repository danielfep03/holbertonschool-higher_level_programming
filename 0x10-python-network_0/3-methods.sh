#!/bin/bash
# This is a super power
 curl -sI -X OPTIONS "$1" | grep -i "allow" | cut -d " " -f 2-
