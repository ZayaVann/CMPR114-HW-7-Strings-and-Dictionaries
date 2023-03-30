##################################################################################################################################################
# Program: m7 homework #7 String Manipulation: 4. Pig Latin
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/28/23
##################################################################################################################################################

# Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In
# one version, to convert a word to Pig Latin, you remove the first letter and place that letter
# at the end of the word. Then, you append the string “ay” to the word. Here is an example:
# English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

def main():
    # Initializing variables
    sentence = ''
    
    # Initialzing Sentence that will be Pig Latin
    pig_latin_sentence  = ''

    # Function Call
    print()
# User Input Function for a string 
    sentence = getString()
    print()

    # Creating a list of words from the sentence
    split_sentence = sentence.split()

    # 1st Version: Remove 1st letter, add it to end of the word
    for each_word in split_sentence:
        each_word = each_word[1:] + each_word[0] + 'ay' # 2nd Version: Add "ay" to the word
        pig_latin_sentence += each_word
        pig_latin_sentence += ' '

    # Displaying the sentence translated to Pig Latin
    print("Pig Latin: " + pig_latin_sentence)
    
def getString():
    """ Input a string to return to main. """
    sentence = input("Enter a sentence: ")

    return (sentence)    

# Calling main
if __name__ == '__main__':
    main()
