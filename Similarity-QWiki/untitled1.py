#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 10:33:07 2019

@author: wanderer
"""

import fitz
import sys

# =============================================================================
# assert len(sys.argv) == 2, "need filename as parameter"
# =============================================================================
#==============================================================================
# Main Program
#==============================================================================
ifile = "123.pdf"
ofile = ifile + ".txt"

doc = fitz.open(ifile)
pages = len(doc)

fout = open(ofile,"w")

for page in doc:
    text = page.getText()
#    fout.write(text.encode("utf-8"))
    print(text)

fout.close()