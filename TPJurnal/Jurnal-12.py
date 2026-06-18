# n = int(input())

# data_tim = []

# # buat masukkin datanya 
# for i in range(n):
#     nama, akurasi, waktu = input().split()

#     tim = {
#         "nama": nama,
#         "akurasi": float(akurasi),
#         "waktu": int(waktu)
#     }

#     data_tim.append(tim)

# # insertion sort buat ganti dari yang paling tinggi ke paling rendah
# for i in range(1, n):

#     key = data_tim[i]
#     j = i - 1

#     while j >= 0 and (
#         data_tim[j]["akurasi"] < key["akurasi"] or (data_tim[j]["akurasi"] == key["akurasi"] and data_tim[j]["waktu"] > key["waktu"])):

#         data_tim[j + 1] = data_tim[j]
#         j -= 1
#     data_tim[j + 1] = key

# # buat hasilnya
# for tim in data_tim:
#     print("")
#     print(tim["nama"],"{:.2f}".format(tim["akurasi"]),tim["waktu"])


# Soal 2

## Kode Program


n = int(input())

data_wilayah = []

# BUAT MASUKKIN DATANYA KE ARRAY
for i in range(n):
    nama, risiko, penduduk = input().split()

    wilayah = {
        "nama": nama,
        "risiko": int(risiko),
        "penduduk": int(penduduk)
    }

    data_wilayah.append(wilayah)

# Selection Sort buat ngurutin dari paling tinggi ke paling rendah
for i in range(n - 1):
    maks = i

    for j in range(i + 1, n):

        if data_wilayah[j]["risiko"] > data_wilayah[maks]["risiko"]:
            maks = j

        elif (data_wilayah[j]["risiko"] == data_wilayah[maks]["risiko"]):

            if (data_wilayah[j]["penduduk"] > data_wilayah[maks]["penduduk"]):
                maks = j

            elif (data_wilayah[j]["penduduk"] == data_wilayah[maks]["penduduk"]):

                if (data_wilayah[j]["nama"] < data_wilayah[maks]["nama"]):

                    maks = j

    temp = data_wilayah[i]
    data_wilayah[i] = data_wilayah[maks]
    data_wilayah[maks] = temp

# Output
for wilayah in data_wilayah:
    print("")
    print(wilayah["nama"],wilayah["risiko"], wilayah["penduduk"])
