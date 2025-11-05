class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        n = len(nums)
        if n == 0:
            return []
        L = []
        while i < n:
            beforei = nums[:i + 1]
            countbeforei = len(set(beforei))
            afteri = nums[i + 1:]
            countafteri = len(set(afteri))
            L.append(countbeforei - countafteri)
            i += 1
            
        return L
