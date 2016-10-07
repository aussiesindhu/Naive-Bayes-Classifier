import os
import sys

spamcount = {}
spamfiles = []
hamfiles= []
hamcount = {}
vocabulary = set()
scounter =[]
hcounter = []
spam_probability ={}
ham_probability = {}

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
        scounter.append(l1)
        if l1 not in spamcount:
            spamcount[l1] = 1
        else:
            spamcount[l1] += 1

for h in hamfiles:
    file2 = open(h, 'r', encoding="latin1")
    list2 = file2.read().split()
    for l2 in list2 :
        hcounter.append(l2)
        if l2 not in hamcount:
            hamcount[l2] = 1
        else:
            hamcount[l2] += 1

with open('nbmodel.txt','w' , encoding="latin1") as d1:
    d1.write(str(len(vocabulary)) + "\n" +str(spamfiles_len) + "\n" + str(hamfiles_len) + "\n" +str(len(scounter)) + "\n" + str(len(hcounter)) + "\n")
    for key in spamcount.keys():
        d1.write("%s-%s " %(key , spamcount[key]))
    d1.write("\n")
    for key in hamcount.keys():
        d1.write("%s-%s " %(key , hamcount[key]))
    d1.write("\n")