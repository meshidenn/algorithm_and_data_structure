from collections import deque


def solve(G, s, t):
    N = len(G)
    dist = [[-1, -1, -1] for _ in range(N)]
    dist[s][0] = 0
    que = deque()
    que.append((s, 0))

    while que:
        v, parity = que.popleft()
        for nv in G[v]:
            np = (parity + 1) % 3
            if dist[nv][np] == -1:
                dist[nv][np] = dist[v][parity] + 1
                que.append((nv, np))

    print(dist)
    if dist[t][0] == -1:
        return -1
    else:
        return dist[t][0]


def main():
    G = [[1, 3], [2, 3, 4], [3, 4, 5], [1], [2, 5], []]
    print(solve(G, 0, 5))


if __name__ == "__main__":
    main()
