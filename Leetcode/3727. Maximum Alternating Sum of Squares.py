class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        n = len(nums)
        k = 0
        p = 0
        if n%2 == 0:
            k = n//2
        else:
            k = (n//2)+1
            p=1
        sum1 = 0
        rev_nums = nums[::-1]
        for i in range(0,k):
            sum1+=(rev_nums[i])
        
        sum2 = 0

        if p == 1:
            for i in range(0,k-1):
                sum2+=(nums[i])
        else:
            for i in range(0,k):
                sum2+=(nums[i])

        ans = abs(sum1-sum2) 
        return ans
        