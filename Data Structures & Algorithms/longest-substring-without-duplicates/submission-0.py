class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        substring = ""

        for letter in s:
            idx = substring.find(letter)
            if idx == -1 :
                substring += letter
            else:
                substring = substring[idx+1:] + letter
            result = max(result, len(substring))

        return result
        