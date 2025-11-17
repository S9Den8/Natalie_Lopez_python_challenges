# Import
pass

# CONSTANTS & VARIABLES
pass



# FUNCTIONS
def password_stregth_checker():
    
    # 1 - Get user's password
    password = (input("Enter a password that is at least 8 characters minimum: "))
    
    # 2 - Check password length (8 characters min. length)
    if len(password) < 8:
        print("Weak: Pasword must be at leaset 8 characters in length.")
        return 
    
    # 3 - Boolean test for password strength, checking password criteria using any() --> must contain at least: 1 = UPPERCASE letter, 1 = lowercase letter, 1 number (#), 1 = symbol ($, %, &, *, @, !, ^, #, ( ), -, _ , +, =)   
    has_upper = any(c.isupper() for c in password)      # .isupper() = this chara is uppercase
    has_lower = any (c.islower() for c in password)     # .islower() = this chara is lowercase
    has_digit = any (c.isdigit() for c in password)     # .isdigit() = this chara is a number
    has_symbol = any (not c.isalnum() for c in password)    # .isalnum() = this chara is NOT a letter  & NOT a number  --> symbols = not letters/numbers, generates True/False, depending on password

    # 4 - Determine Password Strength: adding rating logic 
    """Passwords are strong when they include ALL four categories (1 uppercase, 1 lowercase, 1 number, 1 symbol). If they only contain two or three of the categories, they are considered medium
    strength. Everything else is considered weak."""

    if has_upper and has_lower and has_digit and has_symbol:
        return "Password strength: Strong"
    
    elif (
        (has_upper and has_lower)
        or (has_upper and has_digit)
        or (has_upper and has_symbol)
        or (has_lower and has_digit)
        or (has_lower and has_symbol)
        or (has_digit and has_symbol)
    ):
        return "Password strength: Medium"
    
    else:
        return "Password strength: Weak"


# MAIN():
if __name__ == "__main__":
    while True:
        result = password_stregth_checker()
        print(result)

    # Allow user to try another password

        again = input("Check another password? (y/n): ").lower()        # .lower() turns a str into all lowercase letters, in case users type "Y: or "Yes: instead of "y"
        if again != "y":        # != --> NOT equal, if user types anything other than "y", then stop
            print("Goodbye")
            break           # break --> "stop looping right now"
