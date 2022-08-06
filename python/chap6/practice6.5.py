A = [2, 4, 9, 15, 22, 26, 29, 33]
B = [3, 7, 11, 14, 19, 23, 32, 35]

K = 4
K_ = K - 1

left = 0
right = A[-1] * B[-1]


def lower_bound(L, v):
    left_ = 0
    right_ = len(L) - 1
    if v < L[0]:
        return 0

    while (right_ - left_) > 1:
        i = int((left_ + right_) / 2)
        x = L[i]
        if x > v:
            right_ = i
        else:
            left_ = i

    return left_ + 1


while (right - left) > 1:
    x = int((left + right) / 2)
    k = 0
    for a in A:
        v = int(x / a)
        i = lower_bound(B, v)
        print("loop: ", right, a, x, v, i, k)
        k += i

    print(k, x, left, right)
    if k > K_:
        right = x
    else:
        left = x

print(left + 1)
