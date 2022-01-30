# Consider a loop that counts from 1 to 10 but prints only the odd numbers in that range
currentNumber = 0

while currentNumber <= 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
        continue

    print(currentNumber)
