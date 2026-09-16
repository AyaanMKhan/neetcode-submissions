class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2


            if nums[mid] == target:
                return True
            
            if nums[l] < nums[mid]: # Left Portion
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]: # Right Portion
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1

        
        return False