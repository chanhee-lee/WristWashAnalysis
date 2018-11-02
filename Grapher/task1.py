import androidParser
from plot_data import plot_data
from plot_data import plot_mag
from plot_data import plot_steps
from util import moving_average
from util import vector_magnitude


def count_steps(data):
    print "Accelerometer data graph"
    plot_data(data)
    mag = vector_magnitude(data)
    plot_mag(mag)
    average = moving_average(data, 10)
    plot_mag(average)
    num_steps = 0
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''

    return num_steps

def run():
    # Get data
    file_name = "fusrodah.csv"  # Change to your file name
    print "YO"
    data = androidParser.get_data(file_name)
    print "YOYO"
    number_of_steps = count_steps(data)
    print "Number of steps counted are :", number_of_steps

run()

