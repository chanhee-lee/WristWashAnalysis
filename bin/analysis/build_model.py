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
# 	Creates and saves classifier model based on parameters X, Y into model.pkl
#   X: Array of Feature Vectors
#   Y: Array of Labels for X 
#
# -------------------------------------------------------------------------------

def bm(trainfile): 
    # Set up training file 
    

    # Feature Extraction 
    
    
    pass