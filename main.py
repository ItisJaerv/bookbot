def main():
    text = getBookText("books/frankenstein.txt")
    words = countWords("books/frankenstein.txt")
    print(words, "words found in the document")

def getBookText(filePath):
    with open(filePath) as file:
        fileContent = file.read()
    return fileContent
    
def countWords(filePath):
    with open(filePath) as file:
        fileContent = file.read()
        wordList = fileContent.split()
        Counter = len(wordList)
    return Counter



main()   
