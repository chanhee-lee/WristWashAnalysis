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


# -----------------------------------------------------------------------------------
#	Processing the 6 gesture data files in one participant 
# -----------------------------------------------------------------------------------
def ss(pnumber, ofilename, ext):

    for gesture_number in range(1, 7):

        filename = "../../raw/participant" + str(pnumber) + "/" + ofilename + str(gesture_number) + ext + ".csv"

        # Read data from a text file
        all_cols = genfromtxt(filename, comments='#', delimiter=",")

        data_cols_smoothened_0 = zmv(all_cols[:,0])
        data_cols_smoothened_1 = zmv(all_cols[:,1])
        data_cols_smoothened_2 = zmv(all_cols[:,2])
        data_cols_smoothened_3 = zmv(all_cols[:,3])

        # Create labels for data 
        data_label = []
        for i in range(0,len(data_cols_smoothened_0)):
            data_label.append(gesture_number)
        #############

        data_cols_smoothened = data_cols_smoothened_0
        data_cols_smoothened = column_stack((data_cols_smoothened, data_cols_smoothened_1))
        data_cols_smoothened = column_stack((data_cols_smoothened, data_cols_smoothened_2))
        data_cols_smoothened = column_stack((data_cols_smoothened, data_cols_smoothened_3))
        data_cols_smoothened = column_stack((data_cols_smoothened, data_label))
        
        """
        # Normalize
        data_cols_smoothened_normalized = preprocessing.normalize(data_cols_smoothened, norm='l2')
        """

        # Add relative timestamp
        data_cols_smoothened_final = data_cols_smoothened
        #plot.plot_data_3D(data_cols_smoothened_final)

        savetxt("../../raw/participant" + str(pnumber) + "/" + ofilename + "ss_"+ str(gesture_number) + ext + ".csv", data_cols_smoothened_final, delimiter=",")
    print "SmoothScale Saving..."