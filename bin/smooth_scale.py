from scipy import *
from scipy.signal import *
from sklearn import preprocessing
from numpy import * 
import numpy as np
import plot 

from argparse import ArgumentParser


# -----------------------------------------------------------------------------------
#	Processes data through zero mean variance 
#   values: 1D array of values 
# -----------------------------------------------------------------------------------
def zmv(values): 
    smooth_values = preprocessing.scale(values)
    return smooth_values

"""
# 3 Dimensional Version 
def zmv(values):
    x_raw = []
    y_raw = []
    z_raw = []

    for row in values: 
        x_raw.append(float(row[1]))
        y_raw.append(float(row[1]))
        z_raw.append(float(row[1]))
    
    x_scaled = preprocessing.scale(x_raw)
    y_scaled = preprocessing.scale(y_raw)
    z_scaled = preprocessing.scale(z_raw)

    all_scaled = [] 
    for i in range(0, len(x_raw), 1):
        all_scaled.append(x_scaled[i])
        all_scaled.append(y_scaled[i])
        all_scaled.append(z_scaled[i])

    return all_scaled
"""


# -----------------------------------------------------------------------------------
#	Processing the 6 gesture data files in one participant 
# -----------------------------------------------------------------------------------
def ss(number):

    parser = ArgumentParser()
    parser.add_argument("pnumber")
    args = parser.parse_args()

    # read from file 
    # pass into zmv 
    # write to file 
    print "smooth_scale.py"
    print args.pnumber

    for gesture_number in range(1, 7):

        filename = "../raw/participant" + args.pnumber + "/tc_accel_gyro_label_" + gesture_number + ".csv"

        # Read data from a text file
        all_cols = genfromtxt( filename, comments='#', delimiter=",")

        # Process only the data from accel, ignore the timestamps
        data_cols = all_cols[:,1:]

        data_cols_smoothened_0 = zmv(data_cols[:,0])
        data_cols_smoothened_1 = zmv(data_cols[:,1])
        data_cols_smoothened_2 = zmv(data_cols[:,2])

        # Temp solution 
        data_label = []
        for i in range(0,len(data_cols_smoothened_0)):
            data_label.append(gesture_number)
        #############

        data_cols_smoothened = data_cols_smoothened_0
        data_cols_smoothened = column_stack((data_cols_smoothened, data_cols_smoothened_1))
        data_cols_smoothened = column_stack((data_cols_smoothened, data_cols_smoothened_2))
        data_cols_smoothened = column_stack((data_cols_smoothened, data_label))
        
        """
        # Normalize
        data_cols_smoothened_normalized = preprocessing.normalize(data_cols_smoothened, norm='l2')
        """

        # Add relative timestamp
        data_cols_smoothened_final = data_cols_smoothened
        plot.plot_data_3D(data_cols_smoothened_final)

        savetxt("../raw/participant" + args.pnumber + "/tc_ss_accel_gyro_label_" + gesture_number + ".csv", data_cols_smoothened_final, delimiter=",")
