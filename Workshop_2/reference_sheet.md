# Workshop: Python Reference Sheet

This serves as a reference sheet covering syntaxes from workshops 1 and 2. When in doubt, push the "Ask for Help" button in Zoom.

## Data Types and Variables

```python
# Variables are just names assigned to data using "=" signs.
myVariables = someData

# Strings are characters and start and end with quotes.
myString = "Hello world!"

# Integers are numbers.
myInt = 20

# Floats are decimals.
myFloat = 2.0

# Booleans are True or False.
myBool = True

# Lists start and end with square brackets.
myList = [10, "foobar", 16]

# Tuples are like lists and start and end with parentheses.
myTuple = (10, "foobar", 16)
```

Lists are mutable while tuples are immutable. This means that lists can be changed, but tuples cannot. When in doubt, use a list.

## If-Else Statements

If-Else statements will execute one set of instructions *if* something is true, *else* it will execute another set of instructions.

```python
if <condition>:
	<instructions>
else:
	<instructions>
```

For example:

```python
age = 17

if age < 18:
	print("Sorry, you can't vote!")
else:
	print("You are able to vote.")
```

The condition `age < 18`, takes `age = 17` and becomes `17 < 18`. This is true because `17` *is* less than `18`, and it will therefore execute code in the `if` block.

## While Loops

While loops will continue to execute code *while* a condition is true.

```python
while <condition>:
	<instructions>
```

For example:

```python
i = 9

while i < 60:
	i = (i * 4) + 9
	print(i)
```

This will continue executing code while `i < 60` is true. The moment the opposite, `i >= 60`, is true, then the loop will stop executing the code inside of it.

## For Loops

For loops are iteration based and instead go through some sort of sequence or collection and execute code *for* every item it finds.

```python
for <item> in <collection>:
	<instructions>
```

For example:

```python
values = [10, 20, 80, 29, 68]

for x in values:
	print(x + 10)
```

This will go through the list of `values` and print out each value plus ten.

## Functions

Functions are defined collections of instructions with an arbitrary number of inputs, outputs, and instructions. Functions are like "mini-programs" and must be **def**ined before they can be called (executed).

```python
def <functionName>(<inputs>):

	<instructions>

	return <outputs>
```

For example:

```python
def mean_average(items):

	total = 0
	numberOfItems = 0

	for item in items:
		total += item
		numberOfItems += 1

	return total / numberOfItems
```

Sidenote: I mentioned `+=` very briefly in workshop 1, but `x += y` is essentially a shorthand way of saying `x = x + y`.
