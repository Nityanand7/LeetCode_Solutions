class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        G = defaultdict(list)

        for i, j in product(range(m), range(n)):
            for k, l, d in [(i, j+1, 1), (i, j-1, 2), (i+1, j, 3), (i-1, j, 4)]:
                if 0 <= k < m and 0 <= l < n:
                    G[(i, j)].append(((k, l), int(grid[i][j] != d)))

        src, dest = (0, 0), (m-1, n-1)
        COST = defaultdict(lambda: float("inf"))
        COST[src] = 0
        pq = [[0, src]]
        while pq:
            w_u, u = heapq.heappop(pq)
            if u == dest: return COST[u]
            if w_u > COST[u]: continue
            for v, w_v in G[u]:
                if w_u + w_v < COST[v]:
                    COST[v] = w_u + w_v
                    heapq.heappush(pq, (COST[v], v))
