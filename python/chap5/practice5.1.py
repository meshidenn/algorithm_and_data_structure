Acts = [[1, 2, 3, 4, 5], [3, 2, 1, 4, 1], [5, 4, 3, 2, 1]]

N = 5

happiness = [[0 for _ in range(N)] for _ in range(3)]

for i in range(N):
    for j in range(len(Acts)):
        if i == 0:
            happiness[j][i] += Acts[j][i]
            continue
        for k in range(len(Acts)):
            if j == k:
                continue

            happiness[k][i] = max(happiness[k][i], happiness[j][i - 1] + Acts[k][i])

print(happiness)
print(max([happiness[k][N - 1] for k in range(len(Acts))]))
