class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Used Boyer-Moore Voting Algo
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        max = None
        count = 0

        for num in nums:
            if count == 0:
                max = num
            if num == max:
                count += 1
            else:
                count -= 1

        return max
