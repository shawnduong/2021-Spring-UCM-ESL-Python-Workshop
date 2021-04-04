#!/usr/bin/env python3

from summation import *
from plot import *

def main():

	print(":: Checking your summation function...")

	try:
		assert summation([10, 20, 30]) == 60
		assert summation([0, 0, 0]) == 0
		assert summation([6.7, 1.3, 1.5]) == 9.5
	except:
		print("Summation function failed. Review your code and try again.")
		exit(-1)

	print(":: Your function passed all the test cases!")
	print(":: Your plot function will now be run.")
	graph()

if __name__ == "__main__":
	main()
