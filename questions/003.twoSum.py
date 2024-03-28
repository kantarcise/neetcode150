"""
Q: Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one 
solution, and you may not use the same  element twice.
You can return the answer in any order.

**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # only one solution
        # make index map
        index_map = {}

        for i, elem in enumerate(nums):
            difference = target - elem
            if difference in index_map:
                return [i, index_map[difference]]
            index_map[elem] = i

sol = Solution()

print(sol.twoSum(nums = [2,7,11,15], target = 9))
print(sol.twoSum(nums = [3,2,4], target = 6))
