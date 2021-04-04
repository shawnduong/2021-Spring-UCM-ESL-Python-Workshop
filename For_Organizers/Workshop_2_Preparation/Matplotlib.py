# In order to use a library, it must be imported first.
import matplotlib.pyplot

# We define the data that we want to visualize.
schools = ["ENGR", "SNS", "SSHA", "N/A"]
populations = [2262, 2085, 3438, 338]

# Make a pie plot.
matplotlib.pyplot.pie(populations, explode=(0.1, 0, 0, 0),
	labels=schools, autopct="%1.1f%%", shadow=True)

# Show the pie plot.
matplotlib.pyplot.show()
