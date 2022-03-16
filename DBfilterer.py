import pandas as pd

EnglishDF = pd.read_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/EnglishDF.csv")
FrenchDF = pd.read_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/FrenchDF.csv")
ChineseDF = pd.read_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ChineseDF.csv")
ThaiDF = pd.read_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ThaiDF.csv")

#get country of birth place and make own variable
languages = [ThaiDF,EnglishDF,FrenchDF,ChineseDF]
L2s = set()

for lang in languages:  

    birth_country = []
    for place in lang["birth_place"]:
        country = place.split(", ")[len(place.split(", "))-1]
        birth_country.append(country)
    lang.insert(3,"birth_country",birth_country,True)

    for l2 in lang["other_languages"]:

        allL2s = l2.split()
        for indvL2 in allL2s:
            L2s.add(indvL2)

#get all L2s and convert to dummy variables
L2s = list(L2s)
for lang in languages:

    for l2 in L2s:
        var_name = "L2_"+l2
        lang[var_name] = 0
    

    for i in range(0,len(lang["other_languages"])):

        allL2s = lang["other_languages"][i].split()
        for indvL2 in allL2s:
            
            for var in L2s:
                var_name = "L2_"+var
                if indvL2==var:
                    lang.at[i,var_name]=1

#convert english residence to # years rather than string
for lang in languages:

    for i in range(0,len(lang["english_residence_length"])):

        lang.at[i,"english_residence_length"] = float(lang["english_residence_length"][i].split()[0])


            
EnglishDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/EnglishDF.csv", encoding="UTF-8", index=False) 
FrenchDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/FrenchDF.csv", encoding="UTF-8", index=False) 
ChineseDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ChineseDF.csv", encoding="UTF-8", index=False) 
ThaiDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ThaiDF.csv", encoding="UTF-8", index=False) 