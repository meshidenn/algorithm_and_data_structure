from collections import deque


def search(G, s, seen):
    todo = deque()

    seen[s] = True
    todo.append(s)

    while todo:
        v = todo.pop()

        for x in G[v]:
            if seen[x]:
                continue

            seen[x] = True
            todo.append(x)


def main():
    G = [[5], [3, 6], [5, 7], [0, 7], [1, 2, 6], [], [7], [0]]
    seen = [False for _ in range(len(G))]

    s = 0
    t = 5
    search(G, s, seen)
    print(seen[t])

    seen = [False for _ in range(len(G))]
    s = 1
    t = 2
    search(G, s, seen)
    print(seen[t])


if __name__ == "__main__":
    main()
