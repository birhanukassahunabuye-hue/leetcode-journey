class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        win_sum = sum(nums[:k])
        max_sum = win_sum 
        for right in range(k, len(nums)):
            win_sum = win_sum - nums[right - k] + nums[right]
            max_sum = max(max_sum, win_sum)
        return max_sum/k