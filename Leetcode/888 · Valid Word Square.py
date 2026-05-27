class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def valid_word_square(self, words):
        # Write your code here
        ans = []
        for i in range(len(words)):
            p=""
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]):
                    return False
                if words[i][j] != words[j][i]:
                    return False
        return True
                

            