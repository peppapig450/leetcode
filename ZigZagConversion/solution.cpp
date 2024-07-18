class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;

        string result;
        int cycle = 2 * numRows - 2;

        for (int row = 0; row < numRows; row++) {
            for (int i = row; i < s.length(); i += cycle) {
                result.push_back(s[i]);
                if (row > 0 && row < numRows - 1 && i + cycle - 2 * row < s.length()) {
                    result.push_back(s[i + cycle - 2 * row]);
                }
            }
        }
        return result;
    }
};