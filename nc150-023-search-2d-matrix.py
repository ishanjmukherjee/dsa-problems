# My solution
# Same time complexity as the official solution, arguably cleaner code
# O(log(n * m)) time complexity (as required by problem statement), where
# m : number of rows
# n : number of columns

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        l, r = 0, numRows * numCols
        while l < r:
            midIdx = l + (r - l) // 2
            midVal = matrix[midIdx // numCols][midIdx % numCols]
            if midVal < target:
                l = midIdx + 1
            elif midVal > target:
                r = midIdx
            else:
                return True
        return False
