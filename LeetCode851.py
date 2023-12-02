class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(node):
            # If the answer for this node is already computed, return it
            if answer[node] is None:
                # Start with the person themselves
                answer[node] = node
                for neighbor in graph[node]:
                    # Get the quietest person in the rich set of the neighbor
                    quietest_neighbor = dfs(neighbor)
                    if quiet[quietest_neighbor] < quiet[answer[node]]:
                        answer[node] = quietest_neighbor
            return answer[node]

        # Build the graph
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)

        # Initialize the answer array with None
        answer = [None] * n

        # Run DFS for each person
        for i in range(n):
            dfs(i)

        return answer
