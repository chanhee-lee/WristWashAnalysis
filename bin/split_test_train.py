import csv
from scipy import *
from scipy.signal import *
from sklearn import preprocessing
from numpy import * 
import numpy as np
import plot 

TRAINRATIO = 0.7

def stt(pnumber, filename):
    for gesture_number in range(1, 7, 1):

        # Read data from a text file
        tempfilename = "../raw/participant" + str(pnumber) + "/" + filename + str(gesture_number) + ".csv"
        print tempfilename
        all_cols = genfromtxt( tempfilename, comments='#', delimiter=",")
        
        # Ignore timestamps
        data_cols = all_cols[:, 1:]           

        datalength = len(data_cols)
        trainLength = datalength 
        trainLength *= TRAINRATIO

        train_data = []
        test_data = []

        # rows from 0 to trainLength
        ## From row 
        counter = 0 
        for row in data_cols: 
            if (counter < trainLength):
                train_data.append(row)
                counter += 1
            else: 
                test_data.append(row)
                counter += 1
        print "counter: " + str(counter)

        savetxt("../raw/participant" + str(pnumber) + "/" + filename + str(gesture_number) + "_train" + ".csv", train_data, delimiter=",")
        savetxt("../raw/participant" + str(pnumber) + "/" + filename + str(gesture_number) + "_test" + ".csv", test_data, delimiter=",")

"""

        traindata = []
        testdata = []

        counter = 0

        for row in csvreader: ######this is not working 
            if (counter < trainLength):
                traindata.append(row)
            else: 
                testdata.append(row)


        with open("../raw/participant" + str(pnumber) + "/" + filename + str(gesture_number) + "_train.csv", 'wb') as csvoutputfile:
            csvwritertrain = csv.writer(csvoutputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in traindata:
                csvwritertrain.writerow(row)

        with open("../raw/participant" + str(pnumber) + "/" + filename + str(gesture_number) + "_test.csv", 'wb') as csvoutputfile:
            csvwritertest = csv.writer(csvoutputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in testdata: 
                csvwritertest.writerow(row)
"""
