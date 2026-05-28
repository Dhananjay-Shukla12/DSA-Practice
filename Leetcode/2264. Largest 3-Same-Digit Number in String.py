class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        p=0
        for i in range(0,len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                if ord(num[i])>p:
                    p = ord(num[i])
                    ans = ""
                    ans+=num[i]
                    ans+=num[i+1]
                    ans+=num[i+2]
        
        return ans