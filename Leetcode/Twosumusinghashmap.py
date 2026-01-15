class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            secondvalue = target - nums[i]

            if secondvalue in hashmap:
                return [i,hashmap[secondvalue]]
            else:
                hashmap[nums[i]] = i
        
        return []