#/!/usr/bin/python
# -*- coding: UTF-8 -*-
#This tiny script is available in both Python2.x and Python3.x.

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
para = "Hello World. I'm playfully meeting nltk for the first time. "
print(tokenizer.tokenize(para))

