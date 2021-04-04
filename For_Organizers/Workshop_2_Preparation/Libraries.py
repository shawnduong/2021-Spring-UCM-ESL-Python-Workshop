# A library is imported to be used.
import time

# A function is defined that calculates the nth Fibonacci number.
# This is very inefficient! In real life, we'd use dynamic programming.
def calc_nth_fibo(n):

	if n == 0:
		# Base case.
		return 0

	elif n == 1:
		# Base case.
		return 1

	else:
		# Recursive calls.
		return calc_nth_fibo(n-1) + calc_nth_fibo(n-2)

# Measure the time.
da = time.time()

# We calculate the 35th Fibonacci number.
fib = calc_nth_fibo(35)

# Measure the time.
db = time.time()

# Output the 35th Fibonacci number.
print(fib)

# Calculate elapsed time as dt = db - da.
dt = db - da

# Print the elapsed time.
print(dt)
