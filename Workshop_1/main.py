#!/usr/bin/env python3

import time

from answer_checker import *
from assembled_program import *

def main():

	print(":: Checking your answers...")

	if (msg := answer_checker()) == True:
		print(":: Looks good! Running assembled_program.py now...")
		assembled_program()
	else:
		print(":: Something went wrong in your logic.")
		print(":: Fix your logic and then click 'Run' again.")
		print(msg)

if __name__ == "__main__":
	main()
