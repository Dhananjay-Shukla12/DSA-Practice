from typing import (
    List,
)

class Solution:
    """
    @param arr: the array
    @return: the count of valid elements
    """
    def count_elements(self, arr: List[int]) -> int:
        # write your code here
        hashmap = {}
        for i in arr:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        ans = 0
        for i in arr:
            if  i+1 in hashmap:
                ans+=1
        return ans
            
        