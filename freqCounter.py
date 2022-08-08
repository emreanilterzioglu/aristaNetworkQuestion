import os.path


def updateWordFreqData(sentence, freqDict, sentenceNo):
    for word in sentence.split():
        value = freqDict.get(word.lower(), [])

        value.append(sentenceNo)
        freqDict[word.lower()] = value
        
def main():
    freqDict = {}

    # list of unwanted delimeters. List can be updated
    unwantedDelimeters = [';', ',', ':']
    
    # Check for file existance
    if not os.path.exists("./textFile.txt"):
        print("[ERROR]: textFile.txt does not exist!")
        return
    
    # Read and Check for the string size
    textFile = open("./textFile.txt", "r")
    sentence = textFile.read()
    if len(sentence) == 0:
        print("[ERROR]: textFile.txt is empty!")
        return
    
    # Remove sentence ending delimeters. -1 is string termination -2 should be delimeter
    if (sentence[-2] == ".") or (sentence[-2] == "!") or (sentence[-2] == "?"):
        sentence = sentence[:-2]
    
    # Remove unwanted delimeters
    for delimeter in unwantedDelimeters:
        sentence = sentence.replace(delimeter, '')
        
    updateWordFreqData(sentence, freqDict, 1)
    
    for word in sorted(freqDict.keys()):
        print(word,"\t{",len(freqDict[word]),":",freqDict[word],"}")

if __name__=="__main__":
    main()
