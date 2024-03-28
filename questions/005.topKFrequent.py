"""
Q: Given an integer array nums and an integer k, return 
the k most frequent elements. You may return 
the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

"""

from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # we can use Counters with most_common
        c = Counter(nums)
        return [elem[0] for elem in c.most_common(k)]


    def topKFrequent_(self, nums: list[int], k: int) -> list[int]:
        # or we can take the heap route just to use, nlargest

        # edge case 
        if k == len(nums):
            return nums

        c = Counter(nums)
        
        return nlargest(k, c.keys(), key = c.get)


sol = Solution()
print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent(nums = [1], k = 1))

print(sol.topKFrequent_(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent_(nums = [1], k = 1))