##################################################################################################################################################
# Program: m7 homework #7 String Manipulation: 2. Most Frequent Character
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/28/23
##################################################################################################################################################

# 2. Most Frequent Character
# Write a program that lets the user enter a string and displays the character that appears most
# frequently in the string

# importing Counter from collections
from collections import Counter


def main():
    # Initializing variables
    sentence = ''
    
    # Function Call
# User Input Function a string 
    sentence = getString()
# Displaying the most occuring character
    MostOccuringCh(sentence)
    
def getString():
    """ Input a string to return to main. """
    sentence = input("Enter a sentence: ")

    return (sentence)

def MostOccuringCh(sentence):
    """ Calculating and displays the character that appears most. """

    # Creating a dictionary
    ch_occurance = {}

    for ch in sentence:
        if ch in ch_occurance:
            ch_occurance[ch] += 1 # if character == character, the occurance of that character increments by 1
        else:
            ch_occurance[ch] = 1 # setting the occurance of that character to 1
    
    # Setting the value of the most occurring character
    appears_the_most = max(ch_occurance, key = ch_occurance.get)

    print('The character that appears the most is: ' + appears_the_most + '.')

# Calling main
if __name__ == '__main__':
    main()