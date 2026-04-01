class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        

        for f in range(len(nums)):
            s,t = f+1,len(nums) - 1
            if f-1 >= 0 and nums[f] == nums[f-1]:
                continue
            while s < t:
                tripleSum = nums[f] + nums[s] + nums[t]
                if tripleSum == 0:
                    result.append([ nums[f], nums[s], nums[t] ])
                    t -= 1
                    s += 1
                    while s < t and nums[s] == nums[s-1]:
                        s += 1
                elif tripleSum < 0:
                    s += 1
                elif tripleSum > 0:
                    t -= 1
        return result