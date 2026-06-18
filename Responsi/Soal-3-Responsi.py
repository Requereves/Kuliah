# Simpen data dalam bentuk terstruktur
class datasaham:
    def __init__(self, kode, harga):
        # buat kode saham nya
        self.kode = kode
        # buat harga sahamnya, disimpen dalam bentuk array dalm dictionary
        self.harga = harga
    
# buat cek harga tertinggi pake for, pake for buat ngecek semua datanya di list
def tertinggi(saham):
    tharga = 0
    # manggil data saham mulai dari perulangan J[i] 
    for j in saham:
        # manggil data harga saham dalam sesuai J[i] 
        for k in j.harga:
            # jika k lebih dari tharga maka data tharga diganti ke pake k
            if k > tharga:
                tharga = k
    return tharga

# Buat bandingin harga sama harga dari tiap hari jika disimpanny dalma bentuk array / list
def bullish(harga, g = 1):
    # jika g sama dengan panjang harga
    if g == len(harga):
        return True
    # jika harga
    if harga[g] < harga[g - 1]:
        return False
    
    return bullish(harga, g + 1)

# buat nyetak data sahamnya atau hasil analisisnya
def cetak(saham):
    print(f"All-Time High Keseluruhan: {tertinggi(saham)}")
    for s in saham:
        status = "BULLISH" if bullish(s.harga) else "NON-BULLISH"
        print(f"{s.kode} - Tren: {status}")

# inputan user buat datanya
n = int(input(""))
m = int(input(""))

# ini nanti bentuknya {
# bca [100, 200, 300]
# bni [300, 400, 500]
# } disimpen dalam bentuk dictionary

saham = []

# buat perulangan masukkin datanya sesuai jumlah n
for i in range(n):
    masukkan = int(input(""))
    saham.append(datasaham(masukkan[0], list(map(float, masukkan[1:]))))

cetak(saham)