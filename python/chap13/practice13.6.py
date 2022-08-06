from collections import deque


# def circle(G, s):
#     seen = [False for _ in range(len(G))]
#     finished = [False for _ in range(len(G))]
#     seen[s] = True
#     todo = deque()
#     todo.append(s)
#     route = deque()
#     route.append(s)

#     while todo:
#         v = todo.pop()
#         for i in G[v]:
#             if seen[i]:
#                 continue
#             route.append(i)
#             if s == i:
#                 return True
#             seen[i] = True
#             todo.append(i)
#     return False


def circle(G, s, seen, finished, route):
    seen[s] = True
    route.append(s)
    for next_v in G[s]:
        if next_v == route[0]:
            route.append(next_v)
            return True
        if seen[next_v]:
            continue

        is_circle = circle(G, next_v, seen, finished, route)

        if is_circle:
            return True

    route.pop()
    finished[s] = True
    return False


def main():
    G1 = [[5], [3, 6], [5, 7], [0, 7], [1, 2, 6], [], [7], [0, 2]]

    N = len(G1)

    is_circle = False

    for i in range(N):
        route = deque()
        seen = [False for _ in range(N)]
        finished = [False for _ in range(N)]
        is_circle = circle(G1, i, seen, finished, route)
        if is_circle == True:
            break

    print(i, is_circle, route, seen, finished)


if __name__ == "__main__":
    main()
