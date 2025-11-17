# IMPORT
import os


# CONSTANTS & VARIABLES
pass

# FUNCTIONS
def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise false."""
    # Numbers < 2 not a prime
    if n < 2:
        return False

    # Any number between 2 and n-1 divides evenly into n, it's not a prime    
    for i in range(2, n):   # starting at 2, n = number being tested
        if n % i == 0:
            return False        # If there is a divisor, this means the number divided evenly & is not a prime
    return True     # No divisors found, it's a prime
         

# MAIN FUNCTION:
def main():
    "Testing is_prime function with designated inputs."
    print(is_prime(2))      # True
    print(is_prime(11))     # True
    print(is_prime(15))     # False
    print(is_prime(1))      # False
    print(is_prime(0))      # False
    print(is_prime(29))     # True
    print(is_prime(7879))   # True



if __name__ == "__main__": 
    main()
