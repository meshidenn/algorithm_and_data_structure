N = 100
K = 1000

pairs = []
for i in range(K + 1):
    for j in range(K + 1):
        k = N - i - j
        if 0 <= k <= K:
            pairs.append((i, j, k))
        if k < 0:
            break

print(len(pairs))
