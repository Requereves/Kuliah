class User:
    def __init__(self, nama, durasi):
        self.nama = nama
        self.durasi = durasi


def total_server(data):
    total = 0
    for u in data:
        total += sum(u.durasi)
    return total


def cari_hari(durasi, target, i=0):
    if i == len(durasi):
        return -1
    if durasi[i] > target:
        return i + 1
    return cari_hari(durasi, target, i + 1)


def cetak(data, target):
    print(f"Total Durasi Server: {total_server(data):.2f}")
    for u in data:
        hari = cari_hari(u.durasi, target)
        if hari == -1:
            print(f"{u.nama} belum mencapai target durasi")
        else:
            print(f"{u.nama} menembus target pertama kali pada hari ke-{hari}")


# MAIN
n, m, k = input().split()
n, m = int(n), int(m)
k = float(k)

data = []
for _ in range(n):
    inp = input().split()
    data.append(User(inp[0], list(map(float, inp[1:]))))

cetak(data, k)