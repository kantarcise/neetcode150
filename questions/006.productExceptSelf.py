"""
Q: Given an integer array nums, return an array 
answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of 
nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time 
and without using the division operation.

**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

**Input:** nums = [-1,1,0,-3,3]
**Output:** [0,0,9,0,0]

"""

import random
from time import perf_counter_ns

class Solution:
    def productExceptSelfBruteForce(self, nums: list[int]) -> list[int]:
        # can we brute force it?
        # yeah, but it is not o(n), here it is anyway
        n = len(nums)
        result = [1] * n
        for i in range(n):
            product = 1 
            for j in range(n):
                if j != i:
                    product *= nums[j]
            result[i] = product
        
        return result


    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # here is how you solve it in o(n)

        # how can we solve it in o(n) ? 
        # we basically cannot have nested loops,
        # we can iterate over the list only. No sorting.
        
        # compartmentalize the problem!

        n = len(nums)
        result = [1] * n

        # compute products to the left of each element
        # and store it in result
        left_product = 1
        for i in range(n):
            # multiply the result element with current 
            # left_product
            result[i] *= left_product
            # adjust the left product with given list element
            left_product *= nums[i]

        # compute products to the left of each element
        # and store it in result
        right_product = 1

        # in backwards:
        for i in range(n-1, -1, -1):
            # multiply the result element with current 
            # left_product
            result[i] *= right_product
            # adjust the left product with given list element
            right_product *= nums[i]

        return result

sol = Solution()

print(sol.productExceptSelfBruteForce(nums = [1,2,3,4]))
print(sol.productExceptSelfBruteForce(nums = [-1,1,0,-3,3]))

# this will not finish for a while.
a = perf_counter_ns()
print(sol.productExceptSelfBruteForce(random.sample(range(1,234623576), 2700)))
b = perf_counter_ns()
print(F"Brute force took {(b - a) // 1e9} seconds")
# Brute force took 24.0 seconds

print(sol.productExceptSelf(nums = [1,2,3,4]))
print(sol.productExceptSelf(nums = [-1,1,0,-3,3]))

# this will work!
c = perf_counter_ns()
print(sol.productExceptSelf(random.sample(range(1,234623576), 2700)))
d = perf_counter_ns()
print(F"Linear Time solution took {(d - c) // 1e9} seconds")
# Linear Time solution took 19.0 seconds