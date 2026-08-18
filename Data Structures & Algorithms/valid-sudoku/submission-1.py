def verify_row(row):
    seen = set()

    for entry in row:
        if entry == ".":
            continue
        if entry in seen:
            return False
        seen.add(entry)

    return True


def verify_rows(board):
    return all(verify_row(row) for row in board)


def verify_sub_box(sub_board):
    flattened = [cell for row in sub_board for cell in row]
    return verify_row(flattened)


def verify_sub_boxes(board):
    for i in range(3):
        for j in range(3):
            box = [
                row[j * 3:(j + 1) * 3]
                for row in board[i * 3:(i + 1) * 3]
            ]

            if not verify_sub_box(box):
                return False

    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = list(map(list, zip(*board)))

        return (
            verify_rows(board)
            and verify_rows(columns)
            and verify_sub_boxes(board)
        )