### Task 3.5

languages = ["Esperanto", "Spanish", "Portuguese", "Italian", "French", "English", "German", "Dutch", "Swedish", "Polish", "Turkish"]


user_input = input("Enter a String: ").replace(" ", "").lower()
total_letters = len(user_input) # Total character Count

char_freq = {} # Initialize a Dictionary

# Add Frequency of Letters (count/total count) to dictionary
for char in user_input:     
    if char in char_freq:
        char_freq[char] += 100 * 1/total_letters
    else: 
        char_freq[char] = 100 * 1/total_letters

### Used AI to read Graph to save time. 
"""
Letter frequencies (% of all letters) for 11 languages, matching the
stacked-bar chart. Values are approximate; small letters that are too
thin to read on the chart are included where known.
"""

letter_frequencies = [
    {
        "language": "Esperanto",
        "frequencies": {
            "a": 12.12, "i": 10.01, "e": 8.99, "o": 8.78, "n": 7.96, "l": 6.14,
            "s": 6.09, "r": 5.91, "t": 5.28, "k": 4.16, "j": 3.50, "u": 3.18,
            "d": 3.04, "m": 2.99, "p": 2.76, "v": 1.90, "g": 1.17, "f": 1.04,
            "b": 0.98, "c": 0.78, "ĝ": 0.69, "ĉ": 0.66, "ŭ": 0.52, "z": 0.49,
            "ŝ": 0.39, "h": 0.38, "ĵ": 0.16, "ĥ": 0.02,
        },
    },
    {
        "language": "Spanish",
        "frequencies": {
            "e": 13.68, "a": 12.53, "o": 8.68, "s": 7.98, "r": 6.87, "n": 6.71,
            "i": 6.25, "d": 5.86, "l": 4.97, "c": 4.68, "t": 4.63, "u": 3.93,
            "m": 3.15, "p": 2.51, "b": 1.42, "g": 1.01, "v": 0.90, "y": 0.90,
            "q": 0.88, "h": 0.70, "f": 0.69, "z": 0.52, "j": 0.44, "ñ": 0.31,
            "x": 0.22, "k": 0.02, "w": 0.01,
        },
    },
    {
        "language": "Portuguese",
        "frequencies": {
            "a": 14.63, "e": 12.57, "o": 10.73, "s": 7.81, "r": 6.53, "i": 6.18,
            "n": 5.05, "d": 4.99, "m": 4.74, "u": 4.63, "t": 4.34, "c": 3.88,
            "l": 2.78, "p": 2.52, "v": 1.67, "g": 1.30, "h": 1.28, "q": 1.20,
            "b": 1.04, "f": 1.02, "z": 0.47, "j": 0.40, "x": 0.21, "k": 0.02,
            "w": 0.01, "y": 0.01,
        },
    },
    {
        "language": "Italian",
        "frequencies": {
            "e": 11.79, "a": 11.74, "i": 11.28, "o": 9.83, "n": 6.88, "l": 6.51,
            "r": 6.37, "t": 5.62, "s": 4.98, "c": 4.50, "d": 3.73, "p": 3.05,
            "u": 3.01, "m": 2.51, "v": 2.10, "g": 1.64, "z": 1.18, "f": 1.15,
            "b": 0.93, "h": 0.64, "q": 0.51,
        },
    },
    {
        "language": "French",
        "frequencies": {
            "e": 14.72, "s": 7.95, "a": 7.64, "i": 7.53, "t": 7.24, "n": 7.10,
            "r": 6.69, "u": 6.31, "o": 5.80, "l": 5.46, "d": 3.67, "c": 3.26,
            "m": 2.97, "p": 2.52, "v": 1.84, "é": 1.50, "q": 1.36, "f": 1.07,
            "b": 0.90, "g": 0.87, "h": 0.74, "j": 0.61, "à": 0.49, "x": 0.43,
            "z": 0.33, "è": 0.27, "ê": 0.22, "y": 0.13, "ç": 0.09, "k": 0.07,
            "w": 0.05,
        },
    },
    {
        "language": "English",
        "frequencies": {
            "e": 12.70, "t": 9.06, "a": 8.17, "o": 7.51, "i": 6.97, "n": 6.75,
            "s": 6.33, "h": 6.09, "r": 5.99, "d": 4.25, "l": 4.03, "c": 2.78,
            "u": 2.76, "m": 2.41, "w": 2.36, "f": 2.23, "g": 2.02, "y": 1.97,
            "p": 1.93, "b": 1.49, "v": 0.98, "k": 0.77, "j": 0.15, "x": 0.15,
            "q": 0.10, "z": 0.07,
        },
    },
    {
        "language": "German",
        "frequencies": {
            "e": 17.40, "n": 9.78, "i": 7.55, "s": 7.27, "r": 7.00, "a": 6.51,
            "t": 6.15, "d": 5.08, "h": 4.76, "u": 4.35, "l": 3.44, "c": 3.06,
            "g": 3.01, "m": 2.53, "o": 2.51, "b": 1.89, "w": 1.89, "f": 1.66,
            "k": 1.21, "z": 1.13, "p": 0.79, "v": 0.67, "ü": 0.65, "ä": 0.54,
            "ß": 0.31, "ö": 0.30, "j": 0.27, "y": 0.04, "x": 0.03, "q": 0.02,
        },
    },
    {
        "language": "Dutch",
        "frequencies": {
            "e": 18.91, "n": 10.03, "a": 7.49, "t": 6.79, "i": 6.50, "r": 6.41,
            "o": 6.06, "d": 5.93, "s": 3.73, "l": 3.57, "g": 3.40, "v": 2.85,
            "h": 2.38, "k": 2.25, "m": 2.21, "u": 1.99, "b": 1.58, "p": 1.57,
            "w": 1.52, "j": 1.46, "z": 1.39, "c": 1.24, "f": 0.81, "x": 0.04,
            "y": 0.04, "q": 0.01,
        },
    },
    {
        "language": "Swedish",
        "frequencies": {
            "e": 10.15, "a": 9.38, "n": 8.54, "r": 8.43, "t": 7.69, "s": 6.59,
            "i": 5.82, "l": 5.28, "d": 4.70, "o": 4.48, "m": 3.47, "k": 3.14,
            "g": 2.86, "v": 2.42, "h": 2.09, "f": 2.03, "u": 1.92, "p": 1.84,
            "ä": 1.80, "b": 1.54, "c": 1.49, "å": 1.34, "ö": 1.31, "y": 0.71,
            "j": 0.61, "x": 0.16, "w": 0.14, "z": 0.07, "q": 0.02,
        },
    },
    {
        # Read directly off the chart (least precise of the set)
        "language": "Polish",
        "frequencies": {
            "a": 9.9, "o": 8.9, "i": 8.7, "z": 8.7, "e": 8.5, "n": 5.7,
            "s": 4.7, "r": 4.5, "m": 3.8, "c": 3.8, "w": 3.8, "b": 3.4,
            "p": 3.2, "l": 3.0, "d": 3.0, "u": 3.0, "y": 3.0, "t": 2.9,
            "k": 2.9, "h": 1.6, "g": 1.4, "j": 1.1,
        },
    },
    {
        "language": "Turkish",
        "frequencies": {
            "a": 11.92, "e": 8.91, "i": 8.60, "n": 7.49, "r": 6.72, "l": 5.92,
            "ı": 5.11, "d": 4.71, "k": 4.68, "m": 3.75, "y": 3.34, "u": 3.24,
            "t": 3.01, "s": 3.01, "b": 2.84, "o": 2.48, "ü": 1.85, "ş": 1.78,
            "z": 1.50, "ç": 1.46, "g": 1.25, "h": 1.21, "ğ": 1.13, "v": 0.96,
            "c": 0.96, "p": 0.89, "ö": 0.78, "f": 0.46, "j": 0.03,
        },
    },
]

similarities = [
    {
        "language": "Esperanto",
        "similarity": 0
    },
    {
        "language": "Spanish",
        "similarity": 0
    },
    {
        "language": "Portuguese",
        "similarity": 0
    },
    {
        "language": "Italian",
        "similarity": 0
    },
    {
        "language": "French",
        "similarity": 0
    },
    {
        "language": "English",
        "similarity": 0
    },
    {
        "language": "German",
        "similarity": 0
    },
    {
        "language": "Dutch",
        "similarity": 0
    },
    {
        "language": "Swedish",
        "similarity": 0
    },
    {
        "language": "Polish",
        "similarity": 0
    },
    {
        "language": "Dutch",
        "similarity": 0
    }, 
]

for key in char_freq: ## For each letter in my sentence
    lanuage_frequencies_of_letter = {}
    for lan_freq in letter_frequencies:
        try:
            # print("Letter: " + key)
            # print("Language: " + lan_freq["language"])
            # print("Language Frequency: " + str(lan_freq["frequencies"][key]))
            # print("My Freqency: " + str(char_freq[key]))
            similarity = abs(char_freq[key] - lan_freq["frequencies"][key])
            # print("Similarity: "+ str(similarity))
            # print(type(similarity))
            for language in similarities:
                if language["language"] == lan_freq["language"]:
                    if language["language"] == 0:
                        language["similarity"] = similarity
                        
                    else:
                        # print(type(language["language"]))
                        language["similarity"] -= similarity
        except:
            pass

most_similar_language = ""
most_similar = -1000

for lang_freq in similarities:
    # print(lang_freq)
    if float(lang_freq["similarity"]) > float(most_similar):
        most_similar = lang_freq["similarity"]
        most_similar_language = lang_freq["language"]

print(most_similar_language)

            