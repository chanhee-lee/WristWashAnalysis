# Add in Future README: The preprocessing is meant to annotate one file at a time, manually

"""
# Ensure that you change the filename and labelname variable before running this code 
# filename - the processed data file (most likely will look something like "tc_accel_gyro_1_ss.csv")
# labelname - the label for the gesture 
    1 - Gesture 1
    2 - Gesture 2
    3 - Gesture 3
    4 - Gesture 4
    5 - Gesture 5
    6 - Gesture 6
"""
import csv
# from argparse import ArgumentParser
#
# parser = ArgumentParser()
# parser.add_argument("pnumber")
# args = parser.parse_args()


def a(number):

    # Labels for each hand washing gesture
    label = ""
    if int(number) % 6 == 1:
        # label = "Rubbing Palms"
        label = 1
    elif int(number) % 6 == 2:
        # label = "Rubbing Back of Left Hand"
        label = 2
    elif int(number) % 6 == 3:
        # label = "Rubbing Back of Right Hand"
        label = 3
    elif int(number) % 6 == 4:
        # label = "Rubbing Between Fingers"
        label = 4
    elif int(number) % 6 == 5:
        # label = "Rubbing Under Right Nails"
        label = 5
    elif int(number) % 6 == 0:
        # label = "Rubbing Under Left Nails"
        label = 6
    else:
        # label = "No Movement"
        label = 0

    with open("../raw/datafiles/combine/tc_ss_accel_gyro_label" + number + ".csv", 'wb') as csvoutputfile:

        csvwriter = csv.writer(csvoutputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        # loads accel data into lists
        with open('../raw/datafiles/combine/tc_ss_accel_gyro_' + number + '.csv', 'rb') as csvinputfile:

            csvreader = csv.reader(csvinputfile, delimiter=',', quotechar='|')

            for row in csvreader:
                row.append(label)
                csvwriter.writerow(row)