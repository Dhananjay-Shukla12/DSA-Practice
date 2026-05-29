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
        valueToPos = {}
        for i in range(len(b)):
            valueToPos[b[i]] = i

        
        mappings = [0] * len(a)
        for i in range(len(a)):
            mappings[i] = valueToPos[a[i]]

        return mappings


