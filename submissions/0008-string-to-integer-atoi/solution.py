class Solution:
    def myAtoi(self, s: str) -> int:
        s_stripped = s.lstrip()
        if not s_stripped:
            return 0
        sign = 1
        index = 0
        if s_stripped[0] == '-':
            sign = -1
            index += 1
        elif s_stripped[0] == '+':
            index += 1
        output = 0
        while index < len(s_stripped):
            digit = s_stripped[index]
            if digit.isdigit():
                output = (output * 10) + int(digit)
            else:
                break
            index += 1
        output = output * sign
        if output < -2**31:
            return -2**31
        if output > 2**31 - 1:
            return 2**31 - 1
        return output
