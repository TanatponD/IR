import re
import tfidf


def getRanking(result):
    regex = re.compile(result)
    l = ['this', 'is', 'just', 'a', 'test', 'thos',
         'thus', 'isad', 'isu', 'thailand', 'thinanus']
    matches = [string for string in l if re.match(regex, string)]

    print(matches)
    for i in matches:
        print(i)


getRanking("i")
