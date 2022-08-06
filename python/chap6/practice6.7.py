A = [2, 4, 9, 15, 22, 26, 29, 33]

C = A[-1]

N = len(A)

M = (N * (N + 1)) / 2 / 2

s = 0
S = [s]

for a in A:
    s += a
    S.append(s)

left = 0
right = A

while (right - left) > 1:
    