A = [12, 43, 7, 15, 9]
B = [13, 42, 8, 14, 10]
C = [3, 25, 7, 9, 30]

N = len(A)
M = int(N / 2)

sA = sorted(A)
sB = sorted(B)
sC = sorted(C)

all_pattern = 0


def lower_bound(seq, ref_val):
    left = 0
    right = N
    while (right - left) > 1:
        mid = left + int((right - left) / 2)
        if seq[mid] < ref_val:
            left = mid
        else:
            right = mid

    if ref_val < seq[mid]:
        mid -= 1

    return mid


b_c_pattern = []

for i, b in enumerate(sB):
    i_a_low = lower_bound(sA, b)
    i_c_low = lower_bound(sC, b)
    a_low = sA[i_a_low]
    if b < a_low:
        continue
    c_low = sC[i_c_low]
    if c_low < b:
        if N - 1 <= i_c_low:
            continue
        else:
            i_c_low += 1
            c_low = sC[i_c_low]

    this_pattern = (i_a_low + 1) * (N + 1 - i_c_low)
    all_pattern += this_pattern
    print(i, b, a_low, i_a_low, c_low, i_c_low, this_pattern)
print(all_pattern)
