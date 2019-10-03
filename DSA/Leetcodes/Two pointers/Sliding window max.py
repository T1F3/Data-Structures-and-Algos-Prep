class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        max_window_vals = []
        for i in range(len(nums) - k + 1):
            max_window_vals.append(max(nums[i : i + k]))
        return max_window_vals


import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        mh = []
        for i in range(k):
            heapq.heappush(mh, -nums[i])
        res.append(-mh[0])
        for i in range(len(nums) - k):
            mh.remove(-nums[i])
            heapq.heapify(mh)
            heapq.heappush(mh, -1 * nums[k + i])
            res.append(-mh[0])
        return res
 



