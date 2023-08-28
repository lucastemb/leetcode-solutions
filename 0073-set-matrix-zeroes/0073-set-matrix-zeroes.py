class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp=deepcopy(matrix)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if temp[r][c] == 0:
                    #row
                    for i in range(len(matrix[0])):
                        matrix[r][i]=0
                    #column
                    for j in range(len(matrix)):
                        matrix[j][c]=0


        #TIME: O(M*N)
        #SPACE: O(M*N)
