class Tim:
    def __init__(self, nama, skor):
        self.nama = nama
        self.skor = skor


def rata_global(data):
    total = 0
    count = 0
    for t in data:
        for s in t.skor:
            total += s
            count += 1
    return total / count


def best_score(skor, i=0):
    if i == len(skor) - 1:
        return skor[i]
    return max(skor[i], best_score(skor, i + 1))


def cetak(data):
    print(f"Rata-rata Global: {rata_global(data):.2f}")
    for t in data:
        print(f"{t.nama} - Best Score: {best_score(t.skor):.2f}")


# MAIN
n, m = map(int, input().split())
data = []

for _ in range(n):
    inp = input().split()
    data.append(Tim(inp[0], list(map(float, inp[1:]))))

cetak(data)