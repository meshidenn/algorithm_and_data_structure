from collections import deque


MININF = -1e10


def rec(G, v, seen, order):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue

        rec(G, next_v, seen, order)
    order.append(v)


def chmax(a, b):
    if a < b:
        a = b
        return True
    else:
        return False


def main():
    G = [[5], [3, 6], [5, 7], [0, 7], [1, 2, 6], [], [7], [0]]
    N = len(G)
    seen = [False for _ in range(N)]

    order = []
    for v in range(N):
        if seen[v]:
            continue
        rec(G, v, seen, order)

    order = order[::-1]
    start = order[0]
    end = order[-1]

    dist = [MININF for _ in range(N)]
    dist[start] = 0
    seen = [False for _ in range(N)]
    todo = deque()
    todo.append(start)

    while todo:
        v = todo.popleft()
        for x in G[v]:
            if dist[x] < dist[v] + 1:
                dist[x] = dist[v] + 1
            print(dist[x], dist[v] + 1, dist)
            todo.append(x)

    print(dist[end])


if __name__ == "__main__":
    main()
