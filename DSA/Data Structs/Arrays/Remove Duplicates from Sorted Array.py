class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        last, next_ind = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] > last:
                last = nums[i]
                nums[next_ind], nums[i] =  nums[i], nums[next_ind]
                next_ind += 1
        return next_ind