class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        prefix matrix
        row 0
        row 1 5 6 3 2 = 6 11 14 16
        row 2 1 2 0 1 = 1 3 3 1
        1,1 to 2,2
        
        0  1  2  3
        6 11 14 16
        1  3  3  1

        grab from row 1 columns 2 - (column 1 - 1)
        grab from row 2 columns 2 - (column 1 - 1 )
        """
        self.prefix_matrix = []
        for row in matrix:
            total = 0
            row_arr = []
            for column in row:
                total += column
                row_arr.append(total)
            self.prefix_matrix.append(row_arr)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2+1):
            row_sum = self.prefix_matrix[row][col2] - (self.prefix_matrix[row][col1 -1] if col1 > 0 else 0)
            total += row_sum

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)