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
    G = [
        [1, 2, 4],
        [0, 3, 8],
        [0, 5],
        [1, 7, 8],
        [0, 8],
        [2, 6, 8],
        [5, 7],
        [3, 6],
        [1, 3, 4, 5],
        [],
        [11],
        [10, 12],
        [11],
    ]
    seen = [False for _ in range(len(G))]

    s = 0
    num = 0
    while not all(seen):
        search(G, s, seen)
        print(s, seen)

        for i, se in enumerate(seen):
            if not se:
                break
        s = i
        num += 1

    print(num)


if __name__ == "__main__":
    main()
