class Solution:
    def maxScore(self, s: str) -> int:
        k=0
        max = 0
        total = s.count('1')
        if total == 0:
            return len(s)-1
        for i in range(0,len(s)-1):
            if s[i]=='0':
                k+=1
            else:
                total = total - 1
            
            if (total + k)> max:
                max = total+k
        
        return max
        

        