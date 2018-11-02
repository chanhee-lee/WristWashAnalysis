import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot_data_3D(data):
    # print(data)
    plt.title('X,Y,Z Plot')
    plt.plot([row[0] for row in data], label="x")
    plt.plot([row[1] for row in data], label="y")
    plt.plot([row[2] for row in data], label="z")
    plt.legend(loc='upper right')
    plt.show()

def plot_mag_1D(mag):

    plt.title('X Plot')
    plt.plot([row for row in mag], label="x")
    plt.legend(loc='upper right')
    plt.show()

# plot_data("test.csv")
