A = [2, 4, 9, 15, 22, 26, 29, 33]
B = [3, 7, 11, 14, 19, 23, 32, 35]


def lower_bound(L, v):
    left = 0
    right = len(L)

    while (right - left) > 1:
        i = int((left + right) / 2)
        l = L[i]
        if l > v:
            right = i
        else:
            left = i

    return len(L) - right


k = 0
for a in A:
    i = lower_bound(B, a)
    k += i

print(k)
