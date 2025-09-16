class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        curr_sum = 0
        best_sum = arr[0]
        
        for i in arr:
            if curr_sum+i>i:
                curr_sum = curr_sum+i
            else:
                curr_sum = i
            
            if curr_sum>best_sum:
                best_sum = curr_sum
        
        return best_sum
                