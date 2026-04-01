class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right_pointer = len(numbers) - 1
        left_pointer = 0

        twoSum = numbers[left_pointer] + numbers[right_pointer]
        while twoSum != target:
            if twoSum < target:
                left_pointer += 1
            elif twoSum > target:
                right_pointer -= 1
            twoSum = numbers[left_pointer] + numbers[right_pointer]

        
        return [left_pointer+1, right_pointer+1]