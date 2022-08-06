A = [3, 4, 2, 6, 7, 1, 5]

N = len(A)
W = 20

INF = 100000

S = [[INF for _ in range(W + 1)] for _ in range(N + 1)]
S[0][0] = 0
K = 5

for i in range(N):
    s = A[i]
    for w in range(W + 1):
        if S[i + 1][w] > S[i][w]:
            S[i + 1][w] = S[i][w]
        if w - s >= 0:
            if S[i + 1][w] > S[i][w - s] + 1:
                S[i + 1][w] = S[i][w - s] + 1

print(S)
print([(a, s) for a, s in zip(A, S[1:])])
print(S[N][W] <= K)
