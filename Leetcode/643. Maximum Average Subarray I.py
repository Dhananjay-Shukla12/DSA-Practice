class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        maxaverage = float('-inf')

        i = 0 
        j = 0
        if len(nums)==1:
            return nums[0]
        sum = nums[0]
        while j < len(nums):
            if (j-i+1)!=k:
                j+=1
                sum+=nums[j]
            else:
                if (sum/k) > maxaverage:
                    maxaverage = sum/k
                else:
                    sum = sum - nums[i]
                    i+=1
                    j+=1
                    if j<len(nums):
                        sum+= nums[j]
                        if sum/k > maxaverage:
                            maxaverage = sum/k
                    else:
                        break
        return maxaverage
        