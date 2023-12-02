class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for i in range(n)]

        # Fill in the direct edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Each vertex has a distance of 0 to itself
        for i in range(n):
            dist[i][i] = 0

        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Update the distance if a shorter path is found
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Count the number of reachable cities within the threshold for each city
        result = [sum(dist[i][j] <= distanceThreshold for j in range(n)) for i in range(n)]

        # Find the city with the minimum number of reachable cities
        # If there are multiple cities, return the city with the largest ID
        min_reachable = min(result)
        for i in range(n-1, -1, -1):
            if result[i] == min_reachable:
                return i
