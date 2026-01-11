class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1
        k=0
        p=0
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                k+=1
                r-=1
        l=0
        r= len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                p+=1
                l+=1
        
        if k<=1 or p<=1:
            return True
        return False

