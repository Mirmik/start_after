#!/usr/bin/env python3
#coding:utf-8

import os
import sys
import time

time.sleep(float(sys.argv[1]) / 1000.0)
os.system(" ".join(sys.argv[2:]))