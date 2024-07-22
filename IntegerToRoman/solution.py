class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the value-symbol pairs for the Roman numerals
        val_syms = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
    
        roman_numeral = []
        for val, sym in val_syms:
            while num >= val:
                num -= val
                roman_numeral.append(sym)
    
        return ''.join(roman_numeral)