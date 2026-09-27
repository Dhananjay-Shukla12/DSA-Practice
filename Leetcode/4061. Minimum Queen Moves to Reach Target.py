class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if source[0]== target[0] and source[1]==target[1]:
            return 0
        elif abs(source[0]-target[0])==abs(source[1]-target[1]):
            return 1
        elif abs(source[0]-target[0])==0 and abs(source[1]-target[1])!=0:
            return 1
        elif abs(source[0]-target[0])!=0 and abs(source[1]-target[1])==0:
            return 1
        else:
            return 2
        