class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i,0)+1
        
        for value,count in nums_dict.items():
            if count%2!=0:
                return False
        return True
        