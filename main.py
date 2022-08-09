import commonOps
import stringOps
import freqCountOps
import commonData
         
def main():
    freqDict = {}

    parser = commonOps.initArgParser()
    # check for startup debug parameter
    commonData.debugMode = commonOps.debugModeStatus(parser)
    
    # get file name from startup args
    fileName = commonOps.getFileName(parser)
       
    # read the text
    text = commonOps.getText(fileName)
    if(text == None):
        return    
    
    # get sentences 
    sentencesList = []
    stringOps.extractSentencesFromText(sentencesList, text)
    
    #process sentences
    freqCountOps.preProcessSentences(sentencesList)
    sentenceNo = 0
    for sentence in sentencesList:
        sentenceNo += 1
        freqCountOps.updateWordFreqData(sentence, freqDict, sentenceNo)
    
    
    # Print Pretty Output 
    stringOps.prettyFreqDictPrint(freqDict)

            
if __name__=="__main__":
    main()
