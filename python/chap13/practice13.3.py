from collections import deque


def wfs(G, s, color, cur=0):
    color[s] = cur
    todo = deque()
    todo.append((s, cur))

    while todo:
        v, cur = todo.popleft()
        n_cur = 1 - cur
        for next_v in G[v]:
            if color[next_v] != -1:
                if color[next_v] == cur:
                    return False
                continue

            color[next_v] = n_cur
            todo.append((next_v, n_cur))
            print(next_v, n_cur, todo, color)

    return True


def main():
    G = [[1, 3], [0, 2], [1], [0, 4], [1, 2, 3]]
    N = len(G)
    color = [-1 for _ in range(N)]
    is_bipartie = True
    for v in range(N):
        if color[v] != -1:
            continue
        if not wfs(G, 0, color):
            is_bipartie = False

    if is_bipartie:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
