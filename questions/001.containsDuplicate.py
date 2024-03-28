"""
Q: Given an integer array nums, return true if any value
 appears at least twice in the array, and return false 
 if every element is distinct.
 
**Input:** nums = [1,2,3,1]
**Output:** true

**Input:** nums = [1,2,3,4]
**Output:** false

"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for elem in nums:
            if elem in s:
                return True
            s.add(elem)
        return False
        
sol = Solution()
print(sol.containsDuplicate(nums = [1,2,3,4,5]))
print(sol.containsDuplicate(nums = [1,2,3,4,5,2]))

