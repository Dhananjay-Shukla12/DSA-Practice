class Solution:
    def removeZeros(self, n: int) -> int:
        k = str(n)
        p = ''
        for i in k:
            if i!='0':
                p+=i
        return int(p)
        
        