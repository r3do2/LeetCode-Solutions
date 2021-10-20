class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
    
        #ceil
        mid = n // 2  + n%2

        # Transpose of matrix
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #print(matrix)

        # Taking Mirror Image along mid y axis
        for i in range(n):
            for j in range(mid):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
