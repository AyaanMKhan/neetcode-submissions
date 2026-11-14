class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        
    
        return max(self.robber(nums[1:]), self.robber(nums[:-1]))
    

    def robber(self, nums):
        rob1, rob2 = 0, 0


        for n in nums:
            rob1, rob2 = rob2, max(rob2, rob1+n)
        
        return rob2