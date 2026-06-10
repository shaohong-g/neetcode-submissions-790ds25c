from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        window = deque()

        for i in range(len(nums)):
            # only larger number from the left
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)
            # remove index outside the window 
            if window[0] <= (i - k):
                window.popleft()

            # Add max number to output once it reaches k
            if i + 1 >= k:
                output.append(nums[window[0]])

        return output