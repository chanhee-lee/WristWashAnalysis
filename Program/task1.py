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
    average = moving_average(data, 100)
    plot_mag(average)
    num_steps = 0
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''
    i = 0
    found = False
    stepArray = []
    for x in average: 
        if (x >= 6.5 and x <= 6.55): 
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
    file_name = "task1.csv"  # Change to your file name
    data = androidParser.get_data(file_name)
    number_of_steps = count_steps(data)
    print "Number of steps counted are :", number_of_steps

run()

