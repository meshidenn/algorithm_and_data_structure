Limit = 50
memo = [-1 for _ in range(Limit)]


def tribonat(N):
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    elif memo[N] != -1:
        return memo[N]
    else:
        memo[N] = tribonat(N - 1) + tribonat(N - 2) + tribonat(N - 3)
    return memo[N]


print(tribonat(8))
