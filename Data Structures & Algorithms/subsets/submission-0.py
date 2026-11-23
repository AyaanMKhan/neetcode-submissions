class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        

        res, sol = [], []


        def backtrack(index):
            if index >= len(nums):
                res.append(sol.copy())
                return
            
            sol.append(nums[index])
            backtrack(index+1)
            sol.pop()
            backtrack(index+1)


        backtrack(0)
        return res