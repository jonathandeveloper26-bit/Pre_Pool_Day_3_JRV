#Task 1 Epitech Pre_Pool_Day_3

#Task 1.1
long_string = "Good Morning, this sentence is just meant to store a long string into a variable. Then we are supposed to print it!"
print(f"Long String: {long_string}")

#Task 1.2
print(f"First Character: {long_string[0]}")

#Task 1.3
print(f"Last Character: {long_string[-1]}")

#Task 1.4
print(f"Letters 5-10: {long_string[4:10]}")

#Task 1.5
long_string_lc = long_string.lower()
print(f"Lower Case: {long_string_lc}")

#Task 1.6
input_string = "tutu on the tuki-kata"
desired_output = "tata on the taki-kata"

transformed_string = input_string.replace("tu", "ta")

print(f"Transformed String: {transformed_string}")

#Task 1.7
string = "Hello World!"
position = string.find("a")
print(position)

# My Guess: N/A or None
# Answer: -1 (Good to know!)

#Task 1.8
p = "abcdefghij"
print(p[::2][:5][::-1][3:])
# My Guess: 
# p[::2] -> acegi
# [:5] -> acegi
# [::-1] -> igeca
# [3:] -> ca
# Final Output: ca
# Answer: ca - got it right!

#Task 1.9

p = "abcdefghij"
# From what I can see, the length of the string is irrelevant. 
# -> Just get the 3rd and 1st characters of any string

print(p[2::-2])

#Task 1.10
str_in = "Duplicate 10x\n"
print(str_in * 10)

#Task 1.11
# print("hello" + 42) will not print since you are trying to combine a string and an integer.
# to combine the two to get "hello42", first convert 42 to a string.
print("hello" + str(42))







