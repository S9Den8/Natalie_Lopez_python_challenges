# IMPORTS
import os

# CONSTANTS & VARIABLES


# FUNCTIONS
def caesar_cipher(text, shift):     # defined function = caesar_cipher
    """String = text, Integer = shift. Encode text using Caesar cipher with given shift"""

    # Empty string, my basket that will hold my shifted message 
    cipher_text = ""
    
    for char in text:   # examining every character in text, one by one, use for loop. Remember the : starts the loop block 
        if char.isupper():       # catches uppercase letters only
            # Handle uppercase letters (A-Z)
            shifted_code = (ord(char) - 65 + shift) % 26 + 65     # Shift the charcter; ord() = converts letter into number code (ASCII "ask-ee" value); chr() = converts numbver code back into a letter. chr = the built-in function in Python (turns # into char), can't use chr but you can use char
            new_char = chr(shifted_code)        # turn number back into a charcter
            cipher_text += new_char             # add the new shifted letter to the growing message (cipher_text); (+=) --> means "take what's already in the variable, & add something new to it."). 
        
        elif char.islower():    #catches lowercase letters only
            # Handle lowercase letters (a-z)     
            shifted_code = (ord(char) - 97 + shift) % 26 + 97
            new_char = chr(shifted_code)        # repeat code for lowercase, unicode values (65 = A-uppercase, 97 = a-lowercase) 
            cipher_text += new_char             # repeat code for lowercase
        
        else:
            cipher_text += char             # Keep punctuation, spaces, numbers (unchanged)
    
    return cipher_text

# MAIN EXECUTION
if __name__ == "__main__":      # Accepts str & int 
    print(caesar_cipher("\nHello, World!", 5))     # Expected output: "Mjqqt, Btwqi"
    print(caesar_cipher("\nxyz", 2))                # Expected output: "zab" 
    print(caesar_cipher("\nPython 123!", 5))        # Expected output: "Udymts 123!"
    print(caesar_cipher("\nabc", 3))                # Expected output: "def"
