class Solution:
    def maxScore(self, s: str) -> int:
        
        zeros = 0
        ones = 0

        if s[0] == '0':
            zeros += 1
        else:
            ones += 1
        
        res = float("-inf")

        for i in range(1, len(s)):
            res = max(res, zeros - ones)
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
        
        return res + ones