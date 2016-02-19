#/!/usr/bin/python
# -*- coding: utf-8 -*-
#This script is available in Python2.x
#(cf. 12.1.1 of this page http://www.nltk.org/book-jp/ch12.html#id53)

#import nltk.data
#tokenizer = nltk.data.load('tokenizers/punkt/japanese.mader79') 
#para = "日本語でもうまくいくかな？どうかな。どうかなどうかな。"
#print(tokenizer.tokenize(para))
#I couldn't read the library well, so I couldn't find the file for Japanese.
#import sys :I was thinking that it is necessary to use output or something, but it's not.
import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text

PROMPT = '>>'
INITIAL_PROMPT =  '\n>>May I help you?\n\n -Press P to show the Plain text.\n -Insert a Japanese word to get usage examples of given word.\n -Press M to Morphological analysis.\n'

#def servant():
    

output = INITIAL_PROMPT
while True:
    if output:
        break

print output

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^ 「」！？。]*[！？。]')

jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')
ginga = PlaintextCorpusReader("/home/tatsumi/document/", r'20160216.txt', encoding='utf-8', para_block_reader=read_line_block, sent_tokenizer=jp_sent_tokenizer, word_tokenizer=jp_chartype_tokenizer) #Markdown file is also OK.

#print ginga.raw()
#print '/'.join( ginga.words()[0:50] )
#ginga_t = Text( w.encode('utf-8') for w in ginga.words() )
#ginga_t.concordance("私")

#Below wasn't available at all, eather.
#import nltk
#from nltk.corpus.reader import *
#from nltk.corpus.reader.util import *
#from nltk.text import Text
#jpcfg1 = nltk.parse_cfg("""
#... S -> PP VP
#... PP -> NP P
#... VP -> V TENS
#... NP -> NP 'の' NP
#... NP -> NP 'と' NP
#... NP -> N
#... N -> '先生' | '自転車' | '学校' | '僕'
#... P -> 'は' | 'が' | 'を' | 'で' | 'に'
#... V -> '行k' | '殴r' | '見'
#... TENS -> 'ru' | 'ita'
#... """)
