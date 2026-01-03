class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
            
            freq = Counter(words)
            heap = []
            for word, f in freq.items():
                heapq.heappush(heap,(-f,word))
            
            ans = []
            for _ in range(k):
                ans.append(heapq.heappop(heap)[1])
            return ans