class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # mark
        for n in nums:
            i = abs(n) - 1
            nums[i] = abs(nums[i]) * -1
        
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res