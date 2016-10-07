import os
import math
import sys

result = {}
ham_or_spam=[]
spam_dict = {}
ham_dict ={}

for dirName, subdirList, fileList in os.walk(sys.argv[1]):
    for fname in fileList:
        fullpath = os.path.join(dirName, fname)
        if "txt" in fullpath and ".DS_Store" not in fullpath and "__MACOSX" not in fullpath:
            ham_or_spam.append(fullpath)

params= open('nbmodel.txt', 'r', encoding="latin1").read().split("\n")
vocabulary_cnt=params[0]
spam_len=params[1]
ham_len=params[2]
spam_wordcnt=params[3]
ham_wordcnt=params[4]

s=params[5].split()
for ss in s:
    s2=ss.split('-')
    spam_dict[s2[0]]=s2[1]

h=params[6].split()
for hh in h:
    h2=hh.split('-')
    ham_dict[h2[0]]=h2[1]

def calc_spam_probability(v):
    total=0
    temp_s={}
    for i in v:
        if i in temp_s:
            total+= temp_s.get(i)
        else:
            if i in spam_dict:
                s2=math.log((int(spam_dict.get(i))+ 1)/ (int(spam_wordcnt) + int(vocabulary_cnt)))
                temp_s[i]=s2
                total+= s2
            else:
                if i in ham_dict:
                    temp_s[i] = math.log(1 / (int(spam_wordcnt) + int(vocabulary_cnt)))
                    total +=temp_s[i]
    return total

def calc_ham_probability(v):
    total = 0
    temp_h={}
    for i in v:
        if i in temp_h:
            total+=temp_h.get(i)
        else :
            if i in ham_dict:
                s2 = math.log((int(ham_dict.get(i)) + 1) / (int(ham_wordcnt) + int(vocabulary_cnt)))
                temp_h[i] =s2
                total+= s2
            else:
                if i in spam_dict:
                    temp_h[i] = math.log(1 / (int(ham_wordcnt) + int(vocabulary_cnt)))
                    total+=temp_h[i]
    return total

d1=open('nboutput.txt', 'w', encoding="latin1")

ns1 = math.log(int(spam_len) / (int(spam_len) + int(ham_len)))
nh1 = math.log(int(ham_len) / (int(ham_len) + int(spam_len)))

for x in ham_or_spam:
    f = open(x, 'r', encoding="latin1")
    vocab = []
    v = f.read().split()
    for i in v:
        vocab.append(i)
    ns2=calc_spam_probability(vocab)
    prob_spam =ns1 + ns2
    # print(prob_spam)
    nh2 = calc_ham_probability(vocab)
    prob_ham = nh1 + nh2
    if prob_spam > prob_ham:
        d1.write("SPAM" +" "+ str(x) +"\n")
    else:
        if prob_ham > prob_spam:
            d1.write("HAM" +" "+str(x) + "\n")