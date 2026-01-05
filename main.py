from stats import get_word_count

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

contents = get_book_text()

get_word_count(contents)
    








