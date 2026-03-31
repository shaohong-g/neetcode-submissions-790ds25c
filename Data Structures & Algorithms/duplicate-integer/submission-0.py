class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrSet = set(nums)
        return len(arrSet) != len(nums)