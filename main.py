from stats import countWords
from stats import countChars
from stats import sortByFreq
import sys


def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    words = countWords(sys.argv[1])
    character = countChars(sys.argv[1])
    charSorted = sortByFreq(character)

    print("============ BOOKBOT ============")
    print("Analyzing book found at "+sys.argv[1])
    print("----------- Word Count ----------")
    print("Found", words, "total words")
    print("--------- Character Count -------")


    for i in charSorted:
        print(i["name"]+":", i["num"])

main()   
