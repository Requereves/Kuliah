class Pabrik:
    def __init__(self, nama, emisi):
        self.nama = nama
        self.emisi = emisi


# fungsi rekursif untuk jumlah total emisi
def total_emisi(data, i=0):
    if i == len(data):
        return 0
    return data[i] + total_emisi(data, i + 1)


# fungsi rata-rata kawasan
def rata_kawasan(data):
    total = 0
    jumlah = 0

    for p in data:
        for e in p.emisi:
            total += e
            jumlah += 1

    return total / jumlah


# ================= INPUT =================
# input pertama:
# n = jumlah pabrik
# h = jumlah hari
#
# contoh:
# 2 3
#
# artinya:
# ada 2 pabrik
# data tiap pabrik berisi 3 hari

n, h = map(int, input().split())

pabrik = []

# input data pabrik sebanyak n kali
for i in range(n):

    # format input:
    # NamaPabrik data1 data2 data3 ...
    #
    # karena h = 3
    # maka harus ada 3 data emisi
    #
    # contoh:
    # A 10 20 30

    x = input().split()

    nama = x[0]

    # ambil data emisi mulai index ke-1
    emisi = list(map(float, x[1:]))

    pabrik.append(Pabrik(nama, emisi))


# ================= OUTPUT =================

print(f"Rata-rata Emisi Kawasan: {rata_kawasan(pabrik):.2f}")

for p in pabrik:
    print(f"{p.nama} - Total Emisi: {total_emisi(p.emisi):.2f}")