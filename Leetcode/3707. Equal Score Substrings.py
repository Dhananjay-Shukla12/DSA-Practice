class Solution:
    def scoreBalance(self, s: str) -> bool:
        sum = 0
        k = []
        for i in range(len(s)):
            sum+=(ord(s[i])-96)
            p = ord(s[i])-96
            k.append(p)
        rev = 0
        for i in k:
            rev+=i
            if rev == (sum - rev):
                return True

        return False
    