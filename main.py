import sys
from stats import get_num_words, count_characters, sorted_character_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sorted_character_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
