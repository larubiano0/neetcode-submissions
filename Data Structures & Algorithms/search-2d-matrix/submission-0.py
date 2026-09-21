def ktoij(k,n,m):
    return (k//m, k%m)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = n*m-1

        while low<=high:
            mid = low + (high-low)//2
            i, j = ktoij(mid,n,m)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                low = mid+1
            else:
                high = mid-1

        return False