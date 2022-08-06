from collections import deque

G = [
    [(1, 3), (2, 5)],
    [(2, 4), (3, 12)],
    [(3, 9), (4, 4)],
    [(5, 2)],
    [(1, 1), (3, 7), (5, 8)],
    [],
]

INF = 1e10


def main():
    exist_positive_cycle = False
    N = len(G)
    dist = [-INF for _ in range(N)]
    s = 0
    dist[s] = 0

    for iter in range(N):
        update = False
        for v in range(N):
            if dist[v] == -INF:
                continue
            for to, w in G[v]:
                if dist[to] < dist[v] + w:
                    dist[to] = dist[v] + w
                    update = True

        if not update:
            break

        if iter == N - 1 and update:
            exist_positive_cycle = True

    print(exist_positive_cycle)
    print(dist)


if __name__ == "__main__":
    main()
