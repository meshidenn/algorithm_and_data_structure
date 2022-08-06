from collections import deque


def wfs_dist(G, s):
    N = len(G)
    dist = [-1 for _ in range(N)]
    que = deque()

    dist[s] = 0
    que.append(s)

    while que:
        v = que.popleft()
        for i in G[v]:
            if dist[i] != -1:
                continue

            dist[i] = dist[v] + 1
            que.append(i)

    return dist


def main():
    G = [
        [1, 8],
        [0, 2, 9],
        [1, 3, 10],
        [2, 4],
        [3, 5, 11],
        [4, 6],
        [5, 7, 12],
        [6, 13],
        [0, 9, 14],
        [1, 8, 10],
        [2, 9, 15],
        [4, 17],
        [6, 13, 19],
        [7, 12],
        [8, 20],
        [10, 16, 22],
        [15, 17],
        [11, 16, 18],
        [17, 19],
        [12, 18, 23],
        [14, 21],
        [20, 22, 24],
        [15, 21],
        [19, 27],
        [21, 29],
        [26, 31],
        [25, 27],
        [23, 26],
        [29, 33],
        [24, 28, 30],
        [29, 34],
        [25, 35],
        [38],
        [28, 39],
        [30, 40],
        [31, 36, 42],
        [35, 37, 43],
        [36, 38],
        [32, 44],
        [33],
        [34, 41],
        [40, 42],
        [35, 41, 43],
        [36, 42],
        [38],
    ]

    dist = wfs_dist(G, 0)
    print([(i, d) for i, d in enumerate(dist)])


if __name__ == "__main__":
    main()
