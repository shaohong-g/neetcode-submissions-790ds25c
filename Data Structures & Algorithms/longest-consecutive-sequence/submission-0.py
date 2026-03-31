class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for num in numSet:
            if num - 1 not in numSet:
                counter = 1
                while num + counter in numSet:
                    counter += 1
                result = max(result, counter)
        return result

