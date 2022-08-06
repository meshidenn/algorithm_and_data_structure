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
    uf = UnionFind(V)

    edges = [(0, 1), (0, 2), (0, 5), (2, 5), (2, 3), (2, 4), (1, 3)]
    r_edges = edges[::-1]
    res = [V for _ in range(V)]
    res = []
    cur = V

    for i, e in enumerate(r_edges):
        if uf.root(e[0]) != uf.root(e[1]):
            cur -= 1
        uf.unite(*e)
        res.append(cur)
        print(i, e, res)

    print(res)


if __name__ == "__main__":
    main()
