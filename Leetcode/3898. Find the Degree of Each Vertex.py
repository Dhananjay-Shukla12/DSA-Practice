class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for i in matrix:
            k = 0
            for j in i:
                if j==1:
                    k+=1
            ans.append(k)
        return ans
            
        