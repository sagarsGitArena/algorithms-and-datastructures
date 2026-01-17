

def unique_paths(m:int, n:int):
    grid = [ [1 for _ in range(n)] for _ in range(m)]
    print(grid)
    
    
    #grid = []
    ## Initialization of 2 D array
    # for _ in range(m):
    #     grid.append([0] * n)
    
    # print(grid)
    
    # ## set first column to 1s
    # for i in range(m):
    #     grid[i][0] = 1
    
    # print(grid)
    # ## set first row to 1s
    # for i in range(n):
    #     grid[0][i] = 1

    
    print(grid)
    
   
    
    
    for i in range(1,m):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
    print(grid)
    
    return grid[m-1][n-1]


if __name__ == "__main__":
    m = 3 #three Rows
    n = 7 #Columns
    
    
    num_unique_paths = unique_paths(3,7);
    
    print(f'Unique paths in {m} X {n} grid :{num_unique_paths}')