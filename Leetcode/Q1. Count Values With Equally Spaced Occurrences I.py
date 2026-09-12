class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count = {}
        p = set()
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1
        for i,j in count.items():
            if j==3:
                p.add(i)
        ans =0
        for i in range(len(nums)):
            if nums[i] in p:
                q = i
                t = []
                for j in range(i+1,len(nums)):
                    # if q!=i and nums[j] == nums[i]:
                    #     if q == (j-m):
                    #         ans+=1
                        
                    # elif nums[j]==nums[i]:
                    #     q = j-i
                    #     m = j
                    if nums[i]==nums[j]:
                        t.append(j)
                if t[0]-i == t[1]-t[0]:
                    ans+=1
                p.remove(nums[i])
                
        return ans
                        