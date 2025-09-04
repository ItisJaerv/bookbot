from stats import countWords
from stats import countChars

def main():
    words = countWords("books/frankenstein.txt")
    print(words, "words found in the document")
    character = countChars("books/frankenstein.txt")
    print(character)


main()   
