class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_dict = {}
        ans = 0
        for i in nums:
            if i in count_dict:
                ans+=count_dict[i]
            count_dict[i] = count_dict.get(i, 0) + 1
        
        return ans
                