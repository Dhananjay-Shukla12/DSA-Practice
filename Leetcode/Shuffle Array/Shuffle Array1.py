class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:# type: ignore
        firsthalf = []
        secondhalf = []
        k = 2*n
        for i in range(0,n):
            firsthalf.append(nums[i])
        for i in range(n,k):
            secondhalf.append(nums[i])

        ans = []
        a = 0
        b = 0
        for i in range(0,k):
            if i%2==0:
                ans.append(firsthalf[a])
                a+=1
            else:
                ans.append(secondhalf[b])
                b+=1 
        
        return ans