
class Fibinocci:
    def __init__(self):
        self.memo = {}
        
    ## Exponential solution: Those who cannot remember the past are condemned to repeat it
    def fibinocci_recursive(self, n:int):
        if n==0 or n==1:
            return n
        
        return self.fibinocci_recursive(n-1) + self.fibinocci_recursive(n-2)
    
    
    ## This recursoin with out repetition -- top down
    def fibinocci_memoization(self, n:int):
        if n in self.memo:
            return self.memo[n]
        
        if n==0 or n==1:
            return n
        else:
            self.memo[n] = self.fibinocci_memoization(n - 1) + self.fibinocci_memoization(n-2)
        
        return self.memo[n]
    

if __name__ == "__main__":  
    f = Fibinocci()
    print(f.fibinocci_memoization(8))
    
    print(f.fibinocci_recursive(8))