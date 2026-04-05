class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        result = 0
        count = {}
        max_win = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_win = max(count[s[r]], max_win)
            while (r-l+1) - max_win > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r-l+1)
        return result

