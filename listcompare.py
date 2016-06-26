import os
import re

def getCurrentLevel(scores, score):
    list = []
    for key in scores:
        if scores[key] == score:
            list.append(key)
    return list

def expandHistory(history):
    for i in history:
        ifirst,isecond = i.split("&")
        for j in history:
            jfirst,jsecond = j.split("&")
            newentry = "%s&%s"%(ifirst,jsecond)
            if isecond == jfirst and newentry not in history:
                history.append(newentry)
    return history
    
history = []

filename = raw_input('Enter file path: ') 
print(filename)
names = []
scores = {}
finalscores = {}
if os.path.exists(filename):
    file_contents = open(filename)
    file_contents = file_contents.readlines()
    for line in file_contents:
        line = re.sub("\n", "", line)
        names.append(line)
        print(line)
    numberofitems = len(names)
    numberlist = [numberofitems] * numberofitems
    scoresTuples = zip(names, numberlist)
    #print(scoresTuples)
    scores = dict(scoresTuples)
    #print(scores)
    
        
    for score in range(numberofitems, 0, -1):
        #print(score)
        currentlevel = getCurrentLevel(scores, score)
        while len(currentlevel) is not 1:
            #print(score, currentlevel)
            first = ""
            second = ""
            for i in currentlevel:
                if first == "":
                    first = i
                elif second == "":
                    second = i
                    if "%s&%s"%(first,second) in history:
                        scores[first] = score-1
                    elif "%s&%s"%(second,first) in history:
                        scores[second] = score-1
                    else:
                        choice = raw_input("1.%s or 2.%s? "%(first, second))
                        if choice == "1":
                            scores[first] = score-1
                            history.append("%s&%s"%(first,second))
                        elif choice == "2":
                            scores[second] = score-1
                            history.append("%s&%s"%(second,first))
                        #print (history, first, second)
                    first = ""
                    second = ""
            currentlevel = getCurrentLevel(scores, score)
        finalscores[score] = currentlevel[0]
        #print("%s\n" % history)
        history = expandHistory(history)
        #print("%s\n" % history)
    print(scores)
    for key in finalscores:
        print("%d: %s"%(key,finalscores[key]))
else:
    print("%s does not exist" % filename)

os.system("pause")