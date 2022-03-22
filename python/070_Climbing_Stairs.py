class Solution(object):
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [0] * (n + 1)
    #     dp[0] = 1
    #     dp[1] = 1
    #     for i in range(2, n + 1):
    #         dp[i] = dp[i - 2] + dp[i- 1]
    #     return dp[n]

    def climbStairs(self, n):
        if n <= 1:
            return 1
        dp = [1] * 2
        for i in range(2, n + 1):
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
        return dp[1]

#####################

class Solution:
    def vinclimbStairs(self, n: int) -> int:
        
        if n <= 2: return n
        
        current = 0
        one = 1 
        two = 2
        
        for i in range (2,n):
            current = one + two
            one = two
            two = current
        
        return current
    
    def fibonacci(self,n):
        a = 0
        b = 1

        if n < 0:
            print("Incorrect input")

        elif n == 0:
            return 0

        elif n == 1:
            return b
        else:
            for i in range(1, n):
                c = a + b
                a = b
                b = c
            return b

        
print(sa.climbStairs(5)) # 8

print(sa.fibonacci(6)) # 8
        
https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/
    
#####################
    
    # C = {1: 1, 2: 2}
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n in Solution.C:
    #         return Solution.C[n]
    #     else:
    #         result = Solution.C.get(n - 1, self.climbStairs(n - 1)) + \
    #                  Solution.C.get(n - 2, self.climbStairs(n - 2))
    #         Solution.C[n] = result
    #         return result

