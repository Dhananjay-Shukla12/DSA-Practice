class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        longest = 0
        for i in range(2,len(nums)):
            if nums[i-1]+nums[i-2] == nums[i]:
                ans+=1
            else:
                if ans > longest:
                    longest = ans
                ans = 0
        if ans>longest:
            longest = ans
        return longest+2
    