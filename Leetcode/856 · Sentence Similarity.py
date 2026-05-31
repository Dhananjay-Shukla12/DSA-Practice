from typing import (
    List,
)

class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def is_sentence_similarity(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        # write your code here
        if len(words1)!=len(words2):
            return False
        hashset = set()
        for a,b in pairs:
            hashset.add((a,b))
            hashset.add((b,a))
        
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if (words1[i],words2[i]) not in hashset:
                return False
        return True