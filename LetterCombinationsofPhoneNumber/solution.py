class Solution:
    # Solve using backtracking
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Result list to store the combinations
        result = []

        # Helper function to perform the backtracing
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append("".join(current_combination))
                return
            
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop() # Backtrack

        # Start the backtracking from the first digit
        backtrack(0, [])

        return result
