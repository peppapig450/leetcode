class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter

        freq = Counter(arr)

        distinct_strings = [string for string in arr if freq[string] == 1]

        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""