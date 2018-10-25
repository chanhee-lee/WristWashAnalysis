
import csv
from argparse import ArgumentParser

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

# Labels for each hand washing gesture
label = ""
if int(args.pnumber) % 6 == 1:
    label = "Rubbing Palms"
elif int(args.pnumber) % 6 == 2:
    label = "Rubbing Back of Left Hand"
elif int(args.pnumber) % 6 == 3:
    label = "Rubbing Back of Right Hand"
elif int(args.pnumber) % 6 == 4:
    label = "Rubbing Between Fingers"
elif int(args.pnumber) % 6 == 5:
    label = "Rubbing Under Right Nails"
elif int(args.pnumber) % 6 == 0:
    label = "Rubbing Under Left Nails"
else:
    label = "No Movement"

with open("../raw/datafiles/combine/tc_accel_gyro_label_" + args.pnumber + ".csv", 'wb') as csvoutputfile:

    csvwriter = csv.writer(csvoutputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # loads accel data into lists
    with open('../raw/datafiles/accel/ACCEL' + args.pnumber + '.csv', 'rb') as csvinputfile:

        csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

        for row in csvreader:
            accelX.append(float(row[1]))
            accelY.append(float(row[2]))
            accelZ.append(float(row[3]))

    # loads gyro data into lists
    with open('../raw/datafiles/gyro/GYRO' + args.pnumber + '.csv', 'rb') as csvinputfile:

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
        row.append(label)
        csvwriter.writerow(row)