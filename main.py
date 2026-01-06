import sys

from stats import get_num_words, get_book_text, get_num_char, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    path = sys.argv[1]
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    get_num_words(path)
    print("--------- Character Count -------")
    list = sort_dict(get_num_char(path))
    for entry in list:
        print(f"{entry['char']}: {entry['num']}")


main()

