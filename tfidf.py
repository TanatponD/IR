from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words
import numpy as np
import pandas as pd
import math
import csv
import time


def get_tfidf(input):
    start = time.time()

    """# Preprocessing"""

    def convert_lower_case(data):
        return np.char.lower(data)

    def remove_stop_words(data):
        stop_words = stopwords.words('english')
        words = word_tokenize(str(data))
        new_text = ""
        for w in words:
            if w not in stop_words and len(w) > 1:
                new_text = new_text + " " + w
        return new_text

    def remove_punctuation(data):
        symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
        for i in range(len(symbols)):
            data = np.char.replace(data, symbols[i], ' ')
            data = np.char.replace(data, "  ", " ")
        data = np.char.replace(data, ',', '')
        return data

    def remove_apostrophe(data):
        return np.char.replace(data, "'", "")

    def stemming(data):
        stemmer= PorterStemmer()
        
        tokens = word_tokenize(str(data))
        new_text = ""
        for w in tokens:
            new_text = new_text + " " + stemmer.stem(w)
        return new_text

    def convert_numbers(data):
        tokens = word_tokenize(str(data))
        new_text = ""
        for w in tokens:
            try:
                w = num2words(int(w))
            except:
                a = 0
            new_text = new_text + " " + w
        new_text = np.char.replace(new_text, "-", " ")
        return new_text

    def preprocess(data):
        data = convert_lower_case(data)
        data = remove_punctuation(data) #remove comma seperately
        data = remove_apostrophe(data)
        data = remove_stop_words(data)
        data = convert_numbers(data)
        data = stemming(data)
        data = remove_punctuation(data)
        data = convert_numbers(data)
        data = stemming(data) #needed again as we need to stem the words
        data = remove_punctuation(data) #needed again as num2word is giving few hypens and commas fourty-one
        data = remove_stop_words(data) #needed again as num2word is giving stop words 101 - one hundred and one
        return data

    alpha = 0.3
    arrayURL = []
    arrayList = []

    url = 98
    df = pd.read_csv('test.csv')
    # for i in range(0,len(df)):
    for i in range(0,url):
        arrayURL.append(df['url'][i])

    with open('DataSetTest.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            arrayList.append(row)

    DF = {}

    for i in range(0,url):
        tokens = arrayList[i]
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}

    for i in DF:
        DF[i] = len(DF[i])

    wordsize = len(DF)
    wordsize
    totalword = [x for x in DF]

    def doc_freq(word):
        count = 0
        try:
            count = DF[word]
        except:
            pass
        return count

    """### Calculating TF-IDF for body, we will consider this as the actual tf-idf as we will add the title weight to this."""

    doc = 0
    tf_idf = {}

    for i in range(0,url):
        tokens = arrayList[i]
        counter = Counter(tokens)
        words_count = len(tokens)
        
        for token in np.unique(tokens):
            
            tf = counter[token]/words_count
            df = doc_freq(token)
            idf = np.log((url+1)/(df+1))            
            tf_idf[doc, token] = tf*idf

        doc += 1


    """## Merging the TF-IDF according to weights"""

    for i in tf_idf:
        tf_idf[i] *= alpha

    # print(type(tf_idf))
    # print(tf_idf)

    """# TF-IDF Cosine Similarity Ranking"""

    def cosine_sim(a, b):
        cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
        return cos_sim

    """### Vectorising tf-idf"""

    D = np.zeros((url, wordsize))
    for i in tf_idf:
        try:
            ind = totalword.index(i[1])
            D[i[0]][ind] = tf_idf[i]
        except:
            pass

    def gen_vector(tokens):

        Q = np.zeros((len(totalword)))
        
        counter = Counter(tokens)
        words_count = len(tokens)

        query_weights = {}
        
        for token in np.unique(tokens):
            
            tf = counter[token]/words_count
            df = doc_freq(token)
            idf = math.log((url+1)/(df+1))

            try:
                ind = totalword.index(token)
                Q[ind] = tf*idf
            except:
                pass
        return Q

    def cosine_similarity(k, query):
        # print("Cosine Similarity")
        preprocessed_query = preprocess(query)
        tokens = word_tokenize(str(preprocessed_query))
        
        # print("\nQuery:", query)
        # print("")
        # print(tokens)
        
        d_cosines = []
        
        query_vector = gen_vector(tokens)
        
        for d in D:
            d_cosines.append(cosine_sim(query_vector, d))
            
        out = np.array(d_cosines).argsort()[-k:][::-1]
        # print(len(d_cosines))
        # print(d_cosines)
        # print(sorted(d_cosines))
        # print("")
        
        # print(out)
        # print(sorted(out))

        time_2f = '%.2f' % (time.time() - start)
        times = ((" %s seconds " % time_2f ))
        # print(times)
    #     for i in out:
    #         print(i, dataset[i][0])
        Ranking = {}
        for x in range(0,url):
            Ranking[out[x]] = arrayURL[x]
            # print(arrayURL[x])

        return tokens, dict(sorted(Ranking.items())), times, (d_cosines)
    
    Q = cosine_similarity(url, input)

    print(Q)
    return Q

# print(readfile("Without the drive of Rebeccah's insistence, Kate lost her momentum. She stood next a slatted oak bench, canisters still clutched, surveying"))
# print(readfile('to'))