class Petani:
    def __init__(self, nama, panen):
        self.nama = nama
        self.panen = panen

def total_semua(data):
    total = 0
    count = 0
    for p in data:
        for x in p.panen:
            total += x
            count += 1
    return total / count


def hitung_target(panen, target, i=0):
    if i == len(panen):
        return 0
    if panen[i] > target:
        return 1 + hitung_target(panen, target, i + 1)
    return hitung_target(panen, target, i + 1)


def cetak(data, target):
    print(f"Rata-rata Panen Desa: {total_semua(data):.2f}")
    for p in data:
        print(f"{p.nama} tembus target sebanyak {hitung_target(p.panen, target)} hari")


# MAIN
n, m, t = input().split()
n, m = int(n), int(m)
t = float(t)

data = []
for _ in range(n):
    inp = input().split()
    data.append(Petani(inp[0], list(map(float, inp[1:]))))

cetak(data, t)