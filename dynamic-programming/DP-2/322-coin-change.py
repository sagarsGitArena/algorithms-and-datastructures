class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp_arr = [0 for i in range(0, amount+1)]
        print(dp_arr)
        
        dp_arr[0] = 0
        for i in range(1, len(dp_arr)):
            min_val = float("inf")
            for coin in coins:                
                if i - coin >= 0:
                    prev_hop = i - coin
                    min_val = min(min_val,  dp_arr[prev_hop]+1)
            dp_arr[i] = min_val 
        print(dp_arr)
        if dp_arr[-1] == float("inf"):
            return -1
        else:
            return dp_arr[-1]


if __name__ == "__main__":
    sol = Solution()
    coins = [1,2,5]
    amount = 11
    print(sol.coinChange(coins, amount))
    
    coins = [1,5,7]
    amount = 10
    print(sol.coinChange(coins, amount))
    