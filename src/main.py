def get_content(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def count_words(text):
    tota_words = text.split()
    return tota_words

def count_characters(text):
    characters = {}
    for character in text:
        character = character.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def main():
    path = "books/frankenstein.txt"
    content = get_content(path)
    total_words =count_words(content)
    total_characters = count_characters(content)
    print(content, total_words, total_characters)

if __name__ == '__main__':
    main()