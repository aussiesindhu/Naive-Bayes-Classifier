import os
import math
import sys
import re

result = {}
ham_or_spam=[]
spam_dict = {}
ham_dict ={}

stop=['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'eachd', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

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

for x in ham_or_spam:
    f = open(x, 'r', encoding="latin1")
    vocab = []
    v = f.read().split()
    for i in v:
        ri=re.sub("[^a-zA-Z0-9]","",i)
        if ri not in stop:
            vocab.append(ri)
    ns1= math.log(int(spam_len) / (int(spam_len) + int(ham_len)))
    ns2=calc_spam_probability(vocab)
    prob_spam =ns1 + ns2
    nh1= math.log(int(ham_len) / (int(ham_len) + int(spam_len)))
    nh2 = calc_ham_probability(vocab)
    prob_ham = nh1 + nh2
    if prob_spam > prob_ham:
        d1.write("SPAM" +" "+ str(x) +"\n")
    else:
        if prob_ham > prob_spam:
            d1.write("HAM" +" "+str(x) + "\n")
