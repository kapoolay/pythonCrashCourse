
currentNumber = 1

while currentNumber <= 10000:
	print(currentNumber)
	# Add 1 to the currentNumber, then print again
	currentNumber += 1
	# "+=" operator is shorthand for currentNumber = currentNumber + 1

# Python repeats the loop as long ast he condition "currentNumber <= 5" is true.
# Bc 1 is less than 5, Python prints 1 and then adds 1, making the currentNumber == 2
# Bc 2 is less than 5, Python prints 2 and adds 1 again, making the currentNumber == 3, and so on
# Once the value of currentNumber is greater than 5, the loop stops running
