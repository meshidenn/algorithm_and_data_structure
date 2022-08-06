from collections import deque

INF = 1e10


def triple(G, s, t, d, path_len):
    d += 1
    print(s, d)
    for next_v in G[s]:
        if next_v == t and (d + 1) % 3 == 0:
            print(s, d, next_v, t)
            path_len.append(d)
            return
        triple(G, next_v, t, d, path_len)
    return


def main():
    G = [[5], [3, 6], [5, 7], [0, 7], [1, 2, 6], [], [7], [0]]
    # G = [[5], [3, 6], [7, 8], [0, 7], [1, 2, 6], [], [7], [0, 8], [0, 5]]
    N = len(G)

    path_len = []

    triple(G, 4, 5, -1, path_len)

    print(path_len)


if __name__ == "__main__":
    main()
