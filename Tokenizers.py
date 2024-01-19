from collections import Counter
import re
def dem(doanvan):
    danhsachtu = re.findall(r'\b\w+\b', doanvan.lower())
    tansuattu = Counter(danhsachtu)
    return tansuattu

doanvan = "Đoạn văn bản ví dụ để kiểm tra đếm tần suất từ. Đoạn văn này có một số từ xuất hiện nhiều lần."
ketqua = dem(doanvan)
for tu, tansuat in ketqua.items():
    print(f'{tu}: {tansuat} lần')
