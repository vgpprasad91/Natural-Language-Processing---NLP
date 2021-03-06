#Chunking with NLTK with the help of regular expressions

#get all imports

import nltk
from nltk.corpus import inaugural
from nltk.tokenize import PunktSentenceTokenizer

#Create training and testing data

train_data = inaugural.raw("1789-Washington.txt")
sample_data = inaugural.raw("1793-Washington.txt")

train_tokenizer = PunktSentenceTokenizer(train_data)

#chunking with regular expression

regexpar = nltk.RegexpParser(r"""Chunk: {<.*>+}
                                         }<NNP.?|IN|NNS|TO>+{""")

def chinking():
    try:
        print([regexpar.parse(nltk.pos_tag(nltk.word_tokenize(w))).draw() for w in train_tokenizer.tokenize(sample_data)])

    except Exception as e:
        print(str(e))

chinking()
