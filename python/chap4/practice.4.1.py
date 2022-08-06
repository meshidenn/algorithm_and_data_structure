def tribonat(N):
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        sum = tribonat(N - 1) + tribonat(N - 2) + tribonat(N - 3)
    return sum


print(tribonat(8))
