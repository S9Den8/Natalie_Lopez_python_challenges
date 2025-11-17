# Imports
import string

# CONSTANTS & VARIABLES

# FUNCTIONS 

def is_palindrome_V1(text):
    """Return True if text is a palindrome, ignore case & spaces. Clean up & normalize text before checking for palindrome"""
    
    # Normalize string
    text = text.lower() # Converts to lowercase letters
    text = text.replace(", ", "")   # Removes spaces
    text = ''.join(char for char in text if char not in string.punctuation and char != " ")    # Removes punctuation 

    # Reverse normalized str
    reversed_text = text[::-1] 

    # Compare normalized text with its reverse
    return text == reversed_text

# Main Function
def main():
    print(is_palindrome_V1("Checking tex$tx, to find a palindrome.")) # Output: False
    print(is_palindrome_V1("Hello"))    # Output: False
    print(is_palindrome_V1("A man a plan a canal Panama"))  # Output: True
    print(is_palindrome_V1("race car"))     # Output: True
    print(is_palindrome_V1("e!ye"))     # Output: True



if __name__ == "__main__": 
    main()
