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

    def separate(self, x, y):
        if self.par[x] == y:
            self.par[x] = -1
        else:
            self.par[y] = -1


def main():
    V = 6
    uf = UnionFind(V)

    edges = [(0, 1), (0, 2), (0, 5), (2, 5), (2, 3), (2, 4)]

    num_bridge = 0
    for j, e in enumerate(edges):
        uf.unite(e[0], e[1])
        print(e, uf.par)

    res = 0
    for v in range(V):
        if (uf.root(v)) == v:
            res += 1

    for i, e in enumerate(edges):
        uf.separate(e[0], e[1])
        if uf.root(e[0]) != uf.root(e[1]):
            res += 1
        print(i, e, res, uf.par)

    print(num_bridge)


if __name__ == "__main__":
    main()
