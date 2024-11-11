class  Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            grid[i][j] = 'W'
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
        
        if not grid:
            return 0

        island_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':
                    island_count += 1
                    dfs(grid, i, j)
        
        return island_count

