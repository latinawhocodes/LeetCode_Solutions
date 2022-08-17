#   Question 66 
#
#   You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0s. 
#
#   Increment the large integer by one and return the resulting array of digits. 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        #move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            
            #set the nines to zeros at the end of the array
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                return digits
        
        #all digits are nine
        return [1] + digits 