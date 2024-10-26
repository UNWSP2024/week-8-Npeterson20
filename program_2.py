# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."



def separate_words(camel_case_str):
    result = camel_case_str[0]  # Start with the first character
    for char in camel_case_str[1:]:
        # If char is uppercase, add a space before it and make it lowercase
        if char.isupper():
            result += ' ' + char.lower()
        else:
            result += char
    # Capitalize the first word in the result
    return result.capitalize()

# Input from user
sentence = input("Enter a CamelCase sentence: ")
# Display separated words
print("Separated sentence:", separate_words(sentence))
