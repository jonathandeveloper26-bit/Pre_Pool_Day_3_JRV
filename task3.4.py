## Task 3.4
# 1. Ask a user for a string
# 2. Extracts the first letter of each word
# 3. Joins each of those letters


# Test "Play your trumpet happily on Nights" -> "Python"
user_input = input("Enter a Sentence: ")

# Strategy: 
# Get the Input, iterate through the input to find spaces, take everything before that space and store it in any array as a "word", search for the next space, and so on

words = [] # Empty list of words

# Flags for storing increments where Spaces are Detected
pos1 = 0
pos2 = -1

# For-loop to increment through each letter, searching for spaces
for i in range(len(user_input)):

    #Check if space exists
    if (user_input[i] == " "):
        pos1 = pos2
        pos2 = i
        words.append(user_input[pos1+1:pos2])

    #Final Word (since no space after the final word)
    if (i==len(user_input)-1):
        words.append(user_input[pos2+1:])

# Create New Word
new_word = ""

# Increments through each word in the words list, extracting the first letter only
for word in words:
    new_word+=word[0]

print(new_word)
