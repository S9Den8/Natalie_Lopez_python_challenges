# Imports
import os   # check import type
import string   # contains all punctuation characters or chara or ch
import time

# Check for variables & constants, place here

# Main Tasks: function takes a single str as input & returns that string in reverse order
def reverse_string_V1(text):    # Version 1
    return text[::-1]  


def reverse_string_V2(text):    # Version 2
    characters = []  # My accumulator, it starts empty
    for ch in text:  # for loop that will loop through each character
        characters.insert(0, ch)  # Put each new character at front of the list
    return "".join(characters)

def reverse_string_V3(text):
    """Reverse str & ignore punctuation and whitespace"""
    # Build translation table that removes punctuation + whitespace
    remove = str.maketrans('', '', string.punctuation + string.whitespace) 
    # Remove those chara & reverse remaining text
    cleaned = text.translate(remove)
    return cleaned[::-1]

# Bonus Task:
def reverse_value_1(x):
    """Reverse a str or list & return the same type."""
    if isinstance(x, str):
        return x[::-1]
    elif isinstance(x, list):
        return x[::-1]
    else:
        raise TypeError("Input must be a string or list")

# Stretch Goals
def reverse_value_2(x):    
    """Reverse a strings or lists; ignore punctuation and whitespace for strings."""
    
    # Remove punctuation & whitespace
    remove = str.maketrans('', '', string.punctuation + string.whitespace)      
    
    # Case 1: String input
    if isinstance(x, str):
        cleaned = x.translate(remove)
        return cleaned [::-1]
    
    # Case 2: List input
    elif isinstance(x, list):
        cleaned_list = []
        for item in x:
            if isinstance(item, str):
                cleaned_item = item.translate(remove)
                if cleaned_item:
                    cleaned_list.append(cleaned_item[::-1]) # reverses each str
            else: 
                cleaned_list.append(item)   # keep non-str as is
        return cleaned_list[::-1]   # return reversed list after loop
    else:
        print(f"Invalid type: {type(x).__name__}. Input must be a string or a list.")
        return x

# testing trying to debug
# print(">>> compare_performance() started <<<")....why.......????
# I am having issues here, the timer is not working, no measuring is taking place, need to research further...

def compare_performance():
    """Compare the performance of slicing vs loop methods for long strings"""
    print("Running performance comparison...\n")

    long_text = "1234567890" * 2000000

    try:
        # --- Slicing --- 
        print("Measuring slicing performance...")
        start = time.time()
        reverse_string_V1(long_text)
        slicing_time = time.time() - start

        # --- Loop ---
        print("Measuring loop performance")
        start = time.time()
        reverse_string_V2(long_text)
        loop_time = time.time() - start

        # Print Results 
        print(f"\nSlicing method took: {slicing_time:.6f} seconds")
        print(f"Loop method took: {loop_time:.6f} seconds")

        # Compare Results
        if slicing_time < loop_time:
            print("Slicing is faster.")
        else: 
            print("\nLoop is slower, but it has its advantages.\n")

    except Exception as e:
        print("\nException occured:", type(e).__name__, "-", e)

# Main Function:
def main():
    # Testing V1: the reverse_string function: 
    print(reverse_string_V1("Voynich"), "\n")   # I expect to see "ncinyoV"
    print(reverse_string_V1("prime"), "\n")     # I exsect to see "emirp"

    # Testing V2: manuallly building for loop to reverse str 
    print(reverse_string_V2("Cipher"), "\n")    # I expect to see "rephiC"

    # Testing V3: reverse str, ignore punctuation & whitespace
    print(reverse_string_V3("cele!st,ial"), "\n")   # I expect "laitselec"
    print(reverse_string_V3("The Voynich Manuscript"), "\n")  # Should see "tpircsunamhcinyoV" 
    print(reverse_string_V3("Undecipherable! Codex!!"), "\n")    # Expect "xedoCelbarehpicednU"

    # Testing BONUS reverse_value: reversing a string or list & returning the same
    print(reverse_value_1("center"))  # I expect to see retnec
    print(reverse_value_1([1, 2, 3, 4, 5]))   # I expect to see 5, 4, 3, 2, 1

    # Testing Stretch Goals: reverse_value_2()
    # Reverse_value_2() removes punctuation + whitespace for str & lists
    print("reverse_value_2 STRING tests:")
    print(reverse_value_2("trea s ure! My st ery!"), "\n") # Expect: "yretsyMerusaert"

    print("reverse_value_2 LISTS tests:")
    print(reverse_value_2(["Cicaida, 3301!"]), "\n")  # Expect: ['1033adiaciC"]

    # Performance Comparison: slicing vs. loop
    print("\n--- Performance Comparison ---")
    compare_performance()
    # couldn't get this to work....not sure why after days....


if __name__ == "__main__": 
    main()