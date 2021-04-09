#!/bin/bash
# This is a super power
 curl -iX OPTIONS http://89656d599ee6.99e27b5c.hbtn-cod.io:5000 | grep -i "allow" | cut -d " " -f 2-
