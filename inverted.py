
import nltk  # natural language tool kits
import pandas as pd
import time
import json
from nltk.tokenize import RegexpTokenizer
nltk.download('punkt')  # punkt can clear any character without a-z


def search(wordsearchs):
    l = []
    tokenizer = RegexpTokenizer(r'\w+')
    wordsearch = wordsearchs
    wordsearch = wordsearch.lower()
    wordtoken = tokenizer.tokenize(wordsearch)

    df = pd.read_csv('test.csv')
    f = open('Positional.json')
    mykey = json.load(f, parse_int=int)
    f.close()

    for i in wordtoken:
        if i in mykey:
            for j in mykey[i]:
                l.append(df['url'][int(j)-1])
    return l
