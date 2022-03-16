from fileinput import fileno
from bs4 import BeautifulSoup, SoupStrainer
import bs4, requests, sys, codecs, urllib.request, re
from bs4.element import Comment
import urllib.request
import urllib.parse
from urllib.parse import urljoin, urlencode
import pandas as pd


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = bs4.BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
headers={'User-Agent':user_agent,}

#ENGLISH SPEAKERS: 
EnglishDF = pd.DataFrame(columns=['speakerID','native_language','birth_place','other_languages','age','sex','english_onset_age','english_method','english_residence','english_residence_length'])
parser = 'html.parser'  
request=urllib.request.Request('https://accent.gmu.edu/browse_language.php?function=find&language=english',None,headers)
resp = urllib.request.urlopen(request)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))


 
pages = []
for link in soup.find_all('a', href=True):
    if "speakerid" in str(link):
        lien = "https://accent.gmu.edu/"+str(link['href'])
        pages.append(lien)

soundFile = 1
for webpage in pages:
    #try:
    request=urllib.request.Request(webpage,None,headers) #The assembled request

    response = urllib.request.urlopen(request)
    data = response.read()
    contents = text_from_html(data) 

    speakerID = "speakerID_"+re.findall(r"(?<=speakerid=)[0-9]*",webpage)[0].strip()

    fileNo = "english"+str(soundFile)+".mp3"
    
    native_language = re.findall(r"(?<=native language:).*(?=other)",contents)[0].strip()

    birth_place = re.findall(r"(?<=birth place:).*(?=\(map\))",contents)[0].strip()

    other_languages = re.findall(r"(?<=other language\(s\):).*(?=age\,)",contents)[0].strip()

    age = re.findall(r"(?<=age, sex:).+?(?=\,)",contents)[0].strip()

    sex = re.findall(r"(?<=[0-9]\,).+?(?=age of english)",contents)[0].strip()

    english_onset_age = re.findall(r"(?<=age of english onset:).*(?=english learning method:)",contents)[0].strip()

    english_method = re.findall(r"(?<=english learning method:).+?(?=english residence:)",contents)[0].strip()

    english_residence = re.findall(r"(?<=english residence:).*(?=length of english residence:)",contents)[0].strip()

    english_residence_length = re.findall(r"(?<=length of english residence:).+?s",contents)[0].strip()

    newLine = {"speakerID":speakerID,\
        "sound_file_no":fileNo,\
            "native_language":native_language,\
                "birth_place":birth_place,\
                    "other_languages":other_languages,\
                        "age":age,\
                            "sex":sex,\
                                "english_onset_age":english_onset_age,\
                                    "english_method":english_method,\
                                        "english_residence":english_residence,\
                                            "english_residence_length":english_residence_length}
 
    EnglishDF = EnglishDF.append(newLine,ignore_index=True)
   
    soundFile += 1

EnglishDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/EnglishDF.csv", encoding="UTF-8", index=False) 


#FRENCH SPEAKERS: 
FrenchDF = pd.DataFrame(columns=['speakerID','native_language','birth_place','other_languages','age','sex','english_onset_age','english_method','english_residence','english_residence_length'])
parser = 'html.parser'  
request=urllib.request.Request('https://accent.gmu.edu/browse_language.php?function=find&language=french',None,headers)
resp = urllib.request.urlopen(request)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))


pages = []
for link in soup.find_all('a', href=True):
    if "speakerid" in str(link):
        lien = "https://accent.gmu.edu/"+str(link['href'])
        pages.append(lien)

soundFile = 1
for webpage in pages:
    #try:
    request=urllib.request.Request(webpage,None,headers) #The assembled request

    response = urllib.request.urlopen(request)
    data = response.read()
    contents = text_from_html(data) 

    speakerID = "speakerID_"+re.findall(r"(?<=speakerid=)[0-9]*",webpage)[0].strip()

    fileNo = "french"+str(soundFile)+".mp3"
    
    native_language = re.findall(r"(?<=native language:).*(?=other)",contents)[0].strip()

    birth_place = re.findall(r"(?<=birth place:).*(?=\(map\))",contents)[0].strip()

    other_languages = re.findall(r"(?<=other language\(s\):).*(?=age\,)",contents)[0].strip()

    age = re.findall(r"(?<=age, sex:).+?(?=\,)",contents)[0].strip()

    sex = re.findall(r"(?<=[0-9]\,).+?(?=age of english)",contents)[0].strip()

    english_onset_age = re.findall(r"(?<=age of english onset:).*(?=english learning method:)",contents)[0].strip()

    english_method = re.findall(r"(?<=english learning method:).+?(?=english residence:)",contents)[0].strip()

    english_residence = re.findall(r"(?<=english residence:).*(?=length of english residence:)",contents)[0].strip()

    english_residence_length = re.findall(r"(?<=length of english residence:).+?s",contents)[0].strip()

    newLine = {"speakerID":speakerID,\
        "sound_file_no":fileNo,\
            "native_language":native_language,\
                "birth_place":birth_place,\
                    "other_languages":other_languages,\
                        "age":age,\
                            "sex":sex,\
                                "english_onset_age":english_onset_age,\
                                    "english_method":english_method,\
                                        "english_residence":english_residence,\
                                            "english_residence_length":english_residence_length}
 
    FrenchDF = FrenchDF.append(newLine,ignore_index=True)
    soundFile += 1
    #except:
    #    pass
#print(FrenchDF)
FrenchDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/FrenchDF.csv", encoding="UTF-8", index=False) 

#CHINESE SPEAKERS: 
MandarinDF = pd.DataFrame(columns=['speakerID','native_language','birth_place','other_languages','age','sex','english_onset_age','english_method','english_residence','english_residence_length'])
parser = 'html.parser'  
request=urllib.request.Request('https://accent.gmu.edu/browse_language.php?function=find&language=mandarin',None,headers)
resp = urllib.request.urlopen(request)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))


pages = []
for link in soup.find_all('a', href=True):
    if "speakerid" in str(link):
        lien = "https://accent.gmu.edu/"+str(link['href'])
        pages.append(lien)

soundFile = 1
for webpage in pages:
    #try:
    request=urllib.request.Request(webpage,None,headers) #The assembled request

    response = urllib.request.urlopen(request)
    data = response.read()
    contents = text_from_html(data) 

    speakerID = "speakerID_"+re.findall(r"(?<=speakerid=)[0-9]*",webpage)[0].strip()

    fileNo = "mandarin"+str(soundFile)+".mp3"
    
    native_language = re.findall(r"(?<=native language:).*(?=other)",contents)[0].strip()

    birth_place = re.findall(r"(?<=birth place:).*(?=\(map\))",contents)[0].strip()

    other_languages = re.findall(r"(?<=other language\(s\):).*(?=age\,)",contents)[0].strip()

    age = re.findall(r"(?<=age, sex:).+?(?=\,)",contents)[0].strip()

    sex = re.findall(r"(?<=[0-9]\,).+?(?=age of english)",contents)[0].strip()

    english_onset_age = re.findall(r"(?<=age of english onset:).*(?=english learning method:)",contents)[0].strip()

    english_method = re.findall(r"(?<=english learning method:).+?(?=english residence:)",contents)[0].strip()

    english_residence = re.findall(r"(?<=english residence:).*(?=length of english residence:)",contents)[0].strip()

    english_residence_length = re.findall(r"(?<=length of english residence:).+?s",contents)[0].strip()

    newLine = {"speakerID":speakerID,\
        "sound_file_no":fileNo,\
            "native_language":native_language,\
                "birth_place":birth_place,\
                    "other_languages":other_languages,\
                        "age":age,\
                            "sex":sex,\
                                "english_onset_age":english_onset_age,\
                                    "english_method":english_method,\
                                        "english_residence":english_residence,\
                                            "english_residence_length":english_residence_length}
 
    MandarinDF = MandarinDF.append(newLine,ignore_index=True)
    soundFile += 1
    #except:
    #    pass
#print(FrenchDF)
MandarinDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ChineseDF.csv", encoding="UTF-8", index=False) 



#Thai SPEAKERS: 
ThaiDF = pd.DataFrame(columns=['speakerID','native_language','birth_place','other_languages','age','sex','english_onset_age','english_method','english_residence','english_residence_length'])
parser = 'html.parser'  
request=urllib.request.Request('https://accent.gmu.edu/browse_language.php?function=find&language=thai',None,headers)
resp = urllib.request.urlopen(request)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))


pages = []
for link in soup.find_all('a', href=True):
    if "speakerid" in str(link):
        lien = "https://accent.gmu.edu/"+str(link['href'])
        pages.append(lien)

soundFile = 1
for webpage in pages:
    #try:
    request=urllib.request.Request(webpage,None,headers) #The assembled request

    response = urllib.request.urlopen(request)
    data = response.read()
    contents = text_from_html(data) 

    speakerID = "speakerID_"+re.findall(r"(?<=speakerid=)[0-9]*",webpage)[0].strip()

    fileNo = "thai"+str(soundFile)+".mp3"
    
    native_language = re.findall(r"(?<=native language:).*(?=other)",contents)[0].strip()

    birth_place = re.findall(r"(?<=birth place:).*(?=\(map\))",contents)[0].strip()

    other_languages = re.findall(r"(?<=other language\(s\):).*(?=age\,)",contents)[0].strip()

    age = re.findall(r"(?<=age, sex:).+?(?=\,)",contents)[0].strip()

    sex = re.findall(r"(?<=[0-9]\,).+?(?=age of english)",contents)[0].strip()

    english_onset_age = re.findall(r"(?<=age of english onset:).*(?=english learning method:)",contents)[0].strip()

    english_method = re.findall(r"(?<=english learning method:).+?(?=english residence:)",contents)[0].strip()

    english_residence = re.findall(r"(?<=english residence:).*(?=length of english residence:)",contents)[0].strip()

    english_residence_length = re.findall(r"(?<=length of english residence:).+?s",contents)[0].strip()

    newLine = {"speakerID":speakerID,\
        "sound_file_no":fileNo,\
            "native_language":native_language,\
                "birth_place":birth_place,\
                    "other_languages":other_languages,\
                        "age":age,\
                            "sex":sex,\
                                "english_onset_age":english_onset_age,\
                                    "english_method":english_method,\
                                        "english_residence":english_residence,\
                                            "english_residence_length":english_residence_length}
 
    ThaiDF = ThaiDF.append(newLine,ignore_index=True)
    soundFile += 1
    #except:
    #    pass
#print(FrenchDF)
ThaiDF.to_csv("/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/ThaiDF.csv", encoding="UTF-8", index=False) 