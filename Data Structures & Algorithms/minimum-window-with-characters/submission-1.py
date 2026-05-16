class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        dictS = {}
        dictT = {}
        for i in t:
            dictT[i] = dictT.get(i, 0) + 1

        output = ""
        uniqueCount = 0
        expectedCount = len(dictT.keys())
        left = 0
        for right in range(len(s)):
            dictS[s[right]] = dictS.get(s[right], 0) + 1

            if dictS[s[right]] == dictT.get(s[right], 0):
                uniqueCount += 1
            
            while uniqueCount == expectedCount and left <= right:
                if output == "" or (right - left + 1) < len(output):
                    output = s[left: right + 1]
                dictS[s[left]] -= 1

                if s[left] in dictT and dictS[s[left]] < dictT[s[left]]:
                    uniqueCount -= 1
                left += 1

        return output
