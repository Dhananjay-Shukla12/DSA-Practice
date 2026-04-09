class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:#type: ignore
        nums.sort()
        ans = []
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                ans.append(nums[i])
                break
        for i in range(0,len(nums)):
            if i+1 not in nums:
                ans.append(i+1)
        
        return ans
            

        