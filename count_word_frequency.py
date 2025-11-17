# IMPORT
import os
import string


# CONSTANTS & VARIABLES
# pass

# Functions
def count_word_frequency(filename, remove_stopwords=True):  # funciton defined by the actions: counting words & word frequency. Stop words --> we are filtering these common words.
    with open(filename, "r", encoding="utf-8") as file:     # Open & read ("r") the file, utf-8 --> reads the file codrrectly to prevent read errors, handle all languages & symbols, modern universal standard
        text = file.read()                    

    # 1 - Normalize text (.lowercase --> converts ALL letters to lowercase)
    text = text.lower()     
    
    # 2 - Remove punctuation: 
    for p in string.punctuation:
        text = text.replace(p, "")
        
    # 3 - Split text into words
    words = text.split()

    # 3.5 - Add stop word logic:
    stop_words = {
        "the", "and", "is", "a", "to", "in", "of", "for", "with", "it", "on", "that", "this", "as", "by", "from", "be", "are", "was", "were", "or", "an", "some", "we", "has", "those", "their", "these", "so", "also", "able", "they", "among", "who", "h", "y", "n", "de", "while", "there", "within", "here", "most", "rather", "than"
    }

    # Removing stop words (if enabled)
    if remove_stopwords:
        filtered_words = [word for word in words if word not in stop_words]
    else:
         filtered_words = words

    # 4 - Dictionary: count words using dictionary
    word_count_frequency = {}
        
    for word in filtered_words:         # using the filtered list
        if word in word_count_frequency:
            word_count_frequency[word] += 1
        else:
            word_count_frequency[word] = 1

    # 5 - Sorting by most frequent words --> (key=lambda item: item[1]) = when sorting, look at the second value in each tuple, e.g., ("the", 25); item [0] = the; item[1] = 25 --> we want this! 
    sorted_word_counts = sorted(
        word_count_frequency.items(),   # (word, count)
        key=lambda item: item[1],       # sort by count
        reverse=True                    # highest first 
    )

    return sorted_word_counts   # testing 

# MAIN():
if __name__ == "__main__": 
    # Get the sorted results
    sorted_word_counts = count_word_frequency("count_word_f_text.txt")

    # Save output to a new file
    with open("word_frequency_results.txt", "w", encoding="utf-8") as out:
            for word, count in sorted_word_counts:
                out.write(f"{word}: {count}\n")
    
    print("Results saved to word_frequency_results.txt")
