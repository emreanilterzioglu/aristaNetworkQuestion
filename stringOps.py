from commonData import *

def extractSentencesFromText(sentencesList, text):
    tmpSentencesList = []

    basicSentenceExtractor(tmpSentencesList, text)
    extractionErrorChecker (sentencesList, tmpSentencesList)
    
def prettyFreqDictPrint(freqDict):
    outIndex = 0
    print("\n#*#*#*#*#*#*#*# OUTPUT #*#*#*#*#*#*#*#")
    for word in sorted(freqDict.keys()):
        outIndex +=1
        if len(word) > 12 and len(word) <= 18:
            print(outIndex, "\t", word, "{",len(freqDict[word]),":",freqDict[word],"}")     
        elif len(word) >= 6 and len(word) <= 12:
            print(outIndex, "\t", word, "\t{",len(freqDict[word]),":",freqDict[word],"}")
        else:
            print(outIndex, "\t", word, "\t\t{",len(freqDict[word]),":",freqDict[word],"}")
            
def basicSentenceExtractor(tmpSentencesList,text):
    # change new lines and tabs inside of text with space
    text = text.replace("\n", " ") 
    text = text.replace("\t", " ") 

    # find sentence ending delimeters' positions to detect sentences
    endingPoses = ( [pos for pos, char in enumerate(text) if (char == '.') or (char == '!') or (char == '?')])
    
    # if there is no ending delimeter, whole text is our only sentence; if there are, split to sentences.
    if len(endingPoses) == 0:
        tmpSentencesList.append(text)
    else:
        oldPos = 0
        for pos in endingPoses:
            if (pos + 1) < len(text):  # to control index out of range
                if(text[pos + 1] == " ") or (text[pos + 1] == "\n") or (text[pos + 1] == "\t"):
                    tmpSentencesList.append(text[oldPos:pos + 1])
                    oldPos = pos + 2
            else: # add last sentence
                tmpSentencesList.append(text[oldPos:]) 
                
    return tmpSentencesList
    
def extractionErrorChecker(sentences, tmpSentencesList):

    # Recheck sentences is there any fault occured
    faultyDividedSentenceFlag = False
    for tmpSentence in tmpSentencesList:
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
            
    return sentences
