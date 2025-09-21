class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        ans = set()
        for i in range(0,len(nums)):
            ans.add(nums[i])
            if len(ans)==k:
                break
        rans = list(ans)
        rans.sort(reverse=True)
        return rans
