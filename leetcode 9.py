class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:#negative numbers
            return False
        x = str(x)
        beginning = 0
        end = len(x) - 1  
        
        
        while beginning < end:
            if x[beginning] == x[end]:
                beginning += 1
                end -= 1
            else:
                return False
        
        return True
