

def print_grid( grid:list):
    print('[')
    for i in range(len(grid)):
        print(f' {grid[i]}')
    print(']')


def uniqpaths_obstacle_grid(obstacle_grid:list):
    
    rows = len(obstacle_grid)
    cols = len(obstacle_grid[0])
    print(f'{rows} -  {cols}')
    
    dp = [[ 0 for _ in range(cols)] for _ in range(rows)]

    
    if obstacle_grid[0][0] == 1:
        return 0
    
    dp[0][0] = 1
    #first element in each row is initialized to 1
    for i in range(1,rows):
        if obstacle_grid[i][0] != 1: 
            dp[i][0] = dp[i-1][0]

    for j in range(1,cols):
        if obstacle_grid[0][j] != 1: 
            dp[0][j] = dp[0][j-1]
    
    print_grid(dp)
    
    for i in range(1, rows):
        for j in range(1, cols):
            if obstacle_grid[i][j] != 1 :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            print(f'{i} -- {j}')
    
    
    print_grid(dp)
    return dp[i][j]
if __name__ == "__main__":
    obstacle_grid = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    
    # obstacle_grid = [
    #     [0,0,0],
    #     [0,1,0],
    #     [0,0,0],
      
    # ]
    print(uniqpaths_obstacle_grid(obstacle_grid))