def isJudge(n, ind, mat):
    if (mat[ind] == [0]*n):
        for i in range(n):
            if (i)==(ind):
                continue
            if mat[i][ind]==1:
                continue
            else:
                return False
        return True
    else:
        return False

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(n)]
        for i,j in trust:
            mat[i-1][j-1] = 1
        judges = []
        for m in mat:
            print(m)
        for i in range(n):
            if isJudge(n, i, mat):
                judges.append(i+1)
        if len(judges)==1:
            return judges[0]
        else:
            return -1
