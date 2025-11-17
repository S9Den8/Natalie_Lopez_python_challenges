# imports
import os

# CONSTANTS & VARIABLES


# Functions
def find_max(numbers):
    """This list accepts integers & floats. Returns the largest nuimber from the list manually."""
    
    # Handling empty lists  
    if not numbers:
        raise ValueError("The list is empty") 

    # Assume the first number is the max (aka "current_max", local variable)
    current_max = numbers[0]        # [0] = assume the first number in the list is the biggest for now

    # Use a for loop --> looping through the rest of the list
    for num in numbers:         # Checking every number in the list
        if num > current_max:   # Where my function will ask, "Is this number is bigger than the current_max?"
            current_max = num   # Where my function will verify my answer if it finds a greater current_max
    
    return current_max      # Where my function returns the current_max result 

# Safe test wrapper function
def safe_test(numbers):
    try: 
        result = find_max(numbers)
        print(f"List: {numbers} -> Max: {result}\n")
    except Exception as e:
        print(f"List: {numbers} -> Error: {e}\n")

# TEST CASE FUNCTIONS (each calls safe_test)
def test_case_1():
    numbers = [1.2, 4, 17, 80, 15, 38, 45, 56, 65, 75.5]
    safe_test(numbers)       # Expected result: 80

def test_case_2():
    numbers = [20.5, 17.9, 300, 100, 180, 2]
    safe_test(numbers)       # Expected result: 300

def test_case_3():
    numbers = [1200, 40, 50, 10]
    safe_test(numbers)       # Expected result: 1200
     

def test_case_4():
    numbers = [-11, 390, 18.5, 19]
    safe_test(numbers)       # Expected result: 390

def test_case_5():
    numbers = []    # Empty list
    safe_test(numbers)       # Expected result: Error


# Main Execution
if __name__ == "__main__": 
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
