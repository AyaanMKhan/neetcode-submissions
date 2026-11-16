class Solution:
    def maxArea(self, height: list[int]) -> int:
        

        l = 0
        r = len(height)-1

        maxArea = 0

        while l < r:

            width = min(height[l], height[r])
            length = r-l

            area = width * length

            maxArea = max(maxArea, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            

        
        return maxArea