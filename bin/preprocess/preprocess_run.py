"""
This file will be used to call combine.py, time_convert.py,
smooth_scale.py, and annotation.py
"""
from argparse import ArgumentParser

import mag_append
import smooth_scale
import split_test_train
import gesture_combine 
import gesture_combine_indiv

"""
#  Preprocess for n Participants with Split
for n in range(1,3):
    mag_append.tc(n, "na", "tc_")
    split_test_train.stt(n, "tc_")
    smooth_scale.ss(n, "tc_", "_test")
    smooth_scale.ss(n, "tc_", "_train")
    gesture_combine_indiv.gc(n, "tc_ss_", "_test")
    gesture_combine_indiv.gc(n, "tc_ss_", "_train")
"""


# Preprocess for n Participants without Split
for n in range(1,4):
    mag_append.tc(n, "na", "tc_")
    smooth_scale.ss(n, "tc_", "")
    gesture_combine_indiv.gc(n, "tc_ss_", "")

# Creates file compiling all data from all participants 
gesture_combine.gc(2, "tc_ss_", "")
