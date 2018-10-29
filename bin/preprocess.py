"""
This file will be used to call combine.py, time_convert.py,
smooth_scale.py, and annotation.py
"""

from argparse import ArgumentParser

import time_combine
import smooth_scale
import annotation

parser = ArgumentParser()
parser.add_argument("pnumber")
args = parser.parse_args()

time_combine.tc(args.pnumber)
<<<<<<< HEAD
smooth_scale.ss(args.pnumber)
annotation.a(args.pnumber)

=======
>>>>>>> fa820614019d448f6f0bc68d5a508b443d3d3702

smooth_scale.ss(args.pnumber)

