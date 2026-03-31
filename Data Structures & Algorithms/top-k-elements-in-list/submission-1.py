class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kDict = {}

        for num in nums:
            if num in kDict:
                kDict[num] += 1
            else:
                kDict[num] = 1
        
        sorted_list = sorted(kDict, key=kDict.get, reverse=True)
        return sorted_list[:k]