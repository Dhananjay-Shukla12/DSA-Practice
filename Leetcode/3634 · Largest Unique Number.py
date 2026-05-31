from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: The largest and only once occurring integer in the array
    """
    def largest_unique_number(self, nums: List[int]) -> int:
        # write your code here.
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        max = -1
        for items,value in hashmap.items():
            if value == 1 and items>max:
                max=items
        
        return max