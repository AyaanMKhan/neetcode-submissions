class Solution:
    def minOperations(self, s: str) -> int:
        even = 0
        odd = 0

        for i, c in enumerate(s):
            if i % 2 == 0:
                if c != '0':
                    even += 1
                if c != '1':
                    odd += 1
            elif i % 2 == 1:
                if c != '1':
                    even += 1
                if c != '0':
                    odd += 1
        return min(even, odd)