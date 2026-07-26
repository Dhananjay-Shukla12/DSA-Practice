class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        k = 0
        for i in range(len(sentence)):
            if  sentence[i] == ' ' and sentence[i-1] != sentence[i+1]:
                return False
            if sentence[i] == ' ':
                k+=1
        p = len(sentence)
        if sentence[0] != sentence[p-1]:
                return False
        if k==0 and sentence[0] != sentence[p-1]:
            return False
        return True
                