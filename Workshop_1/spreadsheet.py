# This is a helper I wrote for the workshop. I don't comment too much on this
# since this is a little behind the scenes, but more power to you if you wanna
# take on the challenge and read on!
# - Shawn

class spreadsheet:

	path = ""

	def __init__(self, name):

		self.path = name
		open(self.path, "w+")

	def write(self, *data):

		open(self.path, "a").write(", ".join(data) + "\n")

def make_new(name):

	return spreadsheet(name)

