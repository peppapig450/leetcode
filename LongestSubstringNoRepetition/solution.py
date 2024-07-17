class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_length = 0
        char_set = set()
        left = 0
        
        for right in range(length):
            val = s[right]
            if val not in char_set:
                char_set.add(val)
                max_length = max(max_length, right - left + 1)
            else:
                while val in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.add(val)
        
        return max_length