class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Freq = [0] * 26

        for i in magazine:
            Freq[ord(i)-ord('a')] +=1
        
        for i in ransomNote:
            if Freq[ord(i)-ord('a')] == 0:
                return False
            Freq[ord(i)-ord('a')] -= 1
        return True
        
       
        