from scipy import *
from scipy.signal import *
from sklearn import preprocessing
from numpy import * 
import numpy as np
from argparse import ArgumentParser

# -----------------------------------------------------------------------------------
#	Processes data through zero mean variance 
#   values: n x 3 data 
# -----------------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------------
#	Processing 
# -----------------------------------------------------------------------------------

# read from file 
# pass into zmv 
# write to file 