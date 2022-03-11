# Using a Function with a while loop

def get_formatted_name(firstName, lastName):
    """Return a full name, neatly formatted"""
    fullName = f"{firstName} {lastName}"
    return fullName.title()

# This is an infinite loop!

while True:
    print("\nPlease tell me your name:")
    print("(enter \'q\' at anytime to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        print("\nThank you for playing!")
        break
    l_name = input("Last name: ")
    if l_name == "q":
        print("\nThank you for playing!")
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")