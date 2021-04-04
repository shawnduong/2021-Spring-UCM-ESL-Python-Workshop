# This is a helper I wrote for the workshop. I don't comment too much on this
# since this is a little behind the scenes, but more power to you if you wanna
# take on the challenge and read on!
# - Shawn

def read_data(path="./dataset.csv"):

	output = [[] for i in range(12)]

	with open(path, "r") as f:
		for line in f.readlines()[1:]:
			line  = line.split(",")
			month = int(line[2].split("-")[1]) - 1
			output[month].append(float(line[3]))

	return output

