def get_word_count(contents):
    words = contents.split()
    count = len(words)
    return print(f"Found {count} total words")


def get_character_count(contents):

    # Make all characters lowercase
    lowercase = contents.lower()
    
    # Compile unique alphabet library
    alphabets = sorted(set(lowercase))

    character_count = dict()

    for letters in alphabets:
        if letters.isalpha() is True:
            count = lowercase.count(letters)
            print(f"{letters}: {count}")
            character_count[letters] = count

        
        

        

