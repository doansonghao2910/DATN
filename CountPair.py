import io
import numpy as np
from scipy import spatial

fSimlex = './Visim-400.txt'
fAnto = './vi_antonyms.txt'
fSyno = './vi_synonyms.txt'
#fWord2vec = './W2V_150.txt'

# Đọc file Simlex với encoding utf-8
with open(fSimlex, 'r', encoding='utf-8') as fr:
    vsl = fr.readlines()
# Đọc file Anto với encoding utf-8
with open(fAnto, 'r', encoding='utf-8') as fr:
    anto = fr.readlines()
# Đọc file Syno với encoding utf-8
with open(fSyno, 'r', encoding='utf-8') as fr:
    syno = fr.readlines()
listwords = []
for i in vsl:
    s = i.split()
    u1 = s[0].strip()
    u2 = s[1].strip()
    listwords.append(u1)
    listwords.append(u2)
for i in anto:
    s = i.split()
    u1 = s[0].strip()
    u2 = s[1].strip()
    listwords.append(u1)
    listwords.append(u2)
for i in syno:
    s = i.split()
    u1 = s[0].strip()
    u2 = s[1].strip()
    listwords.append(u1)
    listwords.append(u2)
mysetwords = set(listwords)

#Ghi file
with open('dictionnaries.txt', 'w', encoding='utf-8') as fwd:
    i = -1
    for word in mysetwords:
        i +=1
        fwd.write(f"{word} {i}\n")
#Ghi file
listwords = list(mysetwords)
with open('OutPutVisim-400.txt', 'w', encoding='utf-8') as fw:
    for i in range(len(mysetwords) - 1):
        for j in range(i+1, len(mysetwords)):
            fw.write(f"{listwords[i]}  {listwords[j]}\n")

            


