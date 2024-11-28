def dfs(grid, i, j, m, n):
    if grid[i][j] == 0:
        return 0

    area = 1
    grid[i][j] = 0
    if i > 0:
        area += dfs(grid, i-1, j, m, n)
    if i < m - 1:
        area += dfs(grid, i+1, j, m, n)
    if j > 0:
        area += dfs(grid, i, j-1, m, n)
    if j < n - 1:
        area += dfs(grid, i, j+1, m, n)
    return area


def f(grid):
    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    result = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            else:
                area = dfs(grid, i, j, m, n)
                result = max(result, area)
    return result


print(f([[1]]))
print(f([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
