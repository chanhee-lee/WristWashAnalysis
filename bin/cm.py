from __future__ import division
import datetime
import csv
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn import svm, neighbors, metrics, model_selection #cross_validation
#from sklearn.model_selection import cross_validation
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

# parser = ArgumentParser()
# parser.add_argument("pnumber")
# args = parser.parse_args()

frame_size_seconds = 6
step_size_seconds = int(frame_size_seconds/2)
sampling_rate = 15

# Set the frame and step size
frame_size = frame_size_seconds * sampling_rate
step_size = step_size_seconds * sampling_rate

# Get training file for each participant
first_time_in_loop = 1
for target_participant_counter in xrange(1,2):
    participant_file = '../raw/participant' + str(target_participant_counter) + '/gestures_combined_' + str(target_participant_counter) + '.csv'

    print ""
    print "File: " + participant_file
    print ""

	# D: N-dimensional array that delimits waccel_tc_ss_label by ,
    D = genfromtxt(participant_file, delimiter=',')

    # Z is a stack of participant datas stacked vertically 
	# If first time in loop, set Z to D
    if first_time_in_loop==1:
		first_time_in_loop = 0
		Z = D
	# Else stack Z on top of D # Adds D on bottom 
    else:
		Z = vstack((Z,D))

# Number of inputs # .shape[1] gives number of columns # the number of entries in one input 
number_of_inputs = Z.shape[1] - 1
# should be called index of last column 

# -----------------------------------------------------------------------------------
#
#									Training
#
# -----------------------------------------------------------------------------------

# Calculate features for frame
for counter in xrange(0,len(Z),step_size):
	
	# Get the label # from counter row # label is in last column (num_of_input)
	L = Z[counter, number_of_inputs]

    # Get rows from which to calculate features
	# row: frame size from counter onwards
	# col: beginning to number of columns 
	R = Z[counter:counter+frame_size, :number_of_inputs]

	# Calculate features
	M = mean(R,axis=0) # Mean
	V = var(R,axis=0) # Variance
	SK = stats.skew(R,axis=0) # ND skew
	K = stats.kurtosis(R,axis=0) # ND Kurtosis
	RMS = sqrt(mean(R**2,axis=0)) # Root Mean Square

	# H should be stacked arrays of : M, V, SK, K, RMS, L 
	H = hstack((M,V))
	H = hstack((H,SK))
	H = hstack((H,K))
	H = hstack((H,RMS))

	H = hstack((H,L))
	# All: Stacks all hstacks vertically 
	# Row: Horizontally stacked features for on data
	# Col: All the features 
	if counter==0:
		All = H
	else:
		All = vstack((All,H))

# Get features and labels
# X is all the feature, Y is all the label # *5 because num of features? 
X = All[:,:number_of_inputs*5]
Y = All[:,number_of_inputs*5]

# Split the data into a training set and a test set
##X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, random_state=42, test_size=0.33)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.33, random_state=42)

# Run classifier
classifier = RandomForestClassifier(n_estimators=185)
y_pred = classifier.fit(X_train, y_train).predict(X_test)

#ct = pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True).apply(lambda r: r/r.sum(), axis=1)
ct = pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)

print (ct)

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# print(cm)

# Show confusion matrix in a separate window
plt.matshow(cm)	
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()