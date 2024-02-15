def main():

    aggregateReport("books/frankenstein.txt")
    
def aggregateReport(pathString):

    content = openFile(pathString)

    print(f"--- Begin report of {pathString} ---")
    print(f"{numberOfWords(content)} words found in the document")
    print("")

    listOfDicts = []

    for dicts in allChars(content):
        if dicts.isalpha():
            listOfDicts.append({"char": dicts, "num": allChars(content)[dicts]})

    listOfDicts.sort(reverse = True, key = sort_on)

    for value in listOfDicts:
        print(f"The '{value["char"]}' character was found {value["num"]} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def numberOfWords(contentString):
    return len(contentString.split())

def allChars(contentString):
    charDict = {}
    for char in contentString.lower():
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    return charDict

def openFile(pathString):
    with open(pathString) as f:
        content = f.read()
    return content

main()