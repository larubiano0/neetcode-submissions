class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            s = digits[-(i+1)] + carry
            if s==10:
                digits[-(i+1)] = 0
            else:
                digits[-(i+1)] = s
                carry = 0
                break
        if carry==1:
            return [1] + digits
        else:
            return digits