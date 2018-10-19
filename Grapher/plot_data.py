import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plot_data(data):
    # print(data)
    plt.title('X,Y,Z Plot')
    plt.plot([row[0] for row in data], label="x")
    plt.plot([row[1] for row in data], label="y")
    plt.plot([row[2] for row in data], label="z")
    plt.legend(loc='upper right')
    plt.show()

def plot_mag(mag):

    plt.title('X Plot')
    plt.plot([row for row in mag], label="x")
    plt.legend(loc='upper right')
    plt.show()

def plot_steps(average, stepArray):
    idx = 0
    plotx = []
    for idx in range(0, len(stepArray)-1, 2):
        if idx <= len(stepArray):
            plotx.append((stepArray[idx] + stepArray[idx+1])/2)

    plt.title('In Between Plots are Steps')
    xs = []
    for val in range(0,len(average),1):
        xs.append(val)
    
    plt.plot(xs, average, '-gD', markevery=stepArray)
    
    plt.show()

# plot_data("test.csv")
