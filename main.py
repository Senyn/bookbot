import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

contents = get_book_text()

from stats import get_word_count
from stats import get_character_count

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
get_word_count(contents)
print("--------- Character Count -------")
get_character_count(contents)    
print("============= END ===============")







