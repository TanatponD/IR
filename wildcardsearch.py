import re
import tfidf
import pandas as pd


def getRanking(result):
    regex = re.compile(result)
    df = pd.read_csv("DataSetTest.csv")
    matches = [i for i in df if re.match(regex, i)]



getRanking("fox")
