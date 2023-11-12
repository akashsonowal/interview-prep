class Solution:
    # Implementation for Prim's algorithm to compute Minimum Spanning Trees
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        for n1, n2, weight in edges:
            adj[n1].append([n2, weight])
            adj[n2].append([n1, weight])

        minHeap = [[0,0]] # [vertex, weight] start bfs at v=0
        res = 0 # Total weight of the MST
        visit = set()
        while minHeap and len(visit) < n:
            weight, v = heapq.heappop(minHeap)
            if v in visit:
                continue

            res += weight
            visit.add(v)
            for neighbor, weight in adj[v]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, neighbor])

        # Return -1 if not all nodes are visited (unconnected graph)
        return res if len(visit) == n else -1 
