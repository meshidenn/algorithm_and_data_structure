S = "pokemon"
# T = "emo"
T = "pachinko"

LS = len(S)
LT = len(T)

L = [[0 for _ in range(LT + 1)] for _ in range(LS + 1)]

for i in range(LS + 1):
    for j in range(LT + 1):
        if i > 0 and j > 0:
            if S[i - 1] == T[j - 1]:
                L[i][j] = max(L[i][j], L[i - 1][j - 1] + 1)
            else:
                L[i][j] = max(L[i][j], L[i - 1][j - 1])
        # if i > 0:
        #     L[i][j] = max(L[i][j], L[i - 1][j])
        # if j > 0:
        #     L[i][j] = max(L[i][j], L[i][j - 1])
print(L)
print(L[LS][LT])
