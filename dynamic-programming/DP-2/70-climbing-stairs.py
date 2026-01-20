
# f(1) = 1, f(2)=2
#f(n) = f(n-1) + f(n-1)
class ClimbingStairs:

        
    def recursive_solution(self,  n_steps:int):
        
        if n_steps == 0:
            return 0
        
        if n_steps == 1:
            return 1

        if n_steps == 2:
            return 2
        
        return self.recursive_solution(n_steps - 1) + self.recursive_solution(n_steps - 2)
    
    
    memo = {}
    def __init__(self):
        self.memo = {}
        self.memo[0] = 0
        self.memo[1] = 1
        self.memo[2] = 2
    
    ## Top down
    def memoized_recursion(self, n_steps: int):
        if n_steps in self.memo:
            return self.memo[n_steps]
        
            
        self.memo[n_steps] = self.recursive_solution(n_steps - 1) + self.recursive_solution(n_steps - 2)
        return self.memo[n_steps]
    
    
    # Bottom - up space :O(n)
    def tabulation_solution(self, n_steps: int):
        dp = [0] * (n_steps + 1)
        dp[0] = dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n_steps+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n_steps]
        
if __name__ == "__main__":
    cs = ClimbingStairs()
    print(cs.recursive_solution(8))
    print(cs.memoized_recursion(8))
    print(cs.tabulation_solution(8))