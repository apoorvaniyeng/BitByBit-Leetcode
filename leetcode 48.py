class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose (in place possible cuz matrix square)
        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # Reverse each row in place
        for i in range(n):
            start = 0
            end = n - 1
            while start < end:
                temp = matrix[i][start]
                matrix[i][start] = matrix[i][end]
                matrix[i][end] = temp
                start += 1
                end -= 1
