import commonData

def preProcessSentences(sentencesList):
    # Edit delimeters inside sentences then process that sentences

    for sentenceNo in range(0, len(sentencesList), 1): 
        
        if(commonData.debugMode):
            print("\n[DEBUG] ##Sentence No: " + str(sentenceNo + 1) + " Begin##")
            print(sentencesList[sentenceNo])
                
        # Remove unwanted delimeters
        for delimeter in commonData.unwantedDelimeters:
            delimeterPoses = ( [pos for pos, char in enumerate(sentencesList[sentenceNo]) if char == delimeter])
            if len(delimeterPoses) == 0:
                continue
                
            for pos in delimeterPoses:
                if(sentencesList[sentenceNo][pos + 1] == " "):
                    sentencesList[sentenceNo] = sentencesList[sentenceNo][:pos] + " " + sentencesList[sentenceNo][pos + 1:]
        
        # Remove sentence ending delimeters. -1 is string termination -2 should be delimeter
        if (sentencesList[sentenceNo][-1] == ".") or (sentencesList[sentenceNo][-1] == "!") or (sentencesList[sentenceNo][-1] == "?"):
            sentencesList[sentenceNo] = sentencesList[sentenceNo][:-1]
         

def updateWordFreqData(sentence, freqDict, sentenceNo):
    for word in sentence.split():
        value = freqDict.get(word.lower(), [])

        value.append(sentenceNo)
        freqDict[word.lower()] = value
