class Pembalap:
    def __init__(self, nama, lap_times):
        self.nama = nama
        self.lap_times = lap_times
nama = {
    "nama pembalap": nama,
    "waktu lap": waktu
}

def total_waktu(lap_times, i=0):
    if i == len(lap_times):
        return 0
    return lap_times[i] + total_waktu(lap_times, i + 1)


def fastest_lap(data):
    fastest = float('inf')
    for p in data:
        for t in p.lap_times:
            if t < fastest:
                fastest = t
    return fastest


def cetak(data):
    print(f"Fastest Lap Keseluruhan: {fastest_lap(data):.2f}")
    for p in data:
        print(f"{p.nama} - Total Waktu: {total_waktu(p.lap_times):.2f}")


# MAIN
n, m = map(int, input().split())
data = []

for _ in range(n):
    inp = input().split()
    data.append(Pembalap(inp[0], list(map(float, inp[1:]))))

cetak(data)