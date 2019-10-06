#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:55:14 2019

@author: wanderer
"""

# =============================================================================
# from tika import parser
# 
# raw = parser.from_file('How to give instructions _.pdf')
# print(raw['content'])
# =============================================================================

import PyPDF2
pdf_file = open('sample.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print(page_content.encode('utf-8'))