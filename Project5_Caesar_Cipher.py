##################################################################################################################################################
# Program: m7 homework #7 String Manipulation: 5. Caesar Cipher
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/30/23
##################################################################################################################################################

# A “Caesar Cipher” is a simple way of encrypting a message by replacing each letter with a
# letter a certain number of spaces up the alphabet. For example, if shifting the message by
# 13, an A would become an N, while an S would wrap around to the start of the alphabet
# to become an F.
#
# Write a program that asks the user for a message (a string) and a shift amount (an integer).
# The values should be passed to a function that accepts a string and an integer as
# arguments, and returns a string representing the original string encrypted by shifting the
# letters by the integer. For example, a string of “BEWARE THE IDES OF MARCH” and
# an integer of 13 should result in a string of “ORJNER GUR VQRF BS ZNEPU”.

def main():
    # Initializing variables
    message = ''
    shift_amt = 0
    encrypted_message = ''

# Function Call
    print()
# User Input Function for a string 
    message, shift_amt = getStringAndShiftAmt()
    print()
# Returning encrypted message
    encrypted_message = CaesarCipherEncrypt(message, shift_amt)
    print()

# Displaying encrypted message
    PrintEncrypted(encrypted_message)

def getStringAndShiftAmt():
    """ Input a string and int value to return to main. """
    message = input("Enter a message (string): ")
    shift_amt = int(input("Enter a shift amount (integer): "))
    return (message, shift_amt)  

def CaesarCipherEncrypt(message, amount):
    """Encrypt each letter of the message by input amount. """
    # Initializing future encryption string
    CC_Encrypt = ''

    split_sentence = message.split()

    for each_word in split_sentence:
        for ch in each_word:
            if ch.isalpha():
            # Shifting the current character by input amount
                within_Alphabet = ord(ch) + amount
            # Returning back to boundary of alphabet
                if within_Alphabet > ord('z'):
                    within_Alphabet -= 26
                last_letter = chr(within_Alphabet)
                # Placing encrypted letter in new string
                CC_Encrypt += last_letter
        CC_Encrypt += ' '
    
    return(CC_Encrypt)

def PrintEncrypted(encrypted_message):
    """ Displaying the encrypted message. """
    print('The message after being encrypted is: ' + encrypted_message)

# Calling main
if __name__ == '__main__':
    main()