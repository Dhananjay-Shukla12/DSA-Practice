class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)
        for num, f in freq.items():
            heapq.heappush(heap,(f,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while(heap):
            ans.append(heapq.heappop(heap)[1])
        return ans[::-1]