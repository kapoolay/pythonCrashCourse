# # Consider a loop that counts from 1 to 10 but prints only the odd numbers in that range
# currentNumber = 0
#
# while currentNumber < 10:
#     currentNumber += 1
#     if currentNumber % 2 == 0:
#         continue
#
#     print(currentNumber)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Avoiding Infinite Loops
x = 1

while x <= 5:
    print(x)
    x += 1
    # if "x += 1" is omitted, the loop will run forever resulting in infinite 1 values

    # to avoid writing infinite loops, test every while loop and make sure the loop stops when you expect it to --> Unit Testing