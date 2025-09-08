def getBookText(filePath):                  #Function reads txt and returns string
    with open(filePath) as file:
        fileContent = file.read()
    return fileContent
    
def countWords(filePath):                   #Function reads txt, creates a List of all words, and returns List length
    with open(filePath) as file:
        fileContent = file.read()
        wordList = fileContent.split()
        Counter = len(wordList)
    return Counter

def countChars(filePath):                   #Function reads txt, creates a string, lowers all capitals, returns a dict, with count of each character
    with open(filePath) as file:
        fileContent = file.read()
        fileContent = fileContent.lower()
        charCounter = {"a": fileContent.count("a"), "b": fileContent.count("b"), "c": fileContent.count("c"), "d": fileContent.count("d"), "e": fileContent.count("e"), 
        "f": fileContent.count("f"), "g": fileContent.count("g"), "h": fileContent.count("h"), "i": fileContent.count("i"), "j": fileContent.count("j"), 
        "k": fileContent.count("k"), "l": fileContent.count("l"), "m": fileContent.count("m"), "n": fileContent.count("n"), "o": fileContent.count("o"), 
        "p": fileContent.count("p"), "q": fileContent.count("q"), "r": fileContent.count("r"), "s": fileContent.count("s"), "t": fileContent.count("t"), 
        "u": fileContent.count("u"), "v": fileContent.count("v"), "w": fileContent.count("w"), "x": fileContent.count("x"), "y": fileContent.count("y"), 
        "z": fileContent.count("z"), "æ": fileContent.count("æ"), "â": fileContent.count("â"), "ê": fileContent.count("ê"), "ë": fileContent.count("ë"),
        "ô": fileContent.count("ô")}
    return charCounter


def sort_on(items):
    return items["num"]

#function creates a SORTED list of dict-B, out of a dict-A: dict A {"char" : string, "num" int}, sorted by countnumber
def sortByFreq(dictInA):
    listA = []                          # create List
    for key, value in dictInA.items():
        dictB = {"name": key, "num": value}
        listA.append(dictB)                            
    listA.sort(reverse=True, key=sort_on)
    return listA
        