class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def can_permute_palindrome(self, s: str) -> bool:
        # write your code here
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i,0)+1
        
        ans = 0
        k=1
        for items,value in hashmap.items():
            if value%2==0:
                ans+=value
            else:
                ans+=value
                k-=1
        
        if (ans == len(s) or ans ==len(s)-1 )and(k>=0):
            return True
        else:
            return False
