#   Question 724
#   Given an array of integers[nums], calculate the pivot index of the array. 
#
#   The pivot index is the index where the sum of all the numbers strictly on its left equals the sum of all the numbers strictly on the right. If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left ~ also applies to the right. 
#
#   Return the leftmost pivot index. If no such index exists, return -1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        leftmostSum = 0
        
        for i, x in enumerate(nums):
            if leftmostSum == (s - leftmostSum - x):
                return i
            leftmostSum += x
            
        return -1


#   Time Complexity : O(N) where is the length of nums