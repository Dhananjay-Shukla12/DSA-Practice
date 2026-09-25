class Solution:
    def countsort(self,arr):
        max_value = max(arr)
        count = [0] * (max_value+1)
        for i in arr:
            count[i]+=1
        result = []
        for i in range(len(count)):
            for _ in range(count[i]):
                result.append(i)
        return result
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        i = 0 
        j = len(people)-1
        ans = 0
        people = self.countsort(people)
        while i<=j:
            if (people[i]+people[j]) <= limit:
                ans += 1
                i+=1
                j-=1
            elif people[i]>people[j]:
                ans+=1
                i+=1
            else:
                ans+=1
                j-=1
        return ans

        