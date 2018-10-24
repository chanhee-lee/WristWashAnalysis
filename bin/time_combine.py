
import csv



# -------------------------------------------------------------------------------
#
# 	Combines timestamp in milliseconds, accelerometer, and gyroscope data
#   into another file tc_accel_gyro.csv
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

with open("../raw/datafiles/time_accel_gyro.csv", 'wb') as csvoutputfile:

    csvwriter = csv.writer(csvoutputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # loads accel data into lists
    with open('../raw/datafiles/accel/ACCEL16.csv', 'rb') as csvinputfile:

        csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

        for row in csvreader:
            accelX.append(float(row[1]))
            accelY.append(float(row[2]))
            accelZ.append(float(row[3]))

    # loads gyro data into lists
    with open('../raw/datafiles/gyro/GYRO16.csv', 'rb') as csvinputfile:

        csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

        for row in csvreader:
            gyroX.append(float(row[1]))
            gyroY.append(float(row[2]))
            gyroZ.append(float(row[3]))

    for i in range(0, len(accelX), 1):
        row = [] # truncate decimal to first decimal 
        row.append(float(i)/SAMPLING_RATE * 1000)
        row.append(accelX[i])
        row.append(accelY[i])
        row.append(accelZ[i])
        row.append(gyroX[i])
        row.append(gyroY[i])
        row.append(gyroZ[i])
        csvwriter.writerow(row)