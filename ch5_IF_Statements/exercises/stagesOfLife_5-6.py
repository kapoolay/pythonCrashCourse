# if-elif-else chain
# Determine a person's stage of life
# Set a value for the variable 'age'
# if age < 2 years --> 'Baby'
# if age < 4 --> 'Toddler'
# if age < 13 --> 'Kid'
# if age < 20 --> 'Teenager'
# if age < 65 --> 'Adult'
# else >= 65 --> 'Elder'

age = 66

# # OG code
# if age < 2:
#     print('Baby')
# elif age < 4:
#     print('Toddler')
# elif age < 13:
#     print('Kid')
# elif age < 20:
#     print('Teenager')
# elif age < 65:
#     print('Adult')
# else:
#     print('Elder')


# Cleaner code
if age < 2:
    stage = 'Baby'
elif age < 4:
    stage = 'Toddler'
elif age < 13:
    stage = 'Kid'
elif age < 20:
    stage = 'Teenager'
elif age < 65:
    stage = 'Adult'
else:
    stage = 'Elder'

print(f'You are a {stage}!')
