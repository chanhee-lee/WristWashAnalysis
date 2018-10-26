from scipy import *
from scipy.signal import *
from sklearn import preprocessing
from numpy import * 
import numpy as np

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("pnumber")
args = parser.parse_args()

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
#	Processing 
# -----------------------------------------------------------------------------------

# read from file 
# pass into zmv 
# write to file 

x_labeled = []
y_labeled = []
z_labeled = []

##############
parser = ArgumentParser()
parser.add_argument("pnumber")
args = parser.parse_args()
print "smooth_scale.py"
print args.pnumber

filename = "../raw/datafiles/combine/tc_accel_gyro_label_" + args.pnumber

# Read data from a text file
all_cols = genfromtxt( filename, comments='#', delimiter=",")

# Process only the data from accel, ignore the timestamps
data_cols = all_cols[:,2:]

data_cols_smoothened_0 = zmv(data_cols[:,0])
data_cols_smoothened_1 = zmv(data_cols[:,1])
data_cols_smoothened_2 = zmv(data_cols[:,2])

data_cols_smoothened = data_cols_smoothened_0
data_cols_smoothened = column_stack((data_cols_smoothened, data_cols_smoothened_1))
data_cols_smoothened = column_stack((data_cols_smoothened, data_cols_smoothened_2))
"""
# Normalize
data_cols_smoothened_normalized = preprocessing.normalize(data_cols_smoothened, norm='l2')
"""

# Add relative timestamp
data_cols_smoothened_final = column_stack((all_cols[:,1],data_cols_smoothened))

savetxt("../raw/datafiles/combine/tc_accel_gyro_label_" + args.pnumber, data_cols_smoothened_final, delimiter=",")
