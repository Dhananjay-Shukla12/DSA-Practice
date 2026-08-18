class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        if rowIndex == 0:
            return ans
        else:
            for i in range(1,rowIndex+1):
                piku = ans[i-1] * ((rowIndex-i)+1)//i
                ans.append(piku)
            return ans
        