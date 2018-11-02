from constants import data_folder


def get_data(file_name):
    inputfile = open(data_folder + file_name, "r+")
    data = []
    for i in range(3):
        inputfile.readline()  # use next() if 2.7. Skip the first few samples
    for line in inputfile:
        splits = line.split(",")
        data.append((float(splits[1]), float(splits[2]), float(splits[3])))
    return data

# print get_data("test.csv")

def get_data_x(file_name):
    inputfile = open(data_folder + file_name, "r+")
    data = []
    for i in range(3):
        inputfile.readline()  # use next() if 2.7. Skip the first few samples
    for line in inputfile:
        splits = line.split(",")
        data.append((float(splits[1])))
    print data
    return data

def get_data_y(file_name):
    inputfile = open(data_folder + file_name, "r+")
    data = []
    for i in range(3):
        inputfile.readline()  # use next() if 2.7. Skip the first few samples
    for line in inputfile:
        splits = line.split(",")
        data.append((float(splits[2])))
    print data
    return data