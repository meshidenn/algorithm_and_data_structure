A = [3, 4, 2, 6, 7, 1, 5]
N = len(A)

S = [0 for _ in range(N + 1)]

for i in range(N):
    S[i + 1] = S[i] + A[i]

INF = 10000

DP = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    DP[i][i + 1] = 0

for bet in range(2, N + 1):
    for i in range(0, N + 1 - bet):
        j = i + bet
        for k in range(i + 1, j):
            DP[i][j] = min((DP[i][j], DP[i][k] + DP[k][j] + S[j] - S[i]))

print(S)
print(DP)
print(DP[0][N])
