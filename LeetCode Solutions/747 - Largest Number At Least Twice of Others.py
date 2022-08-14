#   Question 747
#   You are given an integer array nums where the largest integer is unique. 
#
#   Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise. 
#
#   CONSTRAINTS:x
#       2 <= nums.length <= 50
#       0 <= nums[i] <= 100
#       The largest element is nums is unique

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        maxIndex = nums.index(maxNum)
        nums.remove(maxNum)
        
        for num in nums:
            if (maxNum < 2 * num):
                return -1
        return maxIndex


# 40ms runtime, faster than 86.59% of Python3 submissions
# 13.8MB memory usage, less than 96.78% of Python3 submissions