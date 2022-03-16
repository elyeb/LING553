#library(reticulate)
#path_to_python <- "~/usr/local/bin/python3/"
#use_python(path_to_python)

import numpy as np
#from numpy import NaN
import pandas as pd


#DF = pd.read_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/EnglishDF.csv")
#country = "usa"
#DF = pd.read_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/FrenchDF.csv")
#country = "france"
DF = pd.read_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ChineseDF.csv")
country = "china"
#DF = pd.read_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ThaiDF.csv")
#country = "thailand"

def getDecision():

    decision = str(input("Continue measuring? Y/N"))
    return decision

def getNextVOT():
    #gets the next recording to measure
    i = 0
    skip = True
    while skip and i < len(DF["birth_country"]):
        if DF.at[i,"birth_country"] != country:
            i += 1
        elif pd.isnull(DF.at[i,"big"])==False:
           
            i += 1
        else:
            skip = False

    return i


    
def inputVOT(ind, decision):

    global DF

    if decision=="Y":
        
        """
        print("Measure VOT for 'peas', "+DF.at[ind,"sound_file_no"])
        sys.stdout.flush()

        releaseBurst = float(input("Input the release burst "))
        DF.at[ind,"peas_st"] = releaseBurst
        voiceStart = float(input("Input the start of voicing "))
        DF.at[ind,"peas_end"] = voiceStart

        VOT = (voiceStart-releaseBurst)*1000
        print("VOT = "+str(VOT)+"ms")
        sys.stdout.flush()

        DF.at[ind,"peas"] = VOT
        

        print("Measure VOT for 'toy', "+DF.at[ind,"sound_file_no"])
        sys.stdout.flush()

        releaseBurst = float(input("Input the release burst "))
        DF.at[ind,"toy_st"] = releaseBurst
        voiceStart = float(input("Input the start of voicing "))
        DF.at[ind,"toy_end"] = voiceStart

        VOT = (voiceStart-releaseBurst)*1000
        print("VOT = "+str(VOT)+"ms")
        sys.stdout.flush()

        DF.at[ind,"toy"] = VOT
        
        """
        print("Measure VOT for 'big', "+DF.at[ind,"sound_file_no"])
        sys.stdout.flush()

        releaseBurst = float(input("Input the release burst "))
        DF.at[ind,"big_st"] = releaseBurst
        voiceStart = float(input("Input the start of voicing "))
        DF.at[ind,"big_end"] = voiceStart

        VOT = (voiceStart-releaseBurst)*1000
        print("VOT = "+str(VOT)+"ms")
        sys.stdout.flush()

        DF.at[ind,"big"] = VOT
        
decision = getDecision()
while(decision=="Y"):
    
    filesComplete= DF.big.notnull().sum()
    print("Completed "+str(filesComplete)+" files")
    sys.stdout.flush()
    ind = getNextVOT()
    inputVOT(ind,decision)
    decision = getDecision()


  

#EnglishDF = DF
#EnglishDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/EnglishDF.csv", encoding="UTF-8", index=False) 
#FrenchDF = DF
#FrenchDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/FrenchDF.csv", encoding="UTF-8", index=False) 
ChineseDF = DF
ChineseDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ChineseDF.csv", encoding="UTF-8", index=False) 
#ThaiDF = DF
#ThaiDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ThaiDF.csv", encoding="UTF-8", index=False) 



