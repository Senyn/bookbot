def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

contents = get_book_text()

def get_word_count(contents):
    words = contents.split()
    count = len(words)
    return print(f"Found {count} total words")

get_word_count(contents)
    








