
import csv
from argparse import ArgumentParser
import plot

def tc(number):

    parser = ArgumentParser()
    parser.add_argument("pnumber")
    args = parser.parse_args()


    # -------------------------------------------------------------------------------
    #
    # 	Combines timestamp in milliseconds, accelerometer, and gyroscope data
    #   into another file tc_accel_gyro_label_fileNumber.csv
    #   To execute this file (time_combine.py), in your terminal type
    #   python time_combine.py number
    #   number is the file number attached to the end of your accel/gyro.csv
    #
    # -------------------------------------------------------------------------------

    # accel data
    accelX = []
    accelY = []
    accelZ = []

    # gyro data
    gyroX = []
    gyroY = []
    gyroZ = []

    # time stamps
    timeStamps = []

    # Sampling Rate Constant
    SAMPLING_RATE = 100

    for gesture_number in range(1, 7, 1):

        with open("../raw/participant" + number + "/tc_accel_gyro_" + str(gesture_number) + ".csv", 'wb') as csvoutputfile:

            csvwriter = csv.writer(csvoutputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            # loads accel data into lists
            with open('../raw/participant' + number + '/ACCEL' + str(gesture_number) + '.csv', 'rb') as csvinputfile:

                csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

                for row in csvreader:
                    accelX.append(float(row[1]))
                    accelY.append(float(row[2]))
                    accelZ.append(float(row[3]))

            # loads gyro data into lists
            with open('../raw/participant' + number + '/GYRO' + str(gesture_number) + '.csv', 'rb') as csvinputfile:

                csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

                for row in csvreader:
                    gyroX.append(float(row[1]))
                    gyroY.append(float(row[2]))
                    gyroZ.append(float(row[3]))

                plotlist = []
            for i in range(0, min(len(accelX), len(gyroX)), 1):
                row = [] # truncate decimal to first decimal
                plotrow = []
                row.append(float(i)/SAMPLING_RATE * 1000)
                row.append(accelX[i])
                row.append(accelY[i])
                row.append(accelZ[i])
                row.append(gyroX[i])
                row.append(gyroY[i])
                row.append(gyroZ[i])
                csvwriter.writerow(row)

                plotrow.append(accelX[i])
                plotrow.append(accelY[i])
                plotrow.append(accelZ[i])
                plotlist.append(plotrow)

            #plot.plot_data_3D(plotlist)