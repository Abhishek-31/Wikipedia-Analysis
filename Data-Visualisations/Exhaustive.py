#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 10:33:07 2019

@author: wanderer
"""

import nltk, string 
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt') # if necessary...
import fitz
import xml.etree.cElementTree as ec
import os
from matplotlib import pyplot as plt

d={}
xaxis=[]
yaxis=[]
xaxis2=[]
yaxis2=[]


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


for _ in range(1,13):
    print(_)
    print('/home/wanderer/Downloads/JOCWIKI1/week'+str(_)+'wiki.xml')
    tree = ec.parse('/home/wanderer/Downloads/JOCWIKI1/week'+str(_)+'wiki.xml')
    wiki1=0
    wiki2=0
    flag=0
    root = tree.getroot()
    i=0
    a=''
    for page in root:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        for child in page:
            if 'title' in child.tag:
                if 'Week '+str(_) in child.text:
                    flag=1
                else:
                    flag=0
                        
            if 'revision' in child.tag and flag==1:
                for each in child:
                    if "text" in each.tag:
                        a=each.text
    t=''  
    for transcript in os.walk('/home/wanderer/Downloads/transcripts/week'+str(_)):
        for transcripts in transcript[2]:
            doc=fitz.open('/home/wanderer/Downloads/transcripts/week'+str(_)+'/'+transcripts)
            for page in doc:
                text=page.getText()
                t=t+text
    
    d[_]=cosine_sim(a,t.encode("utf-8"))
#    print(str(d[_])+ "is the similarity between week" + str(_)+" and transcripts")
    #    fout.write(text.encode("utf-8"))
    xaxis.append(_)
    yaxis.append(d[_])
    

for _ in range(1,13):
    print(_)
    print('/home/wanderer/Downloads/JOCWIKI2/week'+str(_)+'wiki_2.xml')
    tree = ec.parse('/home/wanderer/Downloads/JOCWIKI2/week'+str(_)+'wiki_2.xml')   
    wiki1=0
    wiki2=0
    flag=0
    root = tree.getroot()
    i=0
    a=''
    for page in root:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        for child in page:
            if 'title' in child.tag:
                if 'Week '+str(_) in child.text:
                    flag=1
                else:
                    flag=0
                        
            if 'revision' in child.tag and flag==1:
                for each in child:
                    if "text" in each.tag:
                        a=each.text
    t=''  
    for transcript in os.walk('/home/wanderer/Downloads/transcripts/week'+str(_)):
        for transcripts in transcript[2]:
            doc=fitz.open('/home/wanderer/Downloads/transcripts/week'+str(_)+'/'+transcripts)
            for page in doc:
                text=page.getText()
                t=t+text
    
    d[_]=cosine_sim(a,t.encode("utf-8"))
#    print(str(d[_])+ "is the similarity between week" + str(_)+" and transcripts")
    #    fout.write(text.encode("utf-8"))
    xaxis2.append(_)
    yaxis2.append(d[_])
    
plt.plot(xaxis,yaxis,label='JOCWiki1')
plt.plot(xaxis2,yaxis2,'b--.',label='JOCWiki2')
plt.xlabel("Article")
plt.ylabel("Similarity of wiki articles with video transcripts")
plt.legend()
plt.savefig("Similarity.png")
plt.show()