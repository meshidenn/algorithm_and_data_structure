A = [12, 43, 7, 15, 9]

sA = sorted(A)
args = []
M = int(len(A) / 2)

for i in range(len(A)):
    a = A[i]
    m = M
    while sA[m] != a:
        if a <= sA[m]:
            m = int(m / 2)
        else:
            m = m + int(m / 2)

    args.append(m)

print(args)
