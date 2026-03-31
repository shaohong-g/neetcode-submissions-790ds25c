class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_dict = {}
        for i in s:
            if i not in letter_dict:
                letter_dict[i] = 1
            else:
                letter_dict[i] += 1
        for i in t:
            if i not in letter_dict:
                return False
            letter_dict[i] -= 1
            if letter_dict[i] == 0:
                del letter_dict[i]
        return True
        