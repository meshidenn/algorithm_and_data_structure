A = [2, 3, 3, 4, 9, 10, 11, 12]
B = [3, 7, 8, 10, 12, 13]

dA = {}
for a in A:
    if a in dA:
        dA[a] += 1
    else:
        dA[a] = 1

common = 0

for j, b in enumerate(B):
    if b in dA:
        i = dA[b]
        common += i

print(common)
