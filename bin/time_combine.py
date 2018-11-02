
import csv
from argparse import ArgumentParser
import plot
import math

def tc(pnumber, filename, newfilename):

    parser = ArgumentParser()
    parser.add_argument("pnumber")
    args = parser.parse_args()


    # -------------------------------------------------------------------------------
    #
    # 	Combines timestamp in milliseconds, accelerometer, and gyroscope data
    #   into another file ...
    #   To execute this file ...
    #
    # -------------------------------------------------------------------------------

    # accel data
    accelX = []
    accelY = []
    accelZ = []
    accelMag = []

    # gyro data
    gyroX = []
    gyroY = []
    gyroZ = []
    gyroMag = []

    # time stamps
    timeStamps = []

    # Sampling Rate Constant
    SAMPLING_RATE = 100

    for gesture_number in range(1, 7, 1):

        with open("../raw/participant" + str(pnumber) + "/" + newfilename + str(gesture_number) + ".csv", 'wb') as csvoutputfile:

            csvwriter = csv.writer(csvoutputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            # loads accel data into lists
            with open('../raw/participant' + str(pnumber) + '/ACCEL' + str(gesture_number) + '.csv', 'rb') as csvinputfile:

                csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

                for row in csvreader:
                    accelX.append(float(row[1]))
                    accelY.append(float(row[2]))
                    accelZ.append(float(row[3]))
                    accelMag.append(mag(float(row[1]),float(row[2]),float(row[3])))

            # loads gyro data into lists
            with open('../raw/participant' + str(pnumber) + '/GYRO' + str(gesture_number) + '.csv', 'rb') as csvinputfile:

                csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

                for row in csvreader:
                    gyroX.append(float(row[1]))
                    gyroY.append(float(row[2]))
                    gyroZ.append(float(row[3]))
                    gyroMag.append(mag(float(row[1]),float(row[2]),float(row[3])))

                plotlist = []
            
            for i in range(0, min(len(accelX), len(gyroX)), 1):
                row = [] # truncate decimal to first decimal
                plotrow = []
                row.append(float(i)/SAMPLING_RATE * 1000)
                row.append(accelX[i])
                row.append(accelY[i])
                row.append(accelZ[i])
                row.append(accelMag[i])
                row.append(gyroX[i])
                row.append(gyroY[i])
                row.append(gyroZ[i])
                row.append(gyroMag[i])
                csvwriter.writerow(row)

                plotrow.append(accelX[i])
                plotrow.append(accelY[i])
                plotrow.append(accelZ[i])
                plotlist.append(plotrow)

            #plot.plot_data_3D(plotlist)

def mag(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)