class UnionFindDict2D:
    def __init__(self, n):
        self.n = n
        self.parent = {(r, c): (r, c) for r in range(n) for c in range(n)}
        self.size = {(r, c): 1 for r in range(n) for c in range(n)}


    def find(self, coord):
        if self.parent[coord] != coord:
            self.parent[coord] = self.find(self.parent[coord])
        return self.parent[coord]


    def union(self, c1, c2):
        r1 = self.find(c1)
        r2 = self.find(c2)
        if r1 != r2:
            if self.size[r1] < self.size[r2]:
                r1, r2 = r2, r1
            self.parent[r2] = r1
            self.size[r1] += self.size[r2]
            return True
        return False


def one_round_move(n, population, uf, L, R):
    moved = False
    for r in range(n):
        for c in range(n):
            current = (r, c)
            # 우측 노드 검사
            if c + 1 < n:
                right = (r, c + 1)
                diff = abs(population[r][c] - population[r][c + 1])
                if L <= diff <= R:
                    if uf.union(current, right):
                        moved = True
            # 아래 노드 검사
            if r + 1 < n:
                down = (r + 1, c)
                diff = abs(population[r][c] - population[r + 1][c])
                if L <= diff <= R:
                    if uf.union(current, down):
                        moved = True
    return moved


def redistribute_population(n, population, uf):
    groups = {}
    for r in range(n):
        for c in range(n):
            root = uf.find((r, c))
            if root not in groups:
                groups[root] = []
            groups[root].append((r, c))
    for root, members in groups.items():
        total_pop = sum(population[r][c] for r, c in members)
        avg_pop = total_pop // len(members)
        for r, c in members:
            population[r][c] = avg_pop


def main():
    n, L, R = map(int, input().split())
    population = [list(map(int, input().split())) for _ in range(n)]

    days = 0
    uf = UnionFindDict2D(n)
    moved = True
    while moved:
        # Union-Find 초기화
        uf.parent = {(r, c): (r, c) for r in range(n) for c in range(n)}
        uf.size = {(r, c): 1 for r in range(n) for c in range(n)}

        moved = one_round_move(n, population, uf, L, R)

        if moved:
            redistribute_population(n, population, uf)
            days += 1

    print(days)

if __name__ == "__main__":
    main()