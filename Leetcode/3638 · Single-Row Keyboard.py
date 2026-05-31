class Solution:
    """
    @param keyboard: Customized keyboard strings
    @param word: A string
    @return: Total number of moves
    """
    def calculate_time(self, keyboard: str, word: str) -> int:
        # write your code here
        pos = {}

        for i, ch in enumerate(keyboard):
            pos[ch] = i
        ans = 0
        k = 0
        for j in word:
            ans = ans+abs(k-pos[j])
            k = pos[j]
        
        return ans