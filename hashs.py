import pandas as pd
import csv
import json
from nltk.tokenize import RegexpTokenizer
#### ---hash --####


class HashMap:

    def __init__(self):
        self.size = 15000
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):

        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:

                if pair[0] == key:
                    return pair[1]
            return None


def result(words):
    df = pd.read_csv('test.csv')
    f = open('Positional.json')
    mykey = json.load(f, parse_int=int)
    f.close()
    l = []
    h = HashMap()
    for i in mykey:
        h.add(i, mykey[i])
    for i in range(0, len(words)):
        j = words[i]
        t = h.get(j)
        if t != None:
            for key, var in t.items():
                for k in key:
                    l.append(df['url'][int(k)])
        elif len(l) <= 0:
            l.append(t)
        else:
            continue
    return set(l)


def search(wordsearchs):
    tokenizer = RegexpTokenizer(r'\w+')
    wordsearch = wordsearchs
    wordsearch = wordsearch.lower()
    wordtoken = tokenizer.tokenize(wordsearch)
    return wordtoken
