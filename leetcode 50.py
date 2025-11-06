#Used recursion to reduce time complexity
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base case
        if n == 0:
            return 1
        
        # If power is negative
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half
