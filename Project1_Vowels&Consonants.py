##################################################################################################################################################
# Program: m7 homework #7 String Manipulation: 1. Vowels and Consonants
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/28/23
##################################################################################################################################################

# 1. Vowels and Consonants
# Write a program with a function that accepts a string as an argument and returns the...
# number of vowels that the string contains. 
# The application should have another function that accepts a string as an argument and returns the number of consonants that the string...
# contains. The application should let the user enter a string, and should display the number...
# of vowels and the number of consonants it contains.

def main():
    # Initializing variables
    sentence = ''

    # Function Call
# User Input Function a string 
    sentence = getString()
# Displays the number of Vowels
    NumOfVowels(sentence)
    print()
# Displays the number of Consonants
    NumOfConsonants(sentence)
    print()
    
def getString():
    """ Input a string to return to main. """
    sentence = input("Enter a sentence: ")

    return (sentence)

def NumOfVowels(sentence):
    """ Return the number of Vowels in the sentence. """
    # Vowel accumulator
    vowel_count = 0

    # Count the Vowels (A, a, E, e, I, i, O, o, U, u) (Not Y, y). 
    for ch in sentence:
        if ch == 'A' or ch == 'a':
            vowel_count += 1
        if ch == 'E' or ch == 'e':
            vowel_count += 1
        if ch == 'I' or ch == 'i':
            vowel_count += 1
        if ch == 'O' or ch == 'o':
            vowel_count += 1
        if ch == 'U' or ch == 'u':
            vowel_count += 1

    # Print the result.
    print(f'There are {vowel_count} vowels in this sentence.')

def NumOfConsonants(sentence):
    """ Return the number of Consonants in the sentence. """
    # Consonant accumulator 
    consonant_count = 0

    # Count the Consonants (Every letter but: A, a, E, e, I, i, O, o, U, u) (Counting: Y, y). 
    for ch in sentence:
        if ch == 'B' or ch == 'b':
            consonant_count += 1
        if ch == 'C' or ch == 'c':
            consonant_count += 1
        if ch == 'D' or ch == 'd':
            consonant_count += 1
        if ch == 'F' or ch == 'f':
            consonant_count += 1
        if ch == 'G' or ch == 'g':
            consonant_count += 1
        if ch == 'H' or ch == 'h':
            consonant_count += 1
        if ch == 'J' or ch == 'j':
            consonant_count += 1
        if ch == 'K' or ch == 'k':
            consonant_count += 1
        if ch == 'L' or ch == 'l':
            consonant_count += 1
        if ch == 'M' or ch == 'm':
            consonant_count += 1
        if ch == 'N' or ch == 'n':
            consonant_count += 1
        if ch == 'P' or ch == 'p':
            consonant_count += 1
        if ch == 'Q' or ch == 'q':
            consonant_count += 1
        if ch == 'R' or ch == 'r':
            consonant_count += 1
        if ch == 'S' or ch == 's':
            consonant_count += 1
        if ch == 'T' or ch == 't':
            consonant_count += 1
        if ch == 'V' or ch == 'v':
            consonant_count += 1
        if ch == 'W' or ch == 'w':
            consonant_count += 1
        if ch == 'X' or ch == 'x':
            consonant_count += 1
        if ch == 'Y' or ch == 'y':
            consonant_count += 1
        if ch == 'Z' or ch == 'z':
            consonant_count += 1

    # Print the result.
    print(f'There are {consonant_count} consonants in this sentence.')

# Calling main
if __name__ == '__main__':
    main()