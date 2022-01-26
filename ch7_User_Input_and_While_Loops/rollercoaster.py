# How to use the int() function
# Consider a program that determines whehter people are tall enough to ride a roller coaster

height = input("How tall are you, in inches? ")
# Convert the string inputted value into a numerical value
height = int(height)

if height >= 48:
    print(f"\nYou are tall enough to ride!")
else:
    print(f"\nYou are NOT tall enough")

# # Terminal results (IF Results)
# >>> height = input("How tall are you, in inches? ")
# How tall are you, in inches? 48
# >>> height = int(height)
# >>> if height >= 48:
# ...     print(f"\nYou are tall enough to ride!")
# ... else:
# ...     print(f"\nYou are NOT tall enough")
# ...
#
# You are tall enough to ride!

# # Terminal results (Else Results)
# >>> height = input("How tall are you, in inches? ")
# How tall are you, in inches? 72
# >>> height = int(height)
# >>> if height >= 48:
# ...     print(f"\nYou are tall enough to ride!")
# ... else:
# ...     print(f"\nYou are NOT tall enough")
# ...
#
# You are tall enough to ride!
