#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:08:53 2019

@author: abhishek
"""
with open("/home/abhishek/Documents/Wikipedia-Analysis/Data/Spherical basis.txt","r") as f:
    a=f.read()
#print(a)
c=[]
b=a.split("\n")
for index,value in enumerate(b):
    if("{\displaystyle" in value):
        for i,v in enumerate(b[index-1::-1]):
            b[index-1-i]=b[index-1-i].strip()
            if(len(b[index-1-i])==0 or len(b[index-1-i])==1 or len(b[index-1-i])==2 or len(b[index-1-i])==3):
                print(str(index-1-i)+" : "+b[index-1-i])
                b[index-1-i]=""
            else:
                print(len(b[index-1-i]))
                break
for index,val in enumerate(b):
    if("{\displaystyle" in val):
        b[index]=""
for _ in b:
    if(_):
        c.append(_)
with open("spherical.txt","w+") as l:
    for i,_ in enumerate(c):
        l.write(_)
        l.write("\n")
#try:
#    for _ in b:
#        if("{\displaystyle" in _):
#            print(_)
#            for l in b[b.index(_)-1::-1]:
#                t=b.index(l)
#                b[t]=b[t].strip()
#                if(len(b[t])==0 or len(b[t])==1):
#                    b[t]=" "
#                else:
#                    break
#except:
#    pass                    
#for _ in b:
#    print(_)
#    print(">>")