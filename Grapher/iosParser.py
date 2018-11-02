from constants import data_folder
import re

def get_data(file_name):
    delimiter = re.compile("[^\t]+")
    acc_data = []
    raw_data = open(data_folder+file_name)
    for data in raw_data.readlines():
        if data.find("%") == -1:
            arr = delimiter.findall(data)
            acc_data.append((float(arr[2]), float(arr[3]), float(arr[4])))
    return acc_data