class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        i = 0
        j=0
        maxi = 0
        sum = 0
        while j<len(arr):
            sum+=arr[j]
            if (j-i+1)<k:
                j+=1
            elif (j-i+1)==k:
                maxi = max(maxi,sum)
                sum = sum-arr[i]
                i+=1
                j+=1
        
        return maxi