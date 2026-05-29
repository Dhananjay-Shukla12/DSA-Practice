from typing import (
    List,
)

class Solution:
    """
    @param a: lists A
    @param b: lists B
    @return: the index mapping
    """
    def anagram_mappings(self, a: List[int], b: List[int]) -> List[int]:
        hashmap = {}
        for i in range(0,len(b)):
            hashmap[i] = b[i]
        ans = []
        for i in range(0,len(a)):
            for key,value in hashmap.items():
                if value == a[i]:
                    ans.append(key)
                    value = -1
                    break
        
        return ans
    