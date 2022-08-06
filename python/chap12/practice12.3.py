V = [9, 3, 10, 2, 4, 7, 12, 5, 22, 13]
S = []
K = 4
k = 6

for i, v in enumerate(V):
    S.append(v)
    if i == k:
        break

sS = sorted(S)

print(i, sS[K], sS)

t = sS[K]

for j in range(k + 1, len(V)):
    if V[j] < t:
        t = V[j]
        print(j, t)
