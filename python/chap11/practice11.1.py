class UnionFind:
    def __init__(self, V):
        self.par = [-1 for _ in range(V)]
        self.siz = [1 for _ in range(V)]

    def root(self, i):
        if self.par[i] == -1:
            return i
        else:
            return self.par[i] == self.root(self.par[i])

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
    uf = UnionFind(V)

    edges = [(0, 1), (0, 2), (0, 5), (2, 5), (2, 3), (2, 4)]
    E = len(edges)

    num_bridge = 0
    for i in range(E):
        for j, e in enumerate(edges):
            if j == i:
                cand = e
                continue
            e = edges[i]
            uf.unite(e[0], e[1])
            print(uf.par)

        if uf.root(cand[0]) != uf.root(cand[1]):
            num_bridge += 1

    print(num_bridge)


if __name__ == "__main__":
    main()
