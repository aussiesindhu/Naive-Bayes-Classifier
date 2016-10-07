spam_label = 0
spam_cnt = 0
spam_file_cnt=0
ham_file_cnt=0
ham_label = 0
ham_cnt = 0
global precision_ham
global precision_spam
global recall_ham
global recall_spam
g = open('nboutput.txt', 'r')
lines = g.readlines()

for line in lines:
    line = line.split(" ")
    if line[0] == "SPAM" and "spam.txt" in line[1]:
        spam_label = spam_label + 1
    if line[0] == "SPAM":
        spam_cnt = spam_cnt + 1
    if "spam.txt" in line[1]:
        spam_file_cnt+=1
    if line[0] == "HAM" and "ham.txt" in line[1]:
        ham_label = ham_label + 1
    if line[0] == "HAM":
        ham_cnt = ham_cnt + 1
    if "ham.txt" in line[1]:
        ham_file_cnt+=1
print(spam_file_cnt)
g.close()
if spam_cnt!=0:
    precision_spam = (spam_label / spam_cnt)
    print(precision_spam, " Precision SPAM")
if ham_cnt!=0:
    precision_ham = (ham_label / ham_cnt)
    print(precision_ham, " Precision HAM")
if spam_file_cnt!=0:
    recall_spam = (spam_label / spam_file_cnt)
    print(recall_spam, "Recall SPAM")
if ham_file_cnt!=0:
    recall_ham = (ham_label / ham_file_cnt)
    print(recall_ham, "Recall HAM")


F_SPAM = ((2 * precision_spam * recall_spam) / (precision_spam + recall_spam))
F_HAM = ((2 * precision_ham * recall_ham) / (precision_ham + recall_ham))

print(F_SPAM, "F1 SPAM")
print(F_HAM, "F1 HAM")

weightedAvg = ((spam_file_cnt * F_SPAM) + (ham_file_cnt*F_HAM))/ (ham_file_cnt + spam_file_cnt)
print(weightedAvg,"Weighted average" )
