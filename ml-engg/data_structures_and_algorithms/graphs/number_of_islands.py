from collections import deque 

class Solution: 
    @staticmethod
    def numIslands_bfs(grid): #bfs is iteratove
        if not grid:
            return 0
        
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if ((r) in range(rows) 
                        and (c) in range(cols)
                        and grid[r][c] == "1" 
                        and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
    
    @staticmethod
    def numIslands_dfs(grid):
        if not grid or not grid[0]:
            return 0

        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visited
            ):
                return

            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands

class Test:
    grid = [
              ["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]
            ]
    @classmethod
    def test_solution(cls):
        assert Solution.numIslands_bfs(cls.grid) == 1
        assert Solution.numIslands_dfs(cls.grid) == 1
        print("Both Test success")

Test.test_solution()
      
      
