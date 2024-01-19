import io
import numpy as np
from scipy import spatial

fSimlex = './Visim-401.txt'
#fWord2vec = './W2V_150.txt'


# Đọc file Simlex với encoding utf-8
with open(fSimlex, 'r', encoding='utf-8') as fr:
    vsl = fr.readlines()

danhsachcap = []

for i in vsl:
    s = i.split()
    u1 = s[0].strip()
    u2 = s[1].strip()
    danhsachcap.append(u1)
    danhsachcap.append(u2)

# Ghi file
with open('OutPutVisim-401.txt', 'w', encoding='utf-8') as fw:
    for i in range(len(danhsachcap) - 1):
        for j in range(i+1, len(danhsachcap)):
            fw.write(f"{danhsachcap[i]}  {danhsachcap[j]}\n")


