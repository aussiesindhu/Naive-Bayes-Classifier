import os
import sys
import re

spamcount = {}
spamfiles = []
hamfiles= []
hamcount = {}
vocabulary = set()
scounter =[]
hcounter = []
spam_probability ={}
ham_probability = {}

stop=['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'eachd', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

for dirName, subdirList, fileList in os.walk(sys.argv[1]):
    for fname in fileList:
        fullpath = os.path.join(dirName, fname)
        if ".DS_Store" not in fullpath and "__MACOSX" not in fullpath:
            f =open(fullpath, 'r', encoding="latin1")
            v = f.read().split()
            for i in v:
                vocabulary.add(i)
        if "spam" in fullpath and ".DS_Store" not in fullpath and "__MACOSX" not in fullpath:
            spamfiles.append(fullpath)
        else:
            if "ham" in fullpath and ".DS_Store" not in fullpath and "__MACOSX" not in fullpath:
                hamfiles.append(fullpath)

spamfiles_len =len(spamfiles)
hamfiles_len = len(hamfiles)

for s in spamfiles:
    file1 = open(s, 'r', encoding="latin1")
    list1 = file1.read().split()
    for l1 in list1 :
        l11=re.sub("[^a-zA-Z0-9]+", "", l1)
        if l11 not in stop:
            scounter.append(l11)
            if l11 not in spamcount:
                spamcount[l11] = 1
            else:
                spamcount[l11] += 1

for h in hamfiles:
    file2 = open(h, 'r', encoding="latin1")
    list2 = file2.read().split()
    for l2 in list2 :
        l22=re.sub("[^a-zA-Z0-9]+", "",l2)
        if l22 not in stop:
            hcounter.append(l22)
            if l22 not in hamcount:
                hamcount[l22] = 1
            else:
                hamcount[l22] += 1

with open('nbmodel.txt','w' , encoding="latin1") as d1:
    d1.write(str(len(vocabulary)) + "\n" +str(spamfiles_len) + "\n" + str(hamfiles_len) + "\n" +str(len(scounter)) + "\n" + str(len(hcounter)) + "\n")
    for key in spamcount.keys():
        d1.write("%s-%s " %(key , spamcount[key]))
    d1.write("\n")
    for key in hamcount.keys():
        d1.write("%s-%s " %(key , hamcount[key]))
    d1.write("\n")