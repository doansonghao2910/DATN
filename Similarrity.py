import io
import numpy as np
from scipy import spatial

fOvisim = './OutPutVisim-400.txt'
fWord2vec = './W2V_150.txt'
fDictionnary = './dictionnaries.txt'
fAnto = './vi_antonyms.txt'
fSyno = './vi_synonyms.txt'

# Đọc file Anto với encoding utf-8
with open(fAnto, 'r', encoding="utf-8") as fr:
    anto = fr.readlines()
# Đọc file Syno với encoding utf-8
with open(fSyno, 'r', encoding='utf-8') as fr:
    syno = fr.readlines()

# Đọc file Simlex với encoding utf-8
with open(fOvisim, 'r', encoding="utf-8") as f:
    vsl = f.readlines()

# Đọc file dictionnaries với encoding utf-8
with open(fDictionnary, 'r', encoding="utf-8") as fwd:
    dic = fwd.readlines()

# Load model Word2Vec
with open(fWord2vec, 'r', encoding="utf-8") as f:
    model = {}
    for line in f:
        tem = line.split()
        word = tem[0].strip()
        vec = np.array([float(val) for val in tem[1:]])
        model[word] = vec

dictWordsAt = {}
dictWordsSn = {}
for i in anto:
    s = i.split()
    w = s[0].strip() + " " + s[1].strip()
    r = s[1].strip() + " " + s[0].strip()
    dictWordsAt[w] = 10
    dictWordsAt[r] = 10

for i in syno:
    s = i.split()
    w = s[0].strip() + " " + s[1].strip()
    r = s[1].strip() + " " + s[0].strip()
    dictWordsSn[w] = 1
    dictWordsSn[r] = 1


# Lấy số lượng đỉnh  
Dict = {}
for i in dic:
    s = i.split()
    u1 = s[0].strip()
    u2 = s[1].strip()
    Dict[u1] = u2
for x,y in Dict.items():
    print(x, y)
# rs = []
v = []

antonyms = "antonyms"
synonyms = "synonyms"
with open('danhsachcanh.txt', 'w', encoding='utf-8') as fw:
    fw.write(f"{len(Dict)}\n")
    for i in vsl:
        kt = 0
        s = i.split()
        u1 = s[0].strip()
        u2 = s[1].strip()
        w = u1 + " " + u2
        try:
            valueAt = dictWordsAt[w]
            fw.write(f"{Dict[u1]}  {Dict[u2]} {antonyms} \n")
        except KeyError:
            kt = 1
        if(kt == 1):
            try:
                valueSy = dictWordsSn[w]
                fw.write(f"{Dict[u1]}  {Dict[u2]} {synonyms} \n")
            except KeyError:
                if u1 not in model or u2 not in model:
                    fw.write(f"{Dict[u1]} {Dict[u2]} {10}\n")
                else:
                    
                    v1 = model[u1]
                    v2 = model[u2]
                    if len(v1) != len(v2):
                        fw.write(f"{Dict[u1]} {Dict[u2]} {10}\n")
                    else:
                        k = ((2 - spatial.distance.cosine(v1, v2)) / 2) * 10
                        fw.write(f"{Dict[u1]} {Dict[u2]} {10 - k}\n")


        #Kiểm tra xem từ u1 và u2 có trong model không
        # if u1 not in model or u2 not in model:
        #     continue

        # v1 = model[u1]
        # v2 = model[u2]

        # #Kiểm tra chiều dài của vector
        # if len(v1) != len(v2):
        #     print("Lỗi vector không cùng chiều\n")
        #     continue

        #Kiểm tra xem giá trị thứ ba có thể chuyển đổi thành float không
        # if not s[3].strip().replace(".", "", 1).isdigit():  # Kiểm tra nếu không phải là số
        #    print(f"Lỗi: Giá trị không phải là số - {s[3].strip()}\n")
        #    continue

        #Tính cosine similarity
        # k = ((2 - spatial.distance.cosine(v1, v2)) / 2) * 10

        # fw.write(f"{Dict[u1]} {Dict[u2]} {10 - k}\n")


#    v.append(float(s[3].strip()))
#    print(f"{u1} - {u2} = {10 - k}\n")
#    rs.append(k)

# Tính correlation coefficient và correlate
#if rs and v:  # Kiểm tra nếu có ít nhất một phần tử trong cả hai mảng
#    print(np.corrcoef(rs, v))
#    print(np.correlate(rs, v))
#else:
#    print("Không có dữ liệu để tính toán correlation.")
