import os
import string
from collections import Counter

def readFile(relativePath):
    try:
        with open(relativePath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found at path({relativePath})"

def getWords(fileContent, withContractions = True):
    punctuation_to_remove = string.punctuation
    punctuation_to_remove = punctuation_to_remove.replace("'", "")

    translator = str.maketrans('', '', punctuation_to_remove)
    final_content = fileContent.translate(translator)
    if withContractions == False:
        final_content = removeContractions(final_content)
        
    return final_content.split()

def getWordCount(fileContent, withContractions = True):
    words = getWords(fileContent, withContractions)
    for word in words:
        word = word.lower()
    return Counter(words)

def removeContractions(fileContent):
    apostrophe_translator = str.maketrans("'", " ")
    return fileContent.translate(apostrophe_translator)

def writeToFile(relativePath, text):
    with open(relativePath, "a") as file:
        file.write(text)

def printToConsoleAndFile(path, text):
    print(text, end="\n")
    writeToFile(path, text)