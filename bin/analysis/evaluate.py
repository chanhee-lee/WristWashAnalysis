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
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# -------------------------------------------------------------------------------
#
# 	Evaluates the accuracy of model's predictions on X_test and Y_test
#   for a multiple gestures combined  
#   Uncomment to produce a confusion matrix
#   Returns a single integer score for the total accuracy
#
# -------------------------------------------------------------------------------


def ea(modelname, testfilename):
    # Load Model 
    classifier = joblib.load(modelname)

    # Feature extract test
    test_file = genfromtxt(testfilename, delimiter=',')
    X_test, Y_test = feature_extraction.fe(test_file)

    # Compare Model to Test 
    score = classifier.score(X_test, Y_test)

    ###"""
    Y_pred = classifier.predict(X_test)
    # Cross Table
    ct = pd.crosstab(Y_test, Y_pred, rownames=['True'], colnames=['Predicted'], margins=True)
    print(ct)
    
    """
    # Confusion Matrix
    cm = confusion_matrix(Y_test, Y_pred)
    plt.matshow(cm)	
    plt.title('Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    """

    return score

# https://pypi.org/project/fastdtw/
# https://tslearn.readthedocs.io/en/latest/gen_modules/tslearn.metrics.html