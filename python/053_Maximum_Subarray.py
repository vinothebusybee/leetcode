class Solution(object):
    # def maxSubArray(self, nums):
    #     return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
    #
    # def maxSubArrayHelper(self, nums, l, r):
    #     if l > r:
    #         return -2147483647
    #     mid = (l + r) / 2
    #     leftAns = self.maxSubArrayHelper(nums, l, mid - 1)
    #     rightAns = self.maxSubArrayHelper(nums, mid + 1, r)
    #     lMaxSum = res = 0
    #     for i in range(mid - 1, l -1, -1):
    #         res += nums[i]
    #         lMaxSum = max(res, lMaxSum)
    #     rMaxSum = res = 0
    #     for i in range(mid + 1, r + 1):
    #         res += nums[i]
    #         rMaxSum = max(res, rMaxSum)
    #     return max(lMaxSum + nums[mid] + rMaxSum, max(leftAns, rightAns))

    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     ls = len(nums)
    #     start = [0] * ls
    #     all = [0] * ls
    #     start[-1], all[-1] = nums[-1], nums[-1]
    #     for i in reversed(range(ls - 1)):
    #         start[i] = max(nums[i], nums[i] + start[i + 1])
    #         all[i] = max(start[i], all[i + 1])
    #     return all[0]

    # def maxSubArray(self, nums):
    #     ls = len(nums)
    #     start, all = nums[-1], nums[-1]
    #     for i in reversed(range(ls - 1)):
    #         start = max(nums[i], nums[i] + start)
    #         all = max(start, all)
    #     return all

    def maxSubArray(self, nums):
        maxEndingHere = maxSofFar = nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i]) # if current element is greater than previous sum leave it, consider onlt current element
            maxSofFar = max(maxEndingHere, maxSofFar)
        return maxSofFar
    
# [-2,1,-3,4,-1,2,1,-5,4]

# element -> maxEndingHere -> maxSofFar

# -2-->-2-->-2

#  1--> 1-->1
# -3-->-2-->1
#  4--> 4-->4
# -1--> 3-->4
#  2--> 5-->5
#  1--> 6-->6
# -5--> 1-->6
#  4--> 5-->6
    
    #Neet code
    class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        
        for n in nums:
            if currSum<0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub,currSum)
        return maxSub
    
