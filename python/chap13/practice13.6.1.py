from collections import deque

G = [[5], [3, 6], [5, 7], [0, 7], [1, 2, 6], [], [7], [0]]

N = len(G)

seen = [False for _ in range(N)]
finished = [False for _ in range(N)]
hist = deque()
pos = -1


def dfs(G, v, p):
    global seen
    global finished
    global hist
    global pos
    seen[v] = True
    hist.append(v)

    for nv in G[v]:
        if nv == p:
            continue
        if finished[nv]:
            continue
        if seen[nv] and not finished[nv]:
            pos = nv
            return

        dfs(G, nv, v)

        if pos != -1:
            return
    hist.pop()
    finished[v] = True


def main():
    dfs(G, 0, -1)

    cycle = set()
    while hist:
        t = hist.pop()
        cycle.add(t)
        if t == pos:
            break

    print(cycle)


if __name__ == "__main__":
    main()
