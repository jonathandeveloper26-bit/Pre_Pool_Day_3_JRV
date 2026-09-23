## Task 3.1
user_input = input("Enter your Name: ").lower()
user_input = user_input[0].upper() + user_input[1:]
print(f"Hello {user_input}!")

## Task 3.2
user_input = input("Enter a Number: ")
print(type(user_input)) # Outputs: <class 'str'> - this means that any input is automatically converted to the string class (i.e. even though I entered a numeric number, it's stored as a string number (e.g. 42 vs. "42"))

## Task 3.3

num_input1 = input("Enter your First Number: ")
num_input2 = input("Enter your Second Number: ")

print(int(num_input1) + int(num_input2)) # Wrapping in int() converts to an integer prior to summing

