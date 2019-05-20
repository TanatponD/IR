import tfidf
import re
import pandas as pd


def wildcard(input):
    x = input.split(" ")
    if(len(x) > 1):
        print(x)
        return input
    else:
        regex = re.compile(input)
        df = pd.read_csv("DataSetTest.csv")
        matches = [i for i in df if re.match(regex, i)]

        print(matches)
        return (matches)

# print(wildcard("i"))
