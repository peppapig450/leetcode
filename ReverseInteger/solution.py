class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        negative = x < 0
        x = abs(x)
        
        reversed_str = str(x)[::-1]
        reversed_num = int(reversed_str)

        if negative:
            reversed_num = -reversed_num

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num