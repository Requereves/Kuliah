def volume(a):
    hasil = 3.14 * (r ** 2) * a
    return hasil

def massa(b, a):
    return b * volume(a) 


# r = int(input("Masukkan jari2"))
r = int(input("Masukkan jari2: "))
p1, h1 = map(int, input().split())
p2, h2 = map(int, input().split())
# kali = r ** 2

# if massa() == massa(p2):
#     print(massa(p1))

hasil = massa(p1, h1) - massa(p2, h2)
print(hasil)
# print(massa(p1, h1))
# print(massa(p2, h2))


# print(massa())
