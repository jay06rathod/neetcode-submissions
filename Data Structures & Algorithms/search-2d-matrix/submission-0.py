class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         low = 0
        #         high = len(matrix[i])-1
        #         while low <= high:
        #             mid = low + (high - low) // 2
        #             if matrix[i][mid] == target:
        #                 return True
        #             elif matrix[i][mid]<target:
        #                 low = mid + 1
        #             else:
        #                 high = mid - 1
        
        # return False