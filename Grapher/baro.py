import androidParser
import iosParser
from plot_data import plot_data
from plot_data import plot_mag
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
    return data


def count_steps(data):
    print 'count_steps'
    # Different Algo 
    num_steps = 0
    plot_data(data)
    plot_mag(vector_magnitude(data))
    plot_mag(moving_average((data),230))

    '''
    This function counts the number of steps in data and returns the number of steps
    '''
    return num_steps


def run():
    # Get data
    file_name = "task2baro.csv"  # Change this to your data file name
    data = androidParser.get_data(file_name)
    segmented_data = segment_climbing_walking(data)
    number_of_steps = count_steps(segmented_data)
    print "Number of steps counted are :", number_of_steps

run()
