class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x_list = [digit for digit in str(abs(x))]
        x_list.reverse()
        answer = int("".join(x_list))
        if answer < -2**31 or answer > 2**31 - 1:
            return 0
        else:
            return sign * answer
