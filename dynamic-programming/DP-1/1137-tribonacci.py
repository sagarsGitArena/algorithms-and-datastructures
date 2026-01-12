
class Tribonacci:
    # Time: O(n) and Space: O(n)
    def tribonacci_v1(self, n:int):
        dp = [0]*(n+1)
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n+1):
            dp[i] = dp[i-1]+ dp[i-2]+dp[i-3]
        
        return dp[n]
    
    # Time: O(n) and Space: O(1)
    def tribonacci_v2(self, n:int):
        var0 = 0
        var1 = 1
        var2 = 1
        
        for _ in range(3, n+1):
            curr = var0 + var1 + var2
            var0, var1, var2 = var1, var2, curr
        
        return curr

if __name__ == "__main__": 
    dp_sol = Tribonacci()
    print(dp_sol.tribonacci_v1(25))
    print(dp_sol.tribonacci_v2(25))
        
