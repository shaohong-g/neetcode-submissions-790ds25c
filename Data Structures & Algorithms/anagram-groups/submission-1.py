class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        setDict = {}

        for word in strs:
            word_array = "".join(sorted(list(word)))
            if word_array in setDict:
                setDict[word_array].append(word)
            else:
                setDict[word_array] = [word]
        return list(setDict.values())
        