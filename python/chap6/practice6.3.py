A = [12, 43, 7, 15, 9]

M = 20

S = []


def lower_bound(seq, ref_val):
    left = 0
    right = len(seq)
    while (right - left) > 1:
        mid = left + int((right - left) / 2)
        if seq[mid] < ref_val:
            left = mid
        else:
            right = mid

    if ref_val < seq[mid]:
        mid -= 1

    return mid


A.append(0)

for a1 in A:
    for a2 in A:
        s = a1 + a2
        if s < M:
            S.append(s)

S = sorted(S)

val = 0

for s in S:
    ref_val = M - s
    i_a_lower = lower_bound(S, ref_val)
    a_lower = S[i_a_lower]
    tmp_val = s + a_lower
    if val < tmp_val and tmp_val < M:
        val = tmp_val

print(S)
print(val)
