# f(x) = x^2
f = lambda x: x**2

# Let A = 0, x* = 0, dx = 1.
A = 0
xStar = 0
dx = 1

# While x* < 3, continue.
while xStar < 3:

	# Add f(x*) * dx to A.
	A += f(xStar) * dx

	# Add dx to x*.
	xStar += dx

	# Go back to step 2.
	# This is done automatically by indentation.

# Output A.
print(A)
