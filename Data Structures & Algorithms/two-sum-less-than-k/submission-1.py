class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        _nums = sorted([n for n in nums if n < k])

        max_sum = -1

        l, r = 0, len(_nums)-1

        
        while l < r:
            summ = _nums[l] + _nums[r]
            if summ < k:
                max_sum = max(max_sum, summ)
                l += 1
            else:
                r -= 1
        
        return max_sum
