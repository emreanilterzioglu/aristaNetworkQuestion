import commonData

def preProcessSentences(sentences):
    # Edit delimeters inside sentences then process that sentences
    sentenceCount = 0
    for sentence in sentences: 
        sentenceCount +=1  
        
        if(commonData.debugMode):
            print("\n[DEBUG] ##Sentence No: " + str(sentenceCount) + " Begin##")
            print(sentence)
                
        # Remove unwanted delimeters
        for delimeter in commonData.unwantedDelimeters:
            delimeterPoses = ( [pos for pos, char in enumerate(sentence) if char == delimeter])
            if len(delimeterPoses) == 0:
                continue
                
            for pos in delimeterPoses:
                if(sentence[pos + 1] == " "):
                    sentence = sentence[:pos] + " " + sentence[pos + 1:]
        
        # Remove sentence ending delimeters. -1 is string termination -2 should be delimeter
        if (sentence[-1] == ".") or (sentence[-1] == "!") or (sentence[-1] == "?"):
            sentence = sentence[:-1]

def updateWordFreqData(sentence, freqDict, sentenceNo):
    for word in sentence.split():
        value = freqDict.get(word.lower(), [])

        value.append(sentenceNo)
        freqDict[word.lower()] = value
