
import csv



# -------------------------------------------------------------------------------
#
# 			Combines accelerometer and gyroscope data into another file
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


with open("../raw/combine_accel_gyro/ACCEL_GYRO.csv", 'wb') as csvoutputfile:

    csvwriter = csv.writer(csvoutputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # loads accel data into lists
    with open('../raw/accel/ACCEL16', 'rb') as csvinputfile:

        csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

        for row in csvreader:
            accelX.append(float(row[1]))
            accelY.append(float(row[2]))
            accelZ.append(float(row[3]))

    # loads gyro data into lists
    with open('../raw/gyro/GYRO16', 'rb') as csvinputfile:

        csvreader = csv.reader(csvinputfile, delimter=',', quotechar='|')

        for row in csvreader:
            gyroX.append(float(row[1]))
            gyroY.append(float(row[2]))
            gyroZ.append(float(row[3]))