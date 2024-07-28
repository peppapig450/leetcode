class Solution {
    // Map to store the digit to letter mappings
    private static final Map<Character, String> digitToLetterMap = Map.of(
            '2', "abc",
            '3', "def",
            '4', "ghi",
            '5', "jkl",
            '6', "mno",
            '7', "pqrs",
            '8', "tuv",
            '9', "wxyz");

    public List<String> letterCombinations(String digits) {
        // If input is empty, return an empty list
        if (digits == null || digits.isEmpty()) {
            return List.of();
        }

        // List to store the combinations
        List<String> combinations = new ArrayList<>();

        // Start the backtracking process
        backtrack(combinations, digits, 0, new StringBuilder());
        return combinations;
    }

    private void backtrack(List<String> combinations, String digits, int index, StringBuilder currentCombination) {
        // If the current combination length equals the digits length, add it to the
        // result list
        if (index == digits.length()) {
            combinations.add(currentCombination.toString());
            return;
        }

        // Get the letters corresponding to the current digit
        String letters = digitToLetterMap.get(digits.charAt(index));
        // Iterate over each letter and append it to the current combination
        for (char letter : letters.toCharArray()) {
            currentCombination.append(letter);
            // Move to the next digit
            backtrack(combinations, digits, index + 1, currentCombination);
            // Remove the last added letter to backtrack
            currentCombination.deleteCharAt(currentCombination.length() - 1);
        }
    }
}