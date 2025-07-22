import sys
from stats import get_num_words
from stats import get_num_chars


def get_book_text(filepath):
    f = open(filepath)
    file_contents = f.read()
    f.close()
    return(file_contents)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = str(sys.argv[1])
    doc = get_book_text(filepath)
    num_words = get_num_words(doc)
    char_count = get_num_chars(doc)
    print("============ BOOKBOT ===========")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in char_count.keys():
        if key.isalpha():
            print(f"{key}: {char_count[key]}")


main()