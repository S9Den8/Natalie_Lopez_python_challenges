# Import
pass

# CONSTANTS & VARIABLES
pass

# FUNCTIONS
def cal_operation_add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"Result {result}")
    return result 

def cal_operation_subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"Result: {result}")
    return result

def cal_operation_multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"Result {result}")
    return result 

def cal_operation_divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    
    result = num1 / num2
    print(f"Result: {result}")
    return result  

# MAIN():
def main():
    while True:
        print("\n Basic Calculator ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            cal_operation_add()
        elif choice == "2":
            cal_operation_subtract()
        elif choice == "3":
            cal_operation_multiply()
        elif choice == "4":
            cal_operation_divide()
        elif choice == "5":
            print("Exit operation")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__": 
    main()