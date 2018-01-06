#!/usr/bin/env bash

# $1 = -m
# $2 = <minutes>

cd /home/bundito/joeremote
nohup python3 ~/joeremote/radioclash.py $1 $2 > /dev/null 2>&1 &
