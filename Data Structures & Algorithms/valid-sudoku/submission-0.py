def verify_row(row):
    hashmap = {}
    for entry in row:
        if entry == ".":
            continue
        elif entry in hashmap:
            return False
        else:
            hashmap[entry] = 0
    return True

def verify_rows(board):
    if all(map(verify_row, board)):
        return True
    else:
        return False

def verify_sub_box(sub_board):
    l = sum(sub_board, [])
    if verify_row(l):
        return True
    else:
        return False

def verify_sub_boxes(board):
    for i in range(3):
        for j in range(3):
            row_filtered = board[i*3:(i+1)*3]
            column_filtered = [row[j*3:(j+1)*3] for row in row_filtered]
            if not verify_sub_box(column_filtered):
                return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (verify_rows(board) and verify_rows(list(map(list, zip(*board)))) and verify_sub_boxes(board))
        
        
