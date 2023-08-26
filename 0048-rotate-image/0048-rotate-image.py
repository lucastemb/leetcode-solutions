class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #brute force to optimize
        track=deepcopy(matrix)
        res=[[0] * len(matrix) for i in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                matrix[r][c]=track[(len(matrix)-1-c)][r]

        #time: O(N^2)
        #space: O(N^2)