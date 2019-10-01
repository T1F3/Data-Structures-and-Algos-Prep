class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        max_window_vals = []
        for i in range(len(nums) - k + 1):
            max_window_vals.append(max(nums[i : i + k]))
        return max_window_vals