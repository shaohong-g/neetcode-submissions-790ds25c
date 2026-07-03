class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]
        area = 0
        for i in range(1, len(heights)):
            start_idx = i
            while stack and stack[-1][1] > heights[i]:
                start_idx, h = stack.pop()
                area = max(area, h * (i - start_idx))
            stack.append((start_idx, heights[i]))
        while stack:
            start_idx, h = stack.pop()
            area = max(area, h * (len(heights) - start_idx))
        return area
        