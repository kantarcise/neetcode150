"""
Q: Given two strings s and t, return true if 
t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging
 the letters of a different word or phrase, typically
  using all the original  letters exactly once.

**Input:** s = "anagram", t = "nagaram"
**Output:** true

**Input:** s = "rat", t = "car"
**Output:** false

"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)        

    def isAnagramMap(self, s: str, t: str) -> bool:
        map_1, map_2 = {}, {}

        for elem in s:
            map_1[elem] = map_1.get(elem, 0) + 1

        for elem in t:
            map_2[elem] = map_2.get(elem, 0) + 1

        return map_1 == map_2

sol = Solution()
print(sol.isAnagram(s = "rat", t  = "car")) # False
print(sol.isAnagram(s = "anagram", t  = "nagaram")) # True

print(sol.isAnagramMap(s = "rat", t  = "car")) # False
print(sol.isAnagramMap(s = "anagram", t  = "nagaram")) # True
