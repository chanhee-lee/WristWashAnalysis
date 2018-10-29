"""
This file will be used to call combine.py, time_convert.py,
smooth_scale.py, and annotation.py
"""

import csv
from argparse import ArgumentParser

import time_combine
import smooth_scale

parser = ArgumentParser()
parser.add_argument("pnumber")
args = parser.parse_args()

time_combine.tc(args.pnumber)
smooth_scale.ss(args.pnumber)


