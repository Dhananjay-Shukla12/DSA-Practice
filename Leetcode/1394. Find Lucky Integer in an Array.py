class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_dict = {}
        for i in arr:
            arr_dict[i] = arr_dict.get(i, 0) + 1
        lucky_str = []
        for key,value in arr_dict.items():
            if key == value:
                lucky_str.append(key)
        
        if len(lucky_str)==0:
            return -1
        else:
            return max(lucky_str)