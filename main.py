import tfidf
import re
import pandas as pd


def wildcard(input):
    regex = re.compile(input)
    df = pd.read_csv("DataSetTest.csv")
    matches = [string for string in df if re.match(regex, string)]

    Ranking = []

    for i in matches:
        Ranking.append(tfidf.get_tfidf(i))

    print(Ranking)
    return Ranking

