#Find the maximum difference in an unsorted array with the index of max greater than min.


def get_max_diff(nums):
    if not nums:
        return
    if len(nums) == 1:
        return nums[0]
    max_diff = nums[1] - nums[0]
    min_left = min(nums[0], nums[1])
    for i in range(2, len(nums)):
        max_diff = max(max_diff, nums[i] - min_left)
        min_left = min(min_left, nums[i])
    return max_diff



[2, 3, 10, 6, 4, 8, 1]

