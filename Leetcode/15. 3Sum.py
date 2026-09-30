class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # pos1 = []
        # neg1 = set()
        # ans = []
        # seen = set()
        # for i in nums:
        #     if i<0:
        #         neg1.add(i)
        #     else:
        #         pos1.append(i) 

        # pos2 = set()
        # neg2 = []
        # zero = 0
        # for i in nums:
        #     if i<0:
        #         neg2.append(i)
        #     elif i==0:
        #         zero+=1
        #     else:
        #         pos2.add(i)
        # pos1 = sorted(pos1)
        # neg2 = sorted(neg2)
        # if (len(pos1)==0 and len(neg1)==1) and list(neg1)[0]==0:
        #     return [[0,0,0]]

        # elif (len(pos2)==1 and len(neg2)==0) and list(pos2)[0]==0:
        #     return [[0,0,0]]
    
        # else:
        #     for i in range(0,len(pos1)):
        #         for j in range(i+1,len(pos1)):
        #             k = (pos1[i]+pos1[j])*-1
        #             triplet = [pos1[i],pos1[j],k]
        #             if (pos1[i]+pos1[j])*-1 in neg1 and tuple(triplet) not in seen:
        #                 ans.append([pos1[i],pos1[j],k])
        #                 seen.add(tuple(triplet))
            
        #     for i in range(0,len(neg2)):
        #         for j in range(i+1,len(neg2)):
        #             k = (neg2[i]+neg2[j])*-1
        #             triplet = [neg2[i],neg2[j],k]
        #             if (neg2[i]+neg2[j])*-1 in pos2 and tuple(triplet) not in seen: 
        #                 ans.append([neg2[i],neg2[j],k])
        #                 seen.add(tuple(triplet))
        #     if zero>=3:
        #         ans.append([0,0,0])
        # return ans

        #using Set
        if nums.count(0) == len(nums):
            return [[0, 0, 0]]
        ans = set()
        for i in range(len(nums)):
            p = set()
            for j in range(i+1,len(nums)):
                temp = -(nums[i]+nums[j])
                if temp in p:
                    t = tuple(sorted([nums[i],nums[j],temp]))
                    ans.add(t)
                p.add(nums[j])
        return [list(x) for x in ans]