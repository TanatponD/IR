###--  binarysearchtreee --- ####
import json
from nltk.tokenize import RegexpTokenizer
import pandas as pd

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with the given key


def insert(root, node):
    if root is None:
        # +=1
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                # +=1
                root.right = node
            else:
                # +=1
                insert(root.right, node)
        else:
            if root.left is None:
                # +=1
                root.left = node
            else:
                # +=1
                insert(root.left, node)


# A utility function to do inorder tree traversal
def inorder(root):
    global l
    global wf
    if root:
        global textinput
        inorder(root.left)
        if root.val[0] == wf:
            l.append(root.val)
        inorder(root.right)


def chdic(data, word):
    arr = []
    for i, v in data.items():
        # +=1
        if i == word:
            arr.append(i), arr.append(set(v))
    return arr


def result(words):

    df = pd.read_csv('test.csv')
    word = search(words)
    f = open('Positional.json')
    mykey = json.load(f, parse_int=int)
    f.close()
    global c
    c = 0
    lendic = len(mykey)
    mid = lendic//2
    setmid = ""
    for i, w in enumerate(mykey):
        #  +=1
        if i == mid:
            datanode = chdic(mykey, w)
            setmid = w
    r = Node(datanode)
    for i, w in mykey.items():
        # +=1
        array = chdic(mykey, i)
        insert(r, Node(array))

    global l
    l = []
    l1 = []
    for i in word:
        
        # +=1
        global wf
        wf = i
        inorder(r)
    if len(l) == 0:
        l1.append("Not Found!")
    else:
        for j in l:
            # +=1
            for k in j[1]:
                # +=1
                l1.append(df['url'][int(k)-1])
    return set(l1)


def search(wordsearchs):
    tokenizer = RegexpTokenizer(r'\w+')
    wordsearch = wordsearchs
    wordsearch = wordsearch.lower()
    wordtoken = tokenizer.tokenize(wordsearch)
    return wordtoken
