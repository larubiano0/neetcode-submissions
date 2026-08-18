def is_numeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        number_queue = []
        for token in tokens:
            if is_numeric(token):
                number_queue.append(token)
            elif token == "+":
                second_num = number_queue.pop()
                first_num = number_queue.pop()
                number_queue.append(str(int(first_num)+int(second_num)))
            elif token == "-":
                second_num = number_queue.pop()
                first_num = number_queue.pop()
                number_queue.append(str(int(first_num)-int(second_num)))
            elif token == "*":
                second_num = number_queue.pop()
                first_num = number_queue.pop()
                number_queue.append(str(int(first_num)*int(second_num)))
            elif token == "/":
                second_num = number_queue.pop()
                first_num = number_queue.pop()
                number_queue.append(str(int(int(first_num)/int(second_num))))
        return int(number_queue[0])