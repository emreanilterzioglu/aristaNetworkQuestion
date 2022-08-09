import os.path
import argparse

def getText(path):
    # Check for file existance
    if not os.path.exists(path):
        print("[ERROR]: File does not exist under given path!")
        return None
    
    # Read and Check for the string size
    textFile = open(path, "r")
    text = textFile.read()
    if len(text) == 0:
        print("[ERROR]: File is empty!")
        return None
    else:
        return text
        
      
def initArgParser():
    # startup parameter parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--input', action='store', type=str, required=False)
    return parser
    
def debugModeStatus(parser):

    if(parser.parse_args().debug == True):
        print("Working on Debug Mode\n")
    return parser.parse_args().debug
    
def getFileName(parser):

    if(parser.parse_args().input == None):
        fileName = "./textFile.txt"  
    else:
        fileName = parser.parse_args().input
    print(fileName)
    return fileName

