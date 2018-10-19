import androidParser
import iosParser
from plot_data import plot_data
from plot_data import plot_mag
from plot_data import plot_steps
from util import moving_average
from util import vector_magnitude

def segment_climbing_walking(data):
    '''
    While collecting data on stairs there were times when you were also walking rather than climbing
    It is importing to remove the parts from the data where you were walking in between the flight of stairs
    Write your own algorithm to find segments in data which corresponds to climbing only

    This functions returns
    List of tuples (x,y,z) which corresponds to climbing only.
    i.e. remove data points from the original data which corresponds to walking
    '''
    # Segment points  
    window = [355, 2745, 4484, 7823, 11775, 13237, 14976, 19205]
    seg_data = []
    # Remove every other segment from the data and compile the rest 
    for x in range(355, 2745, 1):
        seg_data.append(data[x])
    for x in range(4484, 7823, 1):
        seg_data.append(data[x])
    for x in range(11775, 13237, 1):
        seg_data.append(data[x])    
    for x in range(14976, 19205, 1):
        seg_data.append(data[x])

    print 'segment_climbing_walking'

    return seg_data


def count_steps(data):
    print 'count_steps'
    plot_data(data)
    mag = vector_magnitude(data)
    plot_mag(mag)
    average = moving_average(data, 100)
    plot_mag(average)
    num_steps = 0

    '''
    This function counts the number of steps in data and returns the number of steps
    ''' 
    i = 0
    found = False
    stepArray = []
    for x in average: 
        if (x >= 4 and x <= 4.03): 
            if found == False:
                num_steps = num_steps+1
                stepArray.append(i)
                found = True
            else:  
                found = False
        i = i + 1

    plot_steps(average, stepArray)

    return num_steps


def run():
    # Get data
    file_name = "task2gyro.csv"  # Change this to your data file name
    data = androidParser.get_data(file_name)
    segmented_data = segment_climbing_walking(data)
    number_of_steps = count_steps(segmented_data)
    print "Number of steps counted are :", number_of_steps

run()
