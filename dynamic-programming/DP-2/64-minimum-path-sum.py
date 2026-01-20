def print_grid( grid:list):
    print('[')
    for i in range(len(grid)):
        print(f' {grid[i]}')
    print(']')



def  minimum_path_sum(grid: list):
    
    rows= len(grid)
    cols = len(grid[0])
    
    dp =   [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    print_grid(dp)
    
    dp[0][0] = grid[0][0]
    ## init first rows
    for i in range(1,rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    print_grid(dp)
    
    ## init cols
    for j in range(1,cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    print_grid(dp)
    
    
    for i in range(1,rows):
        for j in range(1,cols):
            dp[i][j] = grid[i][j] + min(dp[i-1][j],  dp[i][j-1])
    
    return dp[rows-1][cols-1]
            
            
            

if __name__ == "__main__":
    
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    
    print(minimum_path_sum(grid))