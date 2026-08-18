class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        diff = {}
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i],i))
            else:
                while (stack) and (stack[-1][0] < temperatures[i]):
                    temp, j = stack.pop()
                    diff[j] = i-j
                else:
                    stack.append((temperatures[i],i))

        for temp, j in stack:
            if j not in diff:
                diff[j] = 0

        final_list = []
        for i in range(len(temperatures)):
            final_list.append(diff[i])
        
        return final_list

