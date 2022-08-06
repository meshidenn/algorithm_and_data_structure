R = [(1, 3), (10, 9), (7, 20), (2, 2)]
B = [(2, 9), (3, 3), (15, 22), (11, 10)]

sR = sorted(R, key=lambda x: x[0])
sB = sorted(B, key=lambda x: x[0])

N = len(R)
used = [False for _ in range(N)]

i = 0
I = 0
res = 0
pairs = []
print(sR)
print(sB)
for b in sB:
    maxy = -1
    maxid = -1
    for j in range(N):
        if used[j]:
            continue

        if sR[j][0] >= b[0]:
            continue

        if sR[j][1] >= b[1]:
            continue

        if maxy < sR[j][1]:
            maxy = sR[j][1]
            maxid = j

    if maxid == -1:
        continue
    res += 1
    used[maxid] = True
print(res)
print(pairs)
