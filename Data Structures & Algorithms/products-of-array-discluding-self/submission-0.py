class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = [1]
        suffix_list = [1]

        result = 1
        for num in nums:
            result *= num
            prefix_list.append(result)

        result = 1
        for i in range(len(nums)-1, -1, -1):
            result *= nums[i]
            suffix_list.append(result)

        result_list = []
        for i in range(len(nums)):
            suffix_idx = len(nums) - i -1
            prefix_idx = i
            result_list.append(prefix_list[prefix_idx] * suffix_list[suffix_idx])

        return result_list
        