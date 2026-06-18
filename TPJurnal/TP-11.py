n = int(input())

suhu = list(map(float, input().split()))

# fungsi buat nyari max
def carimax(n):
    maks = suhu[0]
    k = 1
    # ganti nilai maks jika nilai maks < dari nilai suhu indeks ke k
    while k < n:
        if maks < suhu[k]:
            maks = suhu[k]
        k = k + 1
    return maks

# fungsi buat nyari min
def carimin(n):
    mini = suhu[0]
    k = 1
    # ganti nilai mini jika nilai mini > dari nilai suhu indeks ke k
    while k < n:
        if mini > suhu[k]:
            mini = suhu[k]
        k = k + 1
    return mini

# hasil1 = max(suhu)

mini = carimin(n)
maks = carimax(n)

# nyari selisih dengan cara maks - mini
selisih = maks - mini

# print outputnya dengan tepat 2 angka dibelakang koma dengan pake .2f
print(f"{maks:.2f} {mini:.2f} {selisih:.2f}")
# print(f"{hasil1:.2f}")