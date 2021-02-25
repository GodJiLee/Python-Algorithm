grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]

# 1. using Depth First Search
class Solution:
    def dfs(self, grid, i, j):
        # stop if not land
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return  # stop

        grid[i][j] = '0'  # prevent re-visiting
        # search for all direction
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        # exception
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)): # iterate m times
            for j in range(len(grid[0])); # iterate n times
            if grid[i][j] == '1': # find land
                self.dfs(grid, i, j)
                # increase 1 count after searching for all lands
                count += 1

        return count

# using nested function
def numIsLands(self, grid: List[List[str]]) -> int:
    def dfs(i, j):
        # stop if no land
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
            return

        grid[i][j] = 0

        # search for all direction
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # count + 1 when searching all lands
                count += 1

    return count