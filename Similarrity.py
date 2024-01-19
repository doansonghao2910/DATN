import io
import numpy as np
from scipy import spatial

fSimlex = './OutPutVisim-401.txt'
fWord2vec = './W2V_150.txt'

# Đọc file Simlex với encoding utf-8
with open(fSimlex, 'r', encoding='utf-8') as f:
    vsl = f.readlines()

# Load model Word2Vec
with open(fWord2vec, 'r', encoding='utf-8') as f:
    model = {}
    for line in f:
        tem = line.split()
        word = tem[0].strip()
        vec = np.array([float(val) for val in tem[1:]])
        model[word] = vec

rs = []
v = []

for i in vsl:
    s = i.split()
    u1 = s[0].strip()
    u2 = s[1].strip()

    # Kiểm tra xem từ u1 và u2 có trong model không
    if u1 not in model or u2 not in model:
        continue

    v1 = model[u1]
    v2 = model[u2]

    # Kiểm tra chiều dài của vector
    if len(v1) != len(v2):
        print("Lỗi vector không cùng chiều\n")
        continue

    # Kiểm tra xem giá trị thứ ba có thể chuyển đổi thành float không
    #if not s[3].strip().replace(".", "", 1).isdigit():  # Kiểm tra nếu không phải là số
    #    print(f"Lỗi: Giá trị không phải là số - {s[3].strip()}\n")
    #    continue

    # Tính cosine similarity
    k = ((2 - spatial.distance.cosine(v1, v2)) / 2) * 10

#    v.append(float(s[3].strip()))
    print(f"{u1} - {u2} = {10 - k}\n")
#    rs.append(k)

# Tính correlation coefficient và correlate
#if rs and v:  # Kiểm tra nếu có ít nhất một phần tử trong cả hai mảng
#    print(np.corrcoef(rs, v))
#    print(np.correlate(rs, v))
#else:
#    print("Không có dữ liệu để tính toán correlation.")
