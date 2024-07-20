class Solution {
    public:
        bool isPalindrome(int x) {
            std::ios_base::sync_with_stdio(false);
            std::cin.tie(NULL);
            std::cout.tie(NULL);
            if (x < 0) {
                return false;
            }
    
            if (x != 0 && x % 10 == 0) {
                return false;
            }
    
            int reversed = 0;
            int original = x;
    
            while (x > 0) {
                int digit = x % 10;
    
                if (reversed > (INT_MAX - digit) / 10) {
                    return false;
                }
                
                reversed = reversed * 10 + digit;
                x /= 10;
            }
    
            return original == reversed;
        }
    };