# -----------------------------------
# Group 15
# JITSUPANG CHANGTHONG 58160060
# PRAEWNAPA PONGPAT 58160312
# KAISNBADEE WONGTHONGLUEA 58660001
# CHARANTORN VONGTHAI 58660044
# -----------------------------------
# Import Lib
import time
import csv
import io
import requests
import pandas 
import pandas as pd
from bs4 import BeautifulSoup
import unicodedata

from wordsegment import load, segment
import nltk 
from nltk.tokenize import RegexpTokenizer
load()
start_time = time.time()

DataSet = []
a = 0

URL = pandas.read_csv('test.csv')

for i in range(0,len(URL)):
# for i in range(0,1):
  a += 1
  print(a)
  print("--- %s seconds ---" % (time.time() - start_time))
  
  resp = requests.get(URL['url'][i])
  soup = BeautifulSoup(resp.content, 'html.parser')

  try:
    content = soup.find("body").get_text()
    # print(type(content))
    strtype = unicodedata.normalize('NFKD', content).encode('ascii','ignore')
    # print(strtype)
    LowerStr = strtype.lower()
    print(str(LowerStr))
    DataSetSegment = segment(str(LowerStr))
    print(DataSetSegment)

    SetDataSetSegment = DataSetSegment

    DataSet.append(DataSetSegment)
    # print(DataSet)

  except:
    print("Not Read File")

# print(type(DataSet))
print(DataSet)

with open("DataSetTest.csv", 'w', encoding='utf-8' ) as csvFile:
  writer = csv.writer(csvFile)
  writer.writerows(DataSet)

