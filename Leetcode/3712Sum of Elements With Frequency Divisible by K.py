class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d = {}
        sum = 0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        for key,values in d.items():
            if values%k == 0: 
                sum+=(key*values)
        
        return sum
    