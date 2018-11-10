# -----------------
# This file can be called by a server 
# Takes in the participant number 
# Preprocesses the 6 gestures for that participant 
# Returns a 2D Array containing the combined gestures 
# -----------------

from argparse import ArgumentParser
from scipy import *
from scipy.signal import *
from sklearn import preprocessing
from numpy import * 
import numpy as np
import plot 

import mag_append
import smooth_scale
import split_test_train
import gesture_combine 
import gesture_combine_indiv

"""
MUST BE CHANGED: Directories of files based on java 
"""

def preprocess(pnumber):
    # Preprocess for n Participants without Split
    n = pnumber
    mag_append.tc(n, "na", "tc_")
    smooth_scale.ss(n, "tc_", "")
    gesture_combine_indiv.gc(n, "tc_ss_", "")

    gestures_combined =  genfromtxt("tc_ss_" + n + ".csv", comments='#', delimiter=",")
    return gestures_combined
