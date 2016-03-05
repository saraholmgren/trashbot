import random
import json
from re import sub
from random import randint,choice

try:
    RWFile = open("RecentWords.json","r+")
    WAFile = open("WordAssociations.json","r+")
    SWFile = open("StartingWords.json","r+")
    print("read")
    Recents = json.loads(RWFile.read())
    Associations = json.loads(WAFile.read())
    Starters = json.loads(SWFile.read())
except:
    print("Failed to load files")
    Recents = []
    Associations = {}
    Starters = []

#Add words to the list of recently used words, as well as add associations.
def read(WordString):
    print("Reading words...")
    global Recents
    global Associations

    sub('[^\.\w]', '', WordString)
    Words = WordString.lower().split(" ")
    for I in range(0,len(Words)-1):
        W = Words[I]
        if W != '':
            Recents.append(W)
            T = list(W)

            if not (W in Associations):
                Associations[W] = []

            if W[-1] != ".":
                Associations[W].append(Words[I+1])

            #Recents.append(removeperiod(W))
            try:
               if I == 0:
                   Starters.append(W)
               elif Words[I-1][-1] == ".":
                   Starters.append(W)
            except:
                print("hurr")
    print(Associations)
    print(Starters)
    trim()
    
def trim():
    global Associations
    global Recents
    try:
        while Recents[5000]:
            Recents.pop(0)
    except:
        pass
    for A in Associations:
        try:
            while Associations[A][175]:
                Associations[A].pop(0)
        except:
            pass
    try:
        while Starters[100]:
            Starters.pop(0)
    except:
        pass
    
##def removeperiod(word):
##    T = list(word)
##    for x in T:
##        if x == ".":
##            T.pop(T.index(x))
##    s = []
##    for x in T:
##        s += x
##    return s

def writesentence(word):
    word = word.lower()
    writing = []
    #if word in Starters:
    try:
        writing.append(word)
    except BaseException as e:
        print(e)
    wtw = randint(3,40)
    for I in range(0,wtw):
        try:
            newword = choice(Associations[writing[I]])
            writing.append(newword)
            print(I)
        except IndexError as e:
            print(e)
        except KeyError as e:
            print(e)
    written = ""
    for x in writing:
        print(x)
        written +=(str(x)+" ")
    return written

def save():
    try:
        global RWFile
        global WAFile
        global SWFile
        RWFile.truncate()
        WAFile.truncate()
        SWFile.truncate()
        #Recents = json.loads(RWFile)
        #Associations = json.loads(WAFile)
        #Starters = json.loads(SWFile)
        #RWFile = open("RecentWords.json","r+")
        #WAFile = open("WordAssociations.json","r+")
        #SWFile = open("StartingWords.json","r+")
        RWFile.write(json.dumps(Recents))
        WAFile.write(json.dumps(Associations))
        SWFile.write(json.dumps(Starters))
    except BaseException as e:
        print(e)

def randomthought():
    try:
        return writesentence(choice(Starters))
    except BaseException as e:
        return "An error has occured. Please notify sasshunter.tumblr.com, referencing randomthought() "+str(e)
    
