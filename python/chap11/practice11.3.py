from collections import defaultdict


class UnionFind:
    def __init__(self, V):
        self.par = [-1 for _ in range(V)]
        self.siz = [1 for _ in range(V)]

    def root(self, i):
        if self.par[i] == -1:
            return i
        else:
            self.par[i] = self.root(self.par[i])
            return self.par[i]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True


def main():
    V = 6
    road = [(0, 1), (0, 2), (0, 5), (2, 5), (2, 4)]
    train = [(0, 1), (0, 2), (2, 3)]
    uf_road = UnionFind(V)
    uf_train = UnionFind(V)

    for r in road:
        uf_road.unite(*r)

    for t in train:
        uf_train.unite(*t)

    num = defaultdict(int)
    for v in range(V):
        rr = uf_road.root(v)
        rt = uf_train.root(v)
        num[(rr, rt)] += 1

    for v in range(V):
        rr = uf_road.root(v)
        rt = uf_train.root(v)
        print(v, num[(rr, rt)])


if __name__ == "__main__":
    main()
