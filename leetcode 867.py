class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        c = len(matrix[0])
        T = []

        for i in range(c):
            row = []
            for j in range(r):
                row.append(matrix[j][i])
            T.append(row)

        return T

