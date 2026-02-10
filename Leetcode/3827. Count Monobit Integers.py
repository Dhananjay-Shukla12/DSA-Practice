class Solution:
    def countMonobit(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            ans = 1
            for i in range(1,n+1):
                if i & (i+1) == 0:
                    ans+=1
            return ans