A = [3, 4, 2, 6, 7, 1, 5]
M = [2, 3, 4, 5, 1, 2, 3]

N = len(A) + 1
W = 50
INF = 10000

S = [[INF for _ in range(W + 1)] for _ in range(N)]
S[0][0] = 0

for i in range(N - 1):
    s = A[i]
    m = M[i]
    for w in range(W + 1):
        if S[i][w] < INF:
            S[i + 1][w] = 0
        if w >= s and S[i + 1][w - s] < m:
            S[i + 1][w] = S[i + 1][w - s] + 1

print([(a, s) for a, s in zip(A, S[1:])])
