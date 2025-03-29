

from stats import get_book_text, get_num_words, get_letter_count, get_sort

import sys

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():

    print("Please Provide a file path to review")
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_counts = get_letter_count(text)
    sorted_chars = get_sort(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
