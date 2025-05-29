import sys
from stats import get_num_words, get_character_count, sort_chars

def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        file = sys.argv[1]
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    contents = get_book_text(file)
    word_count = get_num_words(contents)
    char_count: dict = get_character_count(contents)
    sorted_count: list = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_count:
        if i["char"].isalpha:
            print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
