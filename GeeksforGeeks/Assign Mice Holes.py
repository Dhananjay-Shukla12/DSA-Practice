import math
class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices = list(sorted(mices))
        holes = list(sorted(holes))
        ans = 0
        for i in range(len(mices)):
            ans = max(ans,abs(holes[i]-mices[i]))
        return ans
