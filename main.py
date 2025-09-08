from stats import countWords
from stats import countChars
from stats import sortByFreq


def main():
    words = countWords("books/frankenstein.txt")
    character = countChars("books/frankenstein.txt")
    charSorted = sortByFreq(character)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", words, "total words")
    print("--------- Character Count -------")


    for i in charSorted:
        print(i["name"]+":", i["num"])

main()   
