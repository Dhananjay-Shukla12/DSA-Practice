class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        leasttime = float('inf')
        for x in tasks:
            sum=0
            for y in x:
                sum+=y
            if sum<leasttime:
                leasttime = sum
        return leasttime
            
            