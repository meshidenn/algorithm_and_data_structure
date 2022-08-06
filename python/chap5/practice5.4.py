A = [3, 4, 2, 6, 7, 1, 5]

N = len(A) + 1
W = 20

S = [[0 for _ in range(W + 1)] for _ in range(N)]
S[0][0] = 1
K = 5

for i in range(N - 1):
    s = A[i]
    for w in range(W + 1):
        if S[i][w]:
            S[i + 1][w] = S[i][w]
        if w - s == 0 and S[i][w - s]:
            S[i + 1][w] = 1
        elif w - s > 0 and S[i][w - s]:
            if S[i + 1][w]:
                S[i + 1][w] = min(S[i + 1][w], S[i][w - s] + 1)
            else:
                S[i + 1][w] = S[i][w - s] + 1

print([(a, s) for a, s in zip(A, S[1:])])
print(S[N - 1][W] <= K)
