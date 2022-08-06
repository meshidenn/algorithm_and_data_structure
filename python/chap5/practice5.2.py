A = [3, 4, 2, 6, 7, 1, 5]

N = len(A) + 1
W = 100

S = [[0 for _ in range(W + 1)] for _ in range(N)]

for i in range(1, N):
    s = A[i - 1]
    for w in range(1, W + 1):
        if w - s == 0:
            S[i][w] = S[i - 1][w - s] + 1
        if S[i - 1][w] == 1 and w + s <= W:
            S[i][w + s] = S[i - 1][w]
        S[i][w] = max((S[i][w], S[i - 1][w]))

for i in range(N):
    if S[i][W]:
        print("True")
        break
