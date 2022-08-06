def heapify(a, i, N):
    child1 = i * 2 + 1
    if child1 >= N:
        return
    if child1 + 1 < N and a[child1 + 1] > a[child1]:
        child1 += 1

    if a[child1] <= a[i]:
        return

    a[i], a[child1] = a[child1], a[i]
    print("in: ", i, a)
    heapify(a, child1, N)


def heapsort(a):
    N = len(a)

    print("init: ", a)
    for i in range(int(N / 2) - 1, -1, -1):
        heapify(a, i, N)

    print("heap: ", a)
    for i in range(N - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        print("each step: ", a)
        heapify(a, 0, i)


def main():
    v = [7, 6, 1, 7, 10, 5, 3, 12, 19, 2, 15]
    heapsort(v)
    print("fin: ", v)


if __name__ == "__main__":
    main()
