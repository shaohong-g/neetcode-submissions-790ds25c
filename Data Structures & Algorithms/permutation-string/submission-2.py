class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        letter_dict = {}
        for s in s1:
            letter_dict[s] = letter_dict.get(s, 0) + 1

        l = 0
        r = 0
        track_dict = letter_dict.copy()
        while r < len(s2):
            curr_count = letter_dict.get(s2[r], -1)
            
            if curr_count == -1:
                r += 1
                l = r 
                track_dict = letter_dict.copy()
                continue
            track_dict[s2[r]] -= 1
            while track_dict[s2[r]] < 0:
                track_dict[s2[l]] += 1
                l += 1
            if r - l + 1 == len(s1):
                return True
            r += 1
        
        return False
        