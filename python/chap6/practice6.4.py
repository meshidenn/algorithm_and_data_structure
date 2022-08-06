import numpy as np

A = [2, 4, 9, 15, 22, 26, 29, 33]

M = 4

left = 0
right = A[-1]

val = 0
i = 0

while right - left > 1:
    i += 1
    x = int((left + right) / 2)
    cand = [A[0]]
    point = A[0]
    for a in A:
        if a - point >= x:
            cand.append(a)
            point = a

    print(i, left, right, cand)
    if len(cand) >= M:
        # val = right
        # left = right
        # right *= 2
        left = x
    else:
        right = x

print(left)
print(len(A) * np.log(A[-1]))
