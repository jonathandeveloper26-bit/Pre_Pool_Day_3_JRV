### Epitech Pre_Pool_Day_3

## Initialization of words to look for
words_to_count = ["cat", "mice", "garden"]

## Strings (could also be requested from user) - lowered to make insensitive
str1 = "the CataCat attaCk a Cat"
str1 = str1.lower()
str2 = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
str2 = str2.lower()


## made it easier for myself to switch between the strings I am counting
to_check = str1

## Tracks how many times a word has appeared
word_count = 0

## Checks for words: forward looking
for index in range(len(to_check)):
    for word in words_to_count:
        word_to_check = to_check[index:len(word)+index]
        if word_to_check == word:
            word_count += 1
        else:
            continue

## Checks for words: backwards looking
for index in range(len(to_check)):
    for word in words_to_count:
        new_word = to_check[len(to_check)-index-1:len(to_check)-len(word)-index-1:-1]
        if new_word == word:
            word_count += 1
        else:
            continue

## Prints the word count
print(word_count)