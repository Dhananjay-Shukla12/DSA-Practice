class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # ans_dict = {}
        # for i in strs:
        #     k = tuple(sorted(i))
        #     if k not in ans_dict:
        #         ans_dict[k] = []
        
        # for i in strs:
        #     if tuple(sorted(i)) in ans_dict:
        #         ans_dict[tuple(sorted(i))].append(i)
        
        # ans = []
        # for key,values in ans_dict.items():
        #     ans.append(values)
        # return ans
        

        #using count and removing sorting

        ans  = {}

        for i in strs:
            count = [0]*26

            for j in i:
                count[ord(j)-ord('a')] +=1
            key = tuple(count)
            if key not in ans:
                ans[key] = []
        
            ans[key].append(i)
        return list(ans.values())