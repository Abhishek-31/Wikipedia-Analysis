#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:08:04 2019

@author: abhishek
"""

import wikipedia
#Taking random articles from wikipedia. Instead of this we can also type in manually the ytopics we want to match with.
wikipedia_random_articles=[]
# wikipedia_random_articles=wikipedia.random(5)
wikipedia_random_articles.append('Quantum Mechanics')
wikipedia_random_articles.append('Angular momentum diagrams (quantum mechanics)')
wikipedia_random_articles.append("Einstein's thought experiments")
wikipedia_random_articles.append('Fractional quantum mechanics')
wikipedia_random_articles.append('List of quantum-mechanical systems with analytical solutions')
wikipedia_random_articles.append('Macroscopic quantum phenomena')
wikipedia_random_articles.append('Phase space formulation')
wikipedia_random_articles.append('Regularization (physics)')
wikipedia_random_articles.append('Spherical basis')
wikipedia_article="Regularization (physics)"`
#wikipedia_articles=[]
#for wikipedia_article in wikipedia_random_articles:
with open("%s.txt"%wikipedia_article,"w+") as f:
    f.write(str(wikipedia.page(wikipedia_article).content))