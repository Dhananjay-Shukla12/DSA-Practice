class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        count = {}
        for x in nums:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
        result=[]
        while sum(count.values()) > 0:
            for key in sorted(count):
                if count[key] > 0:
                    result.append(key)
                    count[key] -= 1

        return result