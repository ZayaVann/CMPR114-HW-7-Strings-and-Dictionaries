##################################################################################################################################################
# Program: m7 homework #7 String Manipulation: 3. Word Separator
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/28/23
##################################################################################################################################################

# Write a program that accepts as input a sentence in which all of the words are run together,
# but the first character of each word is uppercase. Convert the sentence to a string in which
# the words are separated by spaces, and only the first word starts with an uppercase letter. For
# example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell
# the roses.”

def main():
    # Initializing variables
    sentence = ''
    split_sentence = ''
    
    # Function Call
    print()
# User Input Function for a string 
    sentence = getString()
    print()

    # index
    i = 0

    for ch in sentence:
        # 1st Arg: if first character in string is Uppercase.
        # 2nd Arg: if index is beyond the 1st character in the sentence.
        if ch.isupper() and i > 0: 
        # Adding a space after the character.
            split_sentence += ' '
        # Next character set to lowercase.
            split_sentence += ch.lower()
        else:
        # The 1st character remains Capitalized.
            split_sentence += ch

        # Index Incrementing
        i += 1

    # Printing New Sentence
    print('Sentence after words have been spaced,')
    print('and every word after the 1st word has been lowercased: ')
    print(split_sentence)

def getString():
    """ Input a string to return to main. """
    print("Enter a sentence in which all of the words are run together,")
    print("but the first character of each word is uppercase: ")
    sentence = input()

    return (sentence)

# Calling main
if __name__ == '__main__':
    main()