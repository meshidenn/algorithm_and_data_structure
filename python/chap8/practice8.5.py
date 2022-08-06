A = [2, 3, 4, 9, 10, 11, 12]
B = [3, 7, 8, 10, 12, 13]

dA = {a: 1 for a in A}

common = 0

for b in B:
    if b in dA:
        common += 1

print(common)
