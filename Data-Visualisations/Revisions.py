#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:38:19 2019

@author: wanderer
"""
from matplotlib import pyplot as plt
import xml.etree.cElementTree as ec
d={}
wiki1=0
wiki2=0
xaxis=[]
yaxis=[]
xaxis2=[]
yaxis2=[]
for _ in range(1,13):
    print('/home/wanderer/Downloads/JOCWIKI1/week'+str(_)+'wiki.xml')
    tree = ec.parse('/home/wanderer/Downloads/JOCWIKI1/week'+str(_)+'wiki.xml')
    wiki1=0
    wiki2=0
    flag=0
    root = tree.getroot()
    i=0
    for page in root:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        for child in page:
            if 'title' in child.tag:
                if 'Week '+str(_) in child.text:
                    flag=1
                else:
                    flag=0
                        
            if 'revision' in child.tag and flag==1:
#                        print(flag)
                wiki1+=1
    
# =============================================================================
#     a.replace("\n","")
#     a.replace("\t","")
#     with open("check.text","a+") as f:
#         f.write(a)
#     print(len(a))
# =============================================================================
    d[_]=wiki1
    xaxis.append(_)
    yaxis.append(d[_])
    d={}
    print('/home/wanderer/Downloads/JOCWIKI2/week'+str(_)+'wiki_2.xml')
    tree = ec.parse('/home/wanderer/Downloads/JOCWIKI2/week'+str(_)+'wiki_2.xml')   
    lag=0
    root = tree.getroot()
    i=0
    for page in root:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        for child in page:
            if 'title' in child.tag:
                if 'Week '+str(_) in child.text:
                    flag=1
                else:
                    flag=0
        
            if 'revision' in child.tag and flag==1:
                    #print(flag)
                    wiki2+=1
    d[_]=wiki2
    xaxis2.append(_)
    yaxis2.append(d[_])
plt.plot(xaxis,yaxis,label='Week1')
plt.plot(xaxis2,yaxis2,label='Week2')
plt.xlabel("Article")
plt.ylabel("Number of Revisions")
plt.legend()
plt.savefig("Revisions.png")
plt.show()

