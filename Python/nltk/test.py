#/!/usr/bin/python
# -*- coding: UTF-8 -*-
#This tiny script is available in both Python2.x and Python3.x.

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/japanese.pickle') 
para = "日本語でもうまくいくかな？どうかな。どうかなどうかな。"
print(tokenizer.tokenize(para))

