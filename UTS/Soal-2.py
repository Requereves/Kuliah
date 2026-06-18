def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil = hasil * i
    return hasil

def permutasiP(a, b):
    return faktorial(a) // faktorial(a-b)

def permutasiC(a, b):
    return faktorial(a) //(faktorial(b) * faktorial(a - b) ) 

x, y, x1, y1 = map(int, input().split())

fx = faktorial(x)
fy = faktorial(y)
fx1 = faktorial(x1)
fy1 = faktorial(y1)

# BUAT P
if x >= y:
    p = permutasiP(x, y)
else:
    p = permutasiP(y, x)

if x >= y:
    p = permutasiC(x, y)
else:
    p = permutasiC(y, x)

# buat C
if x1 >= y1:
    p = permutasiP(x1, y1)
else:
    p = permutasiP(y1, x1)

if x >= y:
    p = permutasiC(x, y)
else:
    p = permutasiC(y, x)  


print(permutasiP(x, y))
print(permutasiC(x, y))
print(permutasiP(x1, y1))
print(permutasiC(x1, y1))