R = [(1, 3), (10, 9), (7, 20), (2, 2)]
B = [(2, 9), (3, 3), (15, 22), (11, 10)]

sR = sorted(R, key=lambda x: x[0])
sB = sorted(B, key=lambda x: x[0])


N = len(R)
i = 0
I = 0
pairs = []
print(sR)
print(sB)
for b in sB:
    j = 0
    while (i <= N - 1) and (sR[i][0] < b[0]) and (sR[i][1] < b[1]):
        print((sR[i][0] < b[0]), (sR[i][1] < b[1]), sR[i], b)
        pairs.append((sR[i], b))
        i += 1
        j += 1

    I += j

print(I)
print(pairs)
