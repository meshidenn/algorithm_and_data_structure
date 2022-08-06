A = [3, 4, 2, 6, 7, 1, 5]

N = len(A) + 1
W = 10

S = [[0 for _ in range(W + 1)] for _ in range(N)]
S[0][0] = 1

for i in range(N - 1):
    s = A[i]
    for w in range(W + 1):
        if S[i][w]:
            S[i + 1][w] = S[i][w]
        if w - s >= 0 and S[i][w - s]:
            S[i + 1][w] += 1

print(S)
print(sum(S[N - 1]) - 1)