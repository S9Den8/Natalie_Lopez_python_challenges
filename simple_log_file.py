# Import
from datetime import datetime       # Tool used by function, imports --> current date & time, datetime tool 

# CONSTANTS & VARIABLES
# pass

# FUNCTIONS
def user_log_entry():
    user_message = input("Enter a log message: ")

    # Obtain current date & time --> uses the import datetime tool to summon the current movement in time 
    current_time = datetime.now()

    # Format timestamp like: [2025-11-13 10:15:00]
    timestamp = current_time.strftime("[%Y-%m-%d %H:%M:%S]")

    # Append the timestamp & message to the log file
    with open("log.txt", "a", encoding="utf-8") as file:        # "a" = append mode, utf-8 = correctly handles: english letters, accented letters, symbols, emojis
        file.write(f"{timestamp} {user_message}\n")             # file.write() = writes text into the file object I already opened.

# MAIN():

if __name__ == "__main__":
    user_log_entry()
