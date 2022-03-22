class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # dp
    #     ls = len(nums)
    #     if ls == 0:
    #         return 0
    #     dp = [0] * ls
    #     dp[0] = nums[0]
    #     for i in range(1, ls):
    #         if i < 2:
    #             dp[i] = max(nums[i], dp[i - 1])
    #         else:
    #             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    #     return dp[ls - 1]

    # def rob(self, nums):
    #     if nums is None or len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
    #     nums[1] = max(nums[0], nums[1])
    #     for i in range(2, len(nums)):
    #         nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
    #     return nums[-1]

    def rob(self, nums):
        prevMax = currMax = 0
        for num in nums:
            temp = currMax
            currMax = max(prevMax + num, currMax)
            prevMax = temp
        return currMax


[2,7,9,3,1]

#2
temp = 0
currMax = 2  max(0+2, 0)
prevmax = 0

#7
temp = 2
currMax = 7   max(0+7, 0)
prevmax = 2

#9
temp = 7
currMax = 11  max(2+9,7)
prevmax = 7

#3
temp = 11
currMax = 11  max(7+3, 11)
prevmax = 11

#1
temp = 11
currMax = 12  max(11+1, 11)
prevmax = 11

    
    
