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

# parser = ArgumentParser()
# parser.add_argument("pnumber")
# args = parser.parse_args()

# Split data 30, 70, Process individually, then use one as test and other as train 

frame_size_seconds = 6
step_size_seconds = int(frame_size_seconds/2)
sampling_rate = 15

# Set the frame and step size
frame_size = frame_size_seconds * sampling_rate
step_size = step_size_seconds * sampling_rate

# Get training file for each participant
first_time_in_loop = 1
for target_participant_counter in xrange(1,2):
	test_file = '../raw/participant' + str(target_participant_counter) + '/gestures_combined_test' + '.csv'
	train_file = '../raw/participant' + str(target_participant_counter) + '/gestures_combined_train' + '.csv'
    
	print ""
	print "File: " + test_file + ", " + train_file
	print ""

	# D: N-dimensional array that delimits waccel_tc_ss_label by ,
	D_test = genfromtxt(test_file, delimiter=',')
	D_train = genfromtxt(train_file, delimiter=',')

    # Stacked_Participant is a stack of participant datas stacked vertically 
	# If first time in loop, set Z to D
	if first_time_in_loop==1:
		first_time_in_loop = 0
		StackedP_Test = D_test
		StackedP_Train = D_train
	# Else stack Z on top of D # Adds D on bottom 
	else:
		StackedP_Test = vstack((StackedP_Test, D_Test))
		StackedP_Train = vstack((StackedP_Train, D_Train))

# Number of inputs # .shape[1] gives number of columns # the number of entries in one input 
last_col_test = StackedP_Test.shape[1] - 1
last_col_train = StackedP_Train.shape[1] - 1
# should be called index of last column 

# -----------------------------------------------------------------------------------
#
#									Training
#
# -----------------------------------------------------------------------------------

# Calculate features for frame
for counter in xrange(0,len(StackedP_Test),step_size):
	
	# Get the label # from counter row # label is in last column (num_of_input)
	L_Test = StackedP_Test[counter, last_col_test]

    # Get rows from which to calculate features
	# row: frame size from counter onwards
	# col: beginning to number of columns 
	R_Test = StackedP_Test[counter:counter+frame_size, :last_col_test]

	# Calculate features
	M_test = mean(R_Test,axis=0) # Mean
	V_test = var(R_Test,axis=0) # Variance
	SK_test = stats.skew(R_Test,axis=0) # ND skew
	K_test = stats.kurtosis(R_Test,axis=0) # ND Kurtosis
	RMS_test = sqrt(mean(R_Test**2,axis=0)) # Root Mean Square

	# H and G should be stacked arrays of : M, V, SK, K, RMS, L 
	H = hstack((M_test,V_test))
	H = hstack((H,SK_test))
	H = hstack((H,K_test))
	H = hstack((H,RMS_test))

	H = hstack((H,L_Test))
	# All: Stacks all hstacks vertically 
	# Row: Horizontally stacked features for on data
	# Col: All the features 
	if counter==0:
		All_test = H
	else:
		All_test = vstack((All_test,H))

# Calculate features for frame
for counter in xrange(0,len(StackedP_Train),step_size):
	# Get the label # from counter row # label is in last column (num_of_input)
	L_Train = StackedP_Train[counter, last_col_train]

    # Get rows from which to calculate features
	# row: frame size from counter onwards
	# col: beginning to number of columns 
	R_Train = StackedP_Train[counter:counter+frame_size, :last_col_train]

	# Calculate features
	M_train = mean(R_Train,axis=0) # Mean
	V_train = var(R_Train,axis=0) # Variance
	SK_train = stats.skew(R_Train,axis=0) # ND skew
	K_train = stats.kurtosis(R_Train,axis=0) # ND Kurtosis
	RMS_train = sqrt(mean(R_Train**2,axis=0)) # Root Mean Square

	# H and G should be stacked arrays of : M, V, SK, K, RMS, L 
	G = hstack((M_train,V_train))
	G = hstack((G,SK_train))
	G = hstack((G,K_train))
	G = hstack((G,RMS_train))

	G = hstack((G,L_Train))
	# All: Stacks all hstacks vertically 
	# Row: Horizontally stacked features for on data
	# Col: All the features 
	if counter==0:
		All_train = G
	else:
		All_train = vstack((All_train, G))


# Get features and labels
# X is all the feature, Y is all the label 
X_test = All_test[:,:last_col_test*5]
Y_test = All_test[:,last_col_test*5]

X_train = All_train[:,:last_col_train*5]
Y_train = All_test[:,last_col_train*5]

# Set up Model
modelClassifier = RandomForestClassifier(n_estimators=185)
modelClassifier.fit(X_train, Y_train)

# Split the data into a training set and a test set
##X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, random_state=42, test_size=0.33)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.33, random_state=42)

# Run classifier
classifier = RandomForestClassifier(n_estimators=185)
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

#ct = pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True).apply(lambda r: r/r.sum(), axis=1)
ct = pd.crosstab(Y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)

print (ct)

# Compute confusion matrix
cm = confusion_matrix(Y_test, Y_pred)

# print(cm)

# Show confusion matrix in a separate window
plt.matshow(cm)	
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()

# Dump model
joblib.dump(modelClassifier, '../model/washmodel.pkl')

## Find code to dump into model 
### joblib.dump(clf, '../model/wrist.pkl')
## https://stackoverflow.com/questions/24906126/how-to-unpack-pkl-file
## http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier
## Use methods on unpacked pkl file --> saved classifier 