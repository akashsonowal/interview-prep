class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Finds the root of x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        # Connects x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            return True
        return False

class Solution:
    # Implementation for Kruskal's algorithm to compute Minimum Spanning Trees
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # Use a min heap to sort the edges
        minHeap = []
        for n1, n2, weight in edges:
            heapq.heappush(minHeap, [weight, n1, n2])

        # Use Union Find to keep track of the connected components
        unionFind = UnionFind(n)
        res, components = 0, n

        # Pop the edges from the min heap and connect the nodes
        while components > 1 and minHeap:
            weight, n1, n2 = heapq.heappop(minHeap)
            if unionFind.union(n1, n2):
                res += weight
                components -= 1

        # Return -1 if not all nodes are visited (unconnected graph)
        return res if components == 1 else -1
