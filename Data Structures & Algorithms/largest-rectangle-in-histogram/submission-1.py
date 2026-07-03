class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack stores most (height, index)
        # clean up by iterating through stack

        max_r = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][0] > h:
                t_h, t_i = stack.pop()
                rect = t_h * (i - t_i)
                max_r = max(max_r, rect)
                start = t_i
            
            stack.append((h, start))

        # clean up stack
        for h, i in stack:
            max_r = max(max_r, (len(heights) - i) * h)
        
        return max_r