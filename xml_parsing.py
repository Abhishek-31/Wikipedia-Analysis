#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:06:43 2019

@author: simransetia
"""
import xml.etree.cElementTree as ec
tree = ec.parse('/Users/simransetia/Documents/research/simran/Others/QWiki code/week4wiki.xml')
flag=0
root = tree.getroot()
for page in root:
    for child in page:
        if 'title' in child.tag:
            if child.text=='Lecture Notes: Week 4':
                #print('yes')
                flag=1
            else:
                flag=0
    
        if 'revision' in child.tag and flag==1:
                #print(flag)
            for each in child:
                if 'text' in each.tag:
                    s=each.text
                    print(s)