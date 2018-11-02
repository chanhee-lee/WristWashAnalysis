"""
This file will be used to call combine.py, time_convert.py,
smooth_scale.py, and annotation.py
"""

from argparse import ArgumentParser

import time_combine
import smooth_scale
import split_test_train

parser = ArgumentParser()
parser.add_argument("pnumber")
args = parser.parse_args()

time_combine.tc(1, "na", "ag_tc_")
split_test_train.stt(1, "ag_tc_")

# time_combine(1, na, ag_tc_) # for 6 gestures
# split_test_train(1, ag_tc_)
# smooth_scale(1, ag_tc_1) # for 6 gestures --> ag_tc_ss_
# gesture_combine(1, ag_tc_ss_, gesture_combine_p1)

# cm(x) # cm on gesture_combine_px.csv 
