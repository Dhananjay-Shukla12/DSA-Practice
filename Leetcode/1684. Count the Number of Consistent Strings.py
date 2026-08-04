class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        p = 0
        allowed = set(allowed)
        for i in words:
            k=0
            for j in i:
                if j not in allowed:
                    k=1
                    break
            if k==0:
                p+=1
        return p
                    

            