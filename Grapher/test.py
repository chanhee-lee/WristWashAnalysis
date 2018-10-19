from plot_data import plot_data
import androidParser
import iosParser

 # Change to iOS parser if using iPhone
data = androidParser.get_data("test.csv")

plot_data(data)
