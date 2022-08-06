A = [2, 3, 3, 4, 9, 10, 11, 12]
B = [2, 3, 3, 4, 9, 10, 11, 12]

K = 23

dA = {a: 0 for a in A}

judge = False
for b in B:
    v = K - b
    if v in A:
        judge = True
        break

print(judge)
