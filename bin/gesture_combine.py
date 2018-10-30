
from __future__ import division
import datetime
import csv
import matplotlib.pyplot as plt
import pandas as pd
from argparse import ArgumentParser
from numpy import *
#
# parser = ArgumentParser()
# parser.add_argument("pnumber")
# args = parser.parse_args()

first_time_in_loop = 1
for x in range(1,3):
    for gdata_number in xrange(1,7):
        participant_file = "../raw/participant" + str(x) + "/tc_ss_accel_gyro_label_" + str(gdata_number) + ".csv"

        # D: N-dimensional array that delimits waccel_tc_ss_label by ,
        D = genfromtxt(participant_file, delimiter=',')

        # Z is a stack of gesture data stacked vertically
        # If first time in loop, set Z to D
        if first_time_in_loop==1:
            first_time_in_loop = 0
            Z = D
        # Else stack Z on top of D # Adds D on bottom
        else:
            Z = vstack((Z,D))

    savetxt("../raw/participant" + str(x) + "/gestures_combined_" + str(x) + ".csv", Z, delimiter=",")
