import re
import json
from nltk.corpus import stopwords
import pandas as pd
import time


df = pd.read_csv('test.csv')  # อ่านไฟล์ csv เพื่อดึง URL มา
f = open('output.json')  # อ่านไฟล์ json
mykey = json.load(f)  # แปลงไฟล์ json เป็น dictionary
f.close()

# function ใช้ตัดคำและ stopword


def stem(content):

    words = re.findall("[A-Za-z]+", content)
    stop = set(stopwords.words('english'))
    stem = []
    for i in words:

        if i not in stop:
            stem.append(i)
    return stem

# function ใช้นับจำนวนคำทั้งหมด


def frequency(word, dicted):

    count = 0
    for i in dicted[word]:

        len(dicted[word][i])
        count = count + len(dicted[word][i])
    return count

# function ใช้ในการ intersection


def intersec(search, dicts):

    intersect = {}
    n = 0
    for i in search:

        if i in dicts.keys():
            lists = []
            for j in dicts[i]:

                lists.append(j)
                s = set(lists)
            intersect[n] = s
            n += 1
        else:
            n = 0
            break
    first = intersect[0]
    for i in intersect.keys():

        s1 = first.intersection(intersect[i])
        first = s1
        (s2) = first
    return list(s2)

# function ค้นหา


def Searching(wordsearchs):
    start = time.time()
    geturl = {}
    word = wordsearchs.lower()  # ทำให้เป็นตัวพิมพ์เล็ก
    wordsearchs = stem(word)  # ตัด stopword ออก
    result = []
    # try:
    if len(wordsearchs) == 0:
        geturl["Error"] = "Not Found"
        return geturl
    else:
        for i in wordsearchs:

            if i in mykey:  # ที่อยู่ในjson
                result.append(i)
                freq = frequency(i, mykey)
                print(i, ": ", freq)
                for j in mykey[i]:

                    print(f"{j} :{mykey[i][j]}")
            else:
                print(f"{i} Not found!")
        print(result)
        flag = 0

        if len(result) == len(wordsearchs):
            inter = intersec(result, mykey)
            inter = list(map(int, inter))  # map ใช้คืนค่ากลุ่มข้อมูล
            print(f"Match in page {inter}")
            if(len(inter) != 0):
                flag = 1
                for i in inter:

                    geturl[i] = df['url'][i-1]
                    print(df['url'][i-1])

        if flag == 0:
            print("Not Match")
    totaltime = time.time()-start
    return geturl
