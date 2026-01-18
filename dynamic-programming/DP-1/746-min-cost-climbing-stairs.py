def min_cost_climbing_Stairs( cost_arr: list):
    
    table = [0 for _ in range(len(cost_arr))]
    table[0] = cost_arr[0]
    table[1] = cost_arr[1]
    
    for i in range(2, len(table)):
        table[i] = min(table[i-1], table[i-2]) + cost_arr[i]
        
    return min(table[-1], table[-2]) 
        
    
if __name__=="__main__":
    cost_arr= [10, 15, 20]
    
    print(min_cost_climbing_Stairs(cost_arr))
    
    cost_arr= [1, 100,1, 1, 1, 100, 1, 1, 100, 1]
    print(min_cost_climbing_Stairs(cost_arr))
    