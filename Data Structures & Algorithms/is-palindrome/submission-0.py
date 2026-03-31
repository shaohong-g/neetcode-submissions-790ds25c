class Solution:
    def isPalindrome(self, s: str) -> bool:
        front_idx = 0
        back_idx = len(s) - 1
        s = s.lower()
        while front_idx < back_idx:
            if not s[front_idx].isalnum():
                front_idx += 1
                continue
            if not s[back_idx].isalnum():
                back_idx -= 1
                continue
            if s[front_idx] != s[back_idx]:
                return False
            
            front_idx += 1
            back_idx -= 1

        return True
        