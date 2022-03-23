class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        return [k for k,v in counter.most_common(k)]
        # return heapq.nlargest(k, count.keys(), key=count.get)
        
    def vintopKFrequent(self, nums, k):
        
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n ,0)
        
        freq=[]
        
        for i in counter:
            freq.append([i,counter[i]])
        
        freq.sort(key = lambda x: x[1],reverse=True)
        
        print(k,"numbers with most occurrences are")
        
        res=[]
        
        for i in range(k):
            res.append(freq[i][0])
            
        return res
        
nums = [3, 1, 4, 4, 5, 2, 6, 1]
k = 2
#2 numbers with most occurrences are
#1 4 


