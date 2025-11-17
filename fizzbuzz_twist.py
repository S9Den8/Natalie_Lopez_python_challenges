## Import
pass

# CONSTANTS & VARIABLES
pass

# FUNCTIONS - FIZZ BUZZ CHALLENGES

def fizzbuzz_twist(): 

    # Loop through #s 1 - 100 --> evaluating loops (True/False), so Python knows whether or not to run that line of code. If condition is True = prints, if != will skip it. 
    for num in range(1, 101):       # Range is from 1 to 100, "start at 1, keep going but stop before you hit 101." It will end at 100 --> range(start, stop)

        output = ""

        if num % 3 == 0:            # == --> means "divide evenly", so the number follows thee rule, % = gives remainder after dividing 
            output += "Fizz"        # += --> means "add something to the variable & save the new value"; += --> means "append", "add on top of what was already there."
        elif num % 5 == 0:
            output += "Buzz"
        elif num % 7 == 0:
            output += "Bang"

    # If no rule matches, print the number
        if output == "":
            print(num)
        else:
            print(output)

# MAIN():

if __name__ == "__main__":
    fizzbuzz_twist()