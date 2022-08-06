A = [3, 4, 2, 6, 7, 1, 5]

INF = 10000
N = len(A) + 1
M = 3
C = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(i):
        if i != j:
            C[j][i] = sum(A[j:i]) / (i - j)

DP = [[0 for _ in range(M + 1)] for _ in range(N)]
for i in range(N):
    for j in range(i):
        for m in range(1, M + 1):
            DP[i][m] = max((DP[i][m], DP[j][m - 1] + C[j][i]))

print(C)
print(DP)
print(DP[N - 1][M])
