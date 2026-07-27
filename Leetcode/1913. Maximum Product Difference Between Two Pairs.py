class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # return nums[n-1]*nums[n-2]-nums[0]*nums[1]
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')


        for i in nums:
            if i>max1:
                max2=max1
                max1=i
            elif i>max2:
                max2=i
            if i<min1:
                min2 = min1
                min1 = i
            elif i<min2:
                min2 = i
        
        return max1*max2 - min1*min2

