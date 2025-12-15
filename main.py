import sys
from stats import get_num_of_words, count_characters, to_sorted_list

def check_param():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text():
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    with open(path) as file:
        file_contents = file.read()
        
    return file_contents

def print_out(num_of_words: int, sorted_characters: list):
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['num']}")

def main():
    check_param()

    text = get_book_text()
    num_of_words = get_num_of_words(text)
    characters = count_characters(text)
    sorted_characters = to_sorted_list(characters)

    print_out(num_of_words, sorted_characters)

main()