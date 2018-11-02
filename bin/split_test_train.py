import csv
from scipy import *
from scipy.signal import *
from sklearn import preprocessing
from numpy import * 
import numpy as np
import plot 

TRAINSPLIT = 70 
TESTSPLIT = 100 - TRAINSPLIT

def stt(pnumber, filename):
    for gesture_number in range(1, 7, 1):

        # Read data from a text file
        tempfilename = "../raw/participant" + str(pnumber) + "/" + filename + str(gesture_number) + ".csv"
        print tempfilename
        all_cols = genfromtxt( tempfilename, comments='#', delimiter=",")
        
        # Ignore timestamps
        data_cols = all_cols[:, 1:]   
        print data_cols

        datalength = 0
        print(len(data_cols))
        print(data_cols)
        trainLength = datalength * (TRAINSPLIT / 100)

        # rows from 0 to trainLength
        ## From row 
        traindata = data_cols[1,2]

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
