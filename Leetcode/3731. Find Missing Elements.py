class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        k = []
        nums.sort()
        for i in range(nums[0],nums[-1]+1):
            if i not in nums:
                k.append(i)

        return k