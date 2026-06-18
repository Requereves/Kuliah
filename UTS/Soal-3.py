a, b, c = map(int, input().split())
# a = int(input("Masukkan: "))
# f = b ** 2
# g = c - 5
# h = (2 * a) + 1

def mesinF(a):
    f = ((((2 * a) + 1) - 5) ** 2)
    return f

def mesinG(b):
    g = (((2 *(b ** 2)) + 1) - 5)
    return g

def mesinH(c):
    h = ((2 * ((c - 5) ** 2) )+ 1) 
    return h

print(mesinF(a))
print(mesinG(b))
print(mesinH(c))
