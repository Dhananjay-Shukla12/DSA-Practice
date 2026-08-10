from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # char_dict = {}

        # for i in chars:
        #     char_dict[i] = char_dict.get(i, 0) + 1
        # ans = 0
        # for i in words:
        #     temp = char_dict.copy()
        #     p = 0
        #     for j in i:
        #         if j in temp and temp.get(j,0)!=0:
        #             temp[j] = temp.get(j,0)-1
        #             p+=1
        #         else:
        #             p=-1
        #             break
        #     if p != -1:
        #         ans+=p
        # return ans
        char_count = Counter(chars)
        ans = 0
        for i in words:
            if not (Counter(i)-char_count):
                ans+=len(i)
        return ans

