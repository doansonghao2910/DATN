import math
fDictionnary = './dictionnaries.txt'

#Đọc file dictionnaries với encoding utf-8
with open(fDictionnary, 'r', encoding="utf-8") as fwd:
    dic = fwd.readlines()
    
Dicttm = {}
Dict = {}
for i in dic:
    s = i.split()
    u1 = s[0].strip()
    u2 = s[1].strip()
    Dict[u2] = u1
    Dicttm[u1] = u2

def tao_do_thi_tu_tap_tin():
    f = open('danhsachcanh.txt')
    so_dinh = int(f.readline().strip())
    cac_canh = f.readlines()
    f.close()


    dt = [[0 for _ in range(so_dinh)] for _ in range(so_dinh)]
    
    for canh in cac_canh:
        canh = canh.strip()
        ds_gia_tri = canh.split()
        if len(ds_gia_tri) != 3:
            continue
        dong = int(ds_gia_tri[0])
        cot = int(ds_gia_tri[1])
        khoang_cach = float(ds_gia_tri[2])
        dt[dong][cot] = khoang_cach
        dt[cot][dong] = khoang_cach
    #End for
    return dt
#End def

def duong_di(ds_dinh_truoc, dinh_dich):
    ds = [dinh_dich]
    dinh = dinh_dich
    while True:
        dinh = ds_dinh_truoc[dinh]
        if dinh == None:
            break
        #End if
        ds.insert(0, dinh)
    #End while
    ds = [Dict[str(x)] for x in ds]
    return '->'.join(ds)
#End def



def khoang_cach_ngan_nhat(ds_khoang_cach, ds_dinh_cay_ngan_nhat):
    nho_nhat = math.inf
    dinh_nho_nhat = math.inf
    for dinh in range(len(ds_khoang_cach)):
        if ds_dinh_cay_ngan_nhat[dinh] == False and ds_khoang_cach[dinh] < nho_nhat:
            nho_nhat = ds_khoang_cach[dinh]
            dinh_nho_nhat = dinh
        # End if
    # End for
    return dinh_nho_nhat
# End def

def dijkstra(do_thi, dinh_nguon):
    so_luong_dinh = len(do_thi)
    ds_khoang_cach = [math.inf for _ in range(so_luong_dinh)]
    ds_khoang_cach[dinh_nguon] = 0

    ds_dinh_truoc = [None for _ in range(so_luong_dinh)]
    ds_dinh_cay_ngan_nhat = [False for _ in range(so_luong_dinh)]

    for i in range(so_luong_dinh):
        x = khoang_cach_ngan_nhat(ds_khoang_cach, ds_dinh_cay_ngan_nhat)
        ds_dinh_cay_ngan_nhat[x] = True
        for y in range(so_luong_dinh):
            if ds_dinh_cay_ngan_nhat[y] == False and do_thi[x][y] > 0 and ds_khoang_cach[y] > ds_khoang_cach[x] + do_thi[x][y]:
                    ds_khoang_cach[y] = ds_khoang_cach[x] + do_thi[x][y]
                    ds_dinh_truoc[y] = x
            #End if
        #End for
    #End for
    for dinh_dich in range(so_luong_dinh):
        noi_dung = Dict[str(dinh_dich)] + " : "
        noi_dung += duong_di(ds_dinh_truoc, dinh_dich) + " : "
        noi_dung += str(ds_khoang_cach[dinh_dich])
        print(noi_dung)
    #End for
#End def

def main():
    do_thi = tao_do_thi_tu_tap_tin()
    dinh_nguon = int(Dicttm[input('Nhập vào một từ: ')])
    if dinh_nguon in range(len(do_thi)):
        dijkstra(do_thi, dinh_nguon)
    else:
        print('Nhập sai từ!')

if __name__ == '__main__':
    main()




