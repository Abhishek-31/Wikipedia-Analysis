# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
# 
# import PyPDF2
# pdf_file = open('123.pdf', 'rb')
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
# number_of_pages = read_pdf.getNumPages()
# page = read_pdf.getPage(0)
# page_content = page.extractText()
# print page_content
# =============================================================================

from PyPDF2 import PdfFileReader

def get_info(path):

    with open(path, 'rb') as f:

        pdf = PdfFileReader(f)
        page=pdf.getPage(0)
        page_content = page.extractText()
        print(page_content.encode("utf-8"))
# =============================================================================
#                 print(i,"EXCEPTION")
# =============================================================================
# =============================================================================
#         print page_content
# =============================================================================
        print repr(page_content)
        info = pdf.getDocumentInfo()

        number_of_pages = pdf.getNumPages()

    print(info)

    author = info.author

    creator = info.creator

    producer = info.producer

    subject = info.subject

    title = info.title

if __name__ == '__main__':

    path = '123_C.pdf'

    get_info(path)