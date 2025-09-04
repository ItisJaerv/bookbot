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
