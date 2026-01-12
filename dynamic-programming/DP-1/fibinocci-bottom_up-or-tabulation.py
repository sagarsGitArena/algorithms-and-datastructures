class Fibinocci:

    # Soltion that runs in linear time, linear space.-- bottom up
    ### Go for Tabulation only if you need all DP states later
    def fibinocci_tabulation(self, n:int):
        table = [0] * (n+1)
        table[0] = 0
        table[1] = 1
        
        for i in range(2, n+1): #n+1 --> as n is exclude. To ensure n is included , we need to have n+1
            table[i] = table[i-1] + table[i-2]
            
        return table[n]

    ### Only when you need the final answer and not interested in intermediate states later.  
    #DP solution that runs in linear time O(1) space  --bottom-up
    def fibinocci_two_variable(self, n:int):
        if n < 2:
            return n
        prev1, prev2 = 0,1
        print(f'{prev1} -- {prev2}')
        
        for _ in range(2, n+1): #n+1 --> as n is exclude. To ensure n is included , we need to have n+1
            
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr

        return curr
if __name__ == "__main__":  
    f = Fibinocci()
    print(f.fibinocci_tabulation(8))
    print(f.fibinocci_two_variable(8))
    
    for i in range(2,8):
        print(i)
    
    