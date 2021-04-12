# Workshop 3 activity: Create a scanner! For this, there is a helper function
# created for you: scan. The usage is as follows:
#
# scan(HOST, PORT)
# - Where HOST is an IP address as a string, and PORT is an integer.
#
# This function will check if a certain PORT is open on the target HOST. It
# can only check one port. Your job is to create a function that will check
# all ports from up to 100.
#

from helper import scan

# For this activity, you may find it useful to review the range function.
# https://docs.python.org/3.8/library/stdtypes.html#typesseq-range
#
# Remember to indent! Your code should look like the following pseudocode:
# |
# | define a function called scanner, which takes no inputs.
# |
# |     let HOST be the target IP address as a string
# |
# |     for every port up to 100:
# |         call scan with the inputs HOST and port
# |
# The first line of code is already done for you.

def scanner():
