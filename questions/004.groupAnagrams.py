"""
Q: Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by 
rearranging the letters  of a different word 
or phrase, typically using  all the original 
letters exactly once.

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]
**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Input:** strs = [""]
**Output:** [[""]]

"""

from collections import Counter
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # we can hold all strings as counters, together
        groups = defaultdict(list)
        
        for s in strs:
            # we can use a frozenset to unify strings
            # and make them comparable
            groups[frozenset(Counter(s).items())].append(s)

        return list(groups.values())

    def groupAnagrams_(self, strs: list[str]) -> list[list[str]]:
        # we can also solve it with sorting the strings:
        strs_map = {}

        for s in strs:
            # sort the word
            sorted_str = "".join(sorted(s))

            if sorted_str not in strs_map:
	            # make an new key for this element
                strs_map[sorted_str] = []
            
            # add the elem to that key
            strs_map[sorted_str].append(s)
            
        return list(strs_map.values())

    def groupAnagrams__(self, strs: list[str]) -> list[list[str]]:
        # we can also take the collections route with tuples
        res = defaultdict(list)
        for s in strs:
	        # we can use a tuple for our dict keys
	        # sorted returns a list
            res[tuple(sorted(s))].append(s)
        return list(res.values()) 

sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams_(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams__(strs = ["eat","tea","tan","ate","nat","bat"]))