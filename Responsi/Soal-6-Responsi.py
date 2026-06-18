armada = []
tertinggi = 0
nmax = 50

class truk :
    def __init__(self,plat_nomor,riwayat_BBM_harian):
        self.riwayat_BBM_harian = riwayat_BBM_harian
        self.plat_nomor = plat_nomor
        
def konsumsi_terendah(armada,data_boros) : 
    terendah = data_boros
    for i in range(len(armada)) : 
        for j in range(len(armada[i].riwayat_BBM_harian)) :
            if armada[i].riwayat_BBM_harian[j] > terendah : 
                terendah = armada[i].riwayat_BBM_terendah[j]
    return terendah

# # 1
# def rekursif_boros (armada,index_truk= 0,index_BBM = 0) : 
#     global tertinggi
#     if index_truk == len(armada) and len(armada[index_truk].riwayat_BBM_harian) == index_BBM : 
#         return tertinggi
    
#     if index_BBM < len(armada[index_truk].riwayat_BBM_harian) : 
#         return rekursif_boros(armada,index_truk, index_BBM+1)
    
#     if index_truk < len(armada) : 
#         return rekursif_boros(armada,index_truk + 1)
    
# 2
def rekursif_boros(armada, index_truk=0, index_BBM=0):
    global tertinggi

    if index_truk == len(armada):
        return tertinggi

    if index_BBM == len(armada[index_truk].riwayat_BBM_harian):
        return rekursif_boros(armada, index_truk + 1, 0)

    if armada[index_truk].riwayat_BBM_harian[index_BBM] > tertinggi:
        tertinggi = armada[index_truk].riwayat_BBM_harian[index_BBM]

    return rekursif_boros(armada, index_truk, index_BBM + 1)


def main() : 
    
    #baris 1
    jumlah_truk = int(input("masukkan jumlah truk : "))
    jumlah_hari = int(input("masukkan jumlah hari : "))
    data_boros = int(input("data boros : "))
    
    for i in range(jumlah_truk) : 
        plat_nomor = str(input("masukkan plat nomor anda : "))
        bbm = []
        for i in range(jumlah_hari) : 
            bbm_perhari = float(input("masukkan BBM : "))
            bbm.append(bbm_perhari)
            
        armada.append(truk(plat_nomor,bbm))

    print(round(konsumsi_terendah(armada,data_boros)),2)
    
if __name__ == "__main__":
    main()