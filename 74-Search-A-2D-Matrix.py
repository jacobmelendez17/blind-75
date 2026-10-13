class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            row, col = mid // cols, mid % cols
            guess = matrix[row][col]

            if guess == target:
                return True
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# In this solution, we use a binary search to find the target in a 2D matrix
# We treat this as a 1D array and find the middle index to eventually find our target since the array is sorted
# The first two lines help us get the total length of the 1D array conversoin
# With that, we get the mid and we are able to get the row and column of the 2D array from the mid using
# integer division on its row and modulo on its column. Then we proceed with binary search as normal