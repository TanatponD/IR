import tfidf
import re
import pandas as pd


def wildcard(input):
    regex = re.compile(input)
    df = pd.read_csv("DataSetTest.csv")
    matches = [i for i in df if re.match(regex, i)]

    print(matches)
    return (matches)
