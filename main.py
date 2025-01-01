def main():
    file = "books/frankenstein.txt"
    text = get_book_text(file)
    length = get_text_length(text)
    characters = sorted(get_characters_occurences(text).items())
    print(f"--- Begin report of {file} ---")
    print(f"{length} words found in the document")
    for character in characters:
        print(f"The '{character[0]}' character was found {character[1]} times")

def get_book_text(file):
    with open(file) as f:
        return f.read()

def get_text_length(text):
    words = text.split()
    return len(words)

def get_characters_occurences(text):
    characters = {}
    for character in text:
        if not character.isalpha():
            continue
        lower = character.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters

main()