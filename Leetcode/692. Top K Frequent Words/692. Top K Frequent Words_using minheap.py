class Node:
    def __init__(self,freq,word):
        self.freq = freq
        self.word = word

    def __lt__(self,other):
        if self.freq !=  other.freq:
            return self.freq< other.freq
        return self.word > other.word
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
            freq = Counter(words)
            heap = []
            for word, f in freq.items():
                heapq.heappush(heap,(Node(f,word)))
                if len(heap)>k:
                    heapq.heappop(heap)
            ans = []
            while heap:
                ans.append(heapq.heappop(heap).word)
            return ans[::-1]