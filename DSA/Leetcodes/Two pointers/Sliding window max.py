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
 


def next_greater_element(arr):
    nge = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            if j < len(arr) and arr[j] > arr[i]:
                break
        nge_i = arr[j] if j < len(arr) else -1
        nge.append(nge_i)
    return nge


