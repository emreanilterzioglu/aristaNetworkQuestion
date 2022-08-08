import os.path
import nltk

def updateWordFreqData(sentence, freqDict, sentenceNo):
    for word in sentence.split():
        value = freqDict.get(word.lower(), [])

        value.append(sentenceNo)
        freqDict[word.lower()] = value
         
def main():
    freqDict = {}
    
    # list of specialWordsList. List can be updated
    specialWordsList = ["Mr.", "St.", "Mrs.", "Ms.", "Dr.", 
    "Inc.", "Ltd.", "Jr.", "Sr.", "Co.", 
    ".com", ".net", ".org", ".io", ".gov", ".edu",
    "i.e.", "etc.", "e.g."]
    
    # list of unwanted delimeters. List can be updated
    unwantedDelimeters = [';', ',', ':']

    # Natural Language ToolKit Init
    #nltk.download('punkt')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
   
    # Check for file existance
    if not os.path.exists("./textFile.txt"):
        print("[ERROR]: textFile.txt does not exist!")
        return
    
    # Read and Check for the string size
    textFile = open("./textFile.txt", "r")
    text = textFile.read()
    if len(text) == 0:
        print("[ERROR]: textFile.txt is empty!")
        return
    
    
    # Split text into sentences
    sentences = []
    faultyDividedSentenceFlag = False
    for tmpSentence in tokenizer.tokenize(text): 
        tmpWordList = tmpSentence.split() 

        if faultyDividedSentenceFlag == True:
            sentences[-1] = sentences[-1] + " " + tmpSentence
            faultyDividedSentenceFlag = False 
            for specialWord in specialWordsList:
                if (specialWord in tmpWordList[-1]):
                    faultyDividedSentenceFlag = True   
        else:
            for specialWord in specialWordsList:
                if (specialWord in tmpWordList[-1]):
                    faultyDividedSentenceFlag = True   
            sentences.append(tmpSentence)

                
    
    # Edit delimeters inside sentences then process that sentences
    sentenceCount = 0
    for sentence in sentences: 
        sentenceCount +=1    
        # Remove sentence ending delimeters. -1 is string termination -2 should be delimeter
        if (sentence[-1] == ".") or (sentence[-1] == "!") or (sentence[-1] == "?"):
            sentence = sentence[:-1]
        
        # Remove unwanted delimeters
        for delimeter in unwantedDelimeters:
            delimeterPoses = ( [pos for pos, char in enumerate(sentence) if char == delimeter])
            if len(delimeterPoses) == 0:
                continue
                
            for pos in delimeterPoses:
                    if(sentence[pos + 1] == " "):
                        sentence = sentence[:pos] + " " + sentence[pos + 1:]
            
        updateWordFreqData(sentence, freqDict, sentenceCount)
    
    
    # Print Pretty Output 
    outIndex = 0
    for word in sorted(freqDict.keys()):
        outIndex +=1
        if len(word) > 12 and len(word) <= 18:
            print(outIndex, "\t", word, "{",len(freqDict[word]),":",freqDict[word],"}")     
        elif len(word) > 6 and len(word) <= 12:
            print(outIndex, "\t", word, "\t{",len(freqDict[word]),":",freqDict[word],"}")
        else:
            print(outIndex, "\t", word, "\t\t{",len(freqDict[word]),":",freqDict[word],"}")
            
if __name__=="__main__":
    main()
