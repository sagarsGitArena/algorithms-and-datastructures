

def pascals_triangle_i_solution(n: int):
    pascals_triangle = []
    
    for i in range(n):       
        row = [1] * (i+1)
        print(row)
        
        for j in range(1, i):
            print(j)
            row[j] = pascals_triangle[i-1][j-1] +  pascals_triangle[i-1][j]
            
        pascals_triangle.append(row)
        #print(row)
        
    print('======================')
    print(pascals_triangle)



def print_pascals_triangle( pascals_triangle:list):
    print('[')
    for i in range(len(pascals_triangle)):
        print(f' {pascals_triangle[i]}')
    print(']')
    


def pascals_triangle_pracice(n:int):
    
    pascals_triangle = []
    for i in range(n):
        row = [1] * (i+1)
        pascals_triangle.append(row)
        print(f'len(row):{len(row)} -- {i}')
        for j in range(1, i):
            pascals_triangle[i][j] = pascals_triangle[i-1][j-1] + pascals_triangle[i-1][j]
            
        
    
    print_pascals_triangle(pascals_triangle)














if __name__ == "__main__":
    #pascals_triangle_i_solution(5)
    pascals_triangle_pracice(5)
    
