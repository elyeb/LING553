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

request=urllib.request.Request('https://accent.gmu.edu/soundtracks/',None,headers) #The assembled request

response = urllib.request.urlopen(request)
data = response.read()
contents = text_from_html(data)

EngMP3s = re.findall(r"(?<=english)[0-9]+?(?=\.mp3)",str(contents))

for num in EngMP3s:
    fileName = "english"+str(num)+".mp3"
    mp3_url = "https://accent.gmu.edu/soundtracks/"+fileName

    r = requests.get(mp3_url) # create HTTP response object
    path = "/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/English/"+fileName
    with open(path,'wb') as f:
        f.write(r.content)


FrMP3s = re.findall(r"(?<=french)[0-9]+?(?=\.mp3)",str(contents))
for num in FrMP3s:
    fileName = "french"+str(num)+".mp3"
    mp3_url = "https://accent.gmu.edu/soundtracks/"+fileName

    r = requests.get(mp3_url) # create HTTP response object
    path = "/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/French/"+fileName
    with open(path,'wb') as f:
        f.write(r.content)

ChMP3s = re.findall(r"(?<=mandarin)[0-9]+?(?=\.mp3)",str(contents))
for num in ChMP3s:
    fileName = "mandarin"+str(num)+".mp3"
    mp3_url = "https://accent.gmu.edu/soundtracks/"+fileName

    r = requests.get(mp3_url) # create HTTP response object
    path = "/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/Chinese/"+fileName
    with open(path,'wb') as f:
        f.write(r.content)



ThMP3s = re.findall(r"(?<=thai)[0-9]+?(?=\.mp3)",str(contents))
for num in ThMP3s:
    fileName = "thai"+str(num)+".mp3"
    mp3_url = "https://accent.gmu.edu/soundtracks/"+fileName

    r = requests.get(mp3_url) # create HTTP response object
    path = "/Users/elyebliss/Desktop/LING553/SpeechAccentArchive/Thai/"+fileName
    with open(path,'wb') as f:
        f.write(r.content)