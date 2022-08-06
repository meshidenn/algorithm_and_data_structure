from collections import deque


def main():
    G = [[5], [3, 6], [5, 7], [0, 7], [1, 2, 6], [], [7], [0]]
    rG = [[3, 7], [4], [4], [1], [], [0, 2], [1, 4], [2, 3, 6]]
    N = len(G)
    deg = [len(v) for v in G]

    que = deque()
    for i in range(N):
        if deg[i] == 0:
            que.append(i)

    order = []
    while que:
        v = que.popleft()
        order.append(v)

        for x in rG[v]:
            deg[x] -= 1

            if not deg[x]:
                que.append(x)

    print(order)


if __name__ == "__main__":
    main()
