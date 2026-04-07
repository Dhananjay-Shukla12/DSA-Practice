class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:#type: ignore
        firsthalf = nums[:n]
        secondhalf = nums[n:]
        ans = []

        for i in range(n):
            ans.extend([firsthalf[i], secondhalf[i]])
        return ans