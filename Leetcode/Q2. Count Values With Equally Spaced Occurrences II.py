class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        # p = set()
        # for i in range(len(nums)):
        #     count[nums[i]] = count.get(nums[i],0)+1
        # for i,j in count.items():
        #     if j>=3:
        #         p.add(i)
        # ans =0
        # for i in range(len(nums)):
        #     if nums[i] in p:
        #         q = i
        #         t = []
        #         for j in range(i+1,len(nums)):
                    # if q!=i and nums[j] == nums[i]:
                    #     if q == (j-m):
                    #         ans+=1
                        
                    # elif nums[j]==nums[i]:
                    #     q = j-i
                    #     m = j
                #     if nums[i]==nums[j]:
                #         t.append(j)
                # z = t[0]-i
                # d = 0
                # for e in range(0,len(t)-1):
                #     if t[e+1]-t[e] != z:
                #         d=1
                # if d==0:
                #     ans+=1
                # p.remove(nums[i])

        # for i in p:
        #     water = []
        #     for j in range(len(nums)):
        #         if i == nums[j]:
        #             water.append(j)
        #     d= 0
        #     z = water[1]-water[0]
        #     for k in range(len(water)-1):
        #         if water[k+1]-water[k] !=z:
        #             d=1
        #     if d == 0:
        #         ans+=1
        # return ans
        count = {}
        ans=0
        for i,x in enumerate(nums):
            if x not in count:
                count[x] = []
            count[x].append(i)

        for i,water in count.items():
            if len(water)<3:
                continue
            else:
                z = water[1]-water[0]
                d = 0
                for j in range(len(water)-1):
                    if water[j+1]-water[j] !=z:
                        d=1
                        break
                if d==0:
                    ans+=1
        return ans
                    
        