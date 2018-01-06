#!/usr/bin/local/python3

import os

TERMPATH="/usr/bin/terminator"

os.spawnl(os.P_NOWAIT, TERMPATH, None)
