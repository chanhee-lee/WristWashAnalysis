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
import feature_extraction

# -------------------------------------------------------------------------------
#
# 	Creates and saves classifier model based on parameters X, Y into model.pkl
#   X: Array of Feature Vectors
#   Y: Array of Labels for X 
#
# -------------------------------------------------------------------------------

def bm(trainfilename, savename): 
    # Set up training file 2D array 
    train_file = genfromtxt(trainfilename, delimiter=',')

    # Feature Extraction 
    FVectors, True_Labels = feature_extraction.fe(train_file)

    # Train classifier    
    classifier = RandomForestClassifier(n_estimators=185)
    classifier.fit(FVectors, True_Labels)
    
    joblib.dump(classifier, savename)