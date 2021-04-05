# Workshop 2 activity #2: Graph the data! You've just finished writing a
# summation function which will be used here. Now, it's time to do some
# research on matplotlib and generate a line graph.

# This imports matplotlib, which we'll need. We call it plt.
import matplotlib.pyplot as plt

# This imports your work as well as some helpers.
from summation import *
from dataset import *

# Some code is written to help you get started. Read the documentation and
# resources and write the rest!
def graph():

	data = read_data()
	totals = []

	for month in data:
		totals.append(summation(month))

	# Hint: Your code should look something like the following pseudocode:
	# |
	# | Let x be a list of strings: "January", "February", etc...
	# | Let y be totals (which was defined in line 17).
	# | Plot x, y
	# | Let the plot x label be the string "Month"
	# | Let the plot y label be the string "Total Precipitation"
	# | Let the plot title be the string "Total Precipitation per Month in 2020"
	# | Show the plot.
	# |
	# -- Your code should be written below this line. -- #
