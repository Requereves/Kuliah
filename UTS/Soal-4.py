x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
xt, yt = map(int, input().split())

def jarak(a, b, c, d):
    d = (c - a)**2 + (d - b)** 2
    hasil = d ** 0.5
    return hasil

# hasiljarak1 = jarak(x1, y1, r1)
# hasiljarak2 = jarak(x2, y2, r2)

if jarak(x1, y1, xt, yt) <= r1 & jarak(x2, y2, xt, yt) <= r2:
    print("jangkauan di radar 1 dan 2")
elif jarak(x1, y1, xt, yt) <= r1 & jarak(x2, y2, xt, yt) >= r2:
    print("jangkauan di radar r1")
elif jarak(x2, y2, xt, yt) <= r2 & jarak(x1, y1, xt, yt) >= r1:
    print("jangkauan di radar r2")
else:
    print("titik diluar jangkauan")

print("hasil")