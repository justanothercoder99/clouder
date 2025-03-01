import string
from collections import Counter
import re

contractions = { "re": "are", "ll": "will", "t": "not", "m": "am" }

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
    without_contractions = fileContent.translate(apostrophe_translator)
    for key, val in contractions.items():
        without_contractions = re.sub(rf'\b{key}\b', val, without_contractions)
    return without_contractions

def writeToFile(relativePath, text):
    with open(relativePath, "a") as file:
        file.write(text)

def printToConsoleAndFile(path, text):
    print(text, end="\n")
    writeToFile(path, text)