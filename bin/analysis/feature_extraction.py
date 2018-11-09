from __future__ import division
import datetime
import csv
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn import svm, neighbors, metrics, model_selection
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import auc, confusion_matrix
from scipy import *
from scipy.stats import *
from scipy.signal import *
from numpy import *
from argparse import ArgumentParser

# -------------------------------------------------------------------------------
#
# 	Extracts features from a single file and returns a 2D array / 2 Arrays 
#   2D ARRAY: Row: Col: 
#   2 Arrays: 1) X: Feature Vectors, Y: List of True Labels 
#
# -------------------------------------------------------------------------------

frame_size_seconds = 6
step_size_seconds = int(frame_size_seconds/2)
sampling_rate = 15	

# Set the frame and step size
frame_size = frame_size_seconds * sampling_rate
step_size = step_size_seconds * sampling_rate
first_time_in_loop = 1

def fe(StackedP):
    last_col = StackedP.shape[1] - 1

    # Calculate features for frame for TRAIN
    for counter in xrange(0,len(StackedP),step_size):
        # Get the label # from counter row # label is in last column (num_of_input)
        L = StackedP[counter, last_col]

        # Get rows from which to calculate features
        # row: frame size from counter onwards
        # col: beginning to number of columns 
        R = StackedP[counter:counter+frame_size, :last_col]

        # Calculate features
        M = mean(R,axis=0) # Mean
        V = var(R,axis=0) # Variance
        SK = stats.skew(R,axis=0) # ND skew
        K = stats.kurtosis(R,axis=0) # ND Kurtosis
        RMS = sqrt(mean(R**2,axis=0)) # Root Mean Square

        # G should be stacked arrays of : M, V, SK, K, RMS, L 
        G = hstack((M,V))
        G = hstack((G,SK))
        G = hstack((G,K))
        G = hstack((G,RMS))

        G = hstack((G,L))
        # All: Stacks all hstacks vertically 
        # Row: Horizontally stacked features for on data
        # Col: All the features 
        if counter==0:
            All = G
        else:
            All = vstack((All, G))

    FVectors = All[:,:last_col*5]
    True_Labels = All[:,last_col*5]
    
    return FVectors, True_Labels